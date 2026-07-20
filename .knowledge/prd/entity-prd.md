---
id: PRD
name: PRD
last_verified: 2026-07-19
---

## What this is

A ratified, test-backed contract for one built system, written as a table of identified requirements with
a pass-or-fail glyph on each. It asserts what must be true and whether it is; it never explains how the
thing is built.

## Why it exists

- A reader can trust a verified row without going and checking the code.
- A requirement stays atomic enough to map to one test.
- Every PRD in every adopting repo has the same shape.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-PRD-1 | A PRD file holds exactly one namespace | `two namespaces in one file` |
| ✅ | R-PRD-2 | A requirement stays within the word cap | `requirement over 25 words` |
| ✅ | R-PRD-3 | A requirement names its tunables, never a numeric literal | `numeric literal in requirement` |
| ✅ | R-PRD-4 | A verified requirement names the test that proves it | `checkmark with no test named` |
| ✅ | R-PRD-5 | A last-verified stamp is present only with a verified row | `last_verified without a checkmark` |
| ✅ | R-PRD-6 | A PRD's filename prefix is a declared component | `filename prefix not a component` |
| ✅ | R-PRD-7 | A PRD uses only the closed schema headings | `heading outside the schema` |
| ✅ | R-PRD-8 | A namespace is owned by exactly one file | `two files claim one namespace` |
| ✅ | R-PRD-9 | The contract homes hold no subdirectories | `a PRD hides in a subdirectory` |
| ✅ | R-PRD-10 | A requirement joins no two assertions with a semicolon | `two assertions joined by a semicolon` |
