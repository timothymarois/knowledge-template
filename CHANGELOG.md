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
| 2.0.0 | 2026-07-19 | Catalogs are maintained by hand (and every home is completeness-checked); `AGENTS.md` must exist and load the trio; one file per namespace enforced; stack-neutral placement ladder. | [`.changes/2026-07-19-v2.0.0.md`](./.changes/2026-07-19-v2.0.0.md) |
| 1.0.1 | 2026-07-19 | Fix: the teeth-test failed its own valid base in any project that had written a PRD. | [`.changes/2026-07-19-v1.0.1.md`](./.changes/2026-07-19-v1.0.1.md) |
| 1.0.0 | 2026-07-16 | First versioned release. Flat `.knowledge/`, catalog READMEs + `guides/` rules, isolated `prd-drafts/`, glyph-table PRDs, `doc-lint`. | [`.changes/2026-07-16-v1.0.0.md`](./.changes/2026-07-16-v1.0.0.md) |
