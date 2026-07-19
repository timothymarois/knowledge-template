---
id: CITE
name: Citations
last_verified: 2026-07-19
---

## What this is

What emerges once contracts reference each other: a graph of requirement IDs. Because each file owns one
namespace (R-PRD-1), an ID names its owner, and a reference to it is the way a shared rule is obeyed in
two places without being written twice.

## Why it exists

- A shared rule is written once and cited, so the two copies can never disagree.
- A reference always leads somewhere, so following one is never wasted.
- A ratified contract never rests on something the owner has not approved.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-CITE-1 | No requirement ID is defined in two files | `duplicate ID across files` |
| ✅ | R-CITE-2 | Every cited requirement ID resolves | `citation resolves nowhere` |
| ✅ | R-CITE-3 | A contract never cites an unapproved draft | `contract cites a draft` |
| ✅ | R-CITE-4 | Citations only go up the layer stack | `citation into a later layer` |
