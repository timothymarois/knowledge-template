# How to write MEMORY — the standard

This guide **is the standard** for `../MEMORY.md`, the always-loaded list of friction to avoid. Shipped and
versioned by `knowledge-template`. **The template is `../MEMORY.md` itself** — one bullet per trap.

`MEMORY.md` holds **the friction we've hit in this codebase and the workaround for each** — traps, gotchas,
non-obvious constraints an agent would pay to have known up front.

**Top rule — never include PII.** MEMORY is committed and world-readable: no real names, emails, secrets,
tokens, or machine paths in a trap — describe the failing thing generically, and refer to people by role.

## A living list, not an archive

- **When friction is genuinely solved — fixed in code, or made impossible by a guard or test — delete its
  entry.** This is the one doc you *shrink* as the project matures.
- If a trap hardens into a permanent "never do X" rule, it graduates to `AGENTS.md` — move it, delete it here.
- Rely on an entry and find it no longer true? Fix or delete it in passing.

## Scope: this codebase only

Not user preferences, not how someone likes to work, not cross-project notes — those live in the agent's own
memory. `MEMORY.md` is about *this repo's* traps and nothing else.

## Form

- **One bullet each:** the trap, and the workaround or what to do instead. State the *why* in a clause.
- **Concrete, not vague.** Not "the X build is flaky" but "run `X` twice — the first run races the codegen
  and fails intermittently".
- **Not a changelog.** Only what's *still* true and still bites.
- **Only touch an entry to add, delete, or correct it.** Never reword an entry for its own sake.
