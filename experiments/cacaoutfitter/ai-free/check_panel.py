"""Exercise the packaged assignment in a real network-isolated JupyterLab."""
import argparse
from contextlib import ExitStack
import json
from pathlib import Path
import secrets
import sys
import time
from urllib.parse import urlsplit
from urllib.request import urlopen

from playwright.sync_api import expect, sync_playwright


def check(args):
    sys.path.insert(0, str(args.ide.resolve() / "integrations/waypoint"))
    from image_smoke import docker, RELAY

    name = "concept-" + secrets.token_hex(6)
    token = secrets.token_urlsafe(24)
    image = docker("image", "inspect", "-f", "{{.Id}}", args.image)
    with ExitStack() as clean:
        net = docker("network", "create", "--internal", name)
        clean.callback(docker, "network", "rm", net)
        server = docker("run", "-d", "--network", net, "--name", name, "-e", "JUPYTER_TOKEN=" + token,
                        image, "jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--port=8888",
                        "--LabApp.expose_app_in_browser=True")
        clean.callback(docker, "rm", "-f", server)
        relay = docker("run", "-d", "-p", "127.0.0.1::8888", image, "python", "-c", RELAY, name)
        clean.callback(docker, "rm", "-f", relay)
        docker("network", "connect", net, relay)
        base = "http://" + docker("port", relay, "8888/tcp")
        for _ in range(100):
            try:
                with urlopen(base + "/api/status?token=" + token, timeout=2):
                    break
            except OSError:
                time.sleep(.3)
        else:
            raise RuntimeError("Local JupyterLab did not become ready")
        blocked = []
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            def route(request):
                url = urlsplit(request.request.url)
                if url.scheme in ("http", "https") and url.netloc != urlsplit(base).netloc:
                    blocked.append(url.hostname)
                    request.abort()
                else:
                    request.continue_()
            page.route("**/*", route)
            page.goto(base + "/lab/tree/INFO-511-NHANES/nhanes-wrangling.ipynb?token=" + token)
            panel = page.locator("#belay-math-inspector")
            expect(panel).to_be_visible(timeout=90000)
            def select(cell_id, source=None):
                page.evaluate("""([id, source]) => {
                  const n=window.jupyterapp.shell.currentWidget.content;
                  const i=n.widgets.findIndex(w=>w.model.id===id);
                  if(i<0) throw Error('Missing assignment cell');
                  n.activeCellIndex=i;
                  if(source!==null) n.activeCell.model.sharedModel.setSource(source);
                }""", [cell_id, source])
            select("learner-work", "joined = demographics.merge(bp_readings)")
            expect(panel.get_by_role("status")).to_contain_text("Joining tables")
            select("learner-work", "long = joined.melt()")
            expect(panel.get_by_role("status")).to_contain_text("Wide to long")
            select("unit-prediction", "One row per reading.")
            expect(panel.get_by_role("status")).to_contain_text("Reading-level rows")
            page.set_viewport_size({"width": 375, "height": 760})
            select("unit-prediction", "I have a different explanation.")
            expect(panel.get_by_role("status")).to_contain_text("Unit of observation")
            assert panel.evaluate("(e) => e.scrollWidth <= e.clientWidth + 1"), "Concept text overflows"
            page.set_viewport_size({"width": 1280, "height": 900})
            select("learner-work", "print(6 * 7)")
            expect(panel.get_by_role("status")).to_contain_text("Concepts for this assignment")
            page.evaluate("""() => {
              const panels = Array.from(window.jupyterapp.shell.widgets('right'));
              panels.find(w => w.id === 'belay-math-inspector').close();
            }""")
            expect(panel).to_have_count(0)
            page.evaluate("() => window.jupyterapp.commands.execute('notebook:run-cell')")
            expect(page.locator(".jp-OutputArea-output").filter(has_text="42").first).to_be_visible(timeout=60000)
            page.evaluate("() => window.jupyterapp.commands.execute('docmanager:save')")
            saved = json.loads(docker("exec", server, "cat", "/home/learner/work/INFO-511-NHANES/nhanes-wrangling.ipynb"))
            cell, = [c for c in saved["cells"] if c["id"] == "learner-work"]
            assert "42" in str(cell["outputs"])
            # Concept selection must still work after the kernel has been shut down.
            page.evaluate("""async () => {
              const app=window.jupyterapp, ctx=app.shell.currentWidget.sessionContext;
              await ctx.shutdown();
              if (ctx.session?.kernel) throw Error('Kernel is still running');
              await app.commands.execute('belay-math:open');
            }""")
            select("learner-work", "joined = demographics.merge(bp_readings)")
            expect(panel.get_by_role("status")).to_contain_text("Joining tables")
            browser.close()
        assert not blocked, "Browser attempted external requests"
    print(json.dumps(dict(image=image, assignment="info511-nhanes-wrangling-v1",
                          conceptual_cues=["merge", "melt", "explicit prediction", "open prediction"],
                          notebook_result=42, notebook_saved_with_panel_closed=True, recognized_with_kernel_off=True, external_browser_requests=len(blocked))))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ide", required=True, type=Path)
    ap.add_argument("--image", default="educloud-info511:ai-free")
    check(ap.parse_args())
