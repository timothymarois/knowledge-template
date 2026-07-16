# AGENTS — knowledge-template

## What this is

**knowledge-template is a versioned documentation system that keeps AI coding agents standardized.** It is copied
into other repos (web apps, games, extensions, libraries — any stack) and gives every kind of knowledge one
home, one writing standard, and a linter that fails the build when a doc drifts.

**This repo is the upstream.** When you work here, you are editing a template that will be duplicated into
many codebases and enforced there by a shipped linter. A sloppy edit here degrades every repo that adopts
it — so the bar is higher than normal.

These rules are law. Do not modify this file without approval; if a rule seems wrong or missing, raise it.

## Why it exists

AI agents write docs well and keep them consistent badly. Left alone, each invents its own structure — PRDs
in three shapes, notes that contradict each other, the same fact in five files — and the docs rot until the
next agent trusts the rot. knowledge-template makes the standard **executable, not a wiki page nobody rereads:**
the rules ship as guides with the template built in, and a linter enforces them in CI, so agents can't
drift and stay drifted. Versioning lets every repo catch up on demand instead of forking its own rules.

## What this repo contains

- **`template/`** — the copy-me payload, and the only thing downstream repos take. Everything lives under
  `template/.knowledge/`: the always-loaded trio (`BRIEF`/`CODEMAP`/`MEMORY`), the map (`README.md`), the version
  stamp (`.version`), the homes, and `scripts/` (the linter and its teeth-test — they ship **with** the
  docs so every repo self-enforces).
- **Root files** — govern *this* repo and are **not** copied: `README.md` (the consumer-facing pitch + the
  `R-DOC` enforced-requirements table), `ADOPT.md` (the step-by-step install guide an adopting agent
  follows), this `AGENTS.md`, `VERSION`, `CHANGELOG.md`, `.changes/` (one dated migration per release),
  `.github/`.

## The model you must preserve

`template/.knowledge/README.md` is the map; the standards in `guides/docs-*.md` are the rules. The shape is
load-bearing — every downstream repo inherits it. **Do not add, remove, rename, or re-scope a home without
approval.**

- **One fact, one home.** Every doc answers one question; no fact is written twice.
- **Catalog vs. rules.** A home's `README.md` is a **catalog** (what's inside). The **rules** for writing
  live in `guides/docs-*.md`, with the template built in — there are no separate `TEMPLATE.md` files.
- **The homes:** `research/` + `references/` (input) → `prd-drafts/` (isolated proposals) → `prd/` (tested
  contracts, the source of truth). `guides/` holds the `docs-*` standards plus project how-tos; `scripts/`
  holds the tooling; `tmp/` is git-ignored scratch; friction lives in `MEMORY.md`. Each has its own catalog
  `README.md`.
- **A PRD is a tested contract.** Glyph-table requirements carry IDs mapped to tests; a `prd/` contract
  never cites a `prd-drafts/` proposal; graduation is a `git mv`, not a rewrite.
- **The trio end with an edit-gated standard pointer** as their last line — an agent reading orientation
  gets the terse content and pulls the full `guides/docs-*.md` into context only when it's about to edit.

## The linter is the law

The rules that matter are checks in `template/.knowledge/scripts/doc-lint`, each **teeth-tested** in
`template/.knowledge/scripts/test_doc_lint.py` — a valid project passes, and breaking a rule fails on that rule.
The full enforced set is the **`R-DOC` requirement table in `README.md`**: knowledge-template holds itself to the
same keyed-table standard it enforces on PRDs. Prose that isn't enforced is teaching, not law.

**So a rule is three things, changed together:** a check in `doc-lint`, a mutation case in
`test_doc_lint.py` that proves it fails, and an `R-DOC-*` row in the README citing that case. Never one
without the others.

## Rules for working in this repo

1. **Stack-neutral, always.** Nothing in `template/` may name a specific language, framework, or project.
   Use `<placeholders>` and generic examples. (Concrete examples belong only in a downstream repo.)
2. **Every home is self-documenting.** Each home has a catalog `README.md`; each doc kind has a
   `guides/docs-*.md` standard. Keep the voice consistent across all of them.
3. **Plain Markdown + one stdlib linter.** No doc-site generators, no build step, no linter dependencies —
   a human or an agent reads and runs it with nothing installed.
4. **A rule = check + test + table row** (see *The linter is the law*). Enforce it, prove it, document it.
5. **Keep everything in sync.** Change the model → update `template/.knowledge/README.md`, the relevant
   `guides/docs-*.md`, and this repo's `README.md` in the same commit. Every cross-reference must resolve
   (the linter checks catalog links; check the rest by eye).
6. **PII-free and public.** Assume world-readable. No names, secrets, or machine paths — refer to people by
   role.

## Cutting a new version

The version is how downstream repos stay in sync without drift. To release a change to the model:

1. **Decide the bump (SemVer).** MAJOR = breaking (a home added/removed/renamed, or a lint rule that fails
   previously-valid docs) · MINOR = additive (a new optional section or non-breaking check) · PATCH = wording.
2. **Make the change** in `template/`, and if it's a rule, in `scripts/doc-lint` + `scripts/test_doc_lint.py`
   + the `R-DOC` table.
3. **Write the migration.** Add `.changes/<YYYY-MM-DD>-v<version>.md` with the exact ordered steps an agent
   runs to move a project onto this version, and a **Verify** section. Add a row to `CHANGELOG.md`.
4. **Bump `VERSION`** and `template/.knowledge/.version` to match.
5. **Tag** `v<version>` after review.

## Definition of Done

A change here is done when the payload is internally consistent and copy-paste ready:

1. `python3 template/.knowledge/scripts/test_doc_lint.py` passes (the linter still has teeth).
2. `python3 template/.knowledge/scripts/doc-lint template/.knowledge` passes (the shipped payload is clean).
3. Nothing in `template/` is stack-specific; all placeholders are intact.
4. `README.md`, `template/.knowledge/README.md`, and the `guides/` still describe the actual tree; every
   cross-reference resolves; if a rule changed, its check, its test, and its `R-DOC` row all match.
5. If the model changed: `VERSION`, `.version`, `CHANGELOG.md`, and a `.changes/` migration are all
   updated together.
