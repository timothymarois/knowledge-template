---
id: ORIENT
name: Orientation trio
last_verified: 2026-07-19
---

## What this is

The three always-loaded docs — brief, codemap, memory — that an agent reads at the start of every task.
Each is terse on purpose and ends with a pointer to its own writing standard, so the full rules are pulled
into context only by an agent about to edit it.

## Why it exists

- An agent orients on every task without paying for the standards it isn't using.
- An agent that edits one of the trio is routed to the rule before it writes.

## Requirements

|  | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-ORIENT-1 | Brief, codemap, and memory end with their standard pointer | `a trio file lost its standard pointer` |
