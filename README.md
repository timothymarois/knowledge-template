# doc-template

**A documentation system that keeps AI coding agents standardized.** Drop it into any repo — web app,
game, browser extension, library — and every kind of knowledge gets exactly one home, one writing
standard, and a linter that fails the build when a doc drifts. Plain Markdown beside the code, one
standard-library linter, zero other tooling.

## What it does

AI agents are good at writing docs and bad at keeping them consistent. Left alone, each agent invents its
own structure — PRDs in three shapes, notes that contradict each other, the same fact in five files. The
docs rot, and the next agent trusts the rot.

doc-template stops that by making the standard **executable**, not a wiki page nobody rereads:

- **One home per kind of knowledge** — orientation, a code map, friction notes, research, visual targets,
  proposals, tested contracts, how-to guides. No fact is written twice.
- **The rules ship as guides, with the template built in.** An agent writing a PRD or a research note reads
  one file and produces the same shape every time — in every repo.
- **A linter enforces it in your build.** A doc that breaks the standard fails CI exactly like broken code,
  so agents can't drift and stay drifted. The linter ships *inside* the payload and self-tests.
- **It's versioned.** One upstream, a dated migration for every change — so every repo can catch up on
  demand instead of forking its own rules.

The result: documentation that stays as trustworthy and current as the code, across every project and
every agent that touches it.

## What's in the box

```
template/            ← the copy-me payload — the ONLY thing a project takes
  .ai/
    BRIEF · CODEMAP · MEMORY     always-loaded orientation (what · where · current friction)
    README.md                    the map of the system
    .doc-version                 which doc-template version this repo is on
    prd/           tested contracts — the source of truth   (catalog README)
    prd-drafts/    proposals, isolated until approved        (catalog README)
    research/      prior-art notes    references/  visual targets   (catalog READMEs)
    guides/        the docs-* writing standards (rules + template) + project how-tos
    scripts/       doc-lint (the linter) + test_doc_lint.py (its teeth-test)
    tmp/           git-ignored scratch

VERSION · CHANGELOG.md · .changes/   version + a dated migration per release (governs this repo, not copied)
```

Two ideas hold it together: **one fact, one home** (a home's `README.md` is its catalog; the rules live in
`guides/`), and **a PRD is a tested contract** — requirements carry IDs mapped to tests, and a proposal
stays isolated in `prd-drafts/` until it's approved, built, and proven.

## What the linter enforces

The doc system holds itself to its own standard — these are the requirements `doc-lint` enforces, in the
same keyed table it enforces on your PRDs. Each is **teeth-tested** in `template/.ai/scripts/test_doc_lint.py`:
a valid project passes, and breaking the rule fails on that row. The Evidence column names the test that
proves it.

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-DOC-1 | Every shipped directory exists | *a home directory was removed* |
| ✅ | R-DOC-2 | Every shipped file and guide exists | *a shipped guide was removed*, *the linter script was renamed away* |
| ✅ | R-DOC-3 | BRIEF, CODEMAP, and MEMORY each end with their standard pointer | *a trio file lost its standard pointer* |
| ✅ | R-DOC-4 | A PRD file holds exactly one namespace | *two namespaces in one file* |
| ✅ | R-DOC-5 | No requirement ID is defined in two files | *duplicate ID across files* |
| ✅ | R-DOC-6 | A requirement is at most 25 words | *requirement over 25 words* |
| ✅ | R-DOC-7 | A requirement names its tunables, never a numeric literal | *numeric literal in requirement* |
| ✅ | R-DOC-8 | A verified requirement names the test that proves it | *checkmark with no test named* |
| ✅ | R-DOC-9 | `last_verified` is present only when a verified row exists | *last_verified without a checkmark* |
| ✅ | R-DOC-10 | Every cited requirement ID resolves | *citation resolves nowhere* |
| ✅ | R-DOC-11 | A contract never cites an unapproved draft | *contract cites a draft* |
| ✅ | R-DOC-12 | Citations only go up the layer stack | *citation into a later layer* |
| ✅ | R-DOC-13 | A PRD's filename prefix is a declared component | *filename prefix not a component* |
| ✅ | R-DOC-14 | A PRD uses only the closed schema headings | *heading outside the schema* |
| ✅ | R-DOC-15 | The prd catalog lists every PRD | *catalog omits a PRD file* |
| ✅ | R-DOC-16 | Every research note is dated | *research note missing its date* |
| ✅ | R-DOC-17 | Every research citation resolves to a source | *research citation without a source* |
| ✅ | R-DOC-18 | Every link in every catalog resolves to a real file | *a catalog links to a missing file* |
| ✅ | R-DOC-19 | Every shipped README keeps its required sections | *a README is missing a required section* |

The checks live in `template/.ai/scripts/doc-lint`; the tests that prove them, in `test_doc_lint.py`. If a
rule isn't in this table, it's teaching, not law.

## Adopting this doc template

1. **Copy the payload.** Copy the contents of `template/` into the target repo — its `.ai/`, including the
   hidden `.doc-version` stamp. Nothing outside `template/` is copied.
2. **Register it in `AGENTS.md`.** Paste the rule block below so every agent loads the project's docs.
3. **Fill orientation.** Fill `.ai/BRIEF.md` and `.ai/CODEMAP.md`; adapt `AGENTS.md` to the stack.
4. **Declare components** in `.ai/prd/README.md` (the owner's call).
5. **Wire the linter into your build** (below), so a broken doc fails the same gate as broken code.

The model never changes between projects — only the orientation content and the component list do.

### Register the docs in `AGENTS.md`

This is the step that makes agents actually use the system. Paste it into the project's `AGENTS.md`:

```md
## Documentation (`.ai/`)

Load first, every task: `.ai/BRIEF.md` (what & why), `.ai/CODEMAP.md` (where things are),
`.ai/MEMORY.md` (current friction). Then read on demand when your task enters an area:

- `.ai/prd/` — tested contracts: what the product must do. The source of truth.
- `.ai/prd-drafts/` — proposals, not yet approved; never cite as settled.
- `.ai/research/` + `.ai/references/` — prior art and visual targets.
- `.ai/guides/` — how to write each doc (`docs-*.md`) and run recurring tasks.

Before editing a doc, read its home's `README.md` (the catalog) and its `guides/docs-*.md` (the rules).
The map is `.ai/README.md`. Run `python3 .ai/scripts/doc-lint .ai` before finishing.
```

### Wire the linter into your build

The linter is stdlib Python with zero install, so any toolchain can call it. Two commands — the self-test
proves the linter is sound, the lint checks your docs:

```
python3 .ai/scripts/test_doc_lint.py     # the linter still has teeth
python3 .ai/scripts/doc-lint .ai         # the docs are valid
```

**pnpm / npm** — add to `package.json` and chain it into your existing gate so it runs on every check:

```json
{
  "scripts": {
    "lint:docs": "python3 .ai/scripts/doc-lint .ai",
    "test:docs": "python3 .ai/scripts/test_doc_lint.py",
    "check": "npm run lint && npm run lint:docs && npm run test:docs"
  }
}
```

**Composer (PHP)** — add to `composer.json`:

```json
{
  "scripts": {
    "lint:docs": "python3 .ai/scripts/doc-lint .ai",
    "check": ["@lint", "@lint:docs", "@test"]
  }
}
```

**Make / anything else:**

```make
lint-docs:
	python3 .ai/scripts/test_doc_lint.py
	python3 .ai/scripts/doc-lint .ai
```

**CI** — run both as steps (see this repo's `.github/workflows/doc-lint.yml` for a reference workflow):

```yaml
- run: python3 .ai/scripts/test_doc_lint.py
- run: python3 .ai/scripts/doc-lint .ai
```

Wherever it runs, the effect is the same: docs that drift from the standard fail the build, so they stay
current with the code instead of rotting beside it.

## Versioning

SemVer, in `VERSION`. A project records its adopted version in `.ai/.doc-version`. When it falls behind,
`CHANGELOG.md` and the dated files in `.changes/` give an agent the exact steps to migrate. See
[`AGENTS.md`](./AGENTS.md) for how to cut a new version.
