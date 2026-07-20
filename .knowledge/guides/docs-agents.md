# How to write AGENTS.md — the standard

This guide **is the standard** for the project's root `AGENTS.md` — the law every agent reads before touching
the repo. Shipped and versioned by `knowledge-template`. `AGENTS.md` is *not* inside `.knowledge/`; it sits at
the repo root and routes agents into it.

`AGENTS.md` does two jobs: **route** agents to the knowledge base, and **encode this stack's rules** so an
agent builds correctly here. Its sections are of two kinds:

- **Ship as written** (identical in every repo): *Before you work*, *Hard gates*, *Documentation duties*, and
  the top of *Never*. Don't reword them per project.
- **Fill in for this project** (by researching the codebase): *Tech stack*, *Architecture*, *Best practices*,
  *Directory structure*, *Build / test / run*, *Definition of done*.

## How to write it

1. **Research the codebase first — don't guess.** Identify the language/runtime, frameworks, the architecture
   and layering (what each layer may depend on), naming/style with the actual format + lint command, the test
   setup, and the one command that gates a change. Delegate the survey to subagents if your harness supports them.
2. **Keep the ship-as-written sections verbatim** — they're what make every repo behave the same.
3. **Encode best practices as enforceable rules** — specific and checkable, with a `✅`/`❌` example where it
   helps. Vague conventions get ignored.
4. **Set the Definition of done** to the real gate command.
5. Keep it lean — rules an agent follows, not prose.

## The template

Copy this. Fill every `<placeholder>`; keep the ship-as-written sections as they are.

```md
# AGENTS

Rules for every agent working in this repository. These rules are law; where they conflict with your general
habits, this file wins.

This is a **<one line: what this project is and its stack>**. The *what & why* lives in `.knowledge/BRIEF.md`;
the knowledge map is `.knowledge/README.md`. This file defines how you build here.

## Before you work

Load light; pull depth only when the task needs it.

1. **Always read first:** `.knowledge/BRIEF.md` (what & why), `.knowledge/CODEMAP.md` (where things are),
   `.knowledge/MEMORY.md` (current friction). `.knowledge/README.md` maps the rest.
2. **On demand, when the task enters an area:** `.knowledge/prd/` (ratified contracts — source of truth),
   `.knowledge/prd-drafts/` (proposals), `.knowledge/research/` + `.knowledge/references/` (prior art, visual
   targets), `.knowledge/guides/` (how to write each doc + project how-tos).
3. **How work flows:** `research/` -> `prd-drafts/` -> `prd/`; a `prd/` contract never cites a draft. New
   guaranteed behavior is a `prd/` row backed by a test — cite its `R-<AREA>-<n>` in the code. Follow a doc's
   guide before writing or modifying it, and keep docs true in the same task. Run
   `python3 .knowledge/scripts/doc-lint .knowledge` before finishing; scratch -> `.knowledge/tmp/`.
4. Read every file before editing it; search before writing new logic — reuse, extend, refactor.
5. When the user raises a concern, investigate before contradicting — evidence, not a hunch.

## Hard gates — require explicit approval

- **Persisted state.** Any change to schema, stored data, or migrations is confirmed first.
- **Dependencies.** Do not add, remove, or major-version-bump a package without approval.
- **Deletions.** Do not delete files outside the task's immediate scope without approval.
- **Commits.** Do not commit or push unless told to.
- **This file.** Never modify `AGENTS.md` without approval.

## Never

- Never touch secrets or commit credentials.
- Never leave debug output or commented-out code in completed work.
- <this stack's own hard "never" rules>

## Tech stack

- **<backend / runtime>:** <frameworks, versions, key services>
- **<frontend / UI>:** <frameworks, libraries>

## Architecture — the one rule that matters

<The core structural rule, then the layering as a table: Layer | Owns | May depend on | Must not.>

## Best practices — do / don't

<Enforceable rules grouped by area, each a Do/Don't, with a right/wrong example where it helps.>

## Directory structure

<A terse tree of where each kind of thing lives.>

## Build, test & run

<The commands to check and run the project, including the one gate command.>

## Documentation duties

Keep docs true in the same task that changes reality. Before creating or editing a doc, read its home
`README.md` and follow its `guides/docs-*.md`.

- Moved/restructured files -> update `.knowledge/CODEMAP.md`.
- Hit friction — **anything that cost you a failed attempt**: an env var or flag you had to discover,
  a guard you had to satisfy, a command that only worked the second way you tried it, an error whose
  message didn't say what to do -> **write the line into `.knowledge/MEMORY.md` the moment you find
  the workaround, before you carry on** — by the end of the task it will feel too small to mention,
  which is exactly how the next agent loses the same hour. Delete it once solved.
- Owner ratifies a draft (**the whole file**, not one row) -> `git mv` it into `prd/`; IDs carry over and
  the conformance review then sets glyphs. **Approval moves a draft, not proof** — proof is the glyph
  column. Behavior and its requirement row change in the same commit.
- Scratch -> `.knowledge/tmp/` (git-ignored).

## Definition of done

1. <the project's gate command> passes.
2. Every rule here held.
3. New guaranteed behavior is proven by a `prd/` requirement and its test.
4. **Friction you hit is written into `.knowledge/MEMORY.md` — or you say plainly that you hit none.**
   Telling the human in your reply does not count: the next agent reads the file, not this conversation.
```

## CLAUDE.md — a router, not a copy

Claude Code reads `CLAUDE.md`. Keep it a thin **router** to `AGENTS.md` — never a second copy of the rules
(which would drift). If the project has none, create it:

```md
# CLAUDE.md

Before you respond to the user, do any task, or any action, you must read and follow
[AGENTS.md](./AGENTS.md) completely.

If you have not read it, your next step must be to read it first, always.
```

## Lint

`doc-lint` checks this file too — it is the entry point that sends an agent into `.knowledge/` at all, so
losing it silently unloads every doc below it. Two checks, deliberately shallow:

- The repo root has an `AGENTS.md`.
- Somewhere in it, all three of `.knowledge/BRIEF.md`, `.knowledge/CODEMAP.md`, and `.knowledge/MEMORY.md`
  are named.

**Nothing else is inspected** — not sections, not wording, not order. How a project writes its rules is its
own business; the lint only guarantees the orientation trio still gets loaded. (Linting a payload not yet
adopted into a repo? Pass `--payload` to skip both.)

## Rules

- **Ship-as-written stays verbatim** across repos — that's what keeps every project consistent.
- **Rules, not prose.** Every filled-in line is something an agent can follow or a reviewer can check.
- **Show, don't tell** — a `✅`/`❌` example beats a paragraph.
- **One law file.** `AGENTS.md` is the only place the stack's rules live; the `.knowledge/` docs never restate them.
