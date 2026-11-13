# SPDX-License-Identifier: Apache-2.0
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

import release


class ReleaseTests(unittest.TestCase):
    def test_deterministic_allowlist_and_source_manifest(self):
        raw = release.build(release.ROOT, 'v1.0.0-rc.1', 'a' * 40)
        self.assertEqual(raw, release.build(release.ROOT, 'v1.0.0-rc.1', 'a' * 40))
        prefix = 'educloud-e1-v1.0.0-rc.1/'
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            self.assertEqual(set(archive.namelist()),
                             {prefix + path for path in release.FILES} | {prefix + 'RELEASE-MANIFEST.json'})
            manifest = json.loads(archive.read(prefix + 'RELEASE-MANIFEST.json'))
            for name, expected in manifest['files'].items():
                self.assertEqual(hashlib.sha256(archive.read(prefix + name)).hexdigest(), expected)

    def test_extracted_tool_tests_and_unavailable_roundtrip(self):
        raw = release.build(release.ROOT, 'v1.0.0-rc.1', 'a' * 40)
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                # Only the just-built source allowlist, never untrusted archives.
                archive.extractall(tmp)
            root = Path(tmp) / 'educloud-e1-v1.0.0-rc.1'
            module = root / release.MODULE
            tests = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s',
                                    str(module), '-p', 'test_e1.py'], capture_output=True, text=True)
            self.assertEqual(tests.returncode, 0, tests.stderr)
            cases = [(['plan', '--manifest', str(module / 'tasks.json'), '--out', str(root / 'plan.json')], 0),
                     (['template', '--plan', str(root / 'plan.json'), '--out', str(root / 'results.json')], 0),
                     (['report', '--plan', str(root / 'plan.json'), '--results', str(root / 'results.json'), '--out', str(root / 'report.json')], 1)]
            for args, code in cases:
                run = subprocess.run([sys.executable, str(module / 'e1.py'), *args], capture_output=True, text=True)
                self.assertEqual(run.returncode, code, run.stderr)
            report = json.loads((root / 'report.json').read_text())
            self.assertEqual(report['evidence_kind'], 'preparation')
            self.assertEqual(report['disposition'], 'incomplete')

    def test_sbom_matches_archive_and_limits_license_claims(self):
        version = 'v1.0.0-rc.1'
        name = f'educloud-e1-{version}.zip'
        revision = 'a' * 40
        created = '2026-11-13T20:00:00Z'
        raw = release.build(release.ROOT, version, revision)
        sbom = release.build_sbom(raw, name, version, revision, created)
        self.assertEqual(sbom, release.build_sbom(raw, name, version, revision, created))
        doc = json.loads(sbom)
        later = json.loads(release.build_sbom(raw, name, version, revision, '2026-11-13T20:00:01Z'))
        self.assertNotEqual(doc['documentNamespace'], later['documentNamespace'])
        self.assertEqual(doc['spdxVersion'], 'SPDX-2.3')
        self.assertEqual(doc['dataLicense'], 'CC0-1.0')
        self.assertEqual(doc['creationInfo']['created'], created)

        package, = doc['packages']
        self.assertEqual(package['packageFileName'], name)
        self.assertEqual(package['versionInfo'], version)
        self.assertTrue(package['sourceInfo'].endswith('/commit/' + revision))
        self.assertEqual(package['checksums'], [
            {'algorithm': 'SHA256', 'checksumValue': hashlib.sha256(raw).hexdigest()}
        ])
        for field in ('licenseDeclared', 'licenseConcluded', 'downloadLocation', 'copyrightText'):
            self.assertEqual(package[field], 'NOASSERTION')

        files = {file['fileName']: file for file in doc['files']}
        ids = {file['SPDXID'] for file in doc['files']}
        self.assertEqual(len(ids), len(doc['files']))
        sha1s = []
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            self.assertCountEqual([file['fileName'] for file in doc['files']],
                                  ['./' + path for path in archive.namelist()])
            for path in archive.namelist():
                with self.subTest(path=path):
                    file = files['./' + path]
                    payload = archive.read(path)
                    sha1 = hashlib.sha1(payload, usedforsecurity=False).hexdigest()
                    sha1s.append(sha1)
                    self.assertEqual(
                        {entry['algorithm']: entry['checksumValue'] for entry in file['checksums']},
                        {'SHA1': sha1, 'SHA256': hashlib.sha256(payload).hexdigest()},
                    )
                    expected = 'Apache-2.0' if path.endswith('.py') else 'NOASSERTION'
                    self.assertEqual(file['licenseInfoInFiles'], [expected])
                    self.assertEqual(file['licenseConcluded'], 'NOASSERTION')
        self.assertEqual(package['packageVerificationCode']['packageVerificationCodeValue'],
                         hashlib.sha1(''.join(sorted(sha1s)).encode(), usedforsecurity=False).hexdigest())
        self.assertCountEqual(
            [(rel['spdxElementId'], rel['relationshipType'], rel['relatedSpdxElement'])
             for rel in doc['relationships']],
            [(doc['SPDXID'], 'DESCRIBES', package['SPDXID']),
             (package['SPDXID'], 'DEPENDS_ON', 'NOASSERTION'),
             *((package['SPDXID'], 'CONTAINS', file_id) for file_id in ids)],
        )

    def test_version_and_symlink_refusal(self):
        with self.assertRaises(ValueError):
            release.build(release.ROOT, '../unsafe', 'a' * 40)
        with self.assertRaises(ValueError):
            release.build(release.ROOT, 'v1.0.0', 'main')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'experiments').symlink_to(release.ROOT / 'experiments', target_is_directory=True)
            with self.assertRaisesRegex(ValueError, 'symlink'):
                release.build(root, 'v1.0.0', 'a' * 40)


if __name__ == '__main__':
    unittest.main()
