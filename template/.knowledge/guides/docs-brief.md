# How to write a BRIEF — the standard

This guide **is the standard** for `../BRIEF.md`, the always-loaded orientation an agent reads first.
Shipped and versioned by `knowledge-template`. **The template is `../BRIEF.md` itself** — start from it and
fill each section by answering its question.

A brief describes **what the project is, who it serves, and what it covers** — about one screen. Not how the
code is built (that's `CODEMAP.md`), not how to work in it (that's `AGENTS.md`).

**Top rule — never include PII.** This file is committed and world-readable: no real name, username, email,
phone, or address; no secrets or machine paths. Refer to people by role; the product by its public brand or
repo name.

## Section guidance

- **Story** — *what is this and why does it exist?* One short paragraph a stranger understands: the project
  and the change it creates. A second identity (a rewrite, a fork) goes in a clause.
- **Why it exists** — the problem, who feels it, and why existing options fall short.
- **Users / ICP** — who uses it, what they're trying to accomplish, and the qualities that matter most to
  them. For an internal project, name the internal role and its job.
- **Scope** — the product areas, features, or surfaces the project spans, and what's explicitly out of scope.
- **External Systems** — the databases, services, and third-party systems it relies on, each with what it's
  used for.

## Quality bar

- **Skimmable** — short bullets, one idea per line, about one screen.
- **No placeholders left** — replace every `<...>` and `_(none)_`; delete a section rather than writing "none".
- **Public and PII-free** — people by role; no private data, secrets, or machine paths.
- **Shape is universal** — the same sections fit any project; adjust the words, not the shape.
- **Change only when it changed** — update when the project's story, users, scope, or systems actually
  shifted, not to reword; leave the rest untouched.
