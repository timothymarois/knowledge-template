# prd/ — tested contracts (catalog)

The **catalog** of this project's PRDs — the ratified, test-backed contracts for what the product does,
one file per built system. This README is navigation, not rules: **how to write a PRD is in
[`../guides/docs-prd.md`](../guides/docs-prd.md)** (the standard, template built in). Browse this
folder on GitHub and this catalog renders above the file list.

It has exactly two parts, with different owners.

## Components — authored

*The project's ontology, in order (`prefix — what it holds`) — the **only** thing a human writes in this
catalog. Adding a component is the largest change in the system: the owner decides, an agent stops and
asks. The lint rejects a line that isn't `prefix — gloss`.*

```
1. base-    — what the domain is fundamentally made of
2. entity-  — each kind of thing the domain contains
3. flow-    — behavior that emerges when entities interact
```

## Contents — generated

*A tree of links, regenerated and diffed by `doc-lint` — a hand-edit or a stale tree fails the build the
same way. Two levels only: component, then file. `— draft` marks a file no row of which has been verified.
Order is derived: component order, then a topological sort of the IDs each file cites.*

- **Base**
  - _(no PRDs yet)_
- **Entities**
  - _(no PRDs yet)_
- **Flow**
  - _(no PRDs yet)_

---
*Proposals not yet approved live isolated in [`../prd-drafts/`](../prd-drafts/) and never appear here
until they graduate.*
