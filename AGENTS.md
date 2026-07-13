# AGENTS — doc-template

This repo is **doc-template**: the canonical documentation scaffold copied into other repos (Laravel
apps, web apps, Axmol games, libraries — any project). When you work here, you are editing a template
that will be duplicated into many codebases. A sloppy edit here degrades every repo that adopts it.

These rules are law. If one seems wrong or missing, raise it with the owner — do not modify this file
without approval.

## What this repo contains

- **Root files** (`README.md`, this `AGENTS.md`) — govern *this* template repo. They are **not** copied
  into downstream projects.
- **`template/`** — the copy-me payload, and the only thing downstream repos take. Everything
  agent-facing lives under one root, `template/.ai/`: the always-loaded orientation trio (`BRIEF` — what
  & why; `CODEMAP` — where; `MEMORY` — current friction) at its top, and the `docs/` knowledge system
  beneath it. A stack-neutral `AGENTS.md` sits at the payload root. Adoption = copy the contents of
  `template/` into the target repo.
- **`examples/`** — the template's `AGENTS.md` filled in for real stacks (Laravel, Axmol), as reference
  for how the skeleton adapts. Not copied downstream. When the model changes, keep these in step.

## The model you must preserve

`template/.ai/docs/README.md` is the source of truth for the documentation model. Its shape is deliberate
and load-bearing — every downstream repo inherits it:

- **One fact, one home.** Every doc answers exactly one question; no fact is written twice.
- **The maturity ladder:** `research/` (prior art + a `references/` subfolder for visual targets) →
  `PRD-drafts/` (proposal) → `PRD/` (tested contract, the source of truth). `guides/` sits alongside.
  There is no status/roadmap file — current state is read from `PRD-drafts/` (in flight) vs `PRD/`
  (shipped). Friction we hit lives in the always-loaded `.ai/MEMORY.md` (a living list, pruned when solved).
- **A PRD is a *tested* contract, born when a system ships — not a plan.** Requirements carry IDs and
  map to tests; behavior and its PRD change in the same commit.

Do not add, remove, rename, or re-scope a home without approval — that is a change to every future repo.

## Applying this template to a project

This is the main use of the repo: standing the setup up in a real codebase (a Laravel app, a web app, an
Axmol game, a library). Follow these steps, and respect the invariant/adapt split — the model's value is
that it's the same everywhere, while the rules bend to each stack.

**Steps.**

1. **Copy the payload.** Put the *contents* of `template/` — its `AGENTS.md` and `.ai/` — at the target
   repo's root. Nothing outside `template/` is copied.
2. **Adapt `AGENTS.md` to the project — the real work.** Fill its **Stack & Conventions** section: the
   language/runtime, framework(s), architecture and layering (and what each layer may depend on), naming
   and style with the actual format/lint command, and the test setup. Encode the project's **best
   practices as enforceable rules** — specific and checkable, with a right/wrong example where it helps;
   vague conventions get ignored. Set the **Definition of Done** command (the one check that must pass).
3. **Write the orientation.** Fill `.ai/BRIEF.md` (what/why/who) and `.ai/CODEMAP.md` (the structure) for
   this project. `.ai/MEMORY.md` starts empty — friction accrues as you work.
4. **Leave the homes alone.** The `docs/<home>/` READMEs and TEMPLATEs are stack-neutral and work as
   shipped. Deleting a `TEMPLATE.md` after the first real doc is optional; changing a home's rules is not.

**Invariant — keep when adopting, adapt only the specifics, never the discipline:**

- **The top rule is always "open `.ai/BRIEF.md` + `.ai/CODEMAP.md` + `.ai/MEMORY.md` first."** Every
  project's `AGENTS.md` keeps the light-by-default load order and depth-on-demand — that is the point.
- **Read a home's `README.md` before writing a doc there.** The doc-writing gate stays.
- **The homes and the ladder**, **one fact, one home**, **PRD = tested contract**, and **self-contained,
  PII-free docs** — unchanged in every repo.

**Adapt per project:** the `AGENTS.md` Stack & Conventions and Definition of Done; and the *content* of
`BRIEF.md` and `CODEMAP.md`. Nothing else.

## Rules for working in this repo

1. **Stack-neutral, always.** Nothing in `template/` may name a specific language, framework, or
   project. Use `<placeholders>` and generic examples. Framework-specific rules belong only in the
   *Stack & Conventions* section of `template/AGENTS.md`, and even there as a fill-in prompt — never
   pre-filled.
2. **Every home is self-documenting.** Each `.ai/docs/<home>/` has a `README.md` (its role, rules, and
   any ID convention) and a `TEMPLATE.md` copy-me skeleton. Keep the voice consistent across all of them.
3. **Plain Markdown, zero tooling.** No doc-site generators, no build step. A human or an agent reads it
   with nothing installed.
4. **Keep the map in sync.** If you change the model, update `template/.ai/docs/README.md` (the map) and
   this repo's `README.md` in the same commit. Cross-references between homes must always resolve.
5. **PII-free and public.** Assume everything here is world-readable. No names, secrets, or machine paths
   — refer to people by role.

## Definition of Done

A change here is done when the payload is **internally consistent and copy-paste ready**:

1. Every home referenced in `template/.ai/docs/README.md` exists with its `README.md` (+ `TEMPLATE.md`
   where the model calls for one), and every cross-reference resolves.
2. Nothing in `template/` is stack-specific; all placeholders are intact.
3. The root `README.md` and `template/.ai/docs/README.md` still describe the actual tree.
