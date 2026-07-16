# How to write a BRIEF — the standard

This guide **is the standard** for `../BRIEF.md`, the always-loaded orientation an agent reads first.
Shipped and versioned by `knowledge-template`. **The template is `../BRIEF.md` itself** — start from it and fill
each section by answering its question.

A brief is a short orientation doc: **what the project is, who it serves, and what it covers.** Keep it to
about one screen. It describes the project itself — not how the code is built (that's `CODEMAP.md`) and not
how to work in it (that's `AGENTS.md`).

**Public and PII-free.** This file is committed and world-readable. No individual's real name, username,
email, phone, or address; no secrets or machine-specific paths. Refer to people by role ("the owner", "an
admin", "a buyer"); refer to the product only by its public brand or repo name.

## Section guidance

- **Story** — *what is this and why does it exist?* One short paragraph a stranger understands: what the
  project is and the change it creates. A second identity (a rewrite, a fork) goes in a clause.
- **Why it exists** — the problem, who feels it, and why existing options fall short. When a decision is
  unclear, an agent comes back here to resolve it.
- **Users / ICP** — who uses it, what they're trying to accomplish, and the qualities that matter most to
  them. For an internal project, name the internal role and the job it does.
- **Scope** — the product areas, features, or surfaces the project spans, and what's explicitly out of
  scope. This sets the boundary of what the project is about.
- **External Systems** — the databases, services, and third-party systems it relies on, each with what
  it's used for.

## Quality bar

- **Skimmable** — short bullets, one idea per line, about one screen.
- **No placeholders left** — replace every `<...>` and `_(none)_`; delete a section rather than writing "none".
- **Public and PII-free** — people by role, never by name; no private data, secrets, or machine paths.
- **Shape is universal** — the same sections fit any kind of project; adjust the words, not the shape.
