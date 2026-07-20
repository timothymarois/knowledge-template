# Memory — knowledge-template

Always-loaded, read at the start of every task: the friction we've hit in **this codebase** and the
workaround for each — so you don't re-hit it. **A living list — delete an entry once it's genuinely solved;
a long MEMORY means something was solved and never pruned.** This codebase only.

## Friction / gotchas

*One bullet each: the trap, and the workaround. Delete when it's genuinely solved.*

- **`guides/` and `scripts/` exist twice** — once in `template/.knowledge/` (the payload) and once in
  `.knowledge/` (this repo's adopted copy). Editing the copy is invisible downstream and breaks the CI
  diff: **always edit the payload, then copy it over the root copy.**
- **Sync `docs-*.md` and the two scripts by name — never whole folders.** `guides/README.md` is a
  *project's own catalog*, not shipped: copying the folder wholesale silently deletes a downstream repo's
  project how-to rows. It happened to the pilot repo, and only the populated teeth-test fixture caught it.
- **The teeth-test copies the live payload**, so a payload edit changes the test's valid base. After any
  change under `template/.knowledge/`, run `test_doc_lint.py` before `doc-lint` — a structural break shows
  up there first, as every case failing at once rather than one.

---
*Editing this file? Follow the standard first: [`guides/docs-memory.md`](./guides/docs-memory.md).*
