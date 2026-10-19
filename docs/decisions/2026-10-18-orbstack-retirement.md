# Local backup verification and Docker Desktop retirement

Date: 18 October 2026 local time; private execution records use 19 October UTC.
Scope: the operator's existing macOS development host, under explicit authority
to verify migrated apps/backups and remove Docker Desktop and its old data.

Status: COMPLETE for the authorized Desktop retirement. All nine user-owned
Desktop app/data/settings roots and eight administrator-owned helper files/links
are absent. Both system helper services are stopped. Backup and post-removal
runtime checks pass within the limits below.

This supplements the [initial cutover record](2026-10-18-local-macos-runtime.md).
Docker-compatible containers and Compose remain the baseline. No production
change, research workload, new allocation, routing change, paid subscription,
source-image promotion or Kubernetes application deployment follows from this
host maintenance.

## Verification evidence

The coordinating operator held the shared maintenance lock for engine work.
Private container configuration, database exports and application identifiers
remain outside this repository; the table reports bounded aggregate evidence.

| Check | Result | Boundary |
| --- | --- | --- |
| Current runtime | PASS: 51 accepted container configurations, 17 active, 34 historical stopped, 13 healthy checks; 57 preserved volumes; 75 original image IDs and 147 references. | A separately coordinated local test recreated one container. Its exact allowed configuration changes, failed reset, subsequent recovery and accepted baseline are retained privately. |
| App/service probes | PASS: 21 read-only checks, with six NOT RUN categories; shared engine guard PASS. | Backend schemas, access refusals, authentication service health and Hub login/static assets only. No full signed-in workflow, notebook spawn, storage writes, mail delivery or frontend equivalence claim. |
| Cold volume recovery | PASS: all 45 migrated volume trees, 106,070 files and 3,493,386,662 bytes restored into disposable storage with exact contents and metadata. | Later cold backup point; not the original pre-start 57-tree census. The 12 preexisting OrbStack volumes were preserved, not included in this migrated-volume archive. |
| Host inputs | PASS: 11 roots and 71 members match contents, modes, numeric ownership and link targets. | Existing host inputs retained; engine socket deliberately excluded. |
| Physical database recovery | PASS: seven isolated same-image clones became queryable, with inventories retained and temporary resources removed. | Ordinary clone-only WAL recovery was permitted for historical stopped databases. No WAL reset or source-database mutation. The containing run remains overall FAIL for its later SQL-restore error. |
| Current SQL recovery | PASS: two isolated SQL restores match the frozen physical inventories, roles, database properties, extensions and table counts; exact dump grantors/membership options also match. | Same recovery point, with no source mutation. Table counts and metadata are checked; no separate row-value equivalence or authenticated-app claim. |
| Historical SQL recovery | PASS: four older recovery points strictly restored and matched their dump declarations and COPY counts; temporary resources removed. | Compared with each exact dump, not current state. Original default-database properties, extension ownership and undeclared versions were not recorded; no row-value or application equivalence claim. |
| Image archive | PASS for native ARM64: 65 unique roots and 517 content-hashed blobs; original five pilot graphs complete. Actual native load returned zero and reported exactly the expected 65 IDs. | Union of original/current container snapshots plus five pilot roots; not an archive of every unused cached image. Existing-engine import only; pristine-engine whole-app recovery NOT RUN. |
| Cross-platform images | FAIL / unavailable: 11 foreign manifests and nine associated attestations. | No native gap accepted. Missing foreign objects remain explicitly outside backup coverage. |

Current SQL recovery preserves the dump's bootstrap administrator identity,
locale archive and final role/membership properties. PostgreSQL distinguishes
the original bootstrap role from another ordinary superuser when recording role
grants; see the [PostgreSQL 17 GRANT reference](https://www.postgresql.org/docs/17/sql-grant.html).
These are bounded clone-recovery adaptations, not changes to live application roles.

## Retirement and retained limitations

The official uninstaller timed out while awaiting macOS administrator
authentication. Its FAIL and the termination of its identified orphaned prompt
are retained. Under the owner's existing removal authority, scoped cleanup then
removed all nine user-owned app/data/settings roots, including the Desktop app
and old disk storage. Four attempted system-link deletions failed with permission
errors; four system helper/plist files also remained. These eight exact remnants
totaled 15,428,622 bytes (about 14.7 MiB). That independently reviewed partial
acceptance remains preserved.

At 19:36 PDT on 18 October, the owner completed a fresh native macOS
administrator prompt. The previously reviewed, hash-pinned cleanup script
removed the exact eight remaining paths and stopped both system helper services.
Independent observation confirms all 17 authorized app/data/helper/link targets
are absent. OrbStack's socket and the shared configuration directory retain
their identities; the 13 configuration files retain the comparisons below.
The subsequent runtime, app probes and shared engine guard all passed again.
The maintenance lock was then released. Earlier timeout/permission failures
remain historical failures, not the current retirement outcome.

The uninstaller removed the shared Compose/Buildx plugin links before its
authentication timeout. The first post-removal runtime check therefore remains
FAIL. Restoring the two prior OrbStack link targets produced a separate PASS:
51 accepted containers, 17 active/34 stopped, 13 healthy checks, 57 volumes,
75 original image IDs/147 references and both command plugins. Post-removal app
probes passed 21 checks with six NOT RUN categories; the shared engine guard also
passed. Twelve shared configuration files remain byte-identical; one JSON file
has identical parsed keys and values with a different serialization. Its initial
byte-comparison FAIL is retained, with a separate strict semantic check.

The three large removed roots accounted for **38.28 GiB allocated**. Immediately
available filesystem space increased by only **0.99 GiB**, to **15.45 GiB**.
These are different measurements; this record does not claim 38.28 GiB of new
free space. Nine purgeable Time Machine snapshots were observed and left intact.
Snapshot or clone retention and concurrent writes may affect the difference;
exact attribution was not measured. [Apple's local-snapshot guidance](https://support.apple.com/en-ca/102154),
checked 18 October, says macOS counts snapshot space as available storage and
removes snapshots as they age or space is needed. No forced snapshot deletion or
additional capacity allowance follows from this maintenance.

A later sample after privileged cleanup, at 19:38 PDT, measured **13.07 GiB**
free. It does not change the earlier immediate before/after measurement. The
intervening change is not attributed; no additional reclaimed-space claim or
capacity qualification follows from either sample.

A redundant task-created initial image export was removed after the final export
passed independent native verification and actual loading, deleting an archive
of 4,947,245,161 bytes. That file size is not a measured free-space gain. Its hash,
completion marker and earlier verification reports
remain. All unique recovery data and the final archive remain private.

The recovery bundle is local to the same Mac. Off-device backup, reboot/startup
behavior, full authenticated application flows and pristine-engine recreation
remain NOT RUN. Neither local recovery nor free disk space qualifies whole-store
capacity, research quotas, independent-human reproduction or live inference.

## Preserved failures

Earlier image-GC loss, the incomplete foreign graph, probe-assumption failures,
the separately coordinated reset failure, and failed preparation/rehearsal attempts
remain recorded. Recovery checks corrected a socket-copy assumption, a database
wrapper exit-code assumption, temporary-container logging settings, an omitted
locale-archive path, the fresh cluster's bootstrap identity, and an OID JSON type mismatch in the checker. Original failed
records were not replaced by later PASS records.

The first image-load guard compared full display rows and reported 24 changed
entries despite a successful load. Raw before/after rows were not retained, so
that exact display difference is unknown. A separate subsequent check verified
all 65 recovery roots and every original ID/reference mapping; it does not erase
the earlier failed guard.

## Private evidence bindings

The following bindings identify private records without publishing inventories,
application names, paths, credentials or database contents. They are not public
reproducibility claims.

| Private record | SHA-256 |
| --- | --- |
| Pre-removal accepted verification | `fa24e591d3c2848fb4375b5b89a88d2d19be49937bffd60ab05b9e79bc95dfd7` |
| Cold volume extraction verification | `fda62749dd471096735ad3f0e82c68fd1daac1def27cef744f4979df0adfde70` |
| Native image archive verification | `282bdd3eb5743c79adb56ccbc56fc30629689a041eb9c1de061ad1e81cf5e492` |
| Native import identity verification | `f5e3d0708c615266e20b859b17f8d6ca79e38f351005ac564f5c1bb48121f6cb` |
| Seven physical successes within retained failed run | `4dadf5a426c53d29b644c73f971dc0f3f4c2e4a68496d0f5fad1d1b2f3a2e73c` |
| Two corrected current SQL restores | `78ea29f405de088c05a7713af015d591c30ee3bbc8e27034e5617be574aca0b8` |
| Four historical SQL restores | `7a2486b2285638b76fa65cbd7fc725fe7273d77b943852f9758b205912b35525` |
| Official uninstall authentication timeout, FAIL | `77f08cd7d168c93b4c11f326b77497cdaec867cc13a27527fb1d704f99443884` |
| Corrected post-removal runtime, PASS | `f2ab9e6d64812bf51985ea80b5312e4f12d9e4ec0504111cd8a0dcb185c00fb2` |
| Final observation with retained byte-comparison FAIL | `c1f76847da095b4048fc626a5d0161b3b78b156b7966d42217bb0cc396d225ad` |
| Shared configuration semantic comparison, PASS | `7e3d46fe06698a3dc4cca5f57851b50f3d25b406d15ee03af52b6e45499ef573` |
| Independently reviewed partial retirement acceptance | `8500aae08fcbdedfe08e7d9fb35c67302fc5e08f55b2fbc728c3787923c54e4e` |
| Authenticated exact-target cleanup result, PASS | `d546e7fb8ca0b61792b56e99679bd7b0756791ee592f867c0eae42c446074cef` |
| Runtime after privileged cleanup, PASS | `04f1ac221c7b7d061ae27485cb60ef3c1b88f8f35d0d569e84568065a27eea75` |
| Completed retirement observation, PASS | `fac42565461e38466d841ec7d268a9e6618aa577aa1fef879bc62c26fb6fd3fe` |
