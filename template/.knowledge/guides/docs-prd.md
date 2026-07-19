# How to write a PRD — the standard

This guide **is the standard** for every PRD in [`../prd/`](../prd/), with the template built in. It is
shipped and versioned by `knowledge-template` — do not rewrite it per project. The per-project **catalog**
(declared components + file list) lives in [`../prd/README.md`](../prd/README.md), not here.

`../prd/` holds the **ratified contracts** for what the product does: one file per built system, every
requirement carrying an ID and a status — ✅ where a test proves it, ❌ where nothing does yet. A PRD
asserts *what must be true, why, and whether it is* — not how it's built. If a claim there has a ✅, a test
proves it.

## A PRD asserts, it never explains

If the file grows while the row count doesn't, you're writing prose instead of requirements. Every fact
has one home; the urge to explain has one, and it is not the PRD:

| The urge | Where it goes |
|---|---|
| Explain how it's built | The design doc |
| Justify why it's built that way | The decision log |
| Say it isn't built, or isn't proven | The ❌ already says it |
| A requirement belongs in another file | **Move it** — a stop-and-ask, not a row |
| Undecided, so the requirement can't be written | `## Open questions`, one line |
| Something deliberately deferred | A `../prd-drafts/` stub — `id`, `name`, one sentence |
| Record what tests don't prove | A ❌ on the row it doesn't prove |
| Restate a rule another PRD owns | Cite its ID |
| Record a value or tunable | The header owns it — cite the symbol |

If none of those fit, you're about to write something with no home. **Raise it, don't write it.**

## Where a requirement lives

Each project declares its own components (layers) in [`../prd/README.md`](../prd/README.md), **in order** —
domain ontology, not architecture. Two universal rules:

1. **Layers are ordered; reading goes one way.** A lower layer may cite an upper one, never the reverse.
2. **Shared behavior goes up, never sideways.** If two entities obey the same rule, it belongs to their
   base or the layer above — one ID, cited by both, never written twice.

### Placement

Read the ladder against **the components this project declared** — the shipped default is
`base-` / `entity-` / `flow-`, but a project may name its own, and the questions apply to whatever it
listed. Ask in order, **stop at the first yes**:

1. True regardless of which kind of thing is involved? → it's about the substrate → the **lowest** layer.
2. True of exactly one kind of thing? → that kind's file, one layer up.
3. Needs two or more kinds interacting before it means anything? → the **emergent** layer above them.
4. About what appears on screen? → **not a PRD requirement.** Presentation.

**A requirement never spans two layers.** If it seems to, it's two — split it. If it doesn't fit one layer
cleanly, **stop and ask.**

## Naming

### Files

**One flat directory. The filename prefix is the layer** — never also a frontmatter field or a subdirectory.
Lowercase, hyphenated, one file per node.

```
prd/
  base-<substrate>.md
  entity-<thing>.md        entity-<other-thing>.md
  flow-<emergent-behavior>.md
```

Entities are singular nouns. Flow files are noun phrases for the emergent thing — never a verb, question,
or computation (`<thing>-access` is a question the graph answers, not a thing). Every file matches a listed
component's prefix or the lint fails. No subdirectories; the only non-PRD file is `README.md`.

### Namespaces and IDs

- Form: `R-<NS>-<n>`. `<NS>` is declared once, in the file's frontmatter `id:`.
- **One namespace per file. One file per namespace.** A second namespace means a second file — as does a
  table past ~15 rows.
- `<n>` is assigned once, monotonically, **permanent**. Never renumber, reuse, or close a gap.
- **Never compound.** `R-A-2 / R-B-2` is illegal — hoist it to a shared file, cited by both.

## The template

Copy this into every PRD. These headings, this order, every time.

```md
---
id: THING
name: Thing
last_verified: 2026-07-16
---

## What this is

<At most three sentences, in domain terms. What the thing is, not how it works.>

## Why it exists

<At most three bullets. What is true for the user when this works.>

- <outcome the user gets>
- <another outcome>

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-THING-1 | <the behavior that must hold, under 25 words> | `<test case name>` |
| ❌ | R-THING-2 | <built but unproven behavior> | src/thing.ext:88 — no test |
| ❌ | R-THING-3 | <nothing exists yet> | — |

## Open questions

<One line each. Design decisions not yet made, so the requirement can't be written.>

- <an unresolved decision>
```

**The glyph is the first column and its header stays blank.** The schema is closed — the only `##` headings
are `What this is`, `Why it exists`, `Requirements`, `Open questions`. Changing it needs approval.

An idea enters as a `../prd-drafts/` stub — two frontmatter lines and a sentence. **You do not write a PRD
to have an idea.**

## Section guidance

- **`What this is`** — what the thing is to someone who doesn't know the system, in the product's vocabulary.
  Not what it owns or depends on. Can't say it in three sentences → it's two files.
- **`Why it exists`** — goals as **outcomes**: what is true for the user when this works. Every requirement
  should serve one.
- **`Requirements`** — the document. Everything else is scaffolding.
- **`last_verified`** — the date **the whole file** was last read row-by-row against its tests. CI runs and
  edits don't move it. Absent until the first review — that's what makes a file a draft.
- **`Open questions`** — design decisions not yet made, one line each. Not build gaps (a requirement that
  exists and isn't proven is a ❌ row).

## Writing a requirement

Requirements come from the owner. **You are transcribing, not authoring** — the rewrite may tighten the
sentence and nothing else.

- **Never add.** If the owner didn't say it, it isn't a requirement.
- **Never generalize.** "No recipients" is not "an invalid recipient set."
- **Never hedge.** "Cannot" does not become "should generally not."
- **Never turn behavior into mechanism** — *how* is the design doc's.
- **A gap is an open question, not a guess.**
- **Contradicts something already written? Stop and ask.** Never reconcile two of the owner's claims.

### Splitting

**Split where it would be built and tested separately.** *"A valid token is required; a missing token is
rejected as unauthorized; an out-of-scope token is refused as forbidden"* is three rows. (Note the status
*names*, not codes — a numeric literal in requirement text fails the lint.) Inverse: **one assertion proven
by several tests is still one requirement** — empty list, all-invalid, filtered-to-zero are situations, not
claims.

### Form

- **No implementation symbols** — not a type, function, class, or file.
- **Tunables by name, never by value** — and only where the name is already the owner's word.
- **One assertion.** "and", "also", "except", or a joining semicolon? Suspect two.
- **Under 25 words.** If it won't fit, it isn't atomic.
- **No numeric literal in the text** — name the tunable instead.
- Present tense, declarative, observable.
- **Cite IDs, never documents.** `R-OTHER-2` is an edge the lint sorts; "see the other doc" is invisible.

**Evidence is the one place technical detail is allowed** — test names, `file:line`, paths. It answers
*where was this proven*. The row above it stays the owner's.

**Cite the ID from the code, too.** The function or module that implements a requirement names its
`R-<NS>-<n>` in a comment or doc-block. Evidence points from the contract to the test; that comment points
from the code back to the contract — so a reader who lands anywhere in the loop can walk the other two.

## Tests and status

Every row answers **one** question: *does an automated test prove this?* ✅ or ❌. No third answer.

- **❌ means failed, blocked, skipped, or not run.** Code that exists but nothing tests is ❌.
- **Evidence says which kind of ❌.** Test name → ✅. `file:line` + `— no test` → built, unproven. `—` →
  nothing exists. **Evidence is empty iff nothing exists.**
- **Never write ✅ without naming the test that proves it.** Can't find one? The row is ❌.
- **A compile is not a test.**
- **Evidence names the test, never describes it** — a name a linter can assert exists.
- A **removed** requirement keeps its ID forever: strike the text, `—` in the glyph column.
- Untestable presentation requirements carry `Evidence: signoff:<date>`.

## Drafts and graduation

Proposals live isolated in [`../prd-drafts/`](../prd-drafts/) until approved — see its README.

- **A ratified PRD may never cite a draft.** Every ID a `prd/` file cites resolves inside `prd/`. The lint
  enforces it.
- **The line between the two homes is approval, not proof.** A draft becomes a contract when the owner
  ratifies its claims — not when its tests go green. **Proof is the glyph column**, and a ratified contract
  is expected to carry ❌ rows: that is what `file:line — no test` exists to say. Waiting for an all-green
  file leaves the source of truth empty and the real knowledge stranded in a home contracts may not cite.
- **Graduation is a move, not a rewrite.** `git mv ../prd-drafts/<file>.md ./<file>.md`; the IDs carry
  across unchanged. The first conformance review then sets glyphs and stamps `last_verified`.

## Refining

- **Change only what the contract changed.** Edit a row when the owner's claim changed or the code drifted
  — never to reword, and never a row the change doesn't touch.
- **The only writable surfaces are a table row, the three sentences, and the three bullets.** Never add prose.
- New behavior → **new row, new ID, appended.** Changed → **edit in place.** Removed → **strike it; row and
  ID stay.**
- Never restate a requirement that has an ID elsewhere — cite it. Never add a `##` heading.

### Stop and ask

Do not proceed if the requirement doesn't fit one layer; needs a new namespace, file, or component; would
move a requirement between files; would make this file cite one it never cited; would create a cycle; or
contradicts an existing requirement.

## Lint

Mechanical, in CI (`doc-lint`). A red lint is a broken PRD, not a style note. **This list is exactly what
the linter checks** — every other rule in this guide is one you hold yourself to.

- Every filename matches a component prefix listed in `../prd/README.md`. `prd/` and `prd-drafts/` are
  **flat** — a subdirectory is rejected, because files inside one would escape every check here.
- One namespace per file; one file per namespace. Every ID matches its file's declared namespace, and the
  namespace in `id:` is a single token.
- Every cited ID resolves; no ID is defined in two files.
- **No `prd/` file cites a `prd-drafts/` id.**
- Every ✅ has something in Evidence.
- `last_verified` present iff the file has at least one ✅ row.
- **Citations only go up the stack**, and the citation graph is a DAG — a cycle *within* one layer fails too.
- No `##` outside the schema. No requirement over 25 words. No numeric literal in requirement text.
- **The catalog is well-formed** — `../prd/README.md` has a Components list (`prefix — gloss`) and a
  Contents list naming every PRD. Catalogs are **maintained by hand**; nothing regenerates them. Add the
  row in the same task you add the file, or the build goes red.

### What the lint cannot check — so you must

The shipped linter is stack-neutral: it has no idea what your test runner is. So **a ✅ is only ever checked
for *having* Evidence — never for that test existing.** A plausible-looking name that matches nothing in the
suite passes forever, and the one claim this whole format rests on quietly becomes untrue.

If ✅ is going to mean anything here, close that gap yourself: pull the backticked Evidence names out of
`../prd/*.md`, list your suite's test names, and fail on any Evidence name the suite doesn't contain. Wire it
into the same gate as `doc-lint` — it is a handful of lines, and it is the difference between a contract and
a claim.

Two more the linter can't see, and therefore owns nothing of: that Evidence is empty **only** where nothing
exists (a `—` on code that does exist is a lie the lint will never catch), and that a requirement is the
owner's claim rather than one you generalized.
