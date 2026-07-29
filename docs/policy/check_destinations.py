#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""check_destinations.py — makes docs/policy/data-destinations.md enforceable.

The destination register in that document's §6 is the single source of truth.
This script parses it directly rather than reading a parallel machine-readable
manifest, deliberately: a second copy of the register would drift from the one
a human maintains, and the register's whole purpose is to be the artifact you
show a reviewer. The table you show and the table CI checks are the same table.

What it enforces (Axis B — records at rest):

  An R2 service (education records) may only be placed on D1 (institutional)
  or D2 (self-stewarded), unless either
    - the placement is explicitly marked synthetic-data-only, or
    - the row carries a recorded authorization per the policy's §4.2.

Axis A rows (inference payload classification) are skipped here. They are
enforced by config absence and are already machine-checked in
portage/tests/test_scale2_profile.py — a different mechanism for a different
question, and conflating them is the exact mistake the policy's §1 warns about.

Usage:
    python docs/policy/check_destinations.py
    python docs/policy/check_destinations.py --register path/to/doc.md

Exits 0 when the register is clean, 1 on any violation or if the register
cannot be found or parsed. Standard library only — no dependencies, so it runs
anywhere without setup. CC-P2 Step 2 wires it into the network-denied CI
workflow alongside check-pins.py and check-spdx.py.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_REGISTER = Path(__file__).resolve().parent / "data-destinations.md"

# The heading that anchors the table. Chosen over a line number or a fragile
# "first table in the file" rule so that reordering the document doesn't
# silently make this script check nothing.
REGISTER_HEADING = re.compile(r"^##\s*6\.\s*Destination register", re.IGNORECASE)

RECORD_CLASSES = {"R0", "R1", "R2", "R3"}
SAFE_TIERS = {"D1", "D2"}
ALL_TIERS = {"D1", "D2", "D3", "D4"}

# Cells that mean "nothing recorded here". The register uses an em dash for
# not-applicable; "pending" means the authorization is sought but not held,
# which is explicitly NOT an authorization.
EMPTY_MARKERS = {"", "—", "-", "n/a", "tbd", "pending"}


class RegisterError(Exception):
    """The register could not be located or parsed. Distinct from a policy
    violation: a register we cannot read is a broken check, not a clean one,
    and must never be reported as passing."""


def extract_table(text: str) -> list[list[str]]:
    """Return the register's rows as lists of stripped cells, header first."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if REGISTER_HEADING.match(line):
            start = i
            break
    if start is None:
        raise RegisterError(
            "could not find a '## 6. Destination register' heading. If the "
            "register moved or was renumbered, update REGISTER_HEADING here — "
            "do not leave this check silently matching nothing."
        )

    rows: list[list[str]] = []
    for line in lines[start + 1 :]:
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            # Skip the markdown separator row (|---|---|).
            if all(set(c) <= set("-: ") for c in cells):
                continue
            rows.append(cells)
        elif rows and stripped.startswith("#"):
            break  # next section; the table is done
    if not rows:
        raise RegisterError("found the register heading but no table under it")
    return rows


def tiers_in(cell: str) -> set[str]:
    """Every destination tier named in a cell, e.g. 'D1 or D2' -> {D1, D2}."""
    return set(re.findall(r"\bD[1-4]\b", cell))


def is_synthetic_only(cell: str) -> bool:
    return "synthetic" in cell.lower()


def has_authorization(cell: str) -> bool:
    normalized = cell.strip().strip("*_` ").lower()
    if normalized in EMPTY_MARKERS:
        return False
    # "Pending; §4.2 applies" is not an authorization, however it's phrased.
    return not normalized.startswith("pending")


def check(rows: list[list[str]]) -> list[str]:
    header = [h.lower() for h in rows[0]]

    def col(name: str) -> int:
        for i, h in enumerate(header):
            if name in h:
                return i
        raise RegisterError(f"register has no column matching {name!r}: {rows[0]}")

    c_service = col("service")
    c_class = col("class")
    c_now = col("destination now")
    c_pilot = col("destination at pilot")
    c_auth = col("authorization")

    problems: list[str] = []
    checked = 0

    for row in rows[1:]:
        if len(row) <= max(c_service, c_class, c_now, c_pilot, c_auth):
            problems.append(f"malformed row (wrong cell count): {row}")
            continue

        service = row[c_service].strip("*_` ")
        klass_cell = row[c_class]

        # Axis A rows are a different question, enforced elsewhere.
        if "axis a" in klass_cell.lower():
            continue

        found = [c for c in RECORD_CLASSES if re.search(rf"\b{c}\b", klass_cell)]
        if not found:
            problems.append(
                f"{service}: class cell {klass_cell!r} names no record class "
                f"(expected one of {sorted(RECORD_CLASSES)})"
            )
            continue
        # A store's class is the highest class it contains (policy §2).
        klass = max(found)

        if klass != "R2":
            continue
        checked += 1

        authorized = has_authorization(row[c_auth])

        for label, cell in (("now", row[c_now]), ("at pilot", row[c_pilot])):
            tiers = tiers_in(cell)
            # A cell naming no tier at all (e.g. "LMS", "Not yet deployed") is
            # outside this register's scope — institutional systems and
            # undeployed services aren't ours to place.
            if not tiers:
                continue
            unsafe = tiers - SAFE_TIERS
            if not unsafe:
                continue
            if label == "now" and is_synthetic_only(cell):
                continue
            if authorized:
                continue
            problems.append(
                f"{service}: R2 data placed on {sorted(unsafe)} ({label}: "
                f"{cell!r}) with no recorded authorization and no "
                f"synthetic-data-only marking. Education records belong on D1 "
                f"or D2 — see data-destinations.md §4.1 and §4.2."
            )

    if checked == 0:
        problems.append(
            "no R2 rows were checked. Either the register lost its education-"
            "record services or the class column changed shape — both are "
            "failures, because a check that silently examines nothing is worse "
            "than no check."
        )
    return problems


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    args = p.parse_args(argv)

    try:
        text = args.register.read_text(encoding="utf-8")
        rows = extract_table(text)
        problems = check(rows)
    except RegisterError as e:
        print(f"check_destinations: {e}", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"check_destinations: cannot read register: {e}", file=sys.stderr)
        return 1

    if problems:
        print(
            f"check_destinations: {len(problems)} data-destination "
            f"violation(s) in {args.register}:",
            file=sys.stderr,
        )
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    print(f"check_destinations: register clean ({args.register.name}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
