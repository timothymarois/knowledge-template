# Brief — knowledge-template

*The always-loaded briefing every agent reads first: the story of what we're building and why. One
screen, stable, PII-free.*

## Story

knowledge-template is a versioned documentation system for repositories worked on by AI coding agents. It
ships as a copy-me `.knowledge/` payload: one home per kind of doc, a writing standard for each, and a
zero-dependency linter that fails the build when a doc drifts. A repo adopts it once, then upgrades by
version bump instead of reinventing its own conventions. This repo is the upstream — and also its own
first adopter, carrying a real `.knowledge/` at the root alongside the payload it publishes.

## Why it exists

Agents write docs well and keep them consistent badly. Left alone, each one invents its own structure —
PRDs in three shapes, notes that contradict each other, the same fact in five files — and the docs rot
until the next agent trusts the rot. A style guide doesn't fix this, because nothing rereads it. The
answer is to make the standard **executable**: the rules ship as guides with the template built in, and a
linter enforces them in CI, so an agent can't drift and stay drifted. Versioning lets every repo catch up
on demand instead of forking its own rules.

## Users / ICP

- **The adopting agent** — installs the payload into a repo and fills its orientation docs. Needs the
  standard unambiguous, stack-neutral, and runnable with nothing installed.
- **The working agent** — reads the orientation trio on every task. Needs it terse enough to always load
  and true enough to trust without verifying.
- **The repo owner** — ratifies requirements and approves upgrades. Needs a green lint to mean something.

## Scope

- **Active areas:** the `.knowledge/` payload (homes, catalogs, orientation trio); the writing standards
  in `guides/docs-*.md`; the `doc-lint` linter and its teeth-test; adoption (`ADOPT.md`); versioning and
  per-release migrations (`VERSION`, `CHANGELOG.md`, `.changes/`).
- **Out of scope:** doc-site generators, rendering, and any build step; formats other than plain Markdown;
  any linter dependency beyond the Python standard library; stack-, framework-, or project-specific
  content inside the payload; the content a downstream repo writes into its own docs.

## How it fits together

- **Payload** — a repo copies `template/.knowledge/` in; that tree is the substrate every other rule
  assumes (`prd/base-payload.md`).
- **Rulebook** — its root `AGENTS.md` routes agents into the orientation trio, and the trio route back to
  their standards when edited (`prd/entity-orientation.md`).
- **Research** — dated notes record how the world outside solved a problem, sourced at the point of claim
  (`prd/entity-research.md`).
- **Proposal** — an idea enters as a draft in `prd-drafts/`, isolated until the owner ratifies it
  (`prd/entity-prd.md`).
- **Contract** — approval moves the file into `prd/`; the glyph column, not the move, records what a test
  proves (`prd/entity-prd.md`).
- **Citation** — contracts reference each other's IDs rather than restating them, forming a one-way graph
  (`prd/flow-citations.md`).
- **Catalog** — each home's `README.md` lists what it holds and links the standard for writing it
  (`prd/entity-catalog.md`).
- **Enforcement** — `doc-lint` checks all of the above in CI, and its teeth-test proves each rule still
  bites (`scripts/`).

## External Systems

- `GitHub Actions` — runs the teeth-test and the lints on every push and pull request.
- `python3` (standard library only) — the runtime for `doc-lint` and its teeth-test; nothing installed.

---
*Editing this file? Follow the standard first: [`guides/docs-brief.md`](./guides/docs-brief.md).*
