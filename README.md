# doc-template

**Keep your AI coding agents' documentation standardized.** One home for every kind of doc, one writing
standard, and a linter that fails the build when a doc drifts. Plain Markdown, one stdlib linter, zero setup.

### Why

Agents write docs well and keep them consistent badly — left alone, each invents its own structure and the
docs rot. doc-template makes the standard **executable**:

- 🏠 **One home per kind of doc** — nothing is written twice
- 📐 **Rules ship as guides** — every agent produces the same shape
- ✅ **A linter enforces it in CI** — a broken doc fails like broken code
- 🔁 **Versioned** — upgrade any repo with a dated migration

### Adopt it

Hand this to your coding agent:

```
Adopt the doc-template documentation system into this repo:
https://github.com/timothymarois/doc-template

Follow its README "Adopting this doc template" section:
copy template/.ai into our repo root, embed the .ai/ load-order rules as the FIRST rules in
AGENTS.md, fill BRIEF.md + CODEMAP.md, declare our components in prd/README.md, and wire
python3 .ai/scripts/doc-lint .ai into CI.
```

### What's inside

```
.ai/
  BRIEF · CODEMAP · MEMORY   read first, every task  (what · where · friction)
  prd/          tested contracts — the source of truth
  prd-drafts/   proposals, isolated until approved
  research/     prior-art notes      references/   visual targets
  guides/       the writing standards + project how-tos
  scripts/      the linter (doc-lint) + its test
```

Two rules hold it together: **one fact, one home** · **a PRD is a tested contract** (IDs mapped to tests).

### What the linter enforces

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

### Wire it into your build

```
python3 .ai/scripts/doc-lint .ai         # the docs are valid
python3 .ai/scripts/test_doc_lint.py     # the linter has teeth
```

Chain both into your existing check gate so docs fail alongside code.

<details>
<summary>package.json · composer.json · CI</summary>

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

**CI** — reference workflow: `.github/workflows/doc-lint.yml`

```yaml
- run: python3 .ai/scripts/test_doc_lint.py
- run: python3 .ai/scripts/doc-lint .ai
```

</details>

### Versioning

SemVer in `VERSION`; each repo stamps its version in `.ai/.doc-version`. Behind? Hand this to your agent:

```
Update this repo's doc-template to the latest version:
https://github.com/timothymarois/doc-template

Compare .ai/.doc-version to the upstream VERSION. If behind, apply each
.changes/<date>-v<version>.md between them in order, re-run python3 .ai/scripts/doc-lint .ai
until clean, then bump .ai/.doc-version.
```

More detail on the model and how to cut a version: [`AGENTS.md`](./AGENTS.md).
