# AGENTS

Rules for every agent working in this repository. These rules are law; where they conflict with your
general habits, this file wins.

This is an **isometric city-builder on the Axmol C++ engine (v2 LTS)**, built on a four-layer stack: a
pure, deterministic simulation core; a render seam; a thin game layer; and a headless test suite that
doubles as the architecture tripwire. The *what & why* lives in [`.ai/BRIEF.md`](./.ai/BRIEF.md); the
knowledge map is [`.ai/docs/README.md`](./.ai/docs/README.md). This file defines how you build on the stack.

> **This is an example** of the doc-template `AGENTS.md` molded to a C++ / game-engine stack. See
> `AGENTS.laravel.md` for a web-app example, and `../template/AGENTS.md` for the blank skeleton.

---

## Before You Work — (invariant)

**Load light by default, then pull depth only when the task reaches for it.**

1. **Always:** read [`.ai/BRIEF.md`](./.ai/BRIEF.md) (what & why), [`.ai/CODEMAP.md`](./.ai/CODEMAP.md)
   (where things are), and [`.ai/MEMORY.md`](./.ai/MEMORY.md) (current friction to avoid).
   [`.ai/docs/README.md`](./.ai/docs/README.md) is the map to everything below.
2. **On demand, when your task enters an area:** the feature's `.ai/docs/PRD/PRD-<System>.md` (tested
   contract) or `.ai/docs/PRD-drafts/` (proposal, not built yet); `.ai/docs/guides/`; `.ai/docs/research/`
   and its `references/` visuals. Current state: `PRD-drafts/` = in flight, `PRD/` = shipped; no status file.
3. Read every file before editing it — the architecture has load-bearing seams not obvious from one file.
4. Search before writing new logic; reuse, extend, refactor. When the user raises a concern, investigate
   before contradicting — evidence (a header, a test, a benchmark), never a hunch.

## Hard Gates — Require Explicit Approval — (invariant)

- **Dependencies.** Do not add third-party libraries or change the pinned engine version without approval.
- **Migrations / save format.** Any change to the serialized save/world format is confirmed first.
- **Deletions.** Do not delete files outside the task's immediate scope without approval.
- **Commits.** Do not commit or push unless told to.
- **This file.** Never modify `AGENTS.md` without approval.

## Never — (invariant core, plus this stack's prohibitions)

- Never touch `.env` or commit credentials, tokens, or keys.
- Never leave debug prints, commented-out code, or disabled tests in completed work.
- Never edit anything under `axmol/` — the engine is a pinned submodule; every fix lives in our own `CMakeLists.txt`.
- Never include an Axmol header under `sim/` — no pixels, colors, or engine types in the sim.
- Never use raw `new`/`delete` — RAII everywhere; `std::unique_ptr` for ownership.
- Never recompute the whole map on a user action — edits touch only the edit region plus its footprint.

---

## Tech Stack — *(adapted for this project)*

- **Core:** C++17, the pure `sim/` static lib (no engine).
- **Engine / render:** Axmol v2 LTS (pinned submodule), OpenGL/Metal via Axmol.
- **Build:** CMake + Ninja generator.

## Architecture — the one rule that matters

Four layers. Dependencies point **one way only**; the arrow never points up — the sim knows nothing about
render or game.

| Layer | Owns | May depend on | Must not |
|---|---|---|---|
| `sim/` | Tile model, iso math, worldgen, terraform, RNG | Standard library only | Include Axmol; know about pixels/sprites/input |
| `render/` | Reading the snapshot, culling, sprite draw, shaders | `sim` + Axmol | Mutate sim state; hold a long-lived pointer into sim storage |
| `game/` | Booting Axmol, owning the world, input → commands | `sim` (+ `render`) | Contain reusable sim logic the next game would want |
| `tests/` | Headless unit + deterministic tests | **`sim` only** | Link Axmol; depend on render or game |

`tests/` linking `sim` alone is the **tripwire**: the day an Axmol include creeps into the sim, the test
binary stops linking and the build goes red. Fix the include, never "fix" it by linking Axmol into tests.

**Placement rule:** if a thing makes *this* game *this* game, it goes in `game/`; if two games on this
stack would both want it, it goes in `sim/`. When unsure, default to `game/` — promoting later is cheap.

## Best Practices — Do / Don't

### Determinism

- **Do** keep RNG in world state — seeded, serialized with the save. **Don't** use a global/unseeded RNG.
- **Do** read last tick, write next tick, then swap. **Don't** mutate the array you're iterating.

```cpp
✅ struct World { sim::Rng rng; };   int roll = world.rng.range(0, 99);   // seeded + saved
❌ int roll = std::rand() % 100;                                          // not reproducible
```

### Rendering

- **Do** set `Director::setProjection(_2D)` in `applicationDidFinishLaunching` (Axmol defaults to a
  perspective camera; iso geometry off z=0 visibly converges). **Don't** relitigate settled render rules.
- **Do** verify render work by building, running, and **looking** at the real window — not "it compiles."

## Code documentation

Document the non-obvious — *why* a method exists, its contract/invariants, and which PRD requirement it
satisfies. Trivial accessors get nothing; a comment restating the code is noise.

- **Complex `sim/` methods get a Doxygen block** (intent · invariants · determinism / edge cases).
  Explain *why*, not *what*.
- **Cite the requirement** — name the `R-<AREA>-<n>` it implements (see `.ai/docs/PRD/`).

```cpp
✅ /// Spreads terraform height outward with a bounded terrace step (R-TERRAFORM-3).
   /// Reads last tick / writes next — safe to call mid-iteration; touches only the
   /// edit region plus its declared footprint, never the whole map.
   DirtyRect raiseRegion(TileSpan span, int step);
❌ // raise the region      ← restates the name; teaches nothing
```

## Directory Structure

```
├── sim/      # pure C++ sim core — no Axmol
├── render/   # simcore + Axmol
├── game/     # executable — boots Axmol, owns the world
├── tests/    # headless, links sim only (the tripwire)
├── axmol/    # pinned engine submodule, never edited
└── .ai/      # agent docs: BRIEF, CODEMAP, docs/ + tmp/ — do not restructure
```

## Build, Test & Run

```bash
cmake --build cmake-build-dev --target <AppTarget>   # build the app (do NOT run by default)
./scripts/dev-test.sh                                # headless sim tests — the tripwire + CI gate
```

**The owner runs the app and provides screenshots** — visual sign-off is his. Build to prove it compiles
and links; run the tests; then hand off. Run the app yourself only when the owner asks in that turn.

---

## Documentation Duties — (invariant)

Keep docs true in the same task that changes reality. **Before creating or editing any doc, read that
home's `README.md` first** (its rules + ID convention), then copy its `TEMPLATE.md`.

- Moved/restructured files → update `.ai/CODEMAP.md`.
- Hit friction (a trap, a non-obvious constraint) → add a line to `.ai/MEMORY.md`; delete it once solved.
- Shipped guaranteed behavior → graduate its `PRD-drafts/` draft to a `PRD/`, every `R-` mapped to a
  passing test, and **delete the draft** (no pointer stub); behavior and PRD change in the same commit.
- Scratch/throwaway files → `.ai/tmp/` (git-ignored).

## Definition of Done

1. `./scripts/dev-test.sh` is green (the tripwire still links).
2. Visual/feel work: you **build** it; the **owner runs it and signs off** from screenshots. "Compiles
   and wired" is not done.
3. Every rule here held — the tripwire links, the sim stayed Axmol-free, determinism held, no whole-map recompute.

**When creating task lists or plans, the final step is always:** _"Re-read `AGENTS.md` and verify Definition of Done."_
