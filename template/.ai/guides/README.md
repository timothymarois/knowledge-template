# guides/ — the rules, and how-tos (catalog)

The **catalog** of guides. Two kinds live here:

- **`docs-*.md` — shipped standards.** How to write each kind of doc (`docs-prd.md`, `docs-research.md`),
  template built in. These are shipped and **versioned by `doc-template`** — do not rewrite them per
  project; they update by version bump (see the root `CHANGELOG.md`).
- **`<verb-noun>.md` — project how-tos.** Recipes for tasks that repeat in *this* repo
  (`add-a-migration.md`, `deploy.md`). Authored fresh per project; a recipe, not a rationale.

## Contents — generated

*Regenerated and diffed by `doc-lint`.*

### Shipped standards (`docs-*`)

| Guide | The standard for |
|---|---|
| [docs-prd.md](./docs-prd.md) | Writing a PRD — tested contracts in `../prd/` (and drafts in `../prd-drafts/`) |
| [docs-research.md](./docs-research.md) | Writing a research note in `../research/` |
| [docs-brief.md](./docs-brief.md) | Writing `../BRIEF.md` — the always-loaded orientation |
| [docs-codemap.md](./docs-codemap.md) | Writing `../CODEMAP.md` — the structural map |
| [docs-memory.md](./docs-memory.md) | Writing `../MEMORY.md` — the friction list |

### Project how-tos

| Guide | How to |
|---|---|
| _(none yet)_ | |

## Rules for a project how-to

- **One task per file**, named for the action. Steps in order, with the actual commands and the check that
  confirms success. Keep it current; self-contained (never a ticket).
