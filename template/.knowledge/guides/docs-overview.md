# How to write an OVERVIEW — the standard

This guide **is the standard** for `../OVERVIEW.md`. Shipped and versioned by `knowledge-template`.
**The template is `../OVERVIEW.md` itself** — start from it and fill each section.

`OVERVIEW.md` is **the one doc written for a stakeholder**. Everything else in `.knowledge/` serves an
agent: `BRIEF.md` orients, `CODEMAP.md` locates, `prd/` contracts. None of them ever shows the platform.

It answers three questions a product owner cannot answer from a demo or a codebase: **what are the
components and how does work flow between them**, **what is actually built versus still proposed**, and
**what governs what is allowed to happen**. Someone should finish it able to explain the product in a
meeting, and to say where the gaps are, without ever having opened the code.

## Who it is for

**A product manager, a founder, a marketer, a new joiner on their first day — not a developer.** Assume the
reader has never opened the repo, will never open the repo, and stopped reading at the first word they
didn't recognise. Every other doc here is for an engineer or an agent; this one is not, and writing it in
engineering vocabulary wastes the only artefact those readers have.

**Use the words the business uses with its customers.** If a term appears in a sales conversation, a
pricing page or a support ticket, it belongs here. If it only appears in code, a protocol spec, or an
architecture discussion, replace it with what it *means* to someone using the product.

```
✅ Delivery — the buyer receives the lead in their own system, and we record whether it arrived
❌ FORM_POST delivery — posts the lead payload to the buyer's configured CRM endpoint

✅ Price quote — a price we have offered, good for a short window before it expires
❌ Bid TTL envelope — a signed bid token with an expiry claim, required on post
```

Banned outright: file names, class and table names, HTTP verbs and status codes, protocol names, and any
acronym the business does not say out loud. Link the contract for anyone who wants the mechanism —
**the link is where technical detail lives, never the sentence.**

The test before you ship it: **could someone in marketing read this aloud on a customer call without
stopping to ask what a word means?** If not, it isn't finished.

**It is written, not generated.** A tool can list what exists and draw the links it finds; it cannot decide
what matters, what to leave out, or what to call things so a newcomer follows. That judgement is the entire
value here. **Distil — do not dump.**

**Public and PII-free.** Assume a stranger reads it: no names, credentials, or machine paths.

## The diagram is the point

Everything else supports it. Rules, in order of how often they're broken:

- **Group by component.** Use one `subgraph` per layer the project declared in
  [`../prd/README.md`](../prd/README.md), in that order. The reader should see the system break into its
  levels before reading a single label.
- **About fifteen boxes, hard.** Past that nobody reads it and nobody maintains it. If the platform has
  forty parts, the diagram shows the fifteen that decide how it behaves — the rest live in
  [`../prd/README.md`](../prd/README.md), which lists everything by design.
- **One box = one thing a *non-technical* person would name.** If a stakeholder has never said the word out
  loud, it is implementation: rename it to what it does for the business, or leave it out.
- **Arrows are the point, not decoration.** An arrow means something real moves or depends: a request, a
  record, an authorisation. A diagram of boxes with no arrows has said nothing — if you cannot draw the
  arrows, you do not yet understand the platform, and that is worth saying out loud.
- **Point at the evidence for every arrow before you draw it** — the requirement, the field, the code path
  that makes it true. **A plausible arrow is the most dangerous thing in this file:** a reader builds their
  mental model from the picture and will never re-check it, and unlike a wrong sentence nobody proofreads a
  wrong line. If two things merely *appear* related, leave the arrow out and ask.
- **Mark anything not fully built, in the diagram itself.** A `·planned` suffix for what doesn't exist and
  `·partial` for what half-exists, styled inside the mermaid block — not explained in prose three sections below. The diagram has to survive being
  screenshotted on its own, and a solid box reads as shipped.
- **Mark what isn't built** — a dashed node or a `·planned` suffix. A picture that quietly includes
  ambitions as though they ship is the most damaging thing this file can do.
- **Label in the product's words**, matching each contract's `name:`, so a reader can jump from a box to
  the contract that governs it.

```mermaid
flowchart LR
  subgraph Entity["Entities"]
    a["Thing"] --> b["Other thing"]
  end
  subgraph Flow["Flows"]
    b --> c["What happens when they meet"]
  end
  classDef planned stroke-dasharray: 4 3;
  class c planned;
```

## Section guidance

- **`The platform`** — the diagram, and nothing else. No prose above it; it should survive being screenshotted.
- **`How it works`** — every component, in the order things flow through them. For each: what it is, what
  it does, what the next one receives, and **whether it is built**. The component is the unit — this is not
  a user story and not a sequence of API calls, it is the business explaining its own moving parts.

  ```
  ✅ Source — where leads come from. A seller registers one; it starts in a safe sandbox until it is
     cleared for live traffic, and once live it feeds the lanes that price its leads. Built.
  ❌ The Source entity is provisioned in sandbox mode and validated against the ping taxonomy on receipt.
  ```

  Same fact, two audiences. The second tells a product owner nothing they can act on.
- **Say what is built, every time — and "partly" is the common answer.** Three states, never two:
  **Built** · **Partly built** · **Not built yet**. Binary marking is how a component whose core exists but
  whose lifecycle doesn't gets presented as finished.
  **"Partly built" is only honest if you say which part**: *"you can create one and revise it; changing its
  status, pausing it, and the alternative pricing models are not built."* A product owner reading this is
  deciding what to promise — the half that doesn't work is the half they need.
  Check each component against its contract's rows before you label it: mostly ❌ is not "Built".
  Partly-built components are marked in the **diagram** too, not only in prose.
- **`What governs it`** — the rules that constrain the journey, and **who sets each one**: the terms both
  sides agreed, the limits, the obligations that pause things when unmet. A stakeholder can watch a demo
  and learn the flow; they cannot see the governance, which is exactly why it is here.

## Keeping it true

- **Update it when the shape changes** — a new system, a system removed, a flow re-routed. Not when a
  requirement changes; that is the contract's job, and this file never restates a requirement.
- **Never copy requirement text here.** Link the contract instead. Copied rules go stale silently, and this
  file is the one place nobody thinks to re-check.
- **If it disagrees with `prd/`, `prd/` wins** — and fix this file in the same task.
- **Where the content comes from:** the contracts in `prd/` and `prd-drafts/` (each one's *What this is*),
  the components declared in `../prd/README.md`, and `CODEMAP.md` for what actually exists. Where those
  leave the ordering ambiguous — and they usually do — **ask the owner rather than guessing a flow.**
