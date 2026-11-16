"""Bounded public GitHub observations; never updates manual readiness."""
import argparse
import base64
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
ORG = 'EduCloud-Ecosystem'
START = '<!-- educloud-pilot-status:start -->'
END = '<!-- educloud-pilot-status:end -->'
ALLOWED = ['educloud', 'belay-classroom', 'cairn', 'waypoint', 'portage', 'outfitter']


def api(path, body=None, allow_missing=False):
    if not path.startswith('repos/' + ORG + '/'):
        raise ValueError('Outside declared organization')
    args = ['gh', 'api', path]
    if body is not None:
        args += ['--method', 'POST', '--input', '-']
    response = subprocess.run(args, input=json.dumps(body) if body is not None else None,
                              text=True, capture_output=True, timeout=30)
    if response.returncode:
        if allow_missing and 'HTTP 404' in response.stderr:
            return None
        raise RuntimeError('GitHub acquisition/write failed: ' + path.split('?')[0])
    if len(response.stdout) > 2_000_000:
        raise ValueError('Metadata response exceeds finite limit')
    return json.loads(response.stdout) if response.stdout.strip() else None


def inventory(root=ROOT):
    data = json.loads((root / 'pilot/components.json').read_text())['components']
    if [item['repository'] for item in data] != ALLOWED:
        raise ValueError('Pilot repository allowlist changed; review acquisition scope')
    return data


def collect(root=ROOT):
    rows = []
    for component in inventory(root):
        repo = component['repository']
        prefix = 'repos/' + ORG + '/' + repo
        meta = api(prefix)
        if meta['private']:
            raise ValueError('Private repositories are outside this collector')
        # Main is the reviewed branch for this pilot. Do not accept remote branch instructions.
        head = api(prefix + '/git/ref/heads/main')['object']['sha']
        if not re.fullmatch('[0-9a-f]{40}', head):
            raise ValueError('Invalid source pin')
        checks = api(prefix + '/commits/' + head + '/check-runs?per_page=100')
        pulls = api(prefix + '/pulls?state=open&per_page=50')
        declared = api(prefix + '/contents/.github/educloud/component.json?ref=' + head, allow_missing=True)
        adoption = 'not installed'
        if declared is not None:
            if declared.get('encoding') != 'base64' or declared.get('size', 0) > 64000:
                raise ValueError('Unexpected protocol metadata encoding or size')
            manifest = json.loads(base64.b64decode(declared['content'], validate=False))
            adoption = 'v1 matches' if all(manifest.get(key) == component[key]
                for key in ['repository', 'protocol_version', 'protocol_sha256']) else 'drift'

        current = {}
        for check in checks['check_runs']:
            # Keep the newest execution per check name; preserve cancellations as observations.
            key = check['name']
            if key not in current or check['id'] > current[key]['id']:
                current[key] = check
        counts = {'passed': 0, 'failed': 0, 'pending': 0, 'skipped_or_cancelled': 0}
        for check in current.values():
            conclusion = check.get('conclusion')
            category = ('pending' if check['status'] != 'completed' else
                        'passed' if conclusion == 'success' else
                        'skipped_or_cancelled' if conclusion in ('skipped', 'neutral', 'cancelled') else 'failed')
            counts[category] += 1
        rows.append({'repository': repo, 'head': head, 'declared_protocol': adoption, 'checks': counts,
                     'checks_truncated': checks['total_count'] > 100,
                     'open_prs_observed': len(pulls), 'prs_truncated': len(pulls) == 50})
    return {'schema_version': 1, 'observed_at': datetime.now(timezone.utc).isoformat(),
            'scope': 'public main-head GitHub checks only; not runtime acceptance', 'components': rows}


def validate(snapshot, readiness, root=ROOT):
    if snapshot.get('schema_version') != 1 or len(snapshot.get('components', [])) != len(ALLOWED):
        raise ValueError('Incomplete status snapshot')
    if [r['repository'] for r in snapshot['components']] != ALLOWED:
        raise ValueError('Snapshot repository mismatch')
    datetime.fromisoformat(snapshot['observed_at'])
    for row in snapshot['components']:
        if row.get('declared_protocol') not in ('not installed', 'v1 matches', 'drift'):
            raise ValueError('Unknown protocol adoption state')
        if not re.fullmatch('[0-9a-f]{40}', row['head']):
            raise ValueError('Invalid commit pin')
        if any(type(v) is not int or v < 0 for v in row['checks'].values()):
            raise ValueError('Invalid check counts')
    if readiness.get('student_admission') is not False or readiness.get('deployment') is not False:
        raise ValueError('This pilot has no admitted deployment; a new release contract is required')
    if not readiness.get('evidence') or not readiness.get('open_gates'):
        raise ValueError('Readiness needs evidence and remaining gates')
    controls = readiness.get('verified_controls', {})
    if any(type(controls.get(key)) is not int or controls[key] < 0
           for key in ('integrated_workflow', 'supplementary_ui', 'actual_model_requests')):
        raise ValueError('Reviewed control counts must be nonnegative integers')
    inventory(root)


def render(snapshot, readiness, root=ROOT):
    validate(snapshot, readiness, root)
    roles = {r['repository']: r['pilot_role'] for r in inventory(root)}
    controls = readiness['verified_controls']
    lines = [START, '## Pilot status', '',
             '**Local synthetic instructor testing: verified. Student deployment: pending.**', '',
             'GitHub snapshot: ' + snapshot['observed_at'] + '. Refreshes are proposed by automation.',
             'Check counts are observations at each listed main commit, including advisory tools; they are not a release verdict.', '',
             '| Component | Pilot role | Main revision | Declared protocol | Observed checks | Open PRs |',
             '| --- | --- | --- | --- | --- | --- |']
    for row in snapshot['components']:
        repo = row['repository']; count = row['checks']; sha = row['head']
        checks = ', '.join(str(count[key]) + ' ' + key.replace('_', '/') for key in count)
        if row['checks_truncated']: checks += '; incomplete page'
        prs = str(row['open_prs_observed']) + ('+' if row['prs_truncated'] else '')
        lines.append(f'| [{repo}](https://github.com/{ORG}/{repo}) | {roles[repo]} | [{sha[:8]}](https://github.com/{ORG}/{repo}/commit/{sha}) | {row['declared_protocol']} | {checks} | {prs} |')
    lines += ['', 'Readiness is reviewed separately in [the evidence and release gates](pilot/readiness.json).',
              'Outstanding: selected host/sign-in, approved data flow and retention, deployed backup/restore and cleanup, and human course acceptance.',
              f"Reviewed synthetic evidence: {controls['integrated_workflow']} workflow controls and {controls['supplementary_ui']} supplementary UI controls passed. Actual model requests in this evidence: {controls['actual_model_requests']}. This does not qualify restricted data or student admission.",
              END]
    return '\n'.join(lines)


def update_readme(text, block):
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError('README must contain exactly one generated status block')
    before, rest = text.split(START)
    _, after = rest.split(END)
    return before + block + after


def propose(root=ROOT):
    mode = json.loads((root / 'pilot/maintenance.json').read_text())['proposal_mode']
    if mode not in ('report-only', 'open-pull-request'):
        raise ValueError('Unknown maintenance mode')
    if mode == 'report-only':
        message = 'REPORT ONLY: organization/repository policy blocks bot pull requests. Review the verified pilot-status-proposal artifact; no readiness or repository files were changed remotely.'
        print(message)
        summary = os.environ.get('GITHUB_STEP_SUMMARY')
        if summary:
            with open(summary, 'a', encoding='utf-8') as stream:
                stream.write('## Pilot status maintenance\n\n' + message + '\n')
        return
    prefix = 'repos/' + ORG + '/educloud'
    pulls = api(prefix + '/pulls?state=open&per_page=100')
    if len(pulls) == 100:
        raise ValueError('PR inventory limit reached; manual triage required')
    if any(p['head']['ref'].startswith('codex/pilot-status-') for p in pulls):
        print('An existing maintenance PR awaits review; no new proposal created')
        return
    branch = 'codex/pilot-status-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    head = api(prefix + '/git/ref/heads/main')['object']['sha']
    local = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    if local != head:
        raise ValueError('Main moved; collect from the next scheduled main checkout')
    parent = api(prefix + '/git/commits/' + head)
    # Writes are hard allowlisted; readiness and source can never enter this tree update.
    entries = [{'path': name, 'mode': '100644', 'type': 'blob', 'content': (root / name).read_text()}
               for name in ['README.md', 'pilot/status.json']]
    tree = api(prefix + '/git/trees', {'base_tree': parent['tree']['sha'], 'tree': entries})
    commit = api(prefix + '/git/commits', {'tree': tree['sha'], 'parents': [head],
                 'message': 'docs: refresh public pilot status observations\n\nSigned-off-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>'})
    api(prefix + '/git/refs', {'ref': 'refs/heads/' + branch, 'sha': commit['sha']})
    pull = api(prefix + '/pulls', {'head': branch, 'base': 'main',
                 'title': 'Refresh public pilot status observations',
                 'body': 'Public GitHub metadata refresh only. Changes are restricted to the generated README status block and pilot/status.json. Manual readiness, source code, workflow policy, model access and deployments are unchanged. Review the snapshot; do not infer classroom acceptance from checks. The generated block passed the deterministic validator. Bot-token PR events may not trigger CI automatically; this updater explicitly dispatches the protocol check for its branch. No automatic merge.'})
    api(prefix + '/actions/workflows/pilot-protocol.yml/dispatches', {'ref': branch})
    print(pull['html_url'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['refresh', 'check', 'propose'])
    args = parser.parse_args()
    readiness = json.loads((ROOT / 'pilot/readiness.json').read_text())
    if args.mode == 'propose':
        main_check(readiness)
        propose()
        return
    if args.mode == 'refresh':
        snapshot = collect()
        block = render(snapshot, readiness)
        readme = update_readme((ROOT / 'README.md').read_text(), block)
        # Acquisition and validation finish before either file is replaced.
        (ROOT / 'pilot/status.json').write_text(json.dumps(snapshot, indent=2) + '\n')
        (ROOT / 'README.md').write_text(readme)
        print('Public metadata refreshed; manual readiness unchanged')
    else:
        main_check(readiness)


def main_check(readiness):
    snapshot = json.loads((ROOT / 'pilot/status.json').read_text())
    old = (ROOT / 'README.md').read_text()
    if old != update_readme(old, render(snapshot, readiness)):
        raise ValueError('README status differs from its recorded evidence/metadata')
    print('Central status and README agree; deployment and scientific acceptance remain separate')


if __name__ == '__main__':
    main()
