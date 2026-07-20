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

## Coverage

| Guide | Exercised by an agent | Notes |
|---|---|---|
| `docs-prd.md` | Yes — 3 runs, 8 agent-tasks | The most tested, and the most linted |
| `docs-agents.md` | Yes — written from scratch, twice | Ship-as-written sections survived verbatim both times |
| `docs-codemap.md` | Yes — written from scratch, twice | Both produced real layers with counts, not the shipped skeleton |
| `docs-brief.md` | Yes — written from scratch, twice | |
| `docs-memory.md` | Partially | Created during adoption; no run has yet *accrued* friction into it |
| `docs-research.md` | Yes — one note written and its sources verified | |

## Known limits of this evidence

- Every task so far has been a **documentation** task. No run has tested whether an agent still follows
  these conventions at hour three of writing application code, which is when conventions actually break.
- The adoption runs used a repo the agent could read in full. A large codebase may defeat `CODEMAP.md`'s
  "survey it layer by layer" instruction in a way a small one cannot.
- `MEMORY.md` has never been tested in its real mode: an agent hitting friction mid-task and recording it.
