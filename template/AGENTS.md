# AGENTS

Rules for every agent working in this repository. These rules are law; where they conflict with your
general habits, this file wins.

> **How to use this file.** The sections marked **(invariant)** are the same in every repo built on this
> setup — keep them. The sections marked ***(adapt per project)*** are yours to fill with this project's
> stack, architecture, and best practices. Replace every `<placeholder>`, delete guidance you've
> satisfied, and never let this file drift from how the code actually works.

<One paragraph identity: what this project is — the product, the core stack, and the shape of its
architecture in a sentence. Point the reader on: the *what & why* lives in [`.ai/BRIEF.md`](./.ai/BRIEF.md);
the knowledge map is [`.ai/docs/README.md`](./.ai/docs/README.md). This file defines how you build here.>

---

## Before You Work — (invariant)

**Load light by default, then pull depth only when the task reaches for it.**

1. **Always** (keeps context light): read [`.ai/BRIEF.md`](./.ai/BRIEF.md) (what & why),
   [`.ai/CODEMAP.md`](./.ai/CODEMAP.md) (where things are), and [`.ai/MEMORY.md`](./.ai/MEMORY.md)
   (current friction to avoid). [`.ai/docs/README.md`](./.ai/docs/README.md) is the map to everything below.
2. **On demand, when your task enters an area — pull only what you need:** `.ai/docs/PRD/PRD-<System>.md`
   (the tested contract, if you're changing its behavior); `.ai/docs/PRD-drafts/<slug>.md` (if it's
   proposed, not yet built); `.ai/docs/guides/<task>.md` (the recipe for a recurring procedure);
   `.ai/docs/research/` and its `references/` visuals (prior art and targets, when designing). Current
   state is read from here — what's in `PRD-drafts/` is in flight, what's in `PRD/` is shipped; there is
   no status file.
3. Read every file before editing it. Search the codebase before writing new logic — if it exists,
   reuse, extend, or refactor. Never duplicate.
4. When the user raises a concern, investigate before contradicting. Contradict only with evidence — a
   header, a test, a benchmark — never a hunch.

## Hard Gates — Require Explicit Approval — (invariant)

- **Migrations / persisted state.** Any change to schema, user data, or stored state is confirmed first.
- **Dependencies.** Do not add, remove, or version-bump a package (or a pinned engine/runtime) without approval.
- **Deletions.** Do not delete files or directories outside the task's immediate scope without approval.
- **Commits.** Do not commit or push unless told to.
- **This file.** Never modify `AGENTS.md` without approval. If a rule seems wrong or missing, raise it.

## Never — (invariant core, plus your stack's prohibitions)

- Never touch `.env` or commit credentials, tokens, or keys.
- Never leave debug output, commented-out code, or disabled tests in completed work.
- Never let two sides of a boundary drift — names, enums, routes, and contracts match across the stack
  at all times; rename on one side, rename on the other in the same task.
- ***(adapt)*** <add this stack's hard prohibitions — the mistakes that must never happen here. e.g.
  "never include an engine header in the pure core", "never validate on the frontend", "never use raw
  `new`/`delete`", "never recompute the whole map on a user action".>

---

## Tech Stack — *(adapt per project)*

> The languages, frameworks, and key libraries — with versions where they're pinned.

- **Core / backend:** `<fill>`
- **UI / frontend:** `<fill>`
- **Data / infra:** `<fill>`

## Architecture — the one rule that matters — *(adapt per project)*

> State the layers, the **one-way** dependency direction, what each layer owns and must not do, and the
> placement rule for where new code goes. If a test or check fails when a boundary is crossed (a
> "tripwire"), name it. A table reads best.

| Layer | Owns | May depend on | Must not |
|---|---|---|---|
| `<layer>` | `<what it owns>` | `<what it may use>` | `<what it must never do>` |

**Placement rule:** <where does new code go by default, and how do you decide?>

## Best Practices — Do / Don't — *(adapt per project)*

> The real conventions of this stack, written as **enforceable rules** — specific and checkable, not
> aspirational. Group by domain (backend, frontend, data, …). Prefer a right/wrong **example** over
> prose; a code block teaches faster than a sentence. Keep only what's actually enforced.

### `<domain — e.g. Backend>`

- **Do** `<the rule>`. **Don't** `<the anti-pattern it replaces>`.
- `<fill>`

```
✅ <the canonical right way — the pattern every file here follows>
❌ <the forbidden pattern — what a reviewer rejects>
```

### `<domain — e.g. Frontend / UI>`

- `<fill>`

## Code documentation — (invariant principle; syntax adapts per stack)

Document the **non-obvious**. A doc-block earns its place by answering what the code itself can't: *why*
this exists, the *contract* it upholds (inputs → result, invariants, edge cases), and *which requirement*
it satisfies. Trivial code — getters, plain CRUD, self-evident one-liners — gets nothing; a comment that
restates the code is noise.

- **Complex or non-obvious methods get a doc-block** — intent, the contract, and any gotcha a caller must
  know. Explain *why*, not *what*.
- **Cite the requirement.** When a method implements a `.ai/docs/PRD/` requirement, name its ID
  (`R-<AREA>-<n>`) in the doc-block — linking the code to its tested contract, so the next agent finds the
  guarantee and its test.
- **Keep it true.** A stale doc-block is worse than none — update it in the same change.
- ***(adapt)*** use this stack's doc-comment syntax: `<PHPDoc /** */ · TSDoc · Doxygen · docstrings>`.

```
✅ /** Applies a zone rectangle, skipping water and occupied tiles (R-ZONE-3).
    *  Corners may be inverted; out-of-bounds or unknown kinds reject atomically.
    *  Returns the exact dirty range so render invalidates only what changed. */
❌ // sets the zone      ← restates the name; teaches nothing
```

## Directory Structure — *(adapt per project)*

```
<repo>/
├── <dir>/   # <what lives here>
├── <dir>/   # <...>
└── .ai/     # agent docs: BRIEF, CODEMAP, docs/ + tmp/ (git-ignored scratch) — do not restructure
```

## Build, Test & Run — *(adapt per project)*

> The exact commands, and **who** runs the app. If the owner runs the UI and provides screenshots, say
> so — build to prove it compiles, hand off for visual sign-off, don't self-run.

```
<build command>
<test command>
<run command — and who runs it>
```

---

## Documentation Duties — (invariant)

Docs are your responsibility, not the user's — keep them true in the same task that changes reality.

**Before creating or editing any doc, read that home's `README.md` first.** It is the contract for that
home: what belongs there, how to write it, and any ID convention (`R-`, `L-`). Then copy its `TEMPLATE.md`
to start a new doc. Don't write into a home whose rules you haven't read.

- Restructured directories or moved files → update `.ai/CODEMAP.md`.
- Hit friction (a trap, a non-obvious constraint, a workaround) → add a line to `.ai/MEMORY.md`, and
  **delete it once the friction is genuinely solved**. This codebase only.
- Shipped a system whose behavior is now guaranteed → its `.ai/docs/PRD-drafts/` draft graduates to a
  `.ai/docs/PRD/`, with every requirement mapped to a passing test, and the **draft is deleted** (no
  pointer stub). **Behavior and its PRD change in the same commit — they never drift.**
- Implementing a `.ai/docs/PRD/` requirement in code → cite its `R-<AREA>-<n>` in the method's doc-block,
  so code ↔ contract ↔ test stay linked.
- Do not add rationale, history, or maintainer commentary to `.ai/` files — they address the next agent
  doing work, nothing else.
- Need a scratch file — a throwaway draft, a generated asset, experiment output? Put it in `.ai/tmp/`.
  It's git-ignored and stays local. Never keep durable knowledge there; that belongs in a `docs/` home.

## Definition of Done — (invariant shape; adapt the command)

A task is done when the change is **verified against its stated requirement** — never based on effort — and:

1. The project's checks pass: `<fill the single command that runs format + lint + types + tests + build>`.
2. Every rule in this file held — the stack prohibitions, the architecture boundaries, and the doc duties.
3. If the change guarantees new behavior, a `PRD/` requirement and its test prove it.

**When creating task lists or plans, the final step is always:** _"Re-read `AGENTS.md` and verify Definition of Done."_
