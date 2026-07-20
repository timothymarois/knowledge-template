# Agent tests

The guides are prompts. Prompts aren't verified by reading them — you give a real agent a real task and
check what it did. This logs every such run, including the ones that found nothing.

The linter's rules are proven separately by `scripts/test_doc_lint.py`. This covers the other half: what no
linter can check.

## How to run one

1. Copy the target's `AGENTS.md` + `.knowledge/` to a scratch dir and `git init` — the diff is the result.
2. Give the task in the owner's words. Never hint at the convention being tested.
3. Read the diff against the guide. **A green lint is not a pass** — most of what these guides ask isn't lintable.
4. Log it below.

**Use two agents.** Every defect here came from two agents disagreeing; where they agreed, they were right.
**Audit anything written rather than generated** — a writer cannot report the rule they never noticed they
dropped.

## Runs

| Date | Under test | Result |
|---|---|---|
| 07-19 | `docs-prd` | Describe the workflow: **3/3 correct** |
| 07-19 | `docs-prd` | Record a ratified claim: **1/3** — two graduated a whole draft on one row |
| 07-19 | `docs-prd` after fix | **2/2** left it a draft and said why |
| 07-19 | `ADOPT` + 4 guides | Cold adoption: **2/2 green**, real layer maps — but two `ADOPT` gaps found |
| 07-19 | `ADOPT` after fix | Migrated and deleted the old docs home; asked before declaring the ontology |
| 07-19 | `docs-memory` | Planted friction: **0/2 recorded it** |
| 07-19 | `docs-memory` ×3 fixes | Best reached **1/2**; one agent never wrote an entry |
| 07-19 | `docs-research` | Note written: **14/15 URLs live**, none fabricated |
| 07-19 | `docs-brief`/`codemap` | Thin-README adoption: CODEMAP pass; BRIEF never said what it inferred |
| 07-19 | `docs-brief` after fix | Split sourced vs inferred unprompted, flagged ICP as owner knowledge |
| 07-19 | `docs-agents` | Audit vs a refined real rulebook: ship-as-written survived 1/2; **0/2 wrote a ✅/❌ pair** |
| 07-19 | `docs-agents` head-to-head | Rebuilt a real `AGENTS.md`: **10/10 sections, 10/15 rules** — all 5 misses underivable from code |
| 07-19 | `docs-agents` reconcile | Existing 128-line rulebook: **32/48 rules kept**, a whole Testing section lost, reported as success |
| 07-19 | `docs-agents` reconcile, fixed | **43/49 kept.** Agent reported "nothing removed"; audit found 4 lost, 2 softened |
| 07-19 | `docs-overview` ×4 + 2 audits | Diagram drew **3 arrows that don't exist**; binary build status showed unbuilt work as shipped |
| 07-19 | `AGENTS.md` rules, coding | Full-stack feature: **zero Never violations**, doc duties fired mid-code; **1/2 shipped an unauthorized route** |
| 07-19 | ditto, after fix | Policy created, `authorize()` on both actions, `cursor-pointer` present |
| 07-20 | `docs-overview` cold read | Reader given only the file: got the mechanics, **couldn't say how it earns or which industry** |
| 07-20 | ditto, after fix | Answered all three; rated it scannable; found 2 terms named but never shown |
| 07-20 | **Adoption from GitHub** | Real README prompt, public repo: payload fetched, adoption **completed green**, CI wired — the README prompt was stale |
| 07-20 | **Upgrade path** | First run of the 1.0.0 migration on a legacy repo: completed, IDs carried, version stamped — two migration defects |
| 07-20 | **Monorepo** | 3 apps + 3 packages: green; CODEMAP mapped **by layer across workspaces**, not per app |
| 07-20 | `docs-overview` framing + surfaces | Written cold ×2: **2/2 wrote both unprompted**; one invented the `prd/`-vs-drafts calibration itself |
| 07-20 | `docs-overview` cold read ×2 | Both answered **"no, and the doc told me"** on what ships; both then asked for a status column |
| 07-20 | `docs-prd` standalone + no-infra | New contract from owner's words ×2: **2/2 clean rows**, both caught a cross-file conflict unprompted |
| 07-20 | ditto | **2/2 copied `*(Proposed — not built)*` from neighbouring files** — a pattern the guide bans |
| 07-20 | `docs-prd` erase & renumber | **Void — harness error.** Both agents were handed the superseded struck-row rule; re-run |
| 07-20 | ditto, re-run | **2/2 erased, renumbered, and swept every citation** across code, tests and roadmap; both found pre-existing mis-citations |
| 07-20 | `docs-overview` **cross-vendor** | Same task on codex, grok and a separate claude CLI: **3/3 wrote the framing line, the `prd/` split and `What you use`** |
| 07-20 | ditto | **Judgment rules degraded:** codex dropped the audience that touches nothing, and invented a `## Why it is different` section |

Targets: a private Laravel marketplace, a public stdlib-Python CLI, a synthetic legacy repo, a synthetic
monorepo. Deliberately different stacks — "stack-neutral" was an untested claim.

## What each defect was

**Ratification granularity.** "The owner ratifies it" didn't say *row or file*. Two of three `git mv`'d a
whole draft into `prd/` on one approved row, promoting every other requirement in it. Now stated, plus a
stop-and-ask.

**`ADOPT` left a prior docs system in place**, producing two homes for one fact — invisible to a linter
never told the old directory exists. And it had agents **author the component ontology silently**, each
picking differently, though `prd/README.md` says it's the owner's call. Both are now steps.

**The `MEMORY` duty never fired.** Two agents hit a real guard, worked around it, wrote nothing. Cause was
chicken-and-egg: the always-loaded line said "hit friction → add a line", while *what counts* lived in the
edit-gated guide. Three rounds of strengthening reached 1/2. **Logged as a negative result:** this duty
can't be carried by prose — it asks an agent to notice mid-task and act later. An empty `MEMORY.md` is not
evidence a codebase has no traps.

**`docs-agents` only described the greenfield case.** Ship-as-written was enforced by intent, not
definition. The ✅/❌ example was hedged "where it helps", so nobody wrote one. And **reconciling an
existing rulebook wasn't covered at all** — the commonest case — losing a Testing section that bound new
commands to specific suites.

**Authorization had no home.** "Authorize in the Policy via the Form Request" covers only actions with
input; a pause button has none, so an agent shipped two unauthorized admin routes — matching a codebase
that authorizes nowhere. Generalised: *a rule routing an obligation through a mechanism must say what
happens without it*, and critical obligations are written "no exceptions" first, *how* second.

**The overview drew arrows that didn't exist**, disproved against the models in minutes. A written diagram
can be wrong in a way a generated one can't, and nobody proofreads a picture. Then a cold reader proved it
**didn't stand alone** — no revenue model, no industry — and, once fixed, that it **named two things it
never showed**.

**The migration manufactured green contracts.** Its step 7 said to copy each old `Tests`-table row to a ✅
plus the test name. That table was never enforced, so the run produced verified rows naming tests that
don't exist. Now: open the test first, or mark the row unproven.

**A disclaimer with no scale is not disclosure.** The framing line worked — two cold readers, given only the
overview, both said unprompted that the platform was not proven and that the document had told them so, and
one said outright he would not have felt misled. Then both asked for the thing the guide forbids: a build
status column. The line said *some of this may not exist* without saying *how much*, which covers five per
cent and ninety-five equally. Both readers had already worked it out for themselves — from the link
targets, every one of them pointing into `prd-drafts/`. The fix was to state what they inferred: name the
two homes, `prd/` ratified and `prd-drafts/` proposed. It is where a file sits, not a build state, so
nothing has to be maintained and nothing can go stale. A third agent, writing an overview from scratch with
no knowledge of the cold reads, invented the same sentence unprompted.

**Renumbering survived contact, because the guide made the sweep part of the change.** Erasing a
requirement re-points every citation at or after it, and nothing catches it: the ID still resolves, the
lint still passes, the reader gets a confident wrong answer. Two agents, given only the owner's sentence,
both erased the row, renumbered, and swept `app/`, `tests/` and the roadmap — and both found citations that
were *already* pointing at the wrong requirement before they started, which a naive shift would have
buried. Both stopped at the code default rather than guessing what replaced it. The rule that did the work
was making the sweep the same change rather than a follow-up: **an obligation phrased as "then also update"
is one an agent finishes without.**

**The overview guide survives another vendor — its structure does, anyway.** Run cold on codex, grok and a
separate claude process, all three produced the framing line *with* the `prd/`-versus-drafts split, a
`What you use` section, no build status and no banned vocabulary, and all three linted clean. The split had
been written hours earlier and no file in the repo demonstrated it, so all three took it from the guide
text alone. Grok independently described recovery correctly as a re-clear — a point the repo's own
hand-written prose had wrong at the time.

**What did not survive was the judgement.** Codex omitted the audience that touches nothing, which the
guide asks for in a sentence, and added a `## Why it is different` positioning section, which the guide
never sanctions. Neither is lintable today, and neither is a misreading — they are the two places the guide
asks for taste rather than structure. **The rules that held were the ones with a shape a reader can copy;
the rules that slipped were the ones phrased as advice.** `prd/` closes its schema and the linter enforces
it; `OVERVIEW.md` does neither, and a section a model invented is what that costs.

**Agents copy the neighbours, not the guide.** Both agents writing a new contract opened with
`*(Proposed — not built.)*` in `What this is` — prose the guide explicitly routes away ("Say it isn't
built → the ❌ already says it"). Neither misread the rule; both had read eight sibling files that did it,
and imitation beat instruction. **A rule the shipped examples violate is not a rule.** The lesson is not a
stronger sentence in the guide — it is that conformance work on existing files is what makes the guide
enforceable, because every file in a repo is a prompt.

## The pattern worth carrying

Four separate duties failed the same way: **a statement is not a gate.** "Finish by diffing", "state what
you inferred", "record friction" — each was a sentence, each was skipped, each left no trace. Every one
started working when it became a step with an artifact someone hands over. If it must happen, it's a step.

## Coverage

| Guide | Exercised | Note |
|---|---|---|
| `docs-prd` | 3 runs, 8 tasks | Most tested, most linted |
| `docs-agents` | Written twice, revised, reconciled twice, head-to-head, 3 coding runs | |
| `docs-codemap` | Written 4×, incl. a monorepo | Maps by layer across workspaces |
| `docs-brief` | Written 4×, incl. a 3-line README | |
| `docs-overview` | 4 runs, 2 audits, 2 cold reads | Written not generated — an audit is mandatory |
| `docs-memory` | 6 runs | **The one that still fails** |
| `ADOPT` + upgrade | 4 adoptions incl. from GitHub, 1 migration | |

## Known limits

- **Research is verified for shape, not truth.** Cited URLs resolve; nobody has checked a source supports
  the claim it's attached to. That check would have caught a vacated regulation still written as current.
- Every coding test was a short task. Conventions break at hour three, not hour one.
- `MEMORY.md` is best-effort. Reliable capture needs a harness hook the payload can't ship.
- A full adoption takes **over ten minutes** of agent time. Budget for it.
