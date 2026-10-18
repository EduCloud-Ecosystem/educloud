"""Inspect downloaded public CI evidence without running brokers or workloads."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
root=Path(__file__).parent
workspace=Path('/Users/gregchism/dev/.educloud-worktrees/waypoint-ci-broker-adoption/research-workspace')
sys.path.insert(0,str(workspace))
from research_workspace.evidence import verify_bundle
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def require(condition,message):
 if condition is not True:raise ValueError(message)
head='e16bcd3ad7d28cf6a56845621e65ca38ac526923'; base='2317eac63a0bad0d691457b0cde2de14bf6bcc7f'; broker='5446438985e31cb739f2048a2aa2176918831a7e'
ci=json.loads((root/'ci-run.json').read_bytes())
require(ci['headSha']==head and ci['conclusion']=='success' and ci['status']=='completed','Wrong CI identity/result')
jobs={j['name']:j['conclusion'] for j in ci['jobs']}
require(jobs=={'controls':'success','actual-docker':'success','clean-source-builds':'skipped'},'Unexpected job results')
log=(root/'ci.log').read_text()
require(re.search(r'Ran 384 tests in [0-9.]+s',log) is not None,'Wrong control count')
require(any(line.endswith(broker) and 'checkout@v4' in line for line in log.splitlines()),'Candidate checkout not observed')
files={str(p.relative_to(root/'artifacts')):p for p in (root/'artifacts').rglob('*') if p.is_file()}
expected={'operation-guard-acceptance/verification.json','recovery-acceptance/before.zip','recovery-acceptance/after.zip','recovery-acceptance/verification.json','reproduction-acceptance/evidence.zip','reproduction-acceptance/report.json','research-acceptance/first-project.zip','research-acceptance/second-project.zip','research-acceptance/verification.json'}
require(set(files)==expected and all(p.stat().st_size>0 for p in files.values()),'Missing/empty/unexpected artifacts')
read=lambda name:json.loads(files[name].read_bytes())
http=read('research-acceptance/verification.json'); recovery=read('recovery-acceptance/verification.json'); guard=read('operation-guard-acceptance/verification.json'); replay=read('reproduction-acceptance/report.json')
require(http['status']=='PASS' and http['checks_passed']==len(http['checks'])==41 and http['all_recorded_runs_cleanup_verified'] is True,'HTTP checks/cleanup')
require(recovery['status']=='PASS' and recovery['checks_passed']==len(recovery['checks'])==25 and 'no_unresolved_provider_liability' in recovery['checks'],'Recovery checks/liability')
require(guard['status']=='PASS' and len(guard['checks'])==12 and all(c['status']=='PASS' for c in guard['checks']),'Guard checks')
require(replay['status']=='PASS' and len(replay['runs'])==3,'Replay result')
selected=[r for r in replay['runs'] if r['selected']]; skipped=[r for r in replay['runs'] if not r['selected']]
require(len(selected)==2 and all(r['attempted'] is True and r['outcome']=='PASS' and r['cleanup_verified'] is True and r['compute']=={'reserved_cpu_seconds':30,'charged_cpu_seconds':30,'provenance':'estimated_upper_bound','unresolved_liability':False} for r in selected),'Replay charge/cleanup')
require(len(skipped)==1 and skipped[0]['original_status']=='failed' and skipped[0]['attempted'] is False and skipped[0]['outcome']=='NOT RUN','Historical failure not preserved')
require(http['broker_binary_sha256']==recovery['broker_binary_sha256'],'Different broker binaries')
source_counts={}
for label,report in [('http',http),('recovery',recovery)]:
 for name,digest in report['source_hashes'].items():require(sha(workspace/name)==digest,'Source mismatch '+name)
 source_counts[label]=len(report['source_hashes'])
bundles={}
for name,p in files.items():
 if p.suffix=='.zip':
  result=verify_bundle(p.read_bytes());require(result['valid'] is True,'Invalid '+name);bundles[name]=result
for name,digest in recovery['artifacts'].items():require(sha(files['recovery-acceptance/'+name])==digest,'Recovery archive mismatch')
require(sha(files['reproduction-acceptance/evidence.zip'])==replay['evidence_sha256'],'Replay archive mismatch')
changed=subprocess.check_output(['git','diff','--name-only',base,head],cwd=workspace.parent,text=True).splitlines()
require(set(changed)=={'.github/workflows/research-workspace.yml','research-workspace/CI-BROKER-ADOPTION.md'},'Scope changed')
report={'format':'waypoint-ci-broker-adoption-artifact-audit-v1','status':'PASS','head':head,'accepted_base':base,'ci_run':39114639604,'broker_commit':broker,'broker_binary_sha256':http['broker_binary_sha256'],'jobs':jobs,'full_controls':384,'http_checks':41,'recovery_checks':25,'guard_checks':12,'replay_passes':2,'historical_failed_run':'NOT RUN','replay_charged_cpu_seconds':60,'bundles_verified':len(bundles),'artifact_files':len(files),'source_hash_counts':source_counts,'source_hash_counts_overlap':True,'artifact_sha256':{name:sha(p) for name,p in sorted(files.items())},'ci_log_sha256':sha(root/'ci.log'),'audit_source_sha256':sha(Path(__file__)),'local_workload_runs':0,'limitations':['Only standard CI adoption; no accepted-state or production deployment change.','The optional frozen source-build qualification was skipped, not newly accepted.','CI checks overlap; no new browser or independent-human acceptance.','No physical storage/all-writer/native/cloud acceptance.']}
(root/'artifact-audit.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','head','full_controls','http_checks','recovery_checks','guard_checks','replay_passes','historical_failed_run','bundles_verified','artifact_files','source_hash_counts']},sort_keys=True))
print('audit_sha256',sha(root/'artifact-audit.json'))
