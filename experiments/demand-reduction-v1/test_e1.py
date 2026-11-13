# SPDX-License-Identifier: Apache-2.0
"""Hermetic interchange controls; fabricated measurements never claim a live run."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import e1

ROOT = Path(__file__).resolve().parent
EVIDENCE = {'reference': 'test-only-not-authenticated', 'sha256': 'a' * 64}


def configured_plan():
    manifest = json.loads((ROOT / 'tasks.json').read_text())
    manifest['endpoint'] = {key: 'test-fixture-' + key for key in e1.PINS}
    manifest['execution_approval'] = EVIDENCE.copy()
    manifest['task_review'] = EVIDENCE.copy()
    return e1.make_plan(manifest, 27)


def test_measurements(plan, *, kind='fixture'):
    result = e1.result_template(plan)
    result['evidence_kind'] = kind
    result['actual_order'] = [row['workflow_id'] for row in result['workflows']]
    result['capture'] = {'application_complete': True,
                         'external_dispatch_complete': True, 'evidence': EVIDENCE.copy()}
    result['setup'] = {'operator_seconds': 10, 'reviewer_seconds': 10,
                       'operator_usd_per_hour': 3.6, 'reviewer_usd_per_hour': 3.6,
                       'cost_basis_evidence': EVIDENCE.copy()}
    for row in result['workflows']:
        candidate = row['workflow_id'].endswith('/candidate')
        row.update(status='complete', task_seconds=60 if candidate else 100,
                   operator_seconds=10, reviewer_seconds=10,
                   variable_cost_usd=0.03 if candidate else 0.05,
                   other_variable_cost_usd=0.009 if candidate else 0.029,
                   completion_evidence=EVIDENCE.copy(),
                   output_sha256='b' * 64,
                   review={'reviewer_id': 'test-reviewer', 'evidence': EVIDENCE.copy(),
                           'useful': True, 'severe_regression': False,
                           'critical_failure': False},
                   attempts=[{'attempt_id': row['workflow_id'] + '/attempt1',
                              'outcome': 'complete', 'dispatches': 1,
                              'input_tokens': 100 if candidate else 200,
                              'output_tokens': 20, 'actual_cost_usd': 0.001,
                              'cost_kind': 'provider_reported',
                              'unresolved_cost_hold_usd': 0,
                              'evidence': EVIDENCE.copy()}])
    ordinary = copy.deepcopy(result['workflows'][0])
    ordinary.update(workflow_id=plan['ordinary_controls'][0], condition_sha256=None,
                    attempts=[], variable_cost_usd=0.02, other_variable_cost_usd=0,
                    completion_kind='deterministic')
    result['workflows'].append(ordinary)
    result['ai_off_journey'] = {'workflow_id': ordinary['workflow_id'],
                                'saved_sha256': 'b' * 64, 'reopened_sha256': 'b' * 64,
                                'exported_sha256': 'b' * 64, 'evidence': EVIDENCE.copy()}
    return result


class E1Tests(unittest.TestCase):
    def setUp(self):
        self.plan = configured_plan()
        # Only test the measured-evidence branch; these are invented unit inputs,
        # not a stored report of an actual experiment.
        self.results = test_measurements(self.plan, kind='measured')

    def report(self):
        return e1.summarize(self.plan, self.results)

    def first_attempt(self):
        return self.results['workflows'][0]['attempts'][0]

    def assert_incomplete(self):
        self.assertEqual(self.report()['disposition'], 'incomplete')

    def test_sample_is_unavailable_balanced_reproducible_and_review_pending(self):
        manifest = e1.read_json(ROOT / 'tasks.json')
        plan = e1.make_plan(manifest, 20261113)
        self.assertEqual(plan, e1.make_plan(manifest, 20261113))
        self.assertEqual(plan['execution_state'], 'execution_unavailable')
        self.assertEqual(len(plan['schedule']), 48)
        self.assertEqual(sum(row['arm'] == 'candidate' for row in plan['schedule'][::2]), 12)
        self.assertEqual(len({row['workflow_id'] for row in plan['schedule']}), 48)
        self.assertEqual(e1.summarize(plan, e1.result_template(plan))['disposition'], 'incomplete')

    def test_preparation_never_claims_measurement_or_observed_order(self):
        template = e1.result_template(self.plan)
        self.assertEqual(template['evidence_kind'], 'preparation')
        self.assertIsNone(template['actual_order'])
        report = e1.summarize(self.plan, template)
        self.assertEqual(report['evidence_kind'], 'preparation')
        self.assertEqual(report['disposition'], 'incomplete')
        self.results['actual_order'] = None
        self.assert_incomplete()

    def test_screening_calculation_and_paired_accounting(self):
        report = self.report()
        self.assertEqual(report['disposition'], 'screening_pass')
        self.assertEqual(report['observed_totals']['attempts'], 48)
        self.assertEqual(report['observed_totals']['dispatches'], 48)
        self.assertAlmostEqual(report['observed_totals']['model_cost_usd'], 0.048)
        self.assertAlmostEqual(report['comparisons']['time_reduction'], 0.4)
        self.assertAlmostEqual(report['comparisons']['cost_per_useful_reduction'], 0.4)
        self.assertEqual(len(report['paired']), 24)
        self.assertEqual(report['paired'][0]['task_seconds_candidate_minus_baseline'], -40)
        self.assertEqual(report['results_sha256'], e1.digest(self.results))

    def test_fixture_cannot_pass(self):
        self.results['evidence_kind'] = 'fixture'
        self.assert_incomplete()

    def test_all_review_and_approval_references_needed(self):
        for field in ('task_review', 'execution_approval', 'endpoint'):
            with self.subTest(field=field):
                manifest = copy.deepcopy(self.plan['manifest'])
                manifest[field] = None
                plan = e1.make_plan(manifest, 27)
                results = test_measurements(plan, kind='measured')
                self.assertEqual(e1.summarize(plan, results)['disposition'], 'incomplete')

    def test_changed_plan_result_and_endpoint_pins_rejected(self):
        plan = copy.deepcopy(self.plan)
        plan['manifest']['tasks'][0]['candidate_prompt'] += ' extra'
        with self.assertRaisesRegex(ValueError, 'altered'):
            e1.summarize(plan, self.results)
        self.results['plan_sha256'] = 'c' * 64
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            self.report()
        self.results['plan_sha256'] = self.plan['plan_sha256']
        self.results['workflows'][0]['condition_sha256'] = 'c' * 64
        with self.assertRaisesRegex(ValueError, 'condition'):
            self.report()

    def test_missing_and_duplicate_workflow_attempt_identities(self):
        row = self.results['workflows'].pop(0)
        self.results['actual_order'].remove(row['workflow_id'])
        self.assert_incomplete()
        self.results['workflows'].append(self.results['workflows'][0])
        with self.assertRaisesRegex(ValueError, 'duplicate workflow'):
            self.report()
        self.results = test_measurements(self.plan, kind='measured')
        self.results['workflows'][1]['attempts'][0]['attempt_id'] = self.first_attempt()['attempt_id']
        with self.assertRaisesRegex(ValueError, 'duplicate attempt'):
            self.report()

    def test_usage_cost_unknown_hold_and_estimate_remain_incomplete(self):
        for field, value in (('input_tokens', None), ('output_tokens', None),
                             ('actual_cost_usd', None), ('cost_kind', 'estimate'),
                             ('unresolved_cost_hold_usd', 0.1), ('evidence', None),
                             ('outcome', 'unknown')):
            with self.subTest(field=field):
                self.results = test_measurements(self.plan, kind='measured')
                self.first_attempt()[field] = value
                if field == 'cost_kind':
                    self.first_attempt()['actual_cost_usd'] = None
                if field == 'outcome':
                    self.results['workflows'][0]['status'] = value
                    self.results['workflows'][0]['review']['useful'] = False
                self.assert_incomplete()

    def test_token_cost_and_staff_ceilings(self):
        for field, value in (('input_tokens', 4097), ('output_tokens', 513),
                             ('actual_cost_usd', 10.1)):
            with self.subTest(field=field):
                self.results = test_measurements(self.plan, kind='measured')
                self.first_attempt()[field] = value
                self.results['workflows'][0]['variable_cost_usd'] = 11
                self.results['workflows'][0]['other_variable_cost_usd'] = 11 - 0.02 - self.first_attempt()['actual_cost_usd']
                self.assertEqual(self.report()['disposition'], 'screening_fail')
        for field in ('operator_seconds', 'reviewer_seconds'):
            self.results = test_measurements(self.plan, kind='measured')
            self.results['setup'][field] = e1.LIMITS[field] + 1
            self.assertEqual(self.report()['disposition'], 'screening_fail')

    def test_repair_attempts_count_even_when_not_dispatched(self):
        for row in self.results['workflows'][:-1]:
            denied = copy.deepcopy(row['attempts'][0])
            denied.update(attempt_id=row['workflow_id'] + '/repair', outcome='denied',
                          dispatches=0, input_tokens=0, output_tokens=0, actual_cost_usd=0)
            row['attempts'].append(denied)
        report = self.report()
        self.assertEqual(report['observed_totals']['attempts'], 96)
        self.assertEqual(report['observed_totals']['dispatches'], 48)
        self.results['workflows'][0]['attempts'].append(copy.deepcopy(self.first_attempt()))
        with self.assertRaisesRegex(ValueError, 'two attempts'):
            self.report()

    def test_human_review_and_capture_required(self):
        self.results['workflows'][0]['review'] = None
        self.assert_incomplete()
        for field in ('application_complete', 'external_dispatch_complete', 'evidence'):
            self.results = test_measurements(self.plan, kind='measured')
            self.results['capture'][field] = None if field == 'evidence' else False
            self.assert_incomplete()

    def test_unknown_and_terminal_output(self):
        self.results['workflows'][0]['status'] = 'unknown'
        self.results['workflows'][0]['review']['useful'] = False
        self.assert_incomplete()
        self.results = test_measurements(self.plan, kind='measured')
        self.first_attempt()['outcome'] = 'failed'
        with self.assertRaisesRegex(ValueError, 'without complete call'):
            self.report()
        self.first_attempt()['outcome'] = 'complete'
        self.results['workflows'][0]['output_sha256'] = None
        with self.assertRaisesRegex(ValueError, 'output identity'):
            self.report()

    def test_regression_and_critical_failure_never_pass(self):
        for field in ('severe_regression', 'critical_failure'):
            self.results = test_measurements(self.plan, kind='measured')
            self.results['workflows'][0]['review'][field] = True
            self.assertEqual(self.report()['disposition'], 'screening_fail')
        self.results = test_measurements(self.plan, kind='measured')
        next(r for r in self.results['workflows'] if r['workflow_id'].endswith('/candidate'))['review']['useful'] = False
        self.assertEqual(self.report()['disposition'], 'screening_fail')

    def test_checking_effort_can_remove_apparent_token_savings(self):
        for row in self.results['workflows']:
            if row['workflow_id'].endswith('/candidate'):
                row['task_seconds'] = 200
                row['reviewer_seconds'] = 150
                row['variable_cost_usd'] = 0.2
                row['other_variable_cost_usd'] = 0.039
        self.assertEqual(self.report()['disposition'], 'screening_fail')

    def test_no_useful_candidate_is_failure_not_missing_denominator(self):
        for row in self.results['workflows']:
            if row['workflow_id'].endswith('/candidate'):
                row['review']['useful'] = False
        self.assertEqual(self.report()['disposition'], 'screening_fail')

    def test_exact_twenty_percent_saving_boundary(self):
        for row in self.results['workflows']:
            if row['workflow_id'].endswith('/candidate'):
                row.update(task_seconds=100, variable_cost_usd=0.04,
                           other_variable_cost_usd=0.019)
        self.assertEqual(self.report()['disposition'], 'screening_pass')
        for row in self.results['workflows']:
            if row['workflow_id'].endswith('/candidate'):
                row['variable_cost_usd'] += 0.00001
                row['other_variable_cost_usd'] += 0.00001
        self.assertEqual(self.report()['disposition'], 'screening_fail')

    def test_zero_priced_route_does_not_invent_cost_saving(self):
        self.results['setup']['operator_usd_per_hour'] = 0
        self.results['setup']['reviewer_usd_per_hour'] = 0
        for row in self.results['workflows']:
            row['variable_cost_usd'] = 0
            row['other_variable_cost_usd'] = 0
            for attempt in row['attempts']:
                attempt['actual_cost_usd'] = 0
        report = self.report()
        self.assertEqual(report['disposition'], 'screening_pass')
        self.assertIsNone(report['comparisons']['cost_per_useful_reduction'])

    def test_actual_order_and_ai_off_bytes_and_dispatches(self):
        self.results['actual_order'].reverse()
        self.assert_incomplete()
        self.results = test_measurements(self.plan, kind='measured')
        self.results['ai_off_journey']['exported_sha256'] = 'c' * 64
        self.assert_incomplete()
        self.results = test_measurements(self.plan, kind='measured')
        self.results['workflows'][-1]['attempts'] = [copy.deepcopy(self.first_attempt())]
        with self.assertRaisesRegex(ValueError, 'AI-off'):
            self.report()

    def test_zero_call_candidate_is_measurable_with_deterministic_evidence(self):
        row = next(r for r in self.results['workflows'] if r['workflow_id'].endswith('/candidate'))
        row.update(completion_kind='deterministic', condition_sha256=None, attempts=[],
                   variable_cost_usd=0.029)
        report = self.report()
        self.assertEqual(report['disposition'], 'screening_pass')
        self.assertEqual(report['observed_totals']['dispatches'], 47)
        row['completion_evidence'] = None
        self.assert_incomplete()

    def test_labor_cost_is_computed_not_asserted(self):
        for row in self.results['workflows']:
            row['task_seconds'] = 100
            if row['workflow_id'].endswith('/candidate'):
                row['reviewer_seconds'] = 85
        with self.assertRaisesRegex(ValueError, 'does not reconcile'):
            self.report()
        self.results = test_measurements(self.plan, kind='measured')
        self.results['setup']['reviewer_usd_per_hour'] = None
        self.assert_incomplete()

    def test_known_unsuccessful_outcomes_are_retained_not_missing(self):
        for status in ('denied', 'unavailable', 'failed', 'timeout', 'cancelled', 'abandoned'):
            with self.subTest(status=status):
                self.results = test_measurements(self.plan, kind='measured')
                row = next(r for r in self.results['workflows'] if r['workflow_id'].endswith('/baseline'))
                row['status'] = status
                row['review']['useful'] = False
                row['attempts'][0]['outcome'] = status
                report = self.report()
                self.assertEqual(report['missing'], [])
                self.assertEqual(report['arms']['baseline']['outcomes'][status], 1)

    def test_cancelled_or_abandoned_work_keeps_charges_and_liability(self):
        for status in ('cancelled', 'abandoned'):
            self.results = test_measurements(self.plan, kind='measured')
            row = self.results['workflows'][0]
            row['status'] = status
            row['review']['useful'] = False
            row['attempts'][0].update(outcome=status, unresolved_cost_hold_usd=0.5)
            report = self.report()
            self.assertEqual(report['disposition'], 'incomplete')
            self.assertEqual(report['observed_totals']['known_unresolved_cost_hold_usd'], 0.5)
            self.assertAlmostEqual(report['observed_totals']['model_cost_usd'], 0.048)

    def test_holds_are_reported_apart_from_actual_cost_and_estimates(self):
        self.first_attempt()['unresolved_cost_hold_usd'] = 0.5
        report = self.report()
        self.assertEqual(report['disposition'], 'incomplete')
        self.assertEqual(report['observed_totals']['known_unresolved_cost_hold_usd'], 0.5)
        self.assertAlmostEqual(report['observed_totals']['model_cost_usd'], 0.048)
        self.first_attempt()['unresolved_cost_hold_usd'] = None
        self.assertEqual(self.report()['observed_totals']['unknown_cost_hold_count'], 1)
        self.first_attempt()['cost_kind'] = 'estimate'
        with self.assertRaisesRegex(ValueError, 'actual charges'):
            self.report()

    def test_bad_numerics_and_misclassified_scope(self):
        for value in (True, -1, float('nan'), float('inf')):
            self.results = test_measurements(self.plan, kind='measured')
            self.results['workflows'][0]['task_seconds'] = value
            with self.assertRaisesRegex(ValueError, 'numeric'):
                self.report()
        for value in ('private', 'student', 'protected'):
            manifest = copy.deepcopy(self.plan['manifest'])
            manifest['tasks'][0]['data_scope'] = value
            with self.assertRaisesRegex(ValueError, 'scope'):
                e1.make_plan(manifest, 27)

    def test_cli_roundtrip_exclusive_outputs_and_duplicate_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def run(*args):
                return subprocess.run([sys.executable, str(ROOT / 'e1.py'), *map(str, args)],
                                      capture_output=True, text=True)
            args = ('plan', '--manifest', ROOT / 'tasks.json', '--out', root / 'plan.json')
            self.assertEqual(run(*args).returncode, 0)
            before = (root / 'plan.json').read_bytes()
            self.assertEqual(run(*args).returncode, 2)
            self.assertEqual((root / 'plan.json').read_bytes(), before)
            self.assertEqual(run('template', '--plan', root / 'plan.json', '--out', root / 'results.json').returncode, 0)
            report = run('report', '--plan', root / 'plan.json', '--results', root / 'results.json', '--out', root / 'report.json')
            self.assertEqual(report.returncode, 1, report.stderr)
            self.assertEqual(json.loads((root / 'report.json').read_text())['disposition'], 'incomplete')
            (root / 'bad.json').write_text('{"schema":1,"schema":2}')
            with self.assertRaisesRegex(ValueError, 'duplicate'):
                e1.read_json(root / 'bad.json')


if __name__ == '__main__':
    unittest.main()
