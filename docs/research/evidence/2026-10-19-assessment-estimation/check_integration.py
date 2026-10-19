"""Independent arithmetic/invariant checks against actual pure Go/Python CLIs."""
from pathlib import Path
from fractions import Fraction
import argparse, copy, hashlib, json, os, subprocess, tempfile, datetime

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--waypoint', type=Path, required=True)
parser.add_argument('--executable', type=Path, required=True)
parser.add_argument('--evidence-dir', type=Path, required=True)
args = parser.parse_args()
ROOT = args.evidence_dir.resolve()
ROOT.mkdir(parents=True, exist_ok=True)
RESULT = ROOT / 'a4-integration.json'
if RESULT.exists() or RESULT.is_symlink():
    parser.error('Use a fresh result artifact; do not overwrite prior evidence')
WP = args.waypoint.resolve()
FIX = WP / 'research-workspace/assessment/fixtures'
BIN = args.executable.resolve()
HEAD = subprocess.check_output(['git', '-C', str(WP), 'rev-parse', 'HEAD'], text=True).strip()
if HEAD != '053bb1ef5ff5e7a359e9f1e2a0cfbdd8d2a4f6ad':
    raise RuntimeError('Use the exact recorded Waypoint revision')
if subprocess.check_output(['git', '-C', str(WP), 'status', '--porcelain'], text=True) != '':
    raise RuntimeError('Use a clean Waypoint checkout')
binary_sha = hashlib.sha256(BIN.read_bytes()).hexdigest()
checks = []
outputs = {}

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()

def ratio(obj):
    return None if obj is None else Fraction(int(obj['numerator']), int(obj['denominator']))

def check(name, value):
    checks.append({'name': name, 'status': 'PASS' if value else 'FAIL'})
    if not value:
        raise RuntimeError(name)

def load(name):
    return json.loads((FIX / 'estimation' / name).read_text())

scenario, series, alternate = load('scenario.json'), load('python-series.json'), load('r-series.json')
with tempfile.TemporaryDirectory(prefix='a4-pure-', dir=ROOT) as temp:
    cwd = Path(temp)
    home = cwd / 'home'
    home.mkdir()
    plan, left, right = cwd / 'scenario.json', cwd / 'series.json', cwd / 'alternate.json'
    for path, value in ((plan, scenario), (left, series), (right, alternate)):
        path.write_bytes(canonical(value))
    before = sorted(str(p.relative_to(cwd)) for p in cwd.rglob('*'))
    env = {**os.environ, 'HOME': str(home), 'XDG_STATE_HOME': str(home/'state'),
           'XDG_CACHE_HOME': str(home/'cache'), 'PYTHONDONTWRITEBYTECODE': '1',
           'PYTHONPATH': str(WP/'research-workspace')}

    def invoke(name, one, sc=None, two=None):
        plan.write_bytes(canonical(scenario if sc is None else sc))
        left.write_bytes(canonical(one))
        args = ['python3', '-W', 'error::ResourceWarning', '-m', 'research_workspace',
                'assessment-estimate', str(plan), '--series', str(left)]
        if two is not None:
            right.write_bytes(canonical(two))
            args.extend(('--series', str(right)))
        args.extend(('--outfitter', str(BIN)))
        run = subprocess.run(args, cwd=cwd, env=env, capture_output=True, timeout=40)
        outputs[name] = {'returncode': run.returncode, 'stdout_bytes': len(run.stdout),
                         'stdout_sha256': hashlib.sha256(run.stdout).hexdigest()}
        return run

    def accepted(name, one, sc=None, two=None):
        run = invoke(name, one, sc, two)
        check(name+'_success', run.returncode == 0)
        obj = json.loads(run.stdout)
        check(name+'_false_authority', all(obj[k] is False for k in
              ('readiness_pass','actual_resource_accepted','execution_authorized','cleanup_trusted','upload_admission','retention_finalized')))
        return obj, run.stdout

    baseline, original = accepted('two_series', series, two=alternate)
    first = baseline['series'][0]
    cpu, duration = first['models']['cpu_consumed'], first['models']['execution_duration']
    check('known_exact_coefficients', ratio(cpu['coefficients']['intercept_nanoseconds']) == 1000 and
          ratio(cpu['coefficients']['slope_nanoseconds_per_row']) == 50)
    check('demand_and_busy_time_separate', ratio(first['totals']['cpu_consumed']['total_nanoseconds']) == 13600 and
          ratio(first['totals']['execution_duration']['total_nanoseconds']) == 6200)
    check('hours_dimensional_conversion', ratio(first['totals']['cpu_consumed']['hours']) == Fraction(13600,3600000000000))
    check('comparison_exact_without_winner', ratio(baseline['comparison']['differences']['cpu_consumed']['right_minus_left']) == 13500 and
          baseline['comparison']['winner'] is None)
    check('liabilities_and_uncertainty_preserved', all(c['remaining_liabilities'] for c in first['cleanup_claims']) and
          cpu['confidence_interval'] is None and cpu['prediction_uncertainty'] == 'not_estimated')
    a, b = copy.deepcopy(alternate), copy.deepcopy(series)
    a['receipts'].reverse(); b['receipts'].reverse()
    ordered, ordered_bytes = accepted('input_permutation', a, two=b)
    check('byte_stable_series_and_receipt_order', original == ordered_bytes)

    one, _ = accepted('one_series', series)
    base_cpu = one['series'][0]['models']['cpu_consumed']
    changed = copy.deepcopy(series)
    for receipt in changed['receipts']:
        if receipt['measurement']['binding']['sample_role'] == 'held_out':
            receipt['measurement']['measured_consumption']['cpu_consumed']['value'] = 100000
    bad_held, _ = accepted('held_out_perturbed', changed)
    held_model = bad_held['series'][0]['models']['cpu_consumed']
    check('held_out_cannot_refit_coefficients', held_model['coefficients'] == base_cpu['coefficients'] and
          held_model['held_out']['status'] == 'outside_declared_tolerance')

    changed = copy.deepcopy(series)
    for receipt in changed['receipts']:
        receipt['measurement']['measured_consumption']['cpu_consumed'].update(availability='unknown',value=None,source='none')
    missing, _ = accepted('missing_cpu', changed)
    check('missing_dimension_not_zero_or_dropped', missing['series'][0]['totals']['cpu_consumed']['total_nanoseconds'] is None and
          missing['series'][0]['models']['execution_duration']['prediction'] is not None)
    sc = copy.deepcopy(scenario); sc['overheads']['idle']['cpu_nanoseconds'] = None
    unknown, _ = accepted('unknown_overhead', series, sc)
    check('unknown_overhead_not_assumed_zero', unknown['series'][0]['totals']['cpu_consumed']['total_nanoseconds'] is None and
          ratio(unknown['series'][0]['totals']['cpu_consumed']['modeled_nanoseconds']) == 13500)

    changed = copy.deepcopy(series)
    changed['receipts'][-1]['measurement']['execution'].update(status='failed',exit_code=137,failure_category='out_of_memory')
    sc = copy.deepcopy(scenario); sc['target_rows'] = 50
    oom, _ = accepted('oom_boundary', changed, sc)
    check('oom_blocks_target_prediction', oom['series'][0]['models']['cpu_consumed']['prediction'] is None and
          'target_at_or_above_oom_boundary' in oom['series'][0]['models']['cpu_consumed']['warning_codes'])

    legacy = copy.deepcopy(series)
    legacy['manifest'] = json.loads((FIX/'research-default.json').read_text())
    legacy['receipts'] = [json.loads((FIX/'legacy-receipts.json').read_text())]
    charge_only, _ = accepted('charge_only_legacy', legacy)
    check('conservative_charge_not_measurement', charge_only['series'][0]['models']['cpu_consumed']['coefficients'] is None and
          charge_only['series'][0]['totals']['cpu_consumed']['total_nanoseconds'] is None)

    for name, change in [('duplicate_attempt', 'duplicate_attempt'),
                         ('duplicate_cleanup_id', 'duplicate_cleanup'),('free_content','content')]:
        bad = copy.deepcopy(series)
        if change == 'duplicate_attempt':
            bad['receipts'][1] = copy.deepcopy(bad['receipts'][0])
            bad['receipts'][1]['cleanup']['receipt_id'] = 'synthetic-fresh-duplicate-probe'
        elif change == 'duplicate_cleanup':
            bad['receipts'][1]['cleanup']['receipt_id'] = bad['receipts'][0]['cleanup']['receipt_id']
        else:
            bad['receipts'][0]['measurement']['raw_source'] = 'PRIVATE_SENTINEL'
        if change != 'content':
            item = bad['receipts'][1]
            item['measurement']['cleanup_receipt_id'] = item['cleanup']['receipt_id']
            item['measurement']['cleanup_receipt_sha256'] = hashlib.sha256(canonical(item['cleanup'])).hexdigest()
        run = invoke(name,bad)
        check(name+'_refused_without_content', run.returncode != 0 and not run.stdout and
              b'PRIVATE_SENTINEL' not in run.stderr)

    check('no_new_isolated_home_or_workdir_files', before == sorted(str(p.relative_to(cwd)) for p in cwd.rglob('*')))

check('head_and_binary_unchanged', HEAD == subprocess.check_output(['git','-C',str(WP),'rev-parse','HEAD'],text=True).strip() and
      binary_sha == hashlib.sha256(BIN.read_bytes()).hexdigest())
record = {'schema':'educloud.a4-independent-integration/v1','waypoint_head':HEAD,
          'outfitter_production_source':'de65bdab9303395226ebfb35e0e0740ab19b4d8e',
          'binary_sha256':binary_sha,'binary_provenance':'Operator-supplied trusted executable; checker does not build or attest it','checks':checks,'cli_runs':outputs,
          'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'scope':'Invented counters; real pure Go validator and Python operator CLI, no resource workloads',
          'not_run':['Actual resource measurement','Authenticated provenance or cleanup','Uploads/private data','Provider conversion or submission']}
with RESULT.open('x') as out: out.write(json.dumps(record,indent=2)+'\n')
print(json.dumps({'passed':sum(c['status']=='PASS' for c in checks),
                  'failed':sum(c['status']=='FAIL' for c in checks),'record':str(RESULT)}))
