---
id: PAYLOAD
name: Payload
last_verified: 2026-07-19
---

## What this is

The shipped `.knowledge/` tree itself: the set of homes and files every adopting repo receives and must
keep. It is the substrate the other contracts assume — nothing else can hold if a home has gone missing
or a stranger has moved in.

## Why it exists

- An agent can rely on a path existing without checking first.
- A home silently deleted or renamed fails the build instead of going unnoticed.
- The tree an adopter runs is the tree the standard describes.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-PAYLOAD-1 | Every shipped directory exists | `a home directory was removed` |
| ✅ | R-PAYLOAD-2 | Every shipped file and guide exists | `a shipped guide was removed`, `the linter script was renamed away` |
| ✅ | R-PAYLOAD-3 | Only the shipped files and homes sit at the root | `an unexpected entry at the root` |
| ✅ | R-PAYLOAD-4 | Every versioned file matches the checksum the payload records for it | `a versioned guide was edited after adoption` |
| ✅ | R-PAYLOAD-5 | The payload records a checksum for every versioned file | `the manifest no longer covers a versioned file`, `the payload manifest is missing` |
