# How to write a research note — the standard

This guide **is the standard** for every note in [`../research/`](../research/), with the template built
in. Shipped and versioned by `knowledge-template`; the per-project catalog of notes lives in
[`../research/README.md`](../research/README.md).

A research note is **a dated report on how the world works outside this codebase**, written so we can
decide something. It is not a requirement, not a plan, and not a summary of a website. It answers one
question, cites what it learned it from, and says what we're doing about it. This is **input, never
truth**: research informs a draft; it never dictates one, and it is never the source of record for our
behavior (that's `../prd/`).

Answers: *"What has the world already done about `<X>`, and what are we aiming at?"*

## The one rule: report the world, then say what we think — never both at once

`What they do` is **reporting**. Borrow, Avoid, and Verdict are **ours**. The most common failure is our
thinking wearing reporting's clothes: an inference or a design position sitting in the reporting section,
indistinguishable from a fact about the industry. Everything downstream is built on that section — so one
contaminated claim quietly becomes a borrow, then a verdict, then a requirement.

**The mechanism is sourcing at the point of claim.** Every non-obvious claim in `What they do` carries a
`[n]`. Then anything uncited is visibly ours, and can't hide.

| The urge | Where it goes |
|---|---|
| Say what they should have done | `What to avoid` |
| Say what we'd do about it | `Verdict for us` |
| State our own design position | `Verdict for us` — **never** inside `What they do`, not even flagged |
| Say what the product must do | Nowhere here. Tell the owner. |
| Say what we'll build next | Nowhere here. That's work, not research. |
| Say what you couldn't find out | `Open questions`, one line |
| Say the world has changed since | Re-read the note whole and re-stamp it |

## The template

```md
# Research: <topic>

**Last updated:** 2026-07-16
**Question it answers:** <one line — what you can decide after reading this>

## What they do

<Reporting only. Every non-obvious claim, and every number, carries [n].>

## What we can borrow

<Ours. The transferable ideas, as short bullets.>

## What to avoid

<Ours. The traps — theirs, and the ones we'd walk into.>

## Verdict for us

<Ours. The decision: what we're doing, deferring, not doing. Name the PRD or component it feeds.>

## Open questions

<One line each. What we didn't learn, and what we haven't decided.>

## Sources

1. <name — url>
2. <name — url>
```

**Do not add a heading.** The schema is closed.

## Section guidance

- **`Question it answers`** — one line, a scope contract. Anything that doesn't serve it is a second note.
- **`What they do`** — the world, as sources describe it. Structure it however the topic wants. One content
  rule, absolute: **nothing of ours goes here.**
- **`What we can borrow`** — transferable ideas, short bullets. Ideas, not decisions.
- **`What to avoid`** — the traps. A trap you'd have walked into is the most valuable line in the note.
- **`Verdict for us`** — **the decision, not a recap.** It chooses: this now, that deferred, that not at
  all, and names the PRD or component it feeds.
- **`Open questions`** — one line each. Honest to have many; a note with none didn't look hard.

## Sourcing

- **Every non-obvious claim carries `[n]`** — every number, date, "the industry does X", legal posture.
- **A source blob at the top is not sourcing.** Cite the specific page you read, not the vendor.
- **Never cite a source you didn't open.** It's the one claim in the note nobody can check.

## How old is it

**`Last updated` is the date the whole note was last re-read against its sources** — not when the file was
touched. A typo fix does not move it. A note that says *"current posture"* with no date is a landmine.
Because the date is whole-note, **updating means re-reading, not patching**: fix one section and re-stamp
and you make every stale paragraph look fresh. What the note said before is git's. So change a note only
when its sources actually moved (or the owner asks) — never to reword, and never a section the change
doesn't touch.

## What a note is not

**It is not a PRD, and nothing in it is binding.** The path is always:

```
research  →  the owner reads it  →  the owner states a requirement  →  a prd/ row
```

Never `research → requirement`. A note informs the decision; the owner makes it; the PRD records it.

## Visual references

Screenshots, competitor captures, and UI targets go in the sibling [`../references/`](../references/)
home — cite them from a note, don't embed the analysis there.

## Lint

- The note carries a `**Last updated:**` date.
- Every `[n]` resolves to a Sources entry; every Sources entry is cited at least once.
- No `##` outside the schema.
