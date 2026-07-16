# How to write a CODEMAP — the standard

This guide **is the standard** for `../CODEMAP.md`, the always-loaded structural map. Shipped and versioned
by `doc-template`. **The template is `../CODEMAP.md` itself** — start from its skeleton and adapt the
sections to the stack.

A codemap is a **structural inventory** — the table of contents of a codebase. It answers "where does X
live and what exists?" so you can navigate without grepping the whole repo first. It lists **what exists**,
layer by layer. It is not a tutorial, not a set of conventions, and not a place for gotchas (those are
`MEMORY.md`).

**Public and PII-free.** Inventory structure, not secrets: never copy credentials, tokens, connection
strings, personal emails, or machine paths; generalize identifiers that embed a person's name. Point to
`.env.example` or config as the source of truth rather than listing real values.

## The research process

Build a codemap by surveying the repo systematically, not from memory.

1. **Identify the stack and its layers.** Look at the framework and the top-level folders. The layers you
   find become your sections.
2. **Survey each layer.** Go folder by folder and list every artifact — its name, a one-line purpose, and
   key relationships. For a large repo, split this across parallel passes, one per layer.
3. **Count what you inventory.** Real counts ("28 models", "66 controllers") show the map is complete and
   make drift obvious next time.
4. **Assemble and compress.** Cut to names + terse notes. Aim for **under ~200 lines** — density over prose.

## Sections are per-layer maps — adapt them to the stack

The starter ships a generic skeleton (Entry Points · Domain/Data · Backend/Services · Frontend/UI · Tests ·
Scripts · Integrations/Jobs · Docs). It is a starting point, not a fixed form: rename, split, drop, and add
sections so each is a real map of a real layer in *this* codebase. Delete any skeleton section with nothing
to list. The shape follows the code:

- A web app maps as its framework layers — models, services, controllers, routes, jobs, pages, components.
- A browser extension maps as manifest & entry points, background worker, content scripts, UI, messaging.
- A native / game project maps as build targets, scenes/entities, systems, assets, scripts, tests.

The only invariant: **one section per layer, each listing what exists.**

## Entry format

- **Group by folder**, with the count in the heading: `## Services (app/Services/ — 18)`.
- **One line per artifact:** name — terse purpose — key relationships/notes.
- **Use a table for dense, relational layers** (e.g. models: Name | Relationships | Notes); bullets for flat lists.
- **Point to the source of truth** rather than copying it.
- Abbreviate ruthlessly — the reader wants the shape of the layer, not prose.

## Keeping it current

- **Refresh on drift, not on a timer.** When a change adds or removes a layer or shifts counts, update the
  affected sections. A count that no longer matches the repo is the first sign the map is stale.
- Record removals too — drop the lines and note it.
