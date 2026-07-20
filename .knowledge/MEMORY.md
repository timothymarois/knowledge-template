# Memory — knowledge-template

Always-loaded, read at the start of every task: the friction we've hit in **this codebase** and the
workaround for each — so you don't re-hit it. **A living list — delete an entry once it's genuinely solved;
a long MEMORY means something was solved and never pruned.** This codebase only.

## Friction / gotchas

*One bullet each: the trap, and the workaround. Delete when it's genuinely solved.*

- **`guides/` and `scripts/` exist twice** — once in `template/.knowledge/` (the payload) and once in
  `.knowledge/` (this repo's adopted copy). Editing the copy is invisible downstream and breaks the CI
  diff: **always edit the payload, then copy it over the root copy.**
- **Sync `docs-*.md` and the two scripts by name — never whole folders, never a multi-file `cp` into a
  home.** `guides/README.md` is a *project's own catalog*, not shipped. `cp -R guides/. dest/guides/`
  overwrites it; so does `cp a.md b.md dest/guides/` when one of those files is another home's README.
  Both mistakes were made here, on the same downstream repo, and only the teeth-test caught them.
  Copy one named file to one named path. **This has now happened three times to the same file** — the
  rule keeps being restated and keeps being broken, because a bulk `cp` is the convenient thing to reach
  for. Before any sync, list exactly which files are shipped; `guides/README.md` is not one of them.
- **Any edit to a `docs-*.md` or to either script invalidates `.payload-manifest`.** Re-run
  `python3 template/.knowledge/scripts/doc-lint --write-manifest template/.knowledge` and copy the file
  down to `.knowledge/.payload-manifest`, or every command goes red on a checksum mismatch that reads like
  the file was tampered with. Regenerate **last**, after the payload edits are final.
- **The teeth-test copies the live payload**, so a payload edit changes the test's valid base. After any
  change under `template/.knowledge/`, run `test_doc_lint.py` before `doc-lint` — a structural break shows
  up there first, as every case failing at once rather than one.

---
*Editing this file? Follow the standard first: [`guides/docs-memory.md`](./guides/docs-memory.md).*
