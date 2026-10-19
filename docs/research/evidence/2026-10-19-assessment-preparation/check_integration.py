"""Coordinator-owned public-fixture interoperability check; no workload execution."""
from pathlib import Path
import copy
import argparse
import datetime
import hashlib
import json
import os
import subprocess
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--waypoint', type=Path, required=True)
parser.add_argument('--outfitter', type=Path, required=True)
parser.add_argument('--executable', type=Path, required=True)
parser.add_argument('--evidence-dir', type=Path, required=True)
args = parser.parse_args()
ROOT = args.evidence_dir.resolve()
ROOT.mkdir(parents=True, exist_ok=True)
WP = args.waypoint.resolve()
OF = args.outfitter.resolve()
BIN = args.executable.resolve()
RESULT = ROOT / 'assessment-integration.json'
if RESULT.exists() or RESULT.is_symlink():
    parser.error('Use an evidence directory with no existing result file.')
FIX = WP / 'research-workspace/assessment/fixtures'
manifest = json.loads((FIX / 'research-default.json').read_text())
receipts = json.loads((FIX / 'legacy-receipts.json').read_text())
expected = json.loads((OF / 'internal/assessment/testdata/validate-result.json').read_text())
checks = []

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()

def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()

def pin(path):
    return subprocess.check_output(['git', '-C', str(path), 'rev-parse', 'HEAD'], text=True).strip()

def clean(path):
    return subprocess.check_output(['git', '-C', str(path), 'status', '--porcelain'], text=True) == ''

initial_wp, initial_of = pin(WP), pin(OF)
initial_binary = hashlib.sha256(BIN.read_bytes()).hexdigest()
initial_clean = clean(WP) and clean(OF)

def check(name, condition):
    checks.append({'name': name, 'status': 'PASS' if condition else 'FAIL'})
    if not condition:
        raise AssertionError(name)

with tempfile.TemporaryDirectory(prefix='assessment-pure-', dir=ROOT) as temp:
    directory = Path(temp)
    home = directory / 'home'
    home.mkdir()
    env = {**os.environ, 'HOME': str(home), 'XDG_STATE_HOME': str(home / 'state'),
           'XDG_CACHE_HOME': str(home / 'cache'), 'PYTHONPATH': str(WP / 'research-workspace'),
           'PYTHONDONTWRITEBYTECODE': '1'}
    plan, receipt = directory / 'manifest.json', directory / 'receipts.json'
    plan.write_bytes(canonical(manifest))
    receipt.write_bytes(canonical(receipts))
    before = sorted(str(p.relative_to(directory)) for p in directory.rglob('*'))

    def go(obj):
        return subprocess.run([str(BIN), 'assessment-receipts'], input=canonical(obj),
                              capture_output=True, cwd=directory, env=env, timeout=10)

    def preview():
        return subprocess.run(['python3', '-W', 'error::ResourceWarning', '-m', 'research_workspace',
                               'assessment-preview', str(plan), str(receipt), '--outfitter', str(BIN)],
                              capture_output=True, cwd=directory, env=env, timeout=15)

    def request(value):
        return {'operation': 'validate', 'manifest': manifest, 'receipts': value}

    valid = go(request(receipts))
    check('real_go_exact_frozen_result', valid.returncode == 0 and valid.stdout == canonical(expected))
    got = json.loads(valid.stdout)
    check('go_false_authority_flags', all(got[k] is False for k in
          ('execution_authorized', 'cleanup_trusted', 'actual_resource_accepted')))
    check('frozen_digests', got['manifest_sha256'] == digest(manifest) and
          got['measurement_sha256'] == digest(receipts['measurement']) and
          got['cleanup_sha256'] == digest(receipts['cleanup']))
    result = preview()
    check('real_go_to_python_cli_preview', result.returncode == 0)
    projection = json.loads(result.stdout)
    check('python_retained_unknowns_and_partial_coverage', projection['retained_record']['execution_claim']['reused'] is receipts['measurement']['execution']['reused']
          and projection['retained_record']['cleanup_claim']['outcome'] == 'unresolved'
          and projection['retained_record']['cleanup_claim']['termination'] == 'unknown'
          and projection['retained_record']['measured_consumption']['cpu_consumed']['value'] is None)
    check('python_false_authority_flags', all(projection[k] is False for k in
          ('execution_authorized', 'cleanup_trusted', 'actual_resource_accepted')))
    check('partial_reservations_not_authority', projection['reservation_coverage'] ==
          {'declared': 1, 'planned': 12, 'status': 'partial', 'references_verified': False}
          and projection['upload_admission'] is False and projection['retention_finalized'] is False)

    source = {'schema_version': 1, 'request_id': manifest['reservations'][0]['attempt_id'],
              'project_id': manifest['project_id'], 'image': manifest['workload']['image'],
              'admitted': True, 'execution_started': True, 'status': 'succeeded', 'exit_code': 0,
              'error': '', 'stdout': 'PRIVATE_SENTINEL', 'stderr': 'PRIVATE_SENTINEL',
              'cleanup_verified': True, 'unresolved_liability': False,
              'created_at': '2026-10-19T20:00:00Z', 'started_at': '2026-10-19T20:00:01Z',
              'finished_at': '2026-10-19T20:00:02Z', 'deadline': '2026-10-19T20:00:30Z',
              'cancel_requested': False, 'compute': {'reserved_cpu_seconds': 30,
              'charged_cpu_seconds': 30, 'provenance': 'estimated_upper_bound'}, 'teardown_risk': ''}
    projected = go({'operation': 'project_legacy', 'manifest': manifest,
                    'binding': receipts['measurement']['binding'], 'cleanup_receipt_id': 'cleanup-1',
                    'source_receipt': source})
    check('real_go_legacy_projection', projected.returncode == 0)
    check('legacy_source_content_excluded', b'PRIVATE_SENTINEL' not in projected.stdout + projected.stderr)
    projected_result = json.loads(projected.stdout)
    receipt.write_bytes(canonical(projected_result['receipts']))
    projected_preview = preview()
    check('real_legacy_go_to_python_projection', projected_preview.returncode == 0)
    check('legacy_unknown_reuse_not_fresh', json.loads(projected_preview.stdout)['retained_record']['execution_claim']['reused'] is None)

    def negative(name, value, alter_manifest=None):
        receipt.write_bytes(canonical(value))
        obj = request(value)
        if alter_manifest is not None:
            obj['manifest'] = alter_manifest
            plan.write_bytes(canonical(alter_manifest))
        rejected = go(obj)
        displayed = preview()
        error = json.loads(rejected.stdout)
        check(name + '_go_refuses', rejected.returncode != 0 and set(error) == {'error'} and
              error['error'] in ('INVALID_RECEIPT_SET', 'CLEANUP_DIGEST_MISMATCH', 'INVALID_MANIFEST'))
        check(name + '_waypoint_refuses', displayed.returncode != 0 and displayed.stdout == b'')
        check(name + '_no_content_echo', b'PRIVATE_SENTINEL' not in rejected.stderr + displayed.stderr)
        plan.write_bytes(canonical(manifest))

    untrusted = copy.deepcopy(receipts)
    untrusted['measurement']['observation']['source_kind'] = 'synthetic_fixture'
    untrusted['cleanup']['observation']['source_kind'] = 'synthetic_fixture'
    untrusted['cleanup']['method']['name'] = 'unverified_scope_observation'
    untrusted['measurement']['cleanup_receipt_sha256'] = digest(untrusted['cleanup'])
    check('untrusted_nonlegacy_baseline_valid', go(request(untrusted)).returncode == 0)
    bad = copy.deepcopy(untrusted)
    bad['cleanup']['outcome'] = 'verified'
    bad['measurement']['cleanup_receipt_sha256'] = digest(bad['cleanup'])
    negative('false_verified_cleanup', bad)
    bad = copy.deepcopy(untrusted)
    bad['cleanup']['termination'] = bad['cleanup']['access_revocation'] = 'verified'
    for scope in bad['cleanup']['observed_scopes']:
        scope['deletion'] = 'reported_complete'
    bad['cleanup']['remaining_liabilities'] = []
    bad['measurement']['cleanup_receipt_sha256'] = digest(bad['cleanup'])
    negative('all_resolved_untrusted_cleanup', bad)
    bad = copy.deepcopy(receipts)
    bad['measurement']['execution']['status'] = 'reserved'
    bad['measurement']['conservative_accounting'].update(charged_cpu_seconds=0, provenance='reserved', unresolved_liability=True)
    bad['cleanup']['remaining_liabilities'].append('accounting_unresolved')
    bad['measurement']['cleanup_receipt_sha256'] = digest(bad['cleanup'])
    negative('reserved_terminal_contradiction', bad)
    bad = copy.deepcopy(receipts)
    bad['measurement']['binding']['attempt_id'] = '4' * 32
    negative('wrong_attempt_binding', bad)
    bad = copy.deepcopy(receipts)
    bad['measurement']['measured_consumption']['cpu_consumed']['value'] = 30
    negative('unknown_metric_with_value', bad)
    bad = copy.deepcopy(receipts)
    bad['measurement']['source_filename'] = 'PRIVATE_SENTINEL'
    negative('free_content_field', bad)
    bad = copy.deepcopy(receipts)
    bad['measurement']['measured_consumption']['cpu_consumed'].update(availability='available', value=30, source='unverified_collector')
    negative('legacy_wall_charge_as_measurement', bad)

    # A partial untrusted terminal observation must remain valid and unresolved.
    unknown = copy.deepcopy(receipts)
    unknown['measurement']['execution'].update(status='unknown', failure_category='unknown')
    unknown['measurement']['conservative_accounting'].update(charged_cpu_seconds=0, provenance='reserved', unresolved_liability=True)
    unknown['cleanup']['remaining_liabilities'].append('accounting_unresolved')
    unknown['measurement']['cleanup_receipt_sha256'] = digest(unknown['cleanup'])
    check('unknown_terminal_cleanup_claim_preserved', go(request(unknown)).returncode == 0)

    generic = copy.deepcopy(receipts)
    generic['measurement']['execution']['reused'] = None
    receipt.write_bytes(canonical(generic))
    generic_preview = preview()
    check('unknown_reuse_stays_null', generic_preview.returncode == 0 and
          json.loads(generic_preview.stdout)['retained_record']['execution_claim']['reused'] is None)

    receipt.write_bytes(canonical(receipts))
    after = sorted(str(p.relative_to(directory)) for p in directory.rglob('*'))
    check('isolated_home_and_workdir_no_new_files', before == after)

check('pinned_checkouts_and_binary_unchanged', initial_clean and clean(WP) and clean(OF) and
      (pin(WP), pin(OF)) == (initial_wp, initial_of) and
      hashlib.sha256(BIN.read_bytes()).hexdigest() == initial_binary)
record = {'schema': 'educloud.coordinator-assessment-integration/v1',
          'scope': 'public frozen fixture; actual pure Go CLI to actual Python operator preview',
          'waypoint_head': initial_wp, 'outfitter_head': initial_of,
          'binary_sha256': initial_binary,
          'binary_provenance': 'Operator-supplied trusted executable; checker does not build or attest it',
          'manifest_sha256': digest(manifest), 'receipt_set_sha256': digest(receipts),
          'checks': checks, 'time': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'not_run': ['workload execution', 'local engine or provider calls', 'network capacity',
                      'authenticated collector or independent cleanup', 'temporary upload or hosted/private-data acceptance']}
with RESULT.open('x') as output:
    output.write(json.dumps(record, indent=2) + '\n')
print(json.dumps({'passed': sum(c['status'] == 'PASS' for c in checks), 'failed': sum(c['status'] == 'FAIL' for c in checks),
                  'record': str(RESULT)}))
