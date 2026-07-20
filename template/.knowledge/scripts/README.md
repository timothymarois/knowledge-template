# scripts/ — tooling & your workspace

Code, not prose — stack-neutral, standard-library only, runs with nothing installed.

The **shipped tooling** below is versioned by `knowledge-template`: don't rewrite it per project, it updates
by version bump. Everything else you drop in here is yours.

## Contents

| Script | What it does |
|---|---|
| [`doc-lint`](./doc-lint) | Enforces the standard on `.knowledge/` — namespaces, IDs, citations, glyph tables, catalogs, research notes. A red lint is a broken doc. |
| [`test_doc_lint.py`](./test_doc_lint.py) | The linter's teeth-test: a valid project passes, each mutation fails on its own rule. If this fails, the linter has lost a tooth. |

## Usage

```
python3 .knowledge/scripts/doc-lint .knowledge       # lint this project's docs
python3 .knowledge/scripts/doc-lint --map --write .knowledge  # regenerate .knowledge/MAP.md
python3 .knowledge/scripts/test_doc_lint.py        # prove the linter still works
```

Wire both into CI. A rule that matters is a check in `doc-lint`, teeth-tested beside it — prose that isn't
enforced is teaching, not law.

## Your scripts

This folder is also a workspace. Add project-specific helper scripts here — generators, build steps, one-off
checks, anything that helps an agent work in this repo. Keep the shipped `doc-lint` and `test_doc_lint.py`
unchanged (they're versioned); everything else here is yours to add and name.
