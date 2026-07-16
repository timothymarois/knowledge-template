# knowledge-template

**Keep your AI coding agents' documentation standardized.** One home for every kind of doc, one writing
standard, and a linter that fails the build when a doc drifts. Plain Markdown, one stdlib linter, zero setup.

### 💡 Why

Agents write docs well and keep them consistent badly — left alone, each invents its own structure and the
docs rot. knowledge-template makes the standard **executable**:

- **One home per kind of doc** — nothing is written twice
- **Rules ship as guides** — every agent produces the same shape
- **A linter enforces it in CI** — a broken doc fails like broken code
- **Versioned** — upgrade any repo with a dated migration

### 🚀 Adopt it

Hand this to your coding agent:

```
Adopt the knowledge-template documentation system into this repo:
https://github.com/timothymarois/knowledge-template

Follow the "Adopt it" steps in its README:
1. Copy template/.knowledge into our repo root (including hidden .doc-version).
2. Embed its rules into our AGENTS.md as the FIRST rules — the load order AND how work flows
   through the docs (PRDs are tested contracts; proposals stay in prd-drafts; keep docs true in
   the same task; run the linter before done). See the "What to embed in AGENTS.md" list below.
3. Fill BRIEF.md + CODEMAP.md; declare our components in prd/README.md.
4. Wire python3 .knowledge/scripts/doc-lint .knowledge into CI.
```

<details>
<summary>Manual steps + <b>what to embed in AGENTS.md</b></summary>

1. **Copy the payload** — `template/`'s contents into the repo root (its `.knowledge/`, including `.doc-version`).
2. **Embed the rules in `AGENTS.md`** (below), at the top, ahead of the stack rules.
3. **Fill orientation** — `.knowledge/BRIEF.md`, `CODEMAP.md`; adapt `AGENTS.md` to the stack.
4. **Declare components** in `.knowledge/prd/README.md`.
5. **Wire the linter** into your build (see *Wire it into your build*).

**What to embed in `AGENTS.md`** — not just the load order, but the whole way work flows through the docs.
Fold the substance into your own rules; don't paste verbatim:

- **Load order.** Every task, read first: `.knowledge/BRIEF.md` (what & why), `CODEMAP.md` (where),
  `MEMORY.md` (friction); map is `.knowledge/README.md`. On demand, when the task enters an area: `prd/`
  (tested contracts — the source of truth), `prd-drafts/` (proposals — never cite as settled), `research/`
  + `references/` (prior art, visual targets), `guides/` (how to write each doc).
- **PRDs are the contract.** A new guaranteed behavior needs a `prd/` requirement **and** a test — behavior
  and its PRD change in the same commit. Requirements come from the owner; a proposal stays in `prd-drafts/`
  until approved, built, and proven, then graduates by `git mv`. When code implements a requirement, cite
  its `R-<AREA>-<n>` so contract ↔ code ↔ test stay linked.
- **Keep docs true in the same task.** Before editing any doc, read its home `README.md` (catalog) and its
  `guides/docs-*.md` (rules). Restructured files → update `CODEMAP.md`. Hit friction → add a line to
  `MEMORY.md`, and delete it once solved.
- **Enforce it.** Run `python3 .knowledge/scripts/doc-lint .knowledge` before finishing; wire it into CI so
  drift fails the build.

</details>

### 📦 What's inside

```
template/                      the copy-me payload — the only thing a repo takes
  .knowledge/
    BRIEF.md                   what & why
    CODEMAP.md                 where things are
    MEMORY.md                  current friction
    README.md                  the map
    .doc-version               the adopted version
    prd/                       tested contracts — the source of truth
    prd-drafts/                proposals, isolated until approved
    research/                  prior-art notes
    references/                visual targets
    guides/                    the writing standards + project how-tos
    scripts/                   the linter + its test
    tmp/                       git-ignored scratch

VERSION                        the current version
CHANGELOG.md                   version history
.changes/                      dated migrations (how to upgrade)
```

Two rules hold it together: **one fact, one home** · **a PRD is a tested contract** (IDs mapped to tests).

### 🛡️ What the linter enforces

**19 rules, every one teeth-tested** — a valid project passes; break any rule and the build fails.

<details>
<summary>See all 19 rules</summary>

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

</details>

### 🔌 Wire it into your build

```
python3 .knowledge/scripts/doc-lint .knowledge         # the docs are valid
python3 .knowledge/scripts/test_doc_lint.py     # the linter has teeth
```

Chain both into your existing check gate so docs fail alongside code.

<details>
<summary>package.json · composer.json · CI</summary>

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

**CI** — reference workflow: `.github/workflows/doc-lint.yml`

```yaml
- run: python3 .knowledge/scripts/test_doc_lint.py
- run: python3 .knowledge/scripts/doc-lint .knowledge
```

</details>

### 🔁 Upgrading

SemVer in `VERSION`; each repo stamps its version in `.knowledge/.doc-version`. Behind? Hand this to your agent:

```
Update this repo's knowledge-template to the latest version:
https://github.com/timothymarois/knowledge-template

Compare .knowledge/.doc-version to the upstream VERSION. If behind, apply each
.changes/<date>-v<version>.md between them in order, re-run python3 .knowledge/scripts/doc-lint .knowledge
until clean, then bump .knowledge/.doc-version.
```
