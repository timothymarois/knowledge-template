# .knowledge/ — what lives here

The project's knowledge base: one home per kind of doc. This maps what's here and where to go — how to write
each lives in its `guides/*.md`. 

## The homes

| Path | Holds | How to write it |
|---|---|---|
| `BRIEF.md` | Orientation — what & why (always-loaded) | `guides/docs-brief.md` |
| `CODEMAP.md` | Orientation — where things are (always-loaded) | `guides/docs-codemap.md` |
| `MEMORY.md` | Orientation — current friction (always-loaded) | `guides/docs-memory.md` |
| `prd/` | **Tested contracts — the source of truth** | `guides/docs-prd.md` |
| `prd-drafts/` | Proposals, not yet approved | `guides/docs-prd.md` |
| `research/` | Prior art — dated notes on how others solved a problem | `guides/docs-research.md` |
| `references/` | Visual targets — screenshots, UI to match | `references/README.md` |
| `guides/` | The writing standards (`docs-*`) + project how-tos | `guides/README.md` |
| `scripts/` | Tooling — the linter + its teeth-test | `scripts/README.md` |
| `tmp/` | Git-ignored scratch | — |

Work flows `research/` + `references/` → `prd-drafts/` → `prd/`.

## Versioning

Versioned by [knowledge-template](https://github.com/timothymarois/knowledge-template); the adopted version
is stamped in `.version`. To update, follow the upgrade steps in that repo.
