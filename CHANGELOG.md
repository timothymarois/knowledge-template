# Changelog — knowledge-template

The version history of the `.knowledge/` documentation system. Each release has a **dated migration file** in
[`.changes/`](./.changes/) with the exact steps an agent runs to move a project onto that version.

**Versioning (SemVer):** **MAJOR** = a breaking model/structure change (a home added, removed, or renamed;
a lint rule that fails previously-valid docs). **MINOR** = additive (a new optional section or a
non-breaking check). **PATCH** = wording.

**Upgrading a project:** compare the project's `.knowledge/.version` to the `VERSION` here. For each release
in between (oldest first), open its `.changes/` file, apply the steps, bump `.knowledge/.version`, and re-run
`doc-lint`.

| Version | Date | Summary | Migration |
|---|---|---|---|
| 1.1.0 | 2026-07-21 | The always-loaded `README.md` now surfaces that `scripts/` holds your own project scripts alongside the versioned linter, and marks `tmp/` throwaway — so agents stop inventing a new top-level dir. Drop-in. | [`.changes/2026-07-21-v1.1.0.md`](./.changes/2026-07-21-v1.1.0.md) |
| 1.0.0 | 2026-07-16 | First versioned release. Flat `.knowledge/`, catalog READMEs + `guides/` rules, isolated `prd-drafts/`, glyph-table PRDs, unbroken ID runs with struck removals, standalone rows, `doc-lint`. | [`.changes/2026-07-16-v1.0.0.md`](./.changes/2026-07-16-v1.0.0.md) |
