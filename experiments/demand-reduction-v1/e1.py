# SPDX-License-Identifier: Apache-2.0
"""Offline E1 plan and content-free result interchange. Never invokes a model."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import random
import re
import sys

CATEGORIES = ('course_hint', 'source_qa', 'routine_draft', 'data_code')
PINS = {'endpoint_id', 'provider', 'model_revision', 'runtime_revision',
        'tokenizer_revision', 'sampling_revision'}
LIMITS = {'workflows': 48, 'attempts': 96, 'input_tokens_per_call': 4096,
          'output_tokens_per_call': 512, 'operator_seconds': 14400,
          'reviewer_seconds': 7200, 'model_cost_usd': 10}
OUTCOMES = {'complete', 'unavailable', 'denied', 'failed', 'timeout', 'unknown',
            'cancelled', 'abandoned'}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def keys(value, expected, label):
    require(isinstance(value, dict) and set(value) == set(expected),
            label + ': unexpected or missing fields')


def label(value):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= 4096


def number(value):
    return type(value) in (int, float) and math.isfinite(value) and value >= 0


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, allow_nan=False).encode('utf-8')


def hex_digest(value):
    return isinstance(value, str) and re.fullmatch('[0-9a-f]{64}', value) is not None


def evidence(value):
    return (isinstance(value, dict) and set(value) == {'reference', 'sha256'}
            and label(value['reference']) and hex_digest(value['sha256']))


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'duplicate JSON key: ' + key)
            result[key] = value
        return result
    require(path.stat().st_size <= 4 * 1024 * 1024, 'JSON exceeds 4 MiB')
    def reject(_):
        raise ValueError('non-finite JSON number')
    return json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_constant=reject)


def validate_manifest(manifest):
    keys(manifest, {'schema', 'data_scope', 'task_review', 'endpoint',
                    'execution_approval', 'candidate_description', 'tasks'}, 'manifest')
    require(manifest['schema'] == 'educloud-e1-manifest-v1', 'manifest version')
    require(manifest['data_scope'] == 'public_synthetic', 'public/synthetic only')
    require(label(manifest['candidate_description']), 'candidate method must be explicit')
    for field in ('task_review', 'execution_approval'):
        require(manifest[field] is None or evidence(manifest[field]), field)
    endpoint = manifest['endpoint']
    if endpoint is not None:
        keys(endpoint, PINS, 'endpoint')
        require(all(label(v) for v in endpoint.values()), 'endpoint pins required')
    tasks = manifest['tasks']
    require(isinstance(tasks, list) and len(tasks) == 24, 'exactly 24 E1 tasks')
    ids = set()
    counts = dict.fromkeys(CATEGORIES, 0)
    for task in tasks:
        keys(task, {'id', 'category', 'data_scope', 'source', 'baseline_prompt',
                    'candidate_prompt', 'ordinary_alternative',
                    'expected_properties'}, 'task')
        require(label(task['id']) and task['id'] not in ids, 'unique task ids')
        ids.add(task['id'])
        require(task['category'] in CATEGORIES, 'unknown task category')
        counts[task['category']] += 1
        require(task['data_scope'] in ('synthetic', 'public'), 'task scope')
        for field in ('source', 'baseline_prompt', 'candidate_prompt',
                      'ordinary_alternative'):
            require(label(task[field]), 'task requires ' + field)
        properties = task['expected_properties']
        require(isinstance(properties, list) and 1 <= len(properties) <= 12
                and all(label(v) for v in properties), 'expected properties')
    require(set(counts.values()) == {6}, 'six tasks in each category')


def make_plan(manifest, seed):
    validate_manifest(manifest)
    require(type(seed) is int and 0 <= seed < 2**32, 'seed must be uint32')
    rng = random.Random(seed)
    tasks = list(manifest['tasks'])
    rng.shuffle(tasks)
    # Counterbalanced pair ordering: exactly half candidate-first.
    first = ['baseline'] * 12 + ['candidate'] * 12
    rng.shuffle(first)
    schedule = []
    for task, arm in zip(tasks, first):
        for selected in (arm, 'candidate' if arm == 'baseline' else 'baseline'):
            schedule.append({'workflow_id': task['id'] + '/' + selected,
                             'task_id': task['id'], 'arm': selected})
    body = {'schema': 'educloud-e1-plan-v1', 'manifest': manifest,
            'seed': seed, 'limits': LIMITS.copy(), 'schedule': schedule,
            'ordinary_controls': [task['id'] + '/ordinary' for task in tasks],
            'condition_sha256': digest(manifest['endpoint']),
            'execution_state': 'configured_requires_external_authority' if all(
                manifest[k] is not None for k in
                ('endpoint', 'execution_approval', 'task_review'))
                else 'execution_unavailable',
            'screening': {'minimum_reduction': 0.20,
                          'maximum_other_measure_increase': 0.05}}
    return {**body, 'plan_sha256': digest(body)}


def validate_plan(plan):
    require(isinstance(plan, dict) and 'manifest' in plan and 'seed' in plan,
            'invalid plan')
    require(plan == make_plan(plan['manifest'], plan['seed']),
            'plan altered or not reproducible')


def result_template(plan):
    validate_plan(plan)
    rows = []
    for entry in plan['schedule']:
        rows.append({'workflow_id': entry['workflow_id'],
                     'condition_sha256': plan['condition_sha256'],
                     'completion_kind': 'model_assisted', 'completion_evidence': None,
                     'status': 'unavailable', 'attempts': [],
                     'task_seconds': None, 'operator_seconds': None,
                     'reviewer_seconds': None, 'variable_cost_usd': None,
                     'other_variable_cost_usd': None,
                     'review': None, 'output_sha256': None})
    return {'schema': 'educloud-e1-results-v1', 'plan_sha256': plan['plan_sha256'],
            'evidence_kind': 'preparation',
            'capture': {'application_complete': False,
                        'external_dispatch_complete': False, 'evidence': None},
            'actual_order': None,
            'setup': {'operator_seconds': None, 'reviewer_seconds': None,
                      'operator_usd_per_hour': None, 'reviewer_usd_per_hour': None,
                      'cost_basis_evidence': None},
            'workflows': rows, 'ai_off_journey': None}


def summarize(plan, results):
    """Validate interchange and screen supplied evidence, not its authenticity."""
    validate_plan(plan)
    keys(results, {'schema', 'plan_sha256', 'evidence_kind', 'capture',
                   'actual_order', 'setup', 'workflows', 'ai_off_journey'}, 'results')
    require(results['schema'] == 'educloud-e1-results-v1', 'results version')
    require(results['plan_sha256'] == plan['plan_sha256'], 'results/plan mismatch')
    require(results['evidence_kind'] in ('preparation', 'fixture', 'measured'), 'evidence kind')
    missing, failures = [], []
    if plan['execution_state'] == 'execution_unavailable':
        missing.append('Endpoint, task review or execution approval is unconfigured.')
    if results['evidence_kind'] != 'measured':
        missing.append('Preparation/fixture evidence cannot establish observed E1 performance.')
    capture = results['capture']
    keys(capture, {'application_complete', 'external_dispatch_complete',
                   'evidence'}, 'capture')
    for field in ('application_complete', 'external_dispatch_complete'):
        require(type(capture[field]) is bool, 'capture requires booleans')
    if not all(capture[k] for k in ('application_complete', 'external_dispatch_complete')) or not evidence(capture['evidence']):
        missing.append('Complete application/dispatch capture evidence is missing.')
    setup = results['setup']
    keys(setup, {'operator_seconds', 'reviewer_seconds', 'operator_usd_per_hour',
                 'reviewer_usd_per_hour', 'cost_basis_evidence'}, 'setup')
    if not evidence(setup['cost_basis_evidence']):
        missing.append('Variable cost basis (including checking/correction labor) missing.')
    totals = {'attempts': 0, 'dispatches': 0, 'model_cost_usd': 0.0,
              'operator_seconds': 0.0, 'reviewer_seconds': 0.0,
              'known_unresolved_cost_hold_usd': 0.0, 'unknown_cost_hold_count': 0}
    for field in ('operator_usd_per_hour', 'reviewer_usd_per_hour'):
        require(setup[field] is None or number(setup[field]), 'labor rate')
        if setup[field] is None:
            missing.append('Missing ' + field)
    for field in ('operator_seconds', 'reviewer_seconds'):
        require(setup[field] is None or number(setup[field]), 'setup time')
        if setup[field] is None:
            missing.append('Missing setup ' + field)
        else:
            totals[field] += setup[field]
    rows = results['workflows']
    require(isinstance(rows, list) and len(rows) <= 72, 'workflow bound')
    expected = {row['workflow_id']: row for row in plan['schedule']}
    ordinary = set(plan['ordinary_controls'])
    seen, attempts_seen = {}, set()
    arms = {arm: {'useful': 0, 'task_seconds': 0.0, 'variable_cost_usd': 0.0,
                  'input_tokens': 0, 'output_tokens': 0, 'attempts': 0,
                  'outcomes': dict.fromkeys(sorted(OUTCOMES), 0)}
            for arm in ('baseline', 'candidate', 'ordinary')}
    for row in rows:
        keys(row, {'workflow_id', 'condition_sha256', 'status', 'attempts',
                   'completion_kind', 'completion_evidence', 'other_variable_cost_usd',
                   'task_seconds', 'operator_seconds', 'reviewer_seconds',
                   'variable_cost_usd', 'review', 'output_sha256'}, 'workflow')
        wid = row['workflow_id']
        require(isinstance(wid, str) and wid not in seen and
                (wid in expected or wid in ordinary), 'unknown/duplicate workflow')
        arm = expected[wid]['arm'] if wid in expected else 'ordinary'
        seen[wid] = row
        require(row['completion_kind'] in ('model_assisted', 'deterministic'),
                'completion kind')
        deterministic = row['completion_kind'] == 'deterministic'
        require(not (arm == 'ordinary' and not deterministic), 'ordinary must be deterministic')
        require(not (arm == 'baseline' and deterministic), 'baseline must use the fixed model')
        require(row['condition_sha256'] == (None if deterministic else
                                            plan['condition_sha256']),
                'different endpoint/model/runtime condition')
        require(row['status'] in OUTCOMES, 'workflow outcome')
        arms[arm]['outcomes'][row['status']] += 1
        if row['status'] == 'unknown':
            missing.append(wid + ': unknown workflow outcome')
        if not evidence(row['completion_evidence']):
            missing.append(wid + ': terminal outcome/completion evidence missing')
        for field in ('task_seconds', 'operator_seconds', 'reviewer_seconds',
                      'variable_cost_usd', 'other_variable_cost_usd'):
            require(row[field] is None or number(row[field]), 'workflow numeric field')
            if row[field] is None:
                missing.append(wid + ': missing ' + field)
            elif field in totals:
                totals[field] += row[field]
            elif field in ('task_seconds', 'variable_cost_usd'):
                arms[arm][field] += row[field]
        if all(row[f] is not None for f in ('task_seconds', 'operator_seconds', 'reviewer_seconds')):
            require(row['task_seconds'] >= row['operator_seconds'] + row['reviewer_seconds'],
                    'task time must include operator/reviewer checking and correction')
        attempts = row['attempts']
        require(isinstance(attempts, list) and len(attempts) <= 2, 'two attempts/workflow maximum')
        require(not (deterministic and attempts), 'deterministic/AI-off has model attempts')
        if not deterministic and not attempts and row['status'] not in ('unavailable',):
            missing.append(wid + ': missing attempt record')
        attempt_cost = 0
        for attempt in attempts:
            keys(attempt, {'attempt_id', 'outcome', 'dispatches', 'input_tokens',
                           'output_tokens', 'actual_cost_usd', 'cost_kind',
                           'unresolved_cost_hold_usd', 'evidence'}, 'attempt')
            aid = attempt['attempt_id']
            require(label(aid) and aid not in attempts_seen, 'duplicate attempt identity')
            attempts_seen.add(aid)
            totals['attempts'] += 1
            arms[arm]['attempts'] += 1
            require(attempt['outcome'] in OUTCOMES, 'attempt outcome')
            require(type(attempt['dispatches']) is int and attempt['dispatches'] in (0, 1),
                    'one application attempt must describe zero or one dispatch')
            totals['dispatches'] += attempt['dispatches']
            require(attempt['cost_kind'] in ('provider_reported', 'reconciled', 'estimate', 'unknown'),
                    'cost kind')
            if attempt['cost_kind'] in ('estimate', 'unknown'):
                missing.append(aid + ': observed cost unavailable')
            if attempt['outcome'] == 'unknown' or not evidence(attempt['evidence']):
                missing.append(aid + ': unresolved outcome/evidence')
            for field in ('actual_cost_usd', 'unresolved_cost_hold_usd'):
                require(attempt[field] is None or number(attempt[field]), 'attempt cost')
            hold = attempt['unresolved_cost_hold_usd']
            if hold is None:
                totals['unknown_cost_hold_count'] += 1
            else:
                totals['known_unresolved_cost_hold_usd'] += hold
            if hold is None or hold > 0:
                missing.append(aid + ': unresolved cost liability')
            cost = attempt['actual_cost_usd']
            require(attempt['cost_kind'] not in ('estimate', 'unknown') or cost is None,
                    'estimates/unknown cost cannot be reported as actual charges')
            if cost is None:
                missing.append(aid + ': missing actual cost')
            else:
                totals['model_cost_usd'] += cost
                attempt_cost += cost
            for field, ceiling in (('input_tokens', 4096), ('output_tokens', 512)):
                value = attempt[field]
                require(value is None or type(value) is int and value >= 0, 'token count')
                if value is None:
                    missing.append(aid + ': missing split ' + field)
                else:
                    arms[arm][field] += value
                    if value > ceiling:
                        failures.append(aid + ': exceeded ' + field + ' ceiling')
            if attempt['outcome'] == 'complete':
                require(attempt['dispatches'] == 1, 'complete call without dispatch')
            if attempt['dispatches'] == 0:
                require(all(attempt[f] == 0 for f in ('input_tokens', 'output_tokens',
                                                      'actual_cost_usd')),
                        'undispatched call cannot report inference usage')
        if row['variable_cost_usd'] is not None:
            require(row['variable_cost_usd'] >= attempt_cost,
                    'variable cost excludes observed model charges')
        cost_fields = ('operator_seconds', 'reviewer_seconds', 'other_variable_cost_usd',
                       'variable_cost_usd')
        if (all(row[f] is not None for f in cost_fields)
                and all(setup[f] is not None for f in ('operator_usd_per_hour', 'reviewer_usd_per_hour'))
                and all(a['actual_cost_usd'] is not None for a in attempts)):
            calculated = (attempt_cost + row['other_variable_cost_usd']
                          + row['operator_seconds'] * setup['operator_usd_per_hour'] / 3600
                          + row['reviewer_seconds'] * setup['reviewer_usd_per_hour'] / 3600)
            require(math.isclose(row['variable_cost_usd'], calculated, rel_tol=1e-9, abs_tol=1e-9),
                    'variable cost does not reconcile with observed charges, labor and other costs')
        if row['status'] == 'complete':
            require(hex_digest(row['output_sha256']), 'complete output identity missing')
            if not deterministic:
                require(any(a['outcome'] == 'complete' for a in attempts),
                        'complete workflow without complete call')
        review = row['review']
        if review is None:
            missing.append(wid + ': human review missing')
        else:
            keys(review, {'reviewer_id', 'evidence', 'useful', 'severe_regression',
                          'critical_failure'}, 'review')
            require(label(review['reviewer_id']), 'reviewer identity')
            require(all(type(review[f]) is bool for f in
                        ('useful', 'severe_regression', 'critical_failure')), 'review booleans')
            require(not review['useful'] or row['status'] == 'complete',
                    'noncomplete outcome cannot be judged a useful completion')
            if not evidence(review['evidence']):
                missing.append(wid + ': review evidence missing')
            if review['useful'] and row['status'] == 'complete':
                arms[arm]['useful'] += 1
            if review['severe_regression'] or review['critical_failure']:
                failures.append(wid + ': severe regression or critical failure')
    absent = sorted(set(expected) - seen.keys())
    if absent:
        missing.append('Missing model workflows: ' + ', '.join(absent))
    order = results['actual_order']
    planned_order = [r['workflow_id'] for r in plan['schedule'] if r['workflow_id'] in seen]
    if order is None:
        missing.append('Actual workflow order has not been observed.')
    else:
        require(isinstance(order, list) and all(isinstance(v, str) for v in order)
                and len(order) == len(set(order)) and set(order) == set(seen) & set(expected),
                'actual order must cover exactly the imported model workflows')
        if order != planned_order:
            missing.append('Actual workflow order deviates from frozen paired schedule.')
    journey = results['ai_off_journey']
    if journey is None:
        missing.append('AI-off save/reopen/export observation missing.')
    else:
        keys(journey, {'workflow_id', 'saved_sha256', 'reopened_sha256',
                       'exported_sha256', 'evidence'}, 'AI-off journey')
        row = seen.get(journey['workflow_id'])
        if not (row and journey['workflow_id'] in ordinary and row['status'] == 'complete'
                and row['review'] and row['review']['useful']
                and evidence(journey['evidence'])
                and hex_digest(journey['saved_sha256'])
                and journey['saved_sha256'] == journey['reopened_sha256']
                == journey['exported_sha256'] == row['output_sha256']):
            missing.append('AI-off journey lacks matching useful saved/reopened/exported bytes.')
    for field in ('attempts', 'model_cost_usd', 'operator_seconds', 'reviewer_seconds'):
        if totals[field] > LIMITS[field]:
            failures.append('Exceeded ' + field + ' ceiling')
    if totals['model_cost_usd'] + totals['known_unresolved_cost_hold_usd'] > LIMITS['model_cost_usd']:
        failures.append('Known actual charges plus unresolved liability exceed model budget.')
    baseline, candidate = arms['baseline'], arms['candidate']
    comparisons = {'time_reduction': None, 'cost_per_useful_reduction': None}
    if not missing and candidate['useful'] < baseline['useful']:
        failures.append('Candidate has fewer useful completions than baseline.')
    if not missing and baseline['useful'] and candidate['useful'] and baseline['task_seconds']:
        bcost = baseline['variable_cost_usd'] / baseline['useful']
        ccost = candidate['variable_cost_usd'] / candidate['useful']
        time_ratio = candidate['task_seconds'] / baseline['task_seconds']
        comparisons['time_reduction'] = 1 - time_ratio
        if bcost:
            comparisons['cost_per_useful_reduction'] = 1 - ccost / bcost
        # A zero-priced baseline has no manufactured percentage cost saving.
        def within(value, limit):
            return value <= limit or math.isclose(value, limit, rel_tol=1e-12, abs_tol=1e-12)
        cost_ok = within(ccost, bcost * 1.05)
        saves_cost = bcost > 0 and within(ccost, bcost * 0.80)
        if not ((within(time_ratio, 0.80) and cost_ok) or (saves_cost and within(time_ratio, 1.05))):
            failures.append('20% efficiency reduction with <=5% other-measure increase not met.')
    elif not missing:
        missing.append('Useful completion/time denominators are insufficient for comparison.')
    paired = []
    for task in plan['manifest']['tasks']:
        left, right = (seen.get(task['id'] + '/' + arm)
                       for arm in ('baseline', 'candidate'))
        pair = {'task_id': task['id'], 'category': task['category'],
                'baseline_status': left['status'] if left else 'missing',
                'candidate_status': right['status'] if right else 'missing'}
        for field in ('task_seconds', 'variable_cost_usd'):
            pair[field + '_candidate_minus_baseline'] = (
                right[field] - left[field] if left and right and
                left[field] is not None and right[field] is not None else None)
        pair['useful_candidate_minus_baseline'] = (
            int(right['review']['useful']) - int(left['review']['useful'])
            if left and right and left['review'] and right['review'] else None)
        paired.append(pair)
    return {'schema': 'educloud-e1-report-v1', 'plan_sha256': plan['plan_sha256'],
            'results_sha256': digest(results), 'paired': paired,
            'candidate_description': plan['manifest']['candidate_description'],
            'evidence_kind': results['evidence_kind'],
            'disposition': 'screening_fail' if failures else
                           'incomplete' if missing else 'screening_pass',
            'failures': failures, 'missing': missing, 'observed_totals': totals,
            'arms': arms, 'comparisons': comparisons,
            'limitations': ['Imported references/judgments are not authenticated here.',
                            'Counts cover application-observable dispatches, not provider-internal execution.',
                            'Declared public/synthetic scope is not automatic content clearance.',
                            'A 24-task screening does not qualify a hosted service or establish campus effectiveness.']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    freeze = commands.add_parser('plan')
    freeze.add_argument('--manifest', type=Path, required=True)
    freeze.add_argument('--seed', type=int, default=20261113)
    report = commands.add_parser('report')
    report.add_argument('--plan', type=Path, required=True)
    report.add_argument('--results', type=Path, required=True)
    template = commands.add_parser('template')
    template.add_argument('--plan', type=Path, required=True)
    for command in (freeze, report, template):
        command.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'plan':
            value = make_plan(read_json(args.manifest), args.seed)
        elif args.command == 'template':
            value = result_template(read_json(args.plan))
        else:
            value = summarize(read_json(args.plan), read_json(args.results))
        # Never replace an earlier plan, failure or report.
        with args.out.open('x') as target:
            target.write(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + '\n')
        print(json.dumps({'output': str(args.out), 'state': value.get('disposition', value.get('execution_state'))}))
        return 0 if value.get('disposition', 'screening_pass') == 'screening_pass' else 1
    except (OSError, ValueError, TypeError, KeyError, RecursionError) as error:
        print('E1 rejected: ' + str(error), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
