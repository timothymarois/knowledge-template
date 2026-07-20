# Adopting knowledge-template

How to install this documentation system into a project and wire it into the project's agent rules. Work
through the steps in order — the result is a project **set up ready to go**: the agent rules wired, the
orientation docs written, the components declared, and the linter green.

## 1. Copy the payload

Copy the **contents of `template/`** into the target repo's root. You get a `.knowledge/` directory —
include the hidden `.knowledge/.version` stamp. Nothing outside `template/` is copied.

## 2. Fold in any docs system already here

If the repo already keeps agent docs somewhere else — `.ai/`, `docs/agents/`, a `CONTEXT.md`, a loose
`PRD/` folder — **migrate its content into the homes and delete the old location in this same task.**
Leaving it produces two homes for the same fact, which is the one failure this system exists to prevent,
and the linter cannot see a stale directory it was never told about. If something there has no home, or
you don't have the standing to delete it, **stop and say so** rather than adopting alongside it.

## 3. Write the project's `AGENTS.md`

`AGENTS.md` sits at the repo root and is the first thing an agent reads — it routes into `.knowledge/` and
encodes this stack's rules. **Write it following `.knowledge/guides/docs-agents.md`**, which carries the full
template: the ship-as-written sections (the `.knowledge/` load order, hard gates, documentation duties) plus
the stack sections you research and adapt (tech, architecture, best practices, build / test / run). Keep the
ship-as-written sections verbatim so this repo behaves like every other.

**Already have an `AGENTS.md`? Reconcile, don't replace** — follow *The repo already has an `AGENTS.md`*
in that guide. Every rule in the old file survives into the new one or is raised; none is dropped in a
reformat.

**This step is required, not optional** — `doc-lint` fails if the repo root has no `AGENTS.md`, or if it
doesn't name all three of `.knowledge/BRIEF.md`, `.knowledge/CODEMAP.md`, and `.knowledge/MEMORY.md`.
Nothing else about the file is inspected; write the rest however this project wants.

## 4. Produce the orientation docs

Write these for this project — leave no placeholders. This means **researching the codebase**, not guessing
from memory. If your harness supports subagents, delegate that research: fan out parallel readers over the
repo's layers and synthesize their findings into the docs — faster, and it keeps your own context lean. Each
doc has a guide that defines its format:

- **`.knowledge/BRIEF.md`** — what the project is, who it serves, and its scope. Write it following
  `.knowledge/guides/docs-brief.md`.
- **`.knowledge/CODEMAP.md`** — the structural map: where each layer and kind of thing lives. Survey the repo
  layer by layer and write it following `.knowledge/guides/docs-codemap.md`.
- **`.knowledge/MEMORY.md`** — starts empty; friction accrues as you work.

**Before moving on, separate what you sourced from what you guessed.** Scope and external systems come out
of the code; **the story, the users, and what the project refuses do not.** List which `BRIEF.md` sections
you sourced (and from where) and which you inferred, and **get the inferred ones confirmed** — the same
sign-off the components need in step 5. A brief that reads as confident and is quietly wrong is loaded on
every task afterwards and nobody re-checks it.

**Leave no placeholder.** `doc-lint` fails while `BRIEF.md` or `CODEMAP.md` still carries a shipped
`<project>` title or a `_(none)_` marker — a green lint is supposed to mean the project really is set up.

## 5. Declare the components

Declare the project's ontology — its layers, in order — in `.knowledge/prd/README.md`, following
`.knowledge/guides/docs-prd.md`. This is what the linter checks every PRD filename against, and every
requirement the project ever writes gets filed against it.

**It is the owner's call, not yours.** Propose a set with a one-line gloss each — the shipped
`base-`/`entity-`/`flow-` default, or names that fit this domain better — and **get the owner's explicit
sign-off before writing it in.** Do not adopt a silent default: an ontology guessed at adoption is the
hardest thing in the system to change later, because IDs are permanent.

## 6. Wire the linter into the build

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
name: Knowledge Lint
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
