# examples/

Reference examples of the template's `AGENTS.md` **molded to real, different tech stacks** — so you can
see how the same skeleton adapts before you fill in your own. These are illustrations, **not** copied into
downstream projects (only the contents of `../template/` are).

| Example | Stack | Shows |
|---|---|---|
| [`AGENTS.laravel.md`](./AGENTS.laravel.md) | Laravel 13 + Inertia/Vue 3 | Thin-controller/service layering, Form-Request validation, Vue component tiers, `pnpm check` DoD |
| [`AGENTS.axmol.md`](./AGENTS.axmol.md) | Axmol (C++17) game engine | Four-layer sim/render/game/tests split, the link-time tripwire, determinism + render rules, owner-runs-the-app DoD |

**What stays the same across both** (the invariant core): the identity paragraph, *Before You Work* load
order (always open `.ai/BRIEF.md` + `.ai/CODEMAP.md`, depth on demand), Hard Gates, the universal *Never*
rules, *Documentation Duties* (read a home's README before writing a doc; graduate design→PRD), and the
Definition-of-Done shape.

**What each one adapts:** *Tech Stack*, *Architecture — the one rule that matters*, *Best Practices
(Do/Don't with ✅/❌ examples)*, *Directory Structure*, *Build/Test/Run*, and the DoD command.

Start from [`../template/AGENTS.md`](../template/AGENTS.md) (the blank skeleton) and use these to see what
"filled in" looks like for your stack.
