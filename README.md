# doc-template

A project-agnostic documentation scaffold for AI-assisted repos. Copy it into any project — a
Laravel app, a web app, an Axmol game, a library — and it gives every kind of knowledge exactly one
home, so the docs **compound instead of sprawling**.

It replaces heavyweight doc sites (VitePress and friends) with plain Markdown that lives beside the
code, versions with it, and is readable by both humans and agents with zero tooling.

## What's in the box

The copy-me payload lives in `template/`. Everything agent-facing sits under one root, `.ai/`:

```
template/
  AGENTS.md            ← the law for any agent in the repo (stack-neutral; fill the Stack section)
  .ai/                 ← EVERYTHING agent-facing lives here
    BRIEF.md             ┐ always-loaded orientation — read first, every task
    CODEMAP.md           ┘   what we're building & why · where things are
    tmp/                 ← local scratch space (git-ignored) for AI temp files/assets
    docs/                ← the knowledge system, read on demand (see docs/README.md first)
      research/            how the world already handled X (prior art) — input, never truth
      references/          targets, competitors, inspiration — what to build toward; drives visuals
      design/              proposals / drafts — rewrite freely until built
      PRD/                 tested contracts — the SOURCE OF TRUTH (requirements ↔ tests)
      guides/              how to perform a recurring task in this repo
      lessons/             what we learned the hard way — never repeat (area-specific)
```

Root `AGENTS.md`, this `README.md`, and `examples/` govern or illustrate the template repo itself and are
**not** copied. `examples/` holds the `AGENTS.md` filled in for real stacks (Laravel, Axmol) so you can
see how the skeleton adapts before writing your own.

## How to adopt it in a new project

In short: copy the *contents* of `template/` into the target repo's root, adapt its `AGENTS.md` to the
project's stack and best practices, and fill `.ai/BRIEF.md` and `.ai/CODEMAP.md`. The documentation model
itself never changes — only the `AGENTS.md` conventions and the orientation content do.

**The full, authoritative playbook — including what stays invariant (the always-open-BRIEF/CODEMAP load
order, one fact one home, PRD = tested contract) versus what you adapt per project — is in
[`AGENTS.md` → *Applying this template to a project*](./AGENTS.md).** Follow that.

## The one idea to internalize

**One fact, one home.** Every doc answers exactly one question, and no fact is written in two places.
`.ai/` is the always-loaded orientation; `.ai/docs/` is the on-demand depth.
`.ai/docs/README.md` defines every home and the flow between them — read it before adding a doc.
