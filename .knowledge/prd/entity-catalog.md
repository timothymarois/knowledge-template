---
id: CATALOG
name: Catalog
last_verified: 2026-07-19
---

## What this is

The `README.md` at the head of each home: what is inside that home, and where the rule for writing it
lives. A catalog lists and routes — it never carries the standard itself, which belongs to the home's
guide.

## Why it exists

- An agent can see everything a home holds without listing the directory.
- An agent about to write a doc is routed to its rule before it starts.
- A catalog that has drifted from the tree fails the build instead of misleading the next reader.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-CATALOG-1 | Every catalog lists everything in its home | `catalog omits a PRD file`, `catalog omits a research note` |
| ✅ | R-CATALOG-2 | Every catalog link resolves to a real file | `a catalog links to a missing file` |
| ✅ | R-CATALOG-3 | Every shipped catalog keeps its required sections | `a README is missing a required section` |
| ✅ | R-CATALOG-4 | Every catalog links to its writing guide | `a catalog is missing its guide link` |
