# doc-template

A project-agnostic, **versioned** documentation system for AI-assisted repos. Copy it into any project —
a web app, a game, a browser extension, a library — and it gives every kind of knowledge exactly one home,
enforced by a linter, so the docs **compound instead of sprawling** and never silently drift.

Plain Markdown that lives beside the code, versions with it, and is read by humans and agents with zero
tooling — plus one stdlib-Python linter that ships in the payload.

## What's in the box

```
template/              ← the copy-me payload — the ONLY thing a project takes
  .ai/
    BRIEF.md  CODEMAP.md  MEMORY.md    always-loaded orientation (fill per project)
    README.md                          the map of the doc system
    .doc-version                       which doc-template version this project is on
    scripts/doc-lint                   the linter (stdlib Python, zero install)
    scripts/test_doc_lint.py           its teeth-test (ships with it)
    prd/            catalog + tested contracts (the source of truth)
    prd-drafts/     catalog + proposals, isolated until approved
    research/       catalog + prior-art notes        references/  catalog + visual targets
    guides/         the docs-* standards (rules, template built in) + project how-tos
    tmp/            git-ignored scratch

VERSION                the current doc-template version
CHANGELOG.md           version history → links to each migration
.changes/              one dated migration file per release (how to upgrade a project)
```

Everything under `template/.ai/` is copied into a project. Everything else governs *this* repo and is not
copied.

## The two ideas to internalize

1. **One fact, one home.** Every doc answers one question; no fact is written twice. A home's `README.md`
   is its **catalog** (what's inside); the **rules** for writing live in `guides/docs-*.md`.
2. **A PRD is a tested contract.** Requirements carry IDs and map to tests; a proposal stays isolated in
   `prd-drafts/` until it's approved, built, and proven. `doc-lint` enforces the whole model.

## Adopt it in a project

1. Copy the contents of `template/` into the target repo (its `.ai/`, including hidden `.doc-version`).
2. Adapt the repo's `AGENTS.md` to the stack; fill `.ai/BRIEF.md` and `.ai/CODEMAP.md`.
3. Declare the project's components in `.ai/prd/README.md` (the owner's call).
4. Wire CI to run `python3 .ai/scripts/test_doc_lint.py` and `python3 .ai/scripts/doc-lint .ai`.

The model never changes between projects — only the orientation content and the component list do.

## Versioning

SemVer, in `VERSION`. A project records its adopted version in `.ai/.doc-version`. When it falls behind,
`CHANGELOG.md` and the dated files in `.changes/` give an agent the exact steps to migrate. See
[`AGENTS.md`](./AGENTS.md) for how to cut a new version.
