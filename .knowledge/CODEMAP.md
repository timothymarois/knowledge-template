# Codemap — knowledge-template

The always-loaded structural map: *where things are*, layer by layer. Keep it current — when you move
or restructure files, update this in the same task.

This repo has no application code. Its layers are **the payload it ships**, **the tooling that enforces
it**, **the governance around releasing it**, and **its own adopted copy**. The one rule that shapes
everything: only `template/` is copied downstream; everything else governs this repo.

## The payload (`template/.knowledge/` — the only thing adopters take)

The shipped tree, copied verbatim into an adopting repo's root. Stack-neutral: no language, framework, or
project may be named anywhere inside it.

| Path | Holds |
|---|---|
| `BRIEF.md` · `CODEMAP.md` · `MEMORY.md` | The always-loaded orientation trio, as fill-in templates; each ends with an edit-gated pointer to its guide |
| `README.md` | The map of the homes |
| `.version` | The adopted version stamp |
| `prd/` · `prd-drafts/` | Tested contracts; isolated proposals. Each a catalog `README.md` |
| `research/` · `references/` | Prior-art notes; visual targets. Each a catalog `README.md` |
| `guides/` | The writing standards + project how-tos (see below) |
| `scripts/` | The linter and its teeth-test (see below) |
| `tmp/` | Git-ignored scratch (`.gitignore` + `README.md`) |

## The standards (`template/.knowledge/guides/` — 6 shipped + a catalog)

One `docs-*.md` per kind of doc; each **is** the rule and carries its template inline. Versioned — a
downstream repo never edits them.

- `docs-prd.md` — PRDs and drafts: placement, namespaces, the glyph table, evidence, graduation. The
  longest and most load-bearing.
- `docs-research.md` — dated research notes: reporting vs. verdict, sourcing at the point of claim.
- `docs-brief.md` · `docs-codemap.md` · `docs-memory.md` — the orientation trio; each names the trio file
  itself as its template.
- `docs-agents.md` — the root `AGENTS.md`: which sections ship as written, which are researched per stack.
- `README.md` — the catalog, split into shipped standards and project how-tos.

## The tooling (`template/.knowledge/scripts/`)

- `doc-lint` — the enforcement. Python 3 standard library only; takes the `.knowledge/` path and an
  optional `--payload` (skips the root-`AGENTS.md` check, for a payload not inside an adopting repo). One
  `Lint` class; `check()` drives the structural checks (manifest, trio pointer, closed root, catalog guide
  links, `AGENTS.md`) then walks `prd/` + `prd-drafts/` for namespace ownership, ID, glyph, word-count, and
  citation rules, then catalog completeness, catalog links, and research. Exits non-zero on any error.
- `test_doc_lint.py` — the teeth-test. Builds a valid base by copying **the real payload** into a temp
  dir and adding two sample PRDs, then applies one mutation per rule and asserts the matching failure.
  Every enforced rule has a case here.
- `README.md` — the catalog, plus the note that this folder is also a project's own script workspace.

## Governance (repo root — not copied)

- `AGENTS.md` — the law for working in this repo. Owner-approved edits only.
- `CLAUDE.md` — a thin router to `AGENTS.md`.
- `README.md` — the consumer-facing pitch, the adopt/upgrade prompts, and the CI wiring snippets.
- `ADOPT.md` — the step-by-step install an adopting agent follows.
- `VERSION` · `CHANGELOG.md` · `.changes/` — SemVer stamp, release history, and one dated migration file
  per release (the mechanism by which a downstream repo catches up).

## CI (`.github/workflows/doc-lint.yml`)

One `doc-lint` job on push and pull request: teeth-test the linter, lint the payload, lint this repo's
own `.knowledge/`, then diff the adopted copy against the payload.

## This repo's own knowledge (`.knowledge/`)

The adopted copy — this repo eats its own payload. `guides/` and `scripts/` here are byte-identical to
`template/.knowledge/`, enforced by the CI diff; **edit the payload, then re-copy, never the other way.**
`prd/` holds the contracts for what `doc-lint` guarantees, each row's evidence naming a
`test_doc_lint.py` case.

---
*Editing this file? Follow the standard first: [`guides/docs-codemap.md`](./guides/docs-codemap.md).*
