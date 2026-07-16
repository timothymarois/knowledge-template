# Adopting knowledge-template

How to install this documentation system into a project and wire it into the project's agent rules. Work
through the steps in order; when `doc-lint` is green, it's installed correctly.

## 1. Copy the payload

Copy the **contents of `template/`** into the target repo's root. You get a `.knowledge/` directory —
include the hidden `.knowledge/.doc-version` stamp. Nothing outside `template/` is copied.

## 2. Wire it into `AGENTS.md` — the important step

The system only works if agents load and follow it. Add the following as the **first rules** in the
project's `AGENTS.md`, ahead of the stack rules. **Adapt the wording to the repo; keep the substance** —
this is the map that sends an agent to the right doc at the right time.

### Load order
- **Every task, read first:** `.knowledge/BRIEF.md` (what & why), `.knowledge/CODEMAP.md` (where things
  are), `.knowledge/MEMORY.md` (current friction). The map of it all is `.knowledge/README.md`.
- **On demand, when the task enters an area:**
  - `.knowledge/prd/` — tested contracts, the source of truth for what the product must do
  - `.knowledge/prd-drafts/` — proposals, not yet approved; never cite as settled
  - `.knowledge/research/` + `.knowledge/references/` — prior art and visual targets
  - `.knowledge/guides/` — how to write each kind of doc (`docs-*.md`) and recurring how-tos

### PRDs are the contract
- A new guaranteed behavior needs a `prd/` requirement **and** a test — behavior and its PRD change in the
  same commit.
- Requirements come from the owner. A proposal stays in `prd-drafts/` until approved, built, and proven,
  then graduates by `git mv` (its IDs carry over unchanged).
- When code implements a requirement, cite its `R-<AREA>-<n>` in the code so contract ↔ code ↔ test stay
  linked.

### Keep docs true in the same task
- Before editing any doc, read its home `README.md` (the catalog) and its `guides/docs-*.md` (the rules).
- Restructured files → update `CODEMAP.md`. Hit friction → add a line to `MEMORY.md`, and delete it once
  solved.

### Enforce it
- Run `python3 .knowledge/scripts/doc-lint .knowledge` before finishing.

## 3. Fill the orientation

Fill `.knowledge/BRIEF.md` (what / why / who) and `.knowledge/CODEMAP.md` (where things are) for this
project. `.knowledge/MEMORY.md` starts empty — friction accrues as you work. Adapt the rest of `AGENTS.md`
to the stack.

## 4. Declare the components

Declare the project's ontology — its layers, in order — in `.knowledge/prd/README.md` (the owner's call).
This is what the linter checks every PRD filename against.

## 5. Wire the linter into the build

Add both commands to the project's check gate so docs fail the build alongside code:

```
python3 .knowledge/scripts/test_doc_lint.py     # the linter has teeth
python3 .knowledge/scripts/doc-lint .knowledge  # the docs are valid
```

**pnpm / npm** — `package.json`:

```json
{ "scripts": {
  "lint:docs": "python3 .knowledge/scripts/doc-lint .knowledge",
  "test:docs": "python3 .knowledge/scripts/test_doc_lint.py"
} }
```

**Composer** — `composer.json`:

```json
{ "scripts": { "lint:docs": "python3 .knowledge/scripts/doc-lint .knowledge" } }
```

**CI** — a reference workflow ships at `.github/workflows/doc-lint.yml`:

```yaml
- run: python3 .knowledge/scripts/test_doc_lint.py
- run: python3 .knowledge/scripts/doc-lint .knowledge
```

## Done

Run `python3 .knowledge/scripts/doc-lint .knowledge` — green means the system is installed and wired
correctly. From here, the docs stay current because a broken one fails the build.
