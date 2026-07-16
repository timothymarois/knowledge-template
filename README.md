# doc-template

**A documentation system that keeps AI coding agents standardized.** Drop it into any repo — web app,
game, extension, library. Every kind of knowledge gets one home, one writing standard, and a linter that
fails the build when a doc drifts. Plain Markdown, one stdlib linter, zero other tooling.

> **Adopting it? Hand this prompt to your coding agent — it runs the whole setup:**
>
> ```
> Adopt the doc-template documentation system into this repo:
> https://github.com/timothymarois/doc-template
>
> Follow its README "Adopting this doc template" section end to end:
> 1. Copy the contents of template/ into our repo root (its .ai/, including hidden .doc-version).
> 2. Embed the .ai/ load-order rules as the FIRST rules in our AGENTS.md.
> 3. Fill .ai/BRIEF.md and .ai/CODEMAP.md for this project.
> 4. Declare our components in .ai/prd/README.md.
> 5. Wire python3 .ai/scripts/doc-lint .ai (and test_doc_lint.py) into our lint/CI.
> ```

## What it does

AI agents write docs well and keep them consistent badly. Left alone, each invents its own structure and
the docs rot. doc-template makes the standard **executable, not a page nobody rereads**:

- **One home per kind of doc** — no fact is written twice.
- **Rules ship as guides, template built in** — every agent produces the same shape.
- **A linter enforces it** — a broken doc fails CI like broken code.
- **Versioned** — one upstream, a dated migration for every change.

## What's in the box

```
template/          ← the copy-me payload (the only thing a project takes)
  .ai/
    BRIEF · CODEMAP · MEMORY   always-loaded orientation (what · where · friction)
    README.md                  the map
    .doc-version               the version this repo is on
    prd/          tested contracts — the source of truth   (catalog)
    prd-drafts/   proposals, isolated until approved        (catalog)
    research/     prior-art notes                           (catalog)
    references/   visual targets                            (catalog)
    guides/       writing standards (docs-*) + project how-tos
    scripts/      doc-lint + test_doc_lint.py
    tmp/          git-ignored scratch

VERSION · CHANGELOG.md · .changes/    version + a dated migration per release (not copied)
```

Two rules hold it together: **one fact, one home** — a home's `README.md` is its catalog, the rules live in
`guides/`; and **a PRD is a tested contract** — requirements carry IDs mapped to tests, and proposals stay
isolated in `prd-drafts/` until proven.

## What the linter enforces

Every rule is a check in `scripts/doc-lint`, teeth-tested in `scripts/test_doc_lint.py` — a valid project
passes, breaking any rule fails on that rule. The linter holds itself to the same keyed table it enforces
on your PRDs:

|  | ID | Requirement |
|:--:|---|---|
| ✅ | R-DOC-1 | Every shipped directory exists |
| ✅ | R-DOC-2 | Every shipped file and guide exists |
| ✅ | R-DOC-3 | BRIEF, CODEMAP, MEMORY end with their standard pointer |
| ✅ | R-DOC-4 | A PRD file holds exactly one namespace |
| ✅ | R-DOC-5 | No requirement ID is defined in two files |
| ✅ | R-DOC-6 | A requirement is at most 25 words |
| ✅ | R-DOC-7 | A requirement names its tunables, never a numeric literal |
| ✅ | R-DOC-8 | A verified requirement names the test that proves it |
| ✅ | R-DOC-9 | `last_verified` is present only with a verified row |
| ✅ | R-DOC-10 | Every cited requirement ID resolves |
| ✅ | R-DOC-11 | A contract never cites an unapproved draft |
| ✅ | R-DOC-12 | Citations only go up the layer stack |
| ✅ | R-DOC-13 | A PRD's filename prefix is a declared component |
| ✅ | R-DOC-14 | A PRD uses only the closed schema headings |
| ✅ | R-DOC-15 | The prd catalog lists every PRD |
| ✅ | R-DOC-16 | Every research note is dated |
| ✅ | R-DOC-17 | Every research citation resolves to a source |
| ✅ | R-DOC-18 | Every catalog link resolves to a real file |
| ✅ | R-DOC-19 | Every shipped README keeps its required sections |

## Adopting this doc template

1. **Copy the payload** — `template/`'s contents into the repo root (its `.ai/`, including `.doc-version`).
2. **Embed it in `AGENTS.md`** — make the `.ai/` load order the first rules (below).
3. **Fill orientation** — `.ai/BRIEF.md`, `.ai/CODEMAP.md`; adapt `AGENTS.md` to the stack.
4. **Declare components** in `.ai/prd/README.md`.
5. **Wire the linter into your build** (below).

### Embed it as the first rule in `AGENTS.md`

Agents must load it **first**, so it goes at the top of `AGENTS.md`. Fold the substance into your own rules
— don't paste verbatim:

- **Load first, every task:** `.ai/BRIEF.md`, `.ai/CODEMAP.md`, `.ai/MEMORY.md`. Map: `.ai/README.md`.
- **On demand:** `.ai/prd/` (contracts — source of truth), `.ai/prd-drafts/` (proposals, never cite as
  settled), `.ai/research/` + `.ai/references/` (prior art, targets), `.ai/guides/` (how to write each doc).
- **Before editing a doc:** read its `README.md` (catalog) and `guides/docs-*.md` (rules).
- **Before finishing:** run `python3 .ai/scripts/doc-lint .ai`.

### Wire the linter into your build

Stdlib Python, zero install — any toolchain can call it:

```
python3 .ai/scripts/test_doc_lint.py     # the linter has teeth
python3 .ai/scripts/doc-lint .ai         # the docs are valid
```

**pnpm / npm** — `package.json`:

```json
{ "scripts": {
  "lint:docs": "python3 .ai/scripts/doc-lint .ai",
  "test:docs": "python3 .ai/scripts/test_doc_lint.py"
} }
```

**Composer** — `composer.json`:

```json
{ "scripts": { "lint:docs": "python3 .ai/scripts/doc-lint .ai" } }
```

**CI** — run both as steps (reference: `.github/workflows/doc-lint.yml`):

```yaml
- run: python3 .ai/scripts/test_doc_lint.py
- run: python3 .ai/scripts/doc-lint .ai
```

Chain them into your existing check gate so docs fail the build alongside code.

## Versioning

SemVer in `VERSION`; a project stamps its adopted version in `.ai/.doc-version`. When it falls behind,
`CHANGELOG.md` and `.changes/` give the exact migration steps.

> **Behind on the version? Hand this prompt to your coding agent:**
>
> ```
> Update this repo's doc-template to the latest version:
> https://github.com/timothymarois/doc-template
>
> 1. Compare our .ai/.doc-version to the upstream VERSION.
> 2. If upstream is newer, read each .changes/<date>-v<version>.md between our version and
>    the latest, in order.
> 3. Apply each migration's steps exactly, then run python3 .ai/scripts/doc-lint .ai until clean.
> 4. Set .ai/.doc-version to the new version.
> ```

See [`AGENTS.md`](./AGENTS.md) to cut a new version.
