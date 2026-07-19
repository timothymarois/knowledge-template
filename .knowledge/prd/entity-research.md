---
id: RESEARCH
name: Research note
last_verified: 2026-07-19
---

## What this is

A dated report on how the world outside the codebase solved a problem, written so someone can decide
something. It is input, never truth: it informs a proposal and is never the source of record for our own
behavior.

## Why it exists

- A reader can tell at a glance whether a note is still current.
- Every claim about the outside world can be traced back to something openable.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-RESEARCH-1 | Every research note is dated | `research note missing its date` |
| ✅ | R-RESEARCH-2 | Every research citation resolves to a source | `research citation without a source` |
| ✅ | R-RESEARCH-3 | A research note uses only the closed schema headings | `research heading outside the schema` |
| ✅ | R-RESEARCH-4 | Every source carries a link | `a source with no link` |
| ✅ | R-RESEARCH-5 | Every source is cited at least once | `a source that is never cited` |
| ✅ | R-RESEARCH-6 | The reporting section cites at least one source | `reporting with no citation` |
