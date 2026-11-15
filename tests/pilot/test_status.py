import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('pilot_status', ROOT / 'tools/pilot/status.py')
status = importlib.util.module_from_spec(spec)
spec.loader.exec_module(status)
vspec = importlib.util.spec_from_file_location('pilot_verify', ROOT / '.github/educloud/verify.py')
verify = importlib.util.module_from_spec(vspec)
vspec.loader.exec_module(verify)


class StatusControls(unittest.TestCase):
    def setUp(self):
        self.readiness = json.loads((ROOT / 'pilot/readiness.json').read_text())
        self.snapshot = {'schema_version': 1, 'observed_at': '2026-11-15T00:00:00+00:00',
                         'components': [{'repository': name, 'head': 'a' * 40, 'declared_protocol': 'v1 matches',
                             'checks': {'passed': 1, 'failed': 1, 'pending': 1, 'skipped_or_cancelled': 1},
                             'checks_truncated': False, 'open_prs_observed': 0, 'prs_truncated': False}
                             for name in status.ALLOWED]}

    def test_failed_and_pending_checks_stay_visible(self):
        text = status.render(self.snapshot, self.readiness)
        self.assertIn('1 failed', text)
        self.assertIn('1 pending', text)
        self.assertIn('Student deployment: pending', text)
        self.assertIn('not a release verdict', text)

    def test_readiness_cannot_be_promoted_by_metadata(self):
        self.readiness['student_admission'] = True
        with self.assertRaises(ValueError): status.render(self.snapshot, self.readiness)

    def test_unknown_or_injected_repository_is_rejected(self):
        self.snapshot['components'][0]['repository'] = '<script>unexpected</script>'
        with self.assertRaises(ValueError): status.render(self.snapshot, self.readiness)

    def test_incomplete_snapshot_rejected(self):
        self.snapshot['components'].pop()
        with self.assertRaises(ValueError): status.render(self.snapshot, self.readiness)

    def test_invalid_commit_rejected(self):
        self.snapshot['components'][0]['head'] = 'latest'
        with self.assertRaises(ValueError): status.render(self.snapshot, self.readiness)

    def test_truncation_visible(self):
        self.snapshot['components'][0].update(checks_truncated=True, prs_truncated=True, open_prs_observed=50)
        text = status.render(self.snapshot, self.readiness)
        self.assertIn('incomplete page', text)
        self.assertIn('50+', text)

    def test_generated_region_preserves_surrounding_text(self):
        original = 'prefix\n' + status.START + '\nold\n' + status.END + '\nsuffix'
        self.assertEqual(status.update_readme(original, status.START + '\nnew\n' + status.END),
                         'prefix\n' + status.START + '\nnew\n' + status.END + '\nsuffix')
        with self.assertRaises(ValueError): status.update_readme(original + status.START, 'x')

    def test_private_repository_stops_acquisition(self):
        with patch.object(status, 'api', return_value={'private': True}):
            with self.assertRaises(ValueError): status.collect()

    def test_latest_check_wins_and_failures_are_counted(self):
        checks = {'total_count': 3, 'check_runs': [
            {'id': 1, 'name': 'tests', 'status': 'completed', 'conclusion': 'success'},
            {'id': 2, 'name': 'tests', 'status': 'completed', 'conclusion': 'failure'},
            {'id': 3, 'name': 'review', 'status': 'in_progress', 'conclusion': None}]}
        answers = [{'private': False}, {'object': {'sha': 'a' * 40}}, checks, [], None] * 6
        with patch.object(status, 'api', side_effect=answers) as api:
            snapshot = status.collect()
        self.assertEqual(api.call_count, 30)
        self.assertEqual(snapshot['components'][0]['checks'],
                         {'passed': 0, 'failed': 1, 'pending': 1, 'skipped_or_cancelled': 0})

    def test_acquisition_failure_does_not_write_previous_snapshot(self):
        old = (ROOT / 'pilot/readiness.json').read_bytes()
        with patch.object(status, 'api', side_effect=RuntimeError('offline')):
            with self.assertRaises(RuntimeError): status.collect()
        self.assertEqual((ROOT / 'pilot/readiness.json').read_bytes(), old)

    def test_existing_proposal_prevents_duplicate_writes(self):
        with patch.object(status, 'api', return_value=[{'head': {'ref': 'codex/pilot-status-existing'}}]) as api:
            status.propose()
        self.assertEqual(api.call_count, 1)

    def test_write_proposal_has_exact_allowlist_and_no_ready_file(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); (root / 'pilot').mkdir()
            (root / 'README.md').write_text('reviewed README')
            (root / 'pilot/status.json').write_text('{}')
            answers = [[], {'object': {'sha': 'a' * 40}}, {'tree': {'sha': 'b' * 40}},
                       {'sha': 'c' * 40}, {'sha': 'd' * 40}, {}, {'html_url': 'https://github.com/example/pr'}, None]
            with patch.object(status, 'api', side_effect=answers) as api, patch.object(status.subprocess, 'check_output', return_value='a' * 40):
                status.propose(root)
            tree = api.call_args_list[3].args[1]['tree']
            self.assertEqual([entry['path'] for entry in tree], ['README.md', 'pilot/status.json'])
            self.assertTrue(api.call_args_list[-1].args[0].endswith('/pilot-protocol.yml/dispatches'))

    def test_policy_copy_drift_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ['.github/educloud/component.json', 'docs/development/PILOT_PROTOCOL_V1.md', 'AGENTS.md']:
                p = root / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes((ROOT / name).read_bytes())
            with (root / 'docs/development/PILOT_PROTOCOL_V1.md').open('a') as f: f.write('\nUnreviewed drift')
            with self.assertRaisesRegex(ValueError, 'differs'): verify.verify(root)


if __name__ == '__main__': unittest.main()
