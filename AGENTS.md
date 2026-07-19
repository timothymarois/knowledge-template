# AGENTS

Rules for every agent working in this repository. These rules are law; where they conflict with your general
habits, this file wins.

This is **knowledge-template**, a versioned documentation system for repos worked on by AI coding agents
(plain Markdown + one standard-library Python linter, no build step): a copy-me `.knowledge/` payload that
gives every kind of knowledge one home, one writing standard, and a linter that fails the build when a doc
drifts. **This repo is the upstream** — what you edit here is duplicated into many codebases and enforced
there, so a sloppy edit degrades every repo that adopts it. It is also its own first adopter. The *what &
why* lives in `.knowledge/BRIEF.md`; the knowledge map is `.knowledge/README.md`. This file defines how you
build here.

## Before you work

Load light; pull depth only when the task needs it.

1. **Always read first:** `.knowledge/BRIEF.md` (what & why), `.knowledge/CODEMAP.md` (where things are),
   `.knowledge/MEMORY.md` (current friction). `.knowledge/README.md` maps the rest.
2. **On demand, when the task enters an area:** `.knowledge/prd/` (tested contracts — source of truth),
   `.knowledge/prd-drafts/` (proposals), `.knowledge/research/` + `.knowledge/references/` (prior art, visual
   targets), `.knowledge/guides/` (how to write each doc + project how-tos).
3. **How work flows:** `research/` -> `prd-drafts/` -> `prd/`; a `prd/` contract never cites a draft. New
   guaranteed behavior is a `prd/` row backed by a test — cite its `R-<AREA>-<n>` in the code. Follow a doc's
   guide before writing or modifying it, and keep docs true in the same task. Run
   `python3 .knowledge/scripts/doc-lint .knowledge` before finishing; scratch -> `.knowledge/tmp/`.
4. Read every file before editing it; search before writing new logic — reuse, extend, refactor.
5. When the user raises a concern, investigate before contradicting — evidence, not a hunch.

## Hard gates — require explicit approval

- **The model.** Do not add, remove, rename, or re-scope a home, a `guides/docs-*.md`, or the closed PRD
  schema. The shape is load-bearing — every downstream repo inherits it.
- **Breaking changes.** A lint rule that fails previously-valid docs is a MAJOR release; confirm before writing it.
- **Deletions.** Do not delete files outside the task's immediate scope without approval.
- **Commits.** Do not commit or push unless told to.
- **This file.** Never modify `AGENTS.md` without approval.

## Never

- Never touch secrets or commit credentials.
- Never leave debug output or commented-out code in completed work.
- **Never name a language, framework, or project inside `template/`** — it is stack-neutral for every
  adopter. Use `<placeholders>` and generic examples; concrete ones belong in a downstream repo.
- **Never add a dependency to the linter.** Python standard library only, no build step, no doc-site
  generator — a human or an agent runs it with nothing installed.
- **Never edit `.knowledge/guides/` or `.knowledge/scripts/` directly** — they are copies. Edit
  `template/.knowledge/`, then re-copy; CI diffs them.
- **Never write a rule in prose alone.** Unenforced prose is teaching, not law.
- Never include PII. Assume world-readable: no names, secrets, or machine paths — refer to people by role.

## Tech stack

- **The payload:** plain Markdown. No frontmatter beyond a PRD's `id` / `name` / `last_verified`.
- **The tooling:** Python 3, standard library only (`doc-lint`, `test_doc_lint.py`). No packages, no venv.
- **CI:** GitHub Actions (`.github/workflows/doc-lint.yml`).

## Architecture — the one rule that matters

**Only `template/` is copied downstream; everything else governs this repo.** A change is either to the
payload (and therefore to every adopter, and therefore versioned) or to this repo's own governance. Know
which one you're making before you edit.

| Layer | Owns | May depend on | Must not |
|---|---|---|---|
| `template/.knowledge/` | The shipped payload — homes, catalogs, orientation trio | Nothing outside itself | Name a stack; reference this repo's root files |
| `template/.knowledge/guides/docs-*.md` | The writing standard for one kind of doc, template built in | The payload's own paths | Restate another guide's rule; carry project specifics |
| `template/.knowledge/scripts/` | Enforcement — `doc-lint` + its teeth-test | Python stdlib | Take a dependency; assume a stack |
| Root (`README`, `ADOPT`, `AGENTS`, `VERSION`, `.changes/`) | This repo: the pitch, the install, the law, the releases | The payload | Get copied downstream |
| `.knowledge/` | This repo's adopted copy — we run what we ship | `template/` (as a verbatim copy) | Be hand-edited |

- **One fact, one home.** Every doc answers one question; no fact is written twice.
- **Catalog vs. rules.** A home's `README.md` is a **catalog** (what's inside). The rules for writing live
  in `guides/docs-*.md`, with the template built in — there are no separate `TEMPLATE.md` files.
- **The homes:** `research/` + `references/` (input) → `prd-drafts/` (isolated proposals) → `prd/` (tested
  contracts). `guides/` holds the standards plus project how-tos; `scripts/` the tooling; `tmp/` is
  git-ignored scratch; friction lives in `MEMORY.md`.
- **A PRD is a tested contract.** Glyph-table requirements carry IDs mapped to tests; a `prd/` contract
  never cites a `prd-drafts/` proposal; graduation is a `git mv`, not a rewrite.
- **The trio ends with an edit-gated standard pointer** — orientation stays terse, and the full standard is
  pulled into context only by an agent about to edit.

## Best practices — do / don't

### Changing a rule

**A rule is three things, changed together:** a check in `doc-lint`, a mutation case in `test_doc_lint.py`
that proves it fails, and a requirement row in `.knowledge/prd/` whose Evidence names that case. Never one
without the others — and a check you haven't watched fail is not proven.

```
✅ doc-lint: raise on a numeric literal in a requirement
   test_doc_lint.py: case "numeric literal in requirement" → expects that failure
   .knowledge/prd/entity-prd.md: | ✅ | R-PRD-3 | ... | `numeric literal in requirement` |
❌ guides/docs-prd.md: "requirements should avoid magic numbers"   // prose nobody enforces
```

### Writing the payload

- **Do** write rules an agent can follow or a reviewer can check. **Don't** write aspiration.
- **Do** show a `✅`/`❌` example instead of a paragraph explaining the same thing.
- **Do** keep the always-loaded trio terse — it is paid for on every task. **Don't** move depth into it;
  depth belongs in a guide, pulled on demand.
- **Do** say what a doc is *not* for, and where that content goes instead. A guide that only says what to
  write leaves the agent to invent a home for everything else.
- **Do** state what the tooling actually does. **Don't** claim automation that doesn't exist — an agent
  that reads "regenerated automatically" stops maintaining the thing by hand.

### Keeping it in sync

- **Do** update `template/.knowledge/README.md`, the relevant `guides/docs-*.md`, this repo's `README.md`,
  and the `.knowledge/` copy in the same commit. **Don't** leave a cross-reference that doesn't resolve.
- **Do** re-run the teeth-test after any payload edit — it copies the live payload as its fixture, so a
  structural break shows up there first.

## Directory structure

```
├── template/.knowledge/            # the copy-me payload — the ONLY thing adopters take
│   ├── BRIEF.md  CODEMAP.md  MEMORY.md  README.md  .version
│   ├── prd/  prd-drafts/  research/  references/  tmp/    # homes, each with a catalog README
│   ├── guides/docs-{prd,research,brief,codemap,memory,agents}.md   # the standards
│   └── scripts/{doc-lint,test_doc_lint.py}                # enforcement + its teeth
├── .knowledge/                     # this repo's adopted copy (guides/ + scripts/ are verbatim)
├── .changes/                       # one dated migration per release
├── README.md  ADOPT.md  AGENTS.md  CLAUDE.md  VERSION  CHANGELOG.md
└── .github/workflows/doc-lint.yml
```

## Build, test & run

```bash
python3 template/.knowledge/scripts/test_doc_lint.py                    # the gate: the linter has teeth
python3 template/.knowledge/scripts/doc-lint --payload template/.knowledge  # the shipped payload is clean
python3 .knowledge/scripts/doc-lint .knowledge                          # our own docs are valid
diff -r template/.knowledge/guides .knowledge/guides && diff -r template/.knowledge/scripts .knowledge/scripts
```

All four are what CI runs. `--payload` skips the `AGENTS.md` check, which an unadopted payload can't satisfy.

## Documentation duties

Keep docs true in the same task that changes reality. Before creating or editing a doc, read its home
`README.md` and follow its `guides/docs-*.md`.

- Moved/restructured files -> update `.knowledge/CODEMAP.md`.
- Hit friction -> add a line to `.knowledge/MEMORY.md`; delete it once solved.
- Shipped guaranteed behavior -> graduate its `prd-drafts/` draft to `prd/` (every `R-` mapped to a passing
  test, delete the draft); behavior and PRD change in the same commit.
- Scratch -> `.knowledge/tmp/` (git-ignored).

## Cutting a new version

The version is how downstream repos stay in sync without drift. To release a change to the model:

1. **Decide the bump (SemVer).** MAJOR = breaking (a home added/removed/renamed, or a lint rule that fails
   previously-valid docs) · MINOR = additive (a new optional section or non-breaking check) · PATCH = wording
   or a fix that changes no rule.
2. **Make the change** in `template/`, and if it's a rule, in `scripts/doc-lint` + `scripts/test_doc_lint.py`
   + `.knowledge/prd/`.
3. **Write the migration.** Add `.changes/<YYYY-MM-DD>-v<version>.md` with the exact ordered steps an agent
   runs to move a project onto this version, and a **Verify** section. Add a row to `CHANGELOG.md`.
4. **Bump `VERSION`** and both `.version` stamps (`template/.knowledge/` and `.knowledge/`) to match.
5. **Tag** `v<version>` after review.

## Definition of done

1. All four commands under *Build, test & run* pass, and the `diff` is clean (we run what we ship).
2. Every rule here held — nothing stack-specific in `template/`, all placeholders intact, no unenforced prose.
3. New guaranteed behavior is proven by a `.knowledge/prd/` requirement and its teeth-test case, and you
   have watched that case fail with the check removed.
4. `README.md`, `ADOPT.md`, `template/.knowledge/README.md`, and the `guides/` still describe the actual
   tree; every cross-reference resolves.
5. If the model changed: `VERSION`, both `.version` stamps, `CHANGELOG.md`, and a `.changes/` migration are
   updated together.
