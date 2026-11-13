# SPDX-License-Identifier: Apache-2.0
"""Build a bounded, deterministic E1 source release; no network or execution."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[2]
MODULE = 'experiments/demand-reduction-v1/'
FILES = tuple(MODULE + name for name in (
    'e1.py', 'tasks.json', 'README.md', 'LICENSE', 'LICENSING.md',
    'test_e1.py', 'release.py', 'test_release.py')) + ('docs/specs/resource-efficiency-v1.md',)


def build(root, version, revision):
    if not re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+(?:-rc\.[0-9]+)?', version):
        raise ValueError('use vMAJOR.MINOR.PATCH or vMAJOR.MINOR.PATCH-rc.N')
    if not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', revision):
        raise ValueError('source revision must be an immutable Git SHA')
    files = {}
    for name in FILES:
        path = root / name
        if any(parent.is_symlink() for parent in (path, *path.parents)):
            raise ValueError('release source must not traverse symlinks')
        if not path.is_file() or path.stat().st_size > 1024 * 1024:
            raise ValueError('missing or oversized release source: ' + name)
        files[name] = path.read_bytes()
    manifest = {'schema': 'educloud-e1-release-v1', 'version': version,
                'source_revision': revision, 'runtime': 'Python 3.12+',
                'execution': 'offline_operator_tool_not_a_hosted_service',
                'files': {name: hashlib.sha256(raw).hexdigest() for name, raw in files.items()}}
    files['RELEASE-MANIFEST.json'] = (json.dumps(manifest, indent=2, sort_keys=True) + '\n').encode()
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo('educloud-e1-' + version + '/' + name, (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, files[name])
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', required=True)
    parser.add_argument('--out', type=Path, required=True, help='Fresh output directory')
    args = parser.parse_args()
    try:
        revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
        dirty = subprocess.check_output(['git', 'status', '--porcelain', '--', *FILES], cwd=ROOT, text=True)
        if dirty:
            raise ValueError('commit all release source before building')
        raw = build(ROOT, args.version, revision)
        args.out.mkdir(parents=False, exist_ok=False)
        name = 'educloud-e1-' + args.version + '.zip'
        (args.out / name).write_bytes(raw)
        (args.out / 'SHA256SUMS').write_text(hashlib.sha256(raw).hexdigest() + '  ' + name + '\n')
        print(json.dumps({'source_revision': revision, 'archive': str(args.out / name),
                          'sha256': hashlib.sha256(raw).hexdigest()}))
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(2, 'Release refused: ' + str(exc) + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
