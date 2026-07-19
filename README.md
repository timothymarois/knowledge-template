# Knowledge Template for Agents

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

Read ADOPT.md in that repo and follow it end to end: copy template/.knowledge into our repo root,
embed its rules into our AGENTS.md as the first rules (load order + how work flows through the docs —
PRDs, drafts, doc duties), fill BRIEF.md + CODEMAP.md, declare our components in prd/README.md, and
wire python3 .knowledge/scripts/doc-lint .knowledge into CI.
```

Full install guide: **[ADOPT.md](./ADOPT.md)**.

### 📦 What's inside

```
template/                      the copy-me payload — the only thing a repo takes
  .knowledge/
    BRIEF.md                   what & why
    CODEMAP.md                 where things are
    MEMORY.md                  current friction
    README.md                  the map
    .version                   the adopted version
    prd/                       tested contracts — the source of truth
    prd-drafts/                proposals, isolated until approved
    research/                  prior-art notes
    references/                visual targets
    guides/                    the writing standards + project how-tos
    scripts/                   the linter + its test
    tmp/                       git-ignored scratch

.knowledge/                    this repo's own adopted copy — we run what we ship
VERSION                        the current version
CHANGELOG.md                   version history
.changes/                      dated migrations (how to upgrade)
```

Two rules hold it together: **one fact, one home** · **a PRD is a tested contract** (IDs mapped to tests).

### 🛡️ What the linter enforces

**21 rules, every one teeth-tested** — a valid project passes; break any rule and the build fails.

The rules are themselves written as contracts under this repo's own `.knowledge/` — because this repo
adopts the system it ships. Each row names the test case that proves it:

| Contract | Enforces |
|---|---|
| [`base-payload`](./.knowledge/prd/base-payload.md) | The shipped tree — every home and file present, nothing else at the root |
| [`entity-orientation`](./.knowledge/prd/entity-orientation.md) | The always-loaded trio keeps its standard pointer |
| [`entity-prd`](./.knowledge/prd/entity-prd.md) | Namespaces, word cap, tunables, evidence, schema |
| [`entity-research`](./.knowledge/prd/entity-research.md) | Notes are dated and sourced |
| [`entity-catalog`](./.knowledge/prd/entity-catalog.md) | Every home's README lists what's in it and links its guide |
| [`flow-citations`](./.knowledge/prd/flow-citations.md) | IDs are unique, resolve, go up the stack, never cite a draft |

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

SemVer in `VERSION`; each repo stamps its version in `.knowledge/.version`. Behind? Hand this to your agent:

```
Update this repo's knowledge-template to the latest version:
https://github.com/timothymarois/knowledge-template

Compare .knowledge/.version to the upstream VERSION. If behind, apply each
.changes/<date>-v<version>.md between them in order, re-run python3 .knowledge/scripts/doc-lint .knowledge
until clean, then bump .knowledge/.version.
```
