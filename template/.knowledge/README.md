# .knowledge/ — what lives here

The project's knowledge base: one home for each kind of doc, read by agents as they work. This is a map of
*what's here and where to go* — how to write each doc lives in its `guides/docs-*.md`.

## Two tiers

- **Always-loaded orientation** — the three files at this level: `BRIEF.md` (what & why), `CODEMAP.md`
  (where things are), `MEMORY.md` (current friction). Read at the start of every task.
- **On-demand depth** — the directories below. Open one only when your task enters that area.

## The homes

Each home's `README.md` is its **catalog** (what's inside); how to *write* the doc lives in the guide named
here.

| Home | Holds | How to write it |
|---|---|---|
| `research/` | Prior art — dated notes on how others solved a problem | `guides/docs-research.md` |
| `references/` | Visual targets — screenshots, UI to match | its catalog README |
| `prd-drafts/` | Proposals, not yet approved | `guides/docs-prd.md` |
| `prd/` | **Tested contracts — the source of truth** | `guides/docs-prd.md` |
| `guides/` | The `docs-*` writing standards + project how-tos | `guides/README.md` |

`scripts/` holds the tooling (the linter + its test); `tmp/` is git-ignored scratch. Work flows
`research/` + `references/` → `prd-drafts/` → `prd/`.

## Versioning

Versioned by [knowledge-template](https://github.com/timothymarois/knowledge-template); the adopted version
is stamped in `.version`. To update, follow the upgrade steps in that repo.
