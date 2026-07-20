---
id: ORIENT
name: Orientation trio
last_verified: 2026-07-19
---

## What this is

The three always-loaded docs — brief, codemap, memory — that an agent reads at the start of every task.
Each is terse on purpose and ends with a pointer to its own writing standard, so the full rules are pulled
into context only by an agent about to edit it. The overview carries the same gate without being
always-loaded.

## Why it exists

- An agent orients on every task without paying for the standards it isn't using.
- An agent that edits one of the trio is routed to the rule before it writes.
- The trio is actually reached, rather than sitting unread behind a rulebook that stopped naming it.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-ORIENT-1 | Every edit-gated doc ends with its standard pointer | `a trio file lost its standard pointer` |
| ✅ | R-ORIENT-2 | The repo root has an agent rulebook | `the repo has no AGENTS.md` |
| ✅ | R-ORIENT-3 | The rulebook names every file in the orientation trio | `AGENTS.md no longer loads the trio` |
| ✅ | R-ORIENT-4 | No shipped placeholder survives adoption | `an unfilled orientation doc` |
| ✅ | R-ORIENT-5 | The rulebook points at its own writing standard | `AGENTS.md no longer points at its own standard` |
