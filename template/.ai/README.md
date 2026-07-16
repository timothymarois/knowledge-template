# .ai/ — how this project remembers what it learns

Read this first. It maps every home so the docs **compound instead of sprawling**. The rule behind all of
it: **one fact, one home.**

**Agent-first, human-readable.** These docs exist so an agent can load the *minimum* context to act
correctly — deterministic structure, cross-references that resolve, every doc self-contained (full context
from the repo, never an external tracker).

## Two tiers

- **Always-loaded orientation** — the three files at this level: `BRIEF.md` (what & why), `CODEMAP.md`
  (where things are), `MEMORY.md` (current friction to avoid). Small and stable; read at the **start of
  every task**.
- **On-demand depth** — the directories below. Open one only when your task **enters that area**.

The split is just files vs. directories: read the three files every task; open a directory when you need it.

## The homes

Each home is a directory with a `README.md` that is its **catalog** (what's inside). The **rules** for
writing live in `guides/`, never in a catalog.

| Home | Holds | Rules |
|---|---|---|
| `research/` | Prior art — dated notes on how the world solves a problem | `guides/docs-research.md` |
| `references/` | Visual targets — screenshots, UI to match | catalog README |
| `prd-drafts/` | Proposals **not yet approved**, isolated | `guides/docs-prd.md` |
| `prd/` | **Tested contracts — the source of truth** | `guides/docs-prd.md` |
| `guides/` | The `docs-*` standards (shipped) + project how-tos | `guides/README.md` |

Two directories here aren't doc homes: `scripts/` holds the shipped tooling (the linter + its teeth-test),
and `tmp/` is git-ignored scratch. Each has its own `README.md`.

```
research/ + references/  ──►  prd-drafts/  ──approve + build + prove──►  prd/<layer-node>.md
(input, aimed-at targets)     (isolated proposal)                       (tested contract)
guides/  = how to write each doc (docs-*) and how to run repeat tasks
MEMORY.md = friction we've hit (always loaded) · delete an entry once it's solved
```

## The one rule that keeps it clean

**A PRD is a *tested* contract, born when a system ships — not a plan for one.**

- A proposal lives isolated in `prd-drafts/`; it graduates to `prd/` only when approved, built, and proven.
- Every requirement has an ID (`R-<AREA>-<n>`) *and* a test; behavior and its PRD change in the same commit.
- One system, one PRD file, one namespace. A `prd/` contract never cites a `prd-drafts/` proposal.
- A PRD states what *is* true. Friction and dead-ends go to `MEMORY.md`, never a PRD.
- Cite, don't copy: link a `research/` note instead of re-explaining it.

## Friction lives in MEMORY, not here

Traps, gotchas, and non-obvious constraints go in `MEMORY.md` (always loaded, this codebase only). It's a
**living list: delete an entry once the friction is solved.** A trap that hardens into a permanent rule
graduates to `AGENTS.md`.

## Writing & upkeep

Before you create or edit a doc, **read its home's `README.md` (the catalog) and the guide it points to**.
Then, for every doc:

- **One question per section**, said once, briefly — never the same fact twice.
- **No stubs** — fill every `<placeholder>`; delete an empty section rather than writing "none".
- **Keep it true** — update a doc in the same task that changes reality; prune stale lines in passing.
- **Self-contained & PII-free** — full context from the repo; refer to people by role; no external tracker.

## Versioning

This doc system is versioned by **[doc-template](https://github.com/timothymarois/doc-template)** — the
adopted version is stamped in `.doc-version`. When it's behind, the source repo's `CHANGELOG.md` and the
dated files in `.changes/` say exactly how to migrate. Run `python3 .ai/scripts/doc-lint .ai` to check the
structure (and `scripts/test_doc_lint.py` to verify the linter itself).
