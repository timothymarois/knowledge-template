# scripts/ — doc-system tooling

The tooling that **enforces** the doc system. Unlike everything else under `.ai/`, this is code, not prose
— stack-neutral, standard-library only, runs with nothing installed. It is **shipped and versioned by
`doc-template`**: do not rewrite it per project; it updates by version bump (see the root `CHANGELOG.md`).

## Contents

| Script | What it does |
|---|---|
| [`doc-lint`](./doc-lint) | Enforces the standard on `.ai/` — namespaces, IDs, citations, glyph tables, catalogs, research notes. A red lint is a broken doc. |
| [`test_doc_lint.py`](./test_doc_lint.py) | The linter's teeth-test: a valid project passes, each mutation fails on its own rule. If this fails, the linter has lost a tooth. |

## Usage

```
python3 .ai/scripts/doc-lint .ai          # lint this project's docs
python3 .ai/scripts/test_doc_lint.py      # prove the linter still works
```

Wire both into CI. The linter is the law: a rule that matters is a check here, teeth-tested beside it —
prose that isn't enforced is teaching, not law.
