# Changelog — doc-template

The version history of the `.ai/` documentation system. Each release has a **dated migration file** in
[`.changes/`](./.changes/) with the exact steps an agent runs to move a project onto that version.

**Versioning (SemVer):** **MAJOR** = a breaking model/structure change (a home added, removed, or renamed;
a lint rule that fails previously-valid docs). **MINOR** = additive (a new optional section or a
non-breaking check). **PATCH** = wording.

**Upgrading a project:** compare the project's `.ai/.doc-version` to the `VERSION` here. For each release
in between (oldest first), open its `.changes/` file, apply the steps, bump `.ai/.doc-version`, and re-run
`doc-lint`.

| Version | Date | Summary | Migration |
|---|---|---|---|
| 1.0.0 | 2026-07-16 | First versioned release. Flat `.ai/`, catalog READMEs + `guides/` rules, isolated `prd-drafts/`, glyph-table PRDs, `doc-lint`. | [`.changes/2026-07-16-v1.0.0.md`](./.changes/2026-07-16-v1.0.0.md) |
