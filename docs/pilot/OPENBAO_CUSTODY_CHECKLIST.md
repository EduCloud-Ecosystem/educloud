# OpenBao password-manager and backup checklist

**Default activation remains blocked.** Merging source or passing CI does not
complete any custody step below. This checklist uses Greg's selected institutional
password manager plus a separately held backup. No secret values belong in Git,
chat, email, CI artifacts or a student workspace.

## Which instance are you protecting?

The existing package is for the **local rehearsal only**:

- Private instructions: `/Users/gregchism/Library/Application Support/EduCloud/OpenBao Recovery/classroom-adoption-01/HANDOFF.md`
- Sensitive import file: `/Users/gregchism/Library/Application Support/EduCloud/OpenBao Recovery/classroom-adoption-01/recovery.json`
- Runtime/evidence: `/Users/gregchism/.codex/worktrees/portage-openbao-trial/portage/.qualification/openbao-classroom-adoption-01/`

Do not import the other `identity-controls-*` test packages. You may use the
classroom-adoption-01 package to rehearse custody or retain that local instance.
It uses one unseal share and a one-day test TLS certificate. **It does not qualify
custody or activation of a future hosted pilot.** That target instance must first
be selected and provisioned; it will generate its own recovery package. Use that
new package for the production/persistent activation record.

## What Greg needs to do

1. **Create one restricted vault item.** Sign in to the institution-approved
   password manager with its required MFA. Use a restricted administrator vault,
   not a course/shared-student vault. Title the current test item
   `EduCloud / OpenBao / LOCAL REHEARSAL / classroom-adoption-01`.
   For a later pilot, use its actual environment and immutable instance ID.
   Record the owner, authorized recovery people and date. Give recovery access
   only to yourself and any explicitly approved backup custodian.

2. **Import the complete recovery record.** Add `recovery.json` as a protected
   attachment if the manager supports it, or copy the entire JSON into an encrypted
   secure note without dropping fields. It contains `unseal_key`,
   `operator_password`, `operator`, `instance`, `address`, `ca_sha256`, `version`
   and `purpose`. Keep the instance and CA binding with the secrets. Do not store
   a bootstrap root token; the workflow revokes it. Do not put these values in a
   general notes app or use a public sharing link. The local staging file is
   owner-only **plaintext**, not an encrypted vault.

3. **Verify retrieval from the vault.** Close the item, lock/sign out, then
   reauthenticate and retrieve the protected attachment/note. Compare the full
   record with the staged original in a private operator session, preserving all
   fields. Do not send either copy here. Record only the vault item reference,
   retrieval date, tester and pass/fail result in the nonsecret custody log.

4. **Make a genuinely separate recovery copy.** Put the same recovery record on
   institution-approved encrypted removable storage or in an approved independent
   escrow. A second item in the same password manager is not a separate recovery
   path. Make its unlocking/recovery method available if the primary vault/account
   is unavailable, using the institution's approved custody procedure. Record who
   controls it and where it is held; do not put its passphrase in the public log.
   This is a duplicate backup of the local single share, not a two-person quorum.

5. **Test the separate copy independently.** With the password manager locked and
   without using the staging file, retrieve/decrypt the backup. Verify it matches
   the full recovery record and the intended instance/CA binding. Record the date,
   tester and pass/fail. Before actual default activation, a controlled recovery
   drill must use material retrieved from this approved custody path, prove old
   service tokens and pending SecretIDs are invalidated, and preserve Portage's
   independent ledger. The local fresh-process drill already passed, but it read
   the staging file; it is not proof of your vault/backup retrieval.

6. **Confirm and clean up.** Confirm the nonsecret facts below. Only after both
   retrievals and the required target-instance recovery drill succeed, remove the
   plaintext staging file and any temporary plaintext downloads. Do not delete
   the sole usable recovery copy, encrypted server backup, audit evidence or
   accounting ledger. Ordinary file deletion does not promise physical erasure
   from SSDs, cloud sync or filesystem snapshots; use institutional handling rules.

## What the server backup must accompany

Recovery material unlocks a server; it is not the server's data backup. Retain an
encrypted operational backup of the corresponding stopped Raft state, TLS/config,
exact source/binary identities and audit evidence. For the local verified restore,
those are `bao/backup/`, `bao/server.hcl`, `bao/tls.crt`, `bao/tls.key` and the run's
result/audit records under the runtime/evidence root above. TLS private keys are
sensitive. Keep unseal/operator recovery material outside that operational backup
and outside runtime mounts.

Preserve `workflow/tutoring/provider/portage.sqlite` independently, including any
required SQLite journals in a real deployment or using its supported consistent
backup procedure. **Never roll accounting backward just because Bao is restored.**
A snapshot can resurrect credentials: admission stays stopped until recovery
invalidates them and verifies the current provider key. The OpenBao rehearsal
backup is not a complete backup of Cairn, course repositories or learner notebooks.
Each component's own consistent backup/retention procedure still applies.

## Nonsecret confirmation to return

Send only:

- Target environment and instance ID (say `local rehearsal` if that is all you did).
- Restricted vault item reference, owner/authorized recovery people, and retrieval-test date/result.
- Separate encrypted backup reference, responsible holder, and independent retrieval-test date/result.
- Target-instance restore-test evidence reference and whether old credentials were refused and accounting preserved.
- Whether temporary plaintext copies were removed after verification.

Never send the JSON, unseal share, operator password, provider key, TLS private key,
backup unlocking secret or screenshots containing any of them. A nonsecret
confirmation is review evidence, not a substitute for actually performing the steps.
The default-activation gate remains closed until this is verified for the actual
pilot instance alongside the existing host, service isolation and course gates.
