#!/usr/bin/env python3
"""Teeth-test for doc-lint — ships in the payload beside the linter.

A valid project must pass; each mutation must fail on its own rule. If any check
here fails, the linter has lost a tooth. Run:

    python3 .ai/scripts/test_doc_lint.py
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DOC_LINT = os.path.join(HERE, "doc-lint")

GOOD = {
    "prd/README.md": """# prd/ — catalog

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
""",
    "prd/base-core.md": """---
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
""",
    "prd/entity-widget.md": """---
id: WIDGET
name: Widget
---

## What this is

A widget, built on R-CORE-1.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ❌ | R-WIDGET-1 | A widget reports its state on demand | — |
""",
}


def build(root, files):
    for rel, content in files.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)


def run(root):
    p = subprocess.run([sys.executable, DOC_LINT, root], capture_output=True, text=True)
    return p.returncode, p.stdout


def case(name, mutate, expect_ok, expect_sub=None):
    files = dict(GOOD)
    mutate(files)
    with tempfile.TemporaryDirectory() as d:
        build(d, files)
        code, out = run(d)
    ok = (code == 0)
    passed = (ok == expect_ok) and (expect_sub is None or expect_sub in out)
    detail = "" if passed else f"  (exit={code}, wanted_ok={expect_ok}, sub={expect_sub!r})\n{out}"
    print(f"[{'PASS' if passed else 'FAIL'}] {name}{detail}")
    return passed


def set_(f, k, v):
    f[k] = v


def main():
    cases = [
        ("valid project passes", lambda f: None, True, None),
        ("two namespaces in one file",
         lambda f: set_(f, "prd/entity-widget.md", f["prd/entity-widget.md"].replace("R-WIDGET-1", "R-OTHER-1")),
         False, "does not match file namespace"),
        ("duplicate ID across files",
         lambda f: set_(f, "prd/base-core.md",
                        f["prd/base-core.md"].replace("id: CORE", "id: WIDGET").replace("R-CORE-1", "R-WIDGET-1")),
         False, "already defined"),
        ("requirement over 25 words",
         lambda f: set_(f, "prd/base-core.md", f["prd/base-core.md"].replace(
             "persists between runs",
             "persists between runs and also across every conceivable restart cycle no matter how many "
             "times the machine happens to reboot itself over and over again without any exception")),
         False, "max 25"),
        ("numeric literal in requirement",
         lambda f: set_(f, "prd/base-core.md", f["prd/base-core.md"].replace("between runs", "for 30 runs")),
         False, "numeric literal"),
        ("checkmark with no test named",
         lambda f: set_(f, "prd/base-core.md", f["prd/base-core.md"].replace("| `coreHolds` |", "| — |")),
         False, "names no test"),
        ("contract cites a draft",
         lambda f: (set_(f, "prd-drafts/entity-future.md",
                         "---\nid: FUTURE\nname: Future\n---\n\n## Requirements\n\n"
                         "|  | ID | Requirement | Evidence |\n|:--:|---|---|---|\n"
                         "| ❌ | R-FUTURE-1 | A future thing exists | — |\n"),
                    set_(f, "prd/entity-widget.md",
                         f["prd/entity-widget.md"].replace("built on R-CORE-1.", "built on R-CORE-1 and R-FUTURE-1."))),
         False, "prd-drafts/ proposal"),
        ("citation resolves nowhere",
         lambda f: set_(f, "prd/entity-widget.md", f["prd/entity-widget.md"].replace("R-CORE-1.", "R-GHOST-9.")),
         False, "resolves nowhere"),
        ("catalog omits a PRD file",
         lambda f: set_(f, "prd/README.md", f["prd/README.md"].replace("  - [entity-widget](./entity-widget.md)\n", "")),
         False, "Contents omits"),
        ("last_verified without a checkmark",
         lambda f: set_(f, "prd/entity-widget.md",
                        f["prd/entity-widget.md"].replace("name: Widget\n---", "name: Widget\nlast_verified: 2026-07-16\n---")),
         False, "no ✅ row"),
    ]
    results = [case(*c) for c in cases]
    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
