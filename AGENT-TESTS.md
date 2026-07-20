# Agent tests

The guides in `template/.knowledge/guides/` are prompts. Prompts are not verified by reading them — they
are verified by giving a real agent a real task and checking what it actually did. This file logs every
such run: what was tested, with which agent, and what broke.

**The linter's rules are proven separately** by `scripts/test_doc_lint.py` (mutation cases, run in CI). This
file covers the other half: the parts of the standard no linter can check, where the only evidence is an
agent's behaviour.

## How to run one

1. Copy a target repo's `AGENTS.md` + `.knowledge/` into a scratch directory and `git init` it, so nothing
   real is touched and the diff is the result.
2. Give the agent a task in the owner's words. Never hint at the convention being tested.
3. Read the diff against the guide. **A green lint is not a pass** — most of what these guides ask for is
   not lintable, which is the reason for testing this way.
4. Log the run below, including the runs that found nothing.

Use more than one agent. Every defect found so far came from **two agents disagreeing** — where they agreed,
they were right, and where they split, the guide was ambiguous.

## Runs

| Date | Under test | Task given | Agents | Result | Defect found |
|---|---|---|---|---|---|
| 2026-07-19 | `docs-prd` | Describe the doc workflow for a new guaranteed behavior (read-only) | Claude Code, Codex, Grok | **3/3 correct** — placement ladder, namespace, next ID, draft-not-contract, ✅ needs a named test, the gate | none |
| 2026-07-19 | `docs-prd` | Actually record a claim the owner ratified | Claude Code, Codex, Grok | **1/3 correct** — two graduated the whole draft into `prd/` on one ratified row | **Ratification granularity** |
| 2026-07-19 | `docs-prd` (after fix) | Same task, corrected wording | Codex, Grok | **2/2 correct** — both left it a draft and said why | — |
| 2026-07-19 | `ADOPT.md`, `docs-agents`, `docs-brief`, `docs-codemap`, `docs-memory` | Cold-adopt the system into a repo that had never seen it | Claude Code, Codex | **2/2 green lint**, real layer maps with counts, ship-as-written intact | **Two `ADOPT.md` defects** |
| 2026-07-19 | `ADOPT.md` (after fix) | Same cold adoption | Codex | **Correct** — migrated and deleted the old docs home, stopped to ask before declaring the ontology | — |
| 2026-07-19 | `docs-memory` | Add a small feature to a repo whose test suite refuses to start without an undocumented env var. Docs never mentioned | Claude Code, Codex | **0/2 recorded it** — both hit the guard, both worked around it, both left `MEMORY.md` empty | **The friction duty never fires** |
| 2026-07-19 | `docs-memory` (after fix) | Same task, concrete trigger in the always-loaded duty | Claude Code, Codex | **1/2 recorded it.** Codex's entry is textbook; Claude recognised the friction as "worth knowing" but put it in its reply, not the file | **Recognition fired, destination didn't** |
| 2026-07-19 | `docs-memory` (after 2nd fix) | Same task, plus a *Definition of done* criterion: friction is in the file or you say you hit none | Claude Code | **Still 0/1.** Made the explicit "no friction" claim once, wrote nothing | Routing still fails |
| 2026-07-19 | `docs-memory` (after 3rd fix) | Same task, plus "write it the moment you find the workaround, not at the end" | Claude Code | **Still 0/1** | **Prose alone does not fix this** |
| 2026-07-19 | `docs-research` | Write a research note answering a market question | Claude Code | **Pass** — closed schema, sourcing at point of claim; **14/15 cited URLs return 200**, the 15th bot-blocked (403), none fabricated | none |

Targets: a private Laravel marketplace app (25 drafts, 8 research notes) and a public standard-library
Python CLI. The Python CLI was chosen deliberately — before it, the payload had only ever met a web app and
a Markdown repo, so "stack-neutral" was an untested claim.

## What each defect was

**Ratification granularity.** The standard said a draft graduates when "the owner ratifies" it, without
saying whether that means a row or the file. Given one ratified claim inside a draft, two of three agents
`git mv`'d the entire file into `prd/` — silently promoting every *other* requirement in it into the source
of truth on the owner's authority. One agent caught it and stopped to ask. Fixed by stating the granularity
and adding it to *Stop and ask*; on re-run, all agents left the file where it was. **Lesson, now law in
this repo's `AGENTS.md`: when prose assigns authority, say over what unit. Ambiguous authority is worse
than an ambiguous rule.**

**`ADOPT.md` left a pre-existing docs system in place.** The target already kept agent docs in another
directory. Both agents adopted *alongside* it and left it, producing two homes for the same facts — the one
failure this system exists to prevent, and invisible to a linter that was never told the old directory
exists. `ADOPT.md` now has a step for folding in and deleting a prior docs home.

**`ADOPT.md` had agents author the component ontology silently.** `prd/README.md` says the components are
the owner's call and "an agent stops and asks", while `ADOPT.md` told the agent to declare them. Both agents
picked one without asking — and picked *differently*. Since IDs are permanent, a guessed ontology is the
hardest thing in the system to undo. `ADOPT.md` now requires proposing them and getting sign-off.

**The `MEMORY.md` duty did not fire at all.** Two agents hit a real guard, discovered the workaround, used
it, finished the task — and wrote nothing down. The cause was a chicken-and-egg: the always-loaded rule said
only *"Hit friction -> add a line"*, while the definition of what **counts** as friction lived in
`docs-memory.md`, which is edit-gated and therefore only read *after* an agent has already decided something
is friction. The trigger is now concrete in the always-loaded line ("anything that cost you a failed
attempt: an env var you had to discover, a guard you had to satisfy…"), and `docs-memory.md` states the test
plainly: *did it cost you an attempt?*

That fixed recognition but not routing: one agent named the friction as "worth knowing" **in its reply** and
still left the file untouched. Two further rounds followed — a *Definition of done* criterion ("friction is
in the file, or say plainly you hit none; telling the human doesn't count"), then a timing instruction
("write it the moment you find the workaround, not at the end"). **Neither worked.** Across four runs one
agent complies reliably and the other never wrote an entry, on a task where it demonstrably hit the guard,
worked around it, and reported the workaround in prose.

**Conclusion, recorded as a negative result: this duty cannot be carried by prose alone.** Every other rule
in this system is either lintable or a judgment made *while writing a doc* — this one asks an agent to
notice something mid-task and act on it later, and that is the one thing the always-loaded file cannot
reliably buy. The improved wording is kept because it moved one agent from silence to a textbook entry and
costs nothing, but a project that genuinely needs friction captured should drive it from its **harness**
(an end-of-task hook that asks the question), not from `AGENTS.md`. That is per-harness, so the payload
cannot ship it.

**Treat `MEMORY.md` as best-effort.** An empty `MEMORY.md` is not evidence that a codebase has no traps.

## Coverage

| Guide | Exercised by an agent | Notes |
|---|---|---|
| `docs-prd.md` | Yes — 3 runs, 8 agent-tasks | The most tested, and the most linted |
| `docs-agents.md` | Yes — written from scratch, twice | Ship-as-written sections survived verbatim both times |
| `docs-codemap.md` | Yes — written from scratch, twice | Both produced real layers with counts, not the shipped skeleton |
| `docs-brief.md` | Yes — written from scratch, twice | |
| `docs-memory.md` | Yes — 6 runs against planted friction | **The only guide that still fails.** Reliable for one agent, never fired for the other |
| `docs-research.md` | Yes — one note written and its sources verified | |

## Known limits of this evidence

- Every task so far has been a **documentation** task. No run has tested whether an agent still follows
  these conventions at hour three of writing application code, which is when conventions actually break.
- The adoption runs used a repo the agent could read in full. A large codebase may defeat `CODEMAP.md`'s
  "survey it layer by layer" instruction in a way a small one cannot.
- The friction used was *planted*. It was real and non-obvious, but an agent meeting a trap it half-expects
  is not the same as one meeting a surprise at hour three.
