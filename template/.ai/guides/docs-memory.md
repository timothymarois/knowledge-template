# How to write MEMORY — the standard

This guide **is the standard** for `../MEMORY.md`, the always-loaded list of friction to avoid. Shipped and
versioned by `doc-template`. **The template is `../MEMORY.md` itself** — one bullet per trap.

`MEMORY.md` holds **the friction we've hit in this codebase and the workaround for each** — so an agent
doesn't re-hit it. Traps, gotchas, non-obvious constraints: the things you learn the hard way and would
pay to have known up front.

## The one rule: it is a living list, not an archive

**When a piece of friction is genuinely solved — fixed in the code, or made impossible by a guard or
test — delete its entry.** A long `MEMORY.md` means something was solved and never pruned. This is the one
doc you *shrink* as the project matures.

- If a trap hardens into a permanent "never do X" rule, it graduates to `AGENTS.md` — move it there and
  delete it here.
- If you rely on an entry and find it no longer true, fix or delete it in passing.

## Scope: this codebase only

Not user preferences, not how someone likes to work, not cross-project notes — those live in the agent's
own memory, never here. `MEMORY.md` is about *this repo's* traps and nothing else.

## Form

- **One bullet each:** the trap, and the workaround or what to do instead. State the *why* in a clause so
  the next agent trusts it.
- **Concrete, not vague.** "The X build is flaky" helps no one; "run `X` twice — the first run races the
  codegen and fails intermittently" does.
- **Not a changelog.** What changed and when is git's. This is only what's *still* true and still bites.
