# AGENTS

Rules for every agent working in this repository. These rules are law; where they conflict with your
general habits, this file wins.

This is a **Laravel + Inertia/Vue web application**: a thin HTTP layer over service/action business logic,
with a Vue 3 SPA rendered through Inertia. The *what & why* lives in [`.ai/BRIEF.md`](./.ai/BRIEF.md); the
knowledge map is [`.ai/docs/README.md`](./.ai/docs/README.md). This file defines how you build here.

> **This is an example** of the doc-template `AGENTS.md` molded to a Laravel/Vue stack. See
> `AGENTS.axmol.md` for a C++ game-engine example, and `../template/AGENTS.md` for the blank skeleton.

---

## Before You Work — (invariant)

**Load light by default, then pull depth only when the task reaches for it.**

1. **Always:** read [`.ai/BRIEF.md`](./.ai/BRIEF.md) (what & why), [`.ai/CODEMAP.md`](./.ai/CODEMAP.md)
   (where things are), and [`.ai/MEMORY.md`](./.ai/MEMORY.md) (current friction to avoid).
   [`.ai/docs/README.md`](./.ai/docs/README.md) is the map to everything below.
2. **On demand, when your task enters an area:** the feature's `.ai/docs/PRD/PRD-<System>.md` (tested
   contract) or `.ai/docs/PRD-drafts/` (proposal, not built yet); `.ai/docs/guides/`; `.ai/docs/research/`
   and its `references/` visuals. Current state: `PRD-drafts/` = in flight, `PRD/` = shipped; no status file.
3. Read every file before editing it. Search before writing new logic — reuse, extend, refactor.
4. When the user raises a concern, investigate before contradicting — evidence, not a hunch.

## Hard Gates — Require Explicit Approval — (invariant)

- **Migrations.** Any change to schema, user data, or persisted state is confirmed first.
- **Dependencies.** Do not add, remove, or major-version-bump a Composer or pnpm package without approval.
- **Deletions.** Do not delete files outside the task's immediate scope without approval.
- **Commits.** Do not commit or push unless told to.
- **This file.** Never modify `AGENTS.md` without approval.

## Never — (invariant core, plus this stack's prohibitions)

- Never touch `.env` or commit credentials. Access env only through `config/` — never call `env()` outside `config/`.
- Never leave `dd()`, `dump()`, `console.log`, or commented-out code in completed work.
- Never validate on the frontend — Laravel Form Requests are the single source of truth; the frontend only
  displays server-returned errors.
- Never let backend and frontend drift — names, props, enums, and routes match between Laravel and Vue at
  all times; rename on one side, rename on the other in the same task.

---

## Tech Stack — *(adapted for this project)*

- **Backend:** Laravel 13+ (PHP 8.4+), Redis via Horizon (queue + cache), Inertia server adapter.
- **Frontend:** Vue 3 (`<script setup>`), Inertia.js, TailwindCSS 4, shadcn-vue (Radix primitives), Lucide icons.

## Architecture — the one rule that matters

The HTTP layer is thin; business logic lives in services and actions. Dependencies point inward.

| Layer | Owns | May depend on | Must not |
|---|---|---|---|
| Controllers | Receive a Form Request, delegate, return a response | Services, Actions | Hold business logic, validate inline, authorize inline |
| Form Requests | Validation + authorization | Policies | — |
| Services / Actions | Business processes / single-purpose ops | Models, other services (constructor-injected) | Touch the HTTP layer; use facades/helpers |
| Vue `ui/` → `app/` → `site/` | Stateless kit → auth surfaces → public pages | inner tiers only | `ui/` may not be app-aware |

**Placement rule:** no app logic → `ui/`; needs Inertia/auth → `app/`; public marketing → `site/`. Search
the component showcase before building a new one — it likely exists.

## Best Practices — Do / Don't

### Backend

- **Do** keep controllers to: Form Request in, Service/Action call, response out. **Don't** put logic there.
- **Do** authorize in Policies (via the Form Request). **Don't** inline role checks in controllers/Blade.

```php
✅ public function store(StoreUserRequest $request): RedirectResponse {
       $this->userService->create($request->validated());
       return redirect()->route('admin.users.index');
   }
❌ public function store(Request $request) {                       // inline validation + logic
       if (! $request->user()->isAdmin()) abort(403);
       $request->validate(['name' => 'required']);
       User::create([...]);
   }
```

### Frontend

- **Do** put `<template>` above `<script setup>`; use Inertia `useForm` for every form. **Don't** hand-roll
  refs for form fields, errors, or processing state.
- **Do** `route()` in scripts / `$route()` in templates; Lucide for icons. **Don't** hardcode URLs or add another icon lib.

```vue
✅ <script setup> const form = useForm({ name: '' }); function submit(){ form.post(route('users.store')); } </script>
❌ <script setup> const name = ref(''); const errors = ref({}); /* manual + client validation */ </script>
```

## Code documentation

Document the non-obvious — *why* a method exists, its contract, and which PRD requirement it satisfies.
Trivial controllers and accessors get nothing; a comment restating the code is noise.

- **Complex Services/Actions get a PHPDoc block** (intent · contract · edge cases). Non-trivial
  composables/utils get TSDoc. Explain *why*, not *what*.
- **Cite the requirement** — name the `R-<AREA>-<n>` a method implements (see `.ai/docs/PRD/`).

```php
✅ /**
    * Provisions a tenant database and seeds its owner (R-TENANT-2).
    * Idempotent: a re-run on a half-provisioned tenant resumes — never duplicates.
    * @throws ProvisioningException when the central connection is unreachable.
    */
   public function provision(Tenant $tenant): void
❌ // provision the tenant      ← restates the name; teaches nothing
```

## Directory Structure

```
├── app/
│   ├── Http/{Controllers,Requests,Middleware}/
│   ├── Services/  Actions/  Policies/  Models/
├── resources/js/
│   ├── components/{ui,app,site}/   pages/   composables/   utils/
└── .ai/      # agent docs: BRIEF, CODEMAP, docs/ + tmp/ — do not restructure
```

## Build, Test & Run

```bash
pnpm check        # Pint, Larastan, Pest, ESLint, Stylelint, tsc, Vitest, client + SSR build
pnpm dev          # local dev server (Herd serves the app)
```

---

## Documentation Duties — (invariant)

Keep docs true in the same task that changes reality. **Before creating or editing any doc, read that
home's `README.md` first** (its rules + ID convention), then copy its `TEMPLATE.md`.

- Moved/restructured files → update `.ai/CODEMAP.md`.
- Hit friction (a trap, a non-obvious constraint) → add a line to `.ai/MEMORY.md`; delete it once solved.
- Shipped guaranteed behavior → graduate its `PRD-drafts/` draft to a `PRD/`, every `R-` mapped to a
  passing Pest test; behavior and PRD change in the same commit.
- Scratch/throwaway files → `.ai/tmp/` (git-ignored).

## Definition of Done

1. `pnpm check` passes (Pint, Larastan level 5, Pest, ESLint, Stylelint, tsc, Vitest, client + SSR build).
2. Every rule here held — thin controllers, validation server-side only, no backend/frontend drift.
3. New guaranteed behavior is proven by a `PRD/` requirement and its Pest test.

**When creating task lists or plans, the final step is always:** _"Re-read `AGENTS.md` and verify Definition of Done."_
