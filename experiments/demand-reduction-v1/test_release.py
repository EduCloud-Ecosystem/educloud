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
