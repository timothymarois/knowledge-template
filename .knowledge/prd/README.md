# prd/ — tested contracts (catalog)

The ratified, test-backed PRDs — one per built system. **To write or modify one, follow [`../guides/docs-prd.md`](../guides/docs-prd.md).**

These are the contracts for what the shipped `.knowledge/` system guarantees. Every row's evidence names a
case in [`../scripts/test_doc_lint.py`](../scripts/test_doc_lint.py); a rule with no case there is not a
rule. **A new rule is three things changed together: a check in `doc-lint`, a case in the teeth-test, and a
row here.**

## Components — authored

The project's ontology, in order (`prefix — gloss`). The owner's call; an agent stops and asks.

```
1. base-    — what the shipped system is made of
2. entity-  — each kind of doc the system governs
3. flow-    — behavior that emerges when docs reference each other
```

## Contents — maintained by hand

Add a row when you add a PRD; `doc-lint` fails the build if one is missing. Component, then file.

- **Base**
  - [base-payload](./base-payload.md) — the shipped tree of homes and files
- **Entities**
  - [entity-catalog](./entity-catalog.md) — each home's `README.md`
  - [entity-orientation](./entity-orientation.md) — the always-loaded trio
  - [entity-prd](./entity-prd.md) — the contracts themselves
  - [entity-research](./entity-research.md) — dated prior-art notes
- **Flow**
  - [flow-citations](./flow-citations.md) — the requirement-ID graph across contracts
