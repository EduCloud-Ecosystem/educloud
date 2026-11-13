# SPDX-License-Identifier: Apache-2.0
"""Build a bounded, deterministic E1 source release; no network or execution."""
import argparse
from datetime import UTC, datetime
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


def build_sbom(raw, name, version, revision, created):
    """Describe the emitted ZIP using only its bytes and known source provenance."""
    package_id = 'SPDXRef-E1-Source'
    files = []
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        for index, path in enumerate(archive.namelist(), start=1):
            payload = archive.read(path)
            header = b'# SPDX-License-Identifier: Apache-2.0'
            # The release license scope covers its Python tools and tests.
            license_in_file = 'NOASSERTION'
            if path.endswith('.py') and header in payload.splitlines()[:2]:
                license_in_file = 'Apache-2.0'
            files.append({
                'SPDXID': f'SPDXRef-File-{index}',
                'fileName': './' + path,
                'checksums': [
                    {'algorithm': 'SHA1', 'checksumValue': hashlib.sha1(payload, usedforsecurity=False).hexdigest()},
                    {'algorithm': 'SHA256', 'checksumValue': hashlib.sha256(payload).hexdigest()},
                ],
                'licenseInfoInFiles': [license_in_file],
                'licenseConcluded': 'NOASSERTION',
                'copyrightText': 'NOASSERTION',
            })
    file_sha1s = sorted(file['checksums'][0]['checksumValue'] for file in files)
    document = {
        'spdxVersion': 'SPDX-2.3',
        'dataLicense': 'CC0-1.0',
        'SPDXID': 'SPDXRef-DOCUMENT',
        'name': name,
        'creationInfo': {
            'created': created,
            'creators': ['Tool: educloud-e1-release-' + version],
        },
        'packages': [{
            'SPDXID': package_id,
            'name': 'educloud-e1',
            'versionInfo': version,
            'packageFileName': name,
            'downloadLocation': 'NOASSERTION',
            'filesAnalyzed': True,
            'packageVerificationCode': {
                'packageVerificationCodeValue': hashlib.sha1(
                    ''.join(file_sha1s).encode('ascii'), usedforsecurity=False
                ).hexdigest(),
            },
            'checksums': [{'algorithm': 'SHA256', 'checksumValue': hashlib.sha256(raw).hexdigest()}],
            'sourceInfo': 'EduCloud Git revision https://github.com/EduCloud-Ecosystem/educloud/commit/' + revision,
            'licenseDeclared': 'NOASSERTION',
            'licenseConcluded': 'NOASSERTION',
            'licenseComments': 'Python headers have limited scope. See the bundled LICENSING.md.',
            'copyrightText': 'NOASSERTION',
        }],
        'files': files,
        'relationships': [
            {'spdxElementId': 'SPDXRef-DOCUMENT', 'relationshipType': 'DESCRIBES',
             'relatedSpdxElement': package_id},
            {'spdxElementId': package_id, 'relationshipType': 'DEPENDS_ON',
             'relatedSpdxElement': 'NOASSERTION',
             'comment': 'Requires external Python 3.12+ and its standard library. '
                        'The specific runtime and its transitive dependencies are outside this source inventory.'},
            *({'spdxElementId': package_id, 'relationshipType': 'CONTAINS',
               'relatedSpdxElement': file['SPDXID']} for file in files),
        ],
    }
    # A change to the inventory or its creation metadata gets a distinct namespace.
    digest = hashlib.sha256(json.dumps(document, sort_keys=True).encode()).hexdigest()
    document['documentNamespace'] = 'https://github.com/EduCloud-Ecosystem/educloud/spdx/e1/' + digest
    return (json.dumps(document, indent=2, sort_keys=True) + '\n').encode()


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
        name = 'educloud-e1-' + args.version + '.zip'
        sbom_name = 'educloud-e1-' + args.version + '.spdx.json'
        created = datetime.now(UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
        artifacts = {name: raw, sbom_name: build_sbom(raw, name, args.version, revision, created)}
        args.out.mkdir(parents=False, exist_ok=False)
        for filename, payload in artifacts.items():
            (args.out / filename).write_bytes(payload)
        (args.out / 'SHA256SUMS').write_text(''.join(
            hashlib.sha256(payload).hexdigest() + '  ' + filename + '\n'
            for filename, payload in artifacts.items()
        ))
        print(json.dumps({'source_revision': revision, 'archive': str(args.out / name),
                          'sbom': str(args.out / sbom_name),
                          'sha256': hashlib.sha256(raw).hexdigest()}))
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(2, 'Release refused: ' + str(exc) + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
