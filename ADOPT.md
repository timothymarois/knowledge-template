# Adopting knowledge-template

How to install this documentation system into a project and wire it into the project's agent rules. Work
through the steps in order — the result is a project **set up ready to go**: the agent rules wired, the
orientation docs written, the components declared, and the linter green.

## 1. Copy the payload

Copy the **contents of `template/`** into the target repo's root. You get a `.knowledge/` directory —
include the hidden `.knowledge/.version` stamp. Nothing outside `template/` is copied.

## 2. Wire it into `AGENTS.md` — the important step

`AGENTS.md`'s job here is small: make the agent **aware** of the knowledge base and route it to the right
doc. It states *what's available and what to follow* — it does **not** restate the rules, which already
live in `.knowledge/guides/` and the map. Add a compact block like this near the top, ahead of the stack
rules (adapt the wording, keep it lean):

```md
## Documentation (`.knowledge/`)

Load light; pull depth only when the task reaches for it.

1. **Always:** read `.knowledge/BRIEF.md` (what & why), `.knowledge/CODEMAP.md` (where things are),
   `.knowledge/MEMORY.md` (current friction). `.knowledge/README.md` is the map to everything else.
2. **On demand, when the task enters an area:** `.knowledge/prd/` (tested contracts — the source of
   truth), `.knowledge/prd-drafts/` (proposals, not yet approved), `.knowledge/research/` +
   `.knowledge/references/` (prior art and visual targets), `.knowledge/guides/` (how to write each doc —
   the `docs-*` standards — plus project how-tos for recurring tasks).
3. Before writing or modifying a doc, follow its guide in `.knowledge/guides/`; for a recurring task, check
   `guides/` for a how-to first. A new guaranteed behavior is a `prd/` requirement backed by a test.
4. `.knowledge/scripts/` holds the doc linter (and is where project helper scripts go); `.knowledge/tmp/`
   is git-ignored scratch for anything you generate.
5. Run `python3 .knowledge/scripts/doc-lint .knowledge` before finishing.
```

That's the whole footprint in `AGENTS.md`. The deeper rules — PRD graduation, citing `R-<AREA>-<n>` in
code, keeping docs true in the same task — live in the guides and the map; the agent reads them on demand,
so they're never copied here (and never drift).

## 3. Produce the orientation docs

Write these for this project — leave no placeholders. This means **researching the codebase**, not guessing
from memory. If your harness supports subagents, delegate that research: fan out parallel readers over the
repo's layers and synthesize their findings into the docs — faster, and it keeps your own context lean. Each
doc has a guide that defines its format:

- **`.knowledge/BRIEF.md`** — what the project is, who it serves, and its scope. Write it following
  `.knowledge/guides/docs-brief.md`.
- **`.knowledge/CODEMAP.md`** — the structural map: where each layer and kind of thing lives. Survey the repo
  layer by layer and write it following `.knowledge/guides/docs-codemap.md`.
- **`.knowledge/MEMORY.md`** — starts empty; friction accrues as you work.

Then adapt the rest of `AGENTS.md` to the stack.

## 4. Declare the components

Declare the project's ontology — its layers, in order — in `.knowledge/prd/README.md`, following
`.knowledge/guides/docs-prd.md` (the owner's call). This is what the linter checks every PRD filename
against.

## 5. Wire the linter into the build

Add both commands to the project's check gate so docs fail the build alongside code:

```
python3 .knowledge/scripts/test_doc_lint.py     # the linter has teeth
python3 .knowledge/scripts/doc-lint .knowledge  # the docs are valid
```

**pnpm / npm** — `package.json`:

```json
{ "scripts": {
  "lint:docs": "python3 .knowledge/scripts/doc-lint .knowledge",
  "test:docs": "python3 .knowledge/scripts/test_doc_lint.py"
} }
```

**Composer** — `composer.json`:

```json
{ "scripts": { "lint:docs": "python3 .knowledge/scripts/doc-lint .knowledge" } }
```

**GitHub Action (do this).** Create `.github/workflows/doc-lint.yml` in the project so the linter runs on
every push and PR — modeled on knowledge-template's own workflow:

```yaml
name: doc-lint
on: [push, pull_request]
jobs:
  doc-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.x' }
      - run: python3 .knowledge/scripts/test_doc_lint.py
      - run: python3 .knowledge/scripts/doc-lint .knowledge
```

## Done

Once everything's in place, **run the linter**: `python3 .knowledge/scripts/doc-lint .knowledge` (and
`test_doc_lint.py`). Green means the project is **set up ready to go** — agent rules wired, orientation
written, components declared, CI auto-checking. From here the docs stay current, because a broken one fails
the build.
