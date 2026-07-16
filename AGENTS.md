# AGENTS — doc-template

This repo is **doc-template**: the canonical, versioned documentation system copied into other repos (web
apps, games, extensions, libraries — any stack). When you work here, you are editing a template that will
be duplicated into many codebases, and enforced by a linter. A sloppy edit here degrades every repo that
adopts it.

These rules are law. If one seems wrong or missing, raise it with the owner — do not modify this file
without approval.

## What this repo contains

- **`template/`** — the copy-me payload, and the only thing downstream repos take. Everything is under
  `template/.ai/`: the always-loaded orientation trio (`BRIEF`, `CODEMAP`, `MEMORY`), the doc-system map
  (`README.md`), the version stamp (`.doc-version`), the linter (`doc-lint`), and the homes.
- **Root files** — govern *this* repo and are **not** copied: `README.md`, this `AGENTS.md`, `VERSION`,
  `CHANGELOG.md`, `.changes/` (dated migrations), `.github/`. The linter and its teeth-test ship in the
  payload: `template/.ai/scripts/doc-lint` + `template/.ai/scripts/test_doc_lint.py`.

## The model you must preserve

`template/.ai/README.md` is the map; the standards in `template/.ai/guides/docs-*.md` are the rules. Their
shape is load-bearing — every downstream repo inherits it. Do not add, remove, rename, or re-scope a home
without approval.

- **One fact, one home.** Every doc answers one question; no fact is written twice.
- **Catalog vs. rules.** A home's `README.md` is a **catalog** (what's inside). The **rules** for writing
  live in `guides/docs-*.md`, with the template built in. There are no separate `TEMPLATE.md` files.
- **The homes:** `research/` + `references/` (input) → `prd-drafts/` (isolated proposals) → `prd/` (tested
  contracts, the source of truth). `guides/` holds the standards and project how-tos. Friction lives in
  `MEMORY.md`.
- **A PRD is a tested contract.** Glyph-table requirements carry IDs mapped to tests; a `prd/` contract
  never cites a `prd-drafts/` proposal; graduation is a `git mv`, not a rewrite.

## Rules for working in this repo

1. **Stack-neutral, always.** Nothing in `template/` may name a specific language, framework, or project.
   Use `<placeholders>` and generic examples.
2. **Every home is self-documenting.** Each home has a catalog `README.md`; each doc kind has a
   `guides/docs-*.md` standard. Keep the voice consistent across all of them.
3. **Plain Markdown + one stdlib linter.** No doc-site generators, no build step, no linter dependencies.
4. **The linter is the law.** A rule that matters is a check in `template/.ai/scripts/doc-lint`,
   teeth-tested in `template/.ai/scripts/test_doc_lint.py`. Change the rule and its test together. Prose
   that isn't enforced is teaching, not law.
5. **Keep the map in sync.** Change the model → update `template/.ai/README.md`, the relevant
   `guides/docs-*.md`, and this repo's `README.md` in the same commit. Cross-references must resolve.
6. **PII-free and public.** Assume world-readable. No names, secrets, or machine paths — people by role.

## Cutting a new version

The version is how projects stay in sync without drift. To release a change to the model:

1. **Decide the bump (SemVer).** MAJOR = breaking (a home added/removed/renamed, or a lint rule that fails
   previously-valid docs) · MINOR = additive · PATCH = wording.
2. **Make the change** in `template/` and, if it's a rule, in `scripts/doc-lint` + `scripts/test_doc_lint.py`.
3. **Write the migration.** Add `.changes/<YYYY-MM-DD>-v<version>.md` with the exact ordered steps an agent
   runs to move a project onto this version, and a **Verify** section. Add a row to `CHANGELOG.md`.
4. **Bump `VERSION`** and `template/.ai/.doc-version` to match.
5. **Tag** `v<version>` after review.

## Definition of Done

A change here is done when the payload is internally consistent and copy-paste ready:

1. `python3 template/.ai/scripts/test_doc_lint.py` passes (the linter still has teeth).
2. `python3 template/.ai/scripts/doc-lint template/.ai` passes (the shipped payload is clean).
3. Nothing in `template/` is stack-specific; all placeholders intact.
4. `README.md`, `template/.ai/README.md`, and the `guides/` still describe the actual tree; every
   cross-reference resolves.
5. If the model changed: `VERSION`, `.doc-version`, `CHANGELOG.md`, and a `.changes/` migration are all
   updated together.
