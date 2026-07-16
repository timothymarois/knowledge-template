#!/usr/bin/env python3
"""Teeth-test for doc-lint — ships in the payload beside the linter.

The valid base is a *copy of the real payload* with two sample PRDs added, so the
structural checks (every shipped dir/guide present, the trio's standard pointer) are
exercised against the actual shipped tree. Each mutation must fail on its own rule.

    python3 .knowledge/scripts/test_doc_lint.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DOC_LINT = os.path.join(HERE, "doc-lint")
PAYLOAD = os.path.dirname(HERE)  # the real .knowledge/ this script ships in

CATALOG = """# prd/ — catalog

## Components

```
1. base- — the substrate
2. entity- — a placed thing
```

## Contents

- **Base**
  - [base-core](./base-core.md)
- **Entities**
  - [entity-widget](./entity-widget.md)
"""
BASE = """---
id: CORE
name: Core
last_verified: 2026-07-16
---

## What this is

The substrate.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-CORE-1 | The substrate persists between runs | `coreHolds` |
"""
WIDGET = """---
id: WIDGET
name: Widget
---

## What this is

A widget, built on R-CORE-1.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ❌ | R-WIDGET-1 | A widget reports its state on demand | — |
"""


def w(aidir, rel, content):
    path = os.path.join(aidir, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def build_base(aidir):
    shutil.copytree(PAYLOAD, aidir)          # the real shipped payload
    w(aidir, "prd/README.md", CATALOG)       # add two sample PRDs + a matching catalog
    w(aidir, "prd/base-core.md", BASE)
    w(aidir, "prd/entity-widget.md", WIDGET)


def run(aidir):
    p = subprocess.run([sys.executable, DOC_LINT, aidir], capture_output=True, text=True)
    return p.returncode, p.stdout


def case(name, mutate, expect_ok, sub=None):
    with tempfile.TemporaryDirectory() as d:
        aidir = os.path.join(d, ".knowledge")
        build_base(aidir)
        mutate(aidir)
        code, out = run(aidir)
    ok = (code == 0)
    passed = (ok == expect_ok) and (sub is None or sub in out)
    detail = "" if passed else f"  (exit={code}, wanted_ok={expect_ok}, sub={sub!r})\n{out}"
    print(f"[{'PASS' if passed else 'FAIL'}] {name}{detail}")
    return passed


def main():
    cases = [
        # --- the shipped structure is intact ---
        ("valid full payload passes", lambda a: None, True),
        ("a shipped guide was removed",
         lambda a: os.remove(os.path.join(a, "guides/docs-brief.md")),
         False, "required file `guides/docs-brief.md` is missing"),
        ("a home directory was removed",
         lambda a: shutil.rmtree(os.path.join(a, "references")),
         False, "required directory `references/` is missing"),
        ("the linter script was renamed away",
         lambda a: os.remove(os.path.join(a, "scripts/doc-lint")),
         False, "required file `scripts/doc-lint` is missing"),
        ("a trio file lost its standard pointer",
         lambda a: w(a, "BRIEF.md", "# Brief\n\nJust a project, no pointer at the bottom.\n"),
         False, "must end with its standard pointer"),
        # --- PRD contract rules ---
        ("two namespaces in one file",
         lambda a: w(a, "prd/entity-widget.md", WIDGET.replace("R-WIDGET-1", "R-OTHER-1")),
         False, "does not match file namespace"),
        ("duplicate ID across files",
         lambda a: w(a, "prd/base-core.md", BASE.replace("id: CORE", "id: WIDGET").replace("R-CORE-1", "R-WIDGET-1")),
         False, "already defined"),
        ("requirement over 25 words",
         lambda a: w(a, "prd/base-core.md", BASE.replace(
             "persists between runs",
             "persists between runs and also across every conceivable restart cycle no matter how many "
             "times the machine happens to reboot itself over and over again without any exception")),
         False, "max 25"),
        ("numeric literal in requirement",
         lambda a: w(a, "prd/base-core.md", BASE.replace("between runs", "for 30 runs")),
         False, "numeric literal"),
        ("checkmark with no test named",
         lambda a: w(a, "prd/base-core.md", BASE.replace("| `coreHolds` |", "| — |")),
         False, "names no test"),
        ("contract cites a draft",
         lambda a: (w(a, "prd-drafts/entity-future.md",
                      "---\nid: FUTURE\nname: Future\n---\n\n## Requirements\n\n"
                      "|  | ID | Requirement | Evidence |\n|:--:|---|---|---|\n"
                      "| ❌ | R-FUTURE-1 | A future thing exists | — |\n"),
                    w(a, "prd/entity-widget.md", WIDGET.replace("built on R-CORE-1.", "built on R-CORE-1 and R-FUTURE-1."))),
         False, "prd-drafts/ proposal"),
        ("citation resolves nowhere",
         lambda a: w(a, "prd/entity-widget.md", WIDGET.replace("R-CORE-1.", "R-GHOST-9.")),
         False, "resolves nowhere"),
        ("catalog omits a PRD file",
         lambda a: w(a, "prd/README.md", CATALOG.replace("  - [entity-widget](./entity-widget.md)\n", "")),
         False, "Contents omits"),
        ("a catalog links to a missing file",
         lambda a: w(a, "guides/README.md",
                     open(os.path.join(a, "guides/README.md"), encoding="utf-8").read()
                     + "\n[ghost](./docs-ghost.md)\n"),
         False, "links to missing"),
        ("a README is missing a required section",
         lambda a: w(a, "research/README.md", "# research/ — catalog\n\nGutted, no sections.\n"),
         False, "missing required section"),
        ("last_verified without a checkmark",
         lambda a: w(a, "prd/entity-widget.md", WIDGET.replace("name: Widget\n---", "name: Widget\nlast_verified: 2026-07-16\n---")),
         False, "no ✅ row"),
        ("citation into a later layer",
         lambda a: w(a, "prd/base-core.md", BASE.replace("The substrate.", "The substrate. Uses R-WIDGET-1.")),
         False, "up the stack"),
        ("filename prefix not a component",
         lambda a: w(a, "prd/gadget-foo.md",
                     "---\nid: GADGET\nname: Gadget\n---\n\n## Requirements\n\n"
                     "|  | ID | Requirement | Evidence |\n|:--:|---|---|---|\n"
                     "| ❌ | R-GADGET-1 | A gadget does a thing | — |\n"),
         False, "filename prefix not a listed component"),
        ("heading outside the schema",
         lambda a: w(a, "prd/entity-widget.md", WIDGET + "\n## Notes\n\nextra prose.\n"),
         False, "not in the closed schema"),
        ("research note missing its date",
         lambda a: w(a, "research/competitor.md",
                     "# Research: competitor\n\n**Question it answers:** what\n\n## What they do\n\nStuff.\n"),
         False, "**Last updated:**"),
        ("research citation without a source",
         lambda a: w(a, "research/market.md",
                     "# Research: market\n\n**Last updated:** 2026-07-16\n\n## What they do\n\nA claim [1].\n"),
         False, "no Sources entry"),
    ]
    results = [case(*c) for c in cases]
    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
