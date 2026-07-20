# Agent tests

The guides in `template/.knowledge/guides/` are prompts. Prompts are not verified by reading them — they
are verified by giving a real agent a real task and checking what it actually did. This file logs every
such run: what was tested, with which agent, and what broke.

**The linter's rules are proven separately** by `scripts/test_doc_lint.py` (mutation cases, run in CI). This
file covers the other half: the parts of the standard no linter can check, where the only evidence is an
agent's behaviour.

## How to run one

1. Copy a target repo's `AGENTS.md` + `.knowledge/` into a scratch directory and `git init` it, so nothing
   real is touched and the diff is the result.
2. Give the agent a task in the owner's words. Never hint at the convention being tested.
3. Read the diff against the guide. **A green lint is not a pass** — most of what these guides ask for is
   not lintable, which is the reason for testing this way.
4. Log the run below, including the runs that found nothing.

Use more than one agent. Every defect found so far came from **two agents disagreeing** — where they agreed,
they were right, and where they split, the guide was ambiguous.

## Runs

| Date | Under test | Task given | Agents | Result | Defect found |
|---|---|---|---|---|---|
| 2026-07-19 | `docs-prd` | Describe the doc workflow for a new guaranteed behavior (read-only) | Claude Code, Codex, Grok | **3/3 correct** — placement ladder, namespace, next ID, draft-not-contract, ✅ needs a named test, the gate | none |
| 2026-07-19 | `docs-prd` | Actually record a claim the owner ratified | Claude Code, Codex, Grok | **1/3 correct** — two graduated the whole draft into `prd/` on one ratified row | **Ratification granularity** |
| 2026-07-19 | `docs-prd` (after fix) | Same task, corrected wording | Codex, Grok | **2/2 correct** — both left it a draft and said why | — |
| 2026-07-19 | `ADOPT.md`, `docs-agents`, `docs-brief`, `docs-codemap`, `docs-memory` | Cold-adopt the system into a repo that had never seen it | Claude Code, Codex | **2/2 green lint**, real layer maps with counts, ship-as-written intact | **Two `ADOPT.md` defects** |
| 2026-07-19 | `ADOPT.md` (after fix) | Same cold adoption | Codex | **Correct** — migrated and deleted the old docs home, stopped to ask before declaring the ontology | — |
| 2026-07-19 | `docs-memory` | Add a small feature to a repo whose test suite refuses to start without an undocumented env var. Docs never mentioned | Claude Code, Codex | **0/2 recorded it** — both hit the guard, both worked around it, both left `MEMORY.md` empty | **The friction duty never fires** |
| 2026-07-19 | `docs-memory` (after fix) | Same task, concrete trigger in the always-loaded duty | Claude Code, Codex | **1/2 recorded it.** Codex's entry is textbook; Claude recognised the friction as "worth knowing" but put it in its reply, not the file | **Recognition fired, destination didn't** |
| 2026-07-19 | `docs-memory` (after 2nd fix) | Same task, plus a *Definition of done* criterion: friction is in the file or you say you hit none | Claude Code | **Still 0/1.** Made the explicit "no friction" claim once, wrote nothing | Routing still fails |
| 2026-07-19 | `docs-memory` (after 3rd fix) | Same task, plus "write it the moment you find the workaround, not at the end" | Claude Code | **Still 0/1** | **Prose alone does not fix this** |
| 2026-07-19 | `docs-agents` | Audit the two cold-adopted `AGENTS.md` against the boundos yardstick | — | **Ship-as-written survived 1/2**; **0/2 wrote a ✅/❌ pair**; **1/2 silently dropped existing rules**, including a credential-permission rule | Three `docs-agents` defects |
| 2026-07-19 | `docs-agents` (after fix) | Cold adoption again | Claude Code | **✅/❌ pairs 0 → 2** (yardstick: 2); Hard gates verbatim with a separate project section; original rules preserved | — |
| 2026-07-19 | `docs-agents` (head-to-head) | Delete a refined real-world `AGENTS.md`, have an agent rewrite it from the guide, diff against the original | Claude Code | **Sections 10/10 identical.** **10/15 rules independently reproduced** — and all 5 misses were rules not derivable from code | **Research can't surface owner rules** |
| 2026-07-19 | `docs-agents` (revision path) | "Revise AGENTS.md: every new Vue component ships with a Vitest test" — on a repo with the new edit gate | Claude Code | **Conformed** — landed in *Best practices*, added a ✅/❌ pair (2 → 3), ship-as-written untouched, +7 lines | none |
| 2026-07-19 | `docs-brief`, `docs-codemap` | Cold-adopt a repo whose README was cut to 3 lines — the case where nothing is written down | Claude Code | CODEMAP **pass** (99 lines, real layers, artifact counts). BRIEF content good but **it never said what it inferred** | Disclosure wasn't a gate |
| 2026-07-19 | `docs-brief` (after fix) | Same thin-README adoption | Claude Code | **Pass** — split sourced vs inferred unprompted, flagged Users/ICP and the refusals as owner knowledge, quoted its inferred *Why it exists* for checking | — |
| 2026-07-19 | `docs-overview` | Write the platform overview for a real product, from the guide alone | Claude Code | Diagram grouped by component, 15 nodes | **3 arrows that don't exist** |
| 2026-07-19 | `docs-overview` (audit) | Second agent audits it adversarially against the models | Claude Code | **FAIL** — proved `Agreement` keys off `Participant`, never `Source`/`BuyerProfile`; unbuilt work shown as shipped | Two guide gaps |
| 2026-07-19 | `docs-overview` (after fixes) | Rewrite with evidence-per-arrow, non-technical vocabulary, build states | Claude Code | Arrows corrected; plain-language groups; `·planned` marked | Binary build state |
| 2026-07-19 | `docs-overview` (2nd audit) | Re-audit | Claude Code | Arrows **PASS**, language **PASS**, no duplication **PASS**; **FAIL** on marking | **Binary Built/Not-built lies** |
| 2026-07-19 | `AGENTS.md` rules (coding) | Build a full-stack admin feature end to end — the first non-documentation task | Claude Code, Codex | **Zero violations** of the *Never* rules; doc duties fired mid-code; **1/2 shipped an unauthorized state-changing route** | **Authorization had no home** |
| 2026-07-19 | `AGENTS.md` rules (after fixes) | Same full-stack task, corrected rules | Claude Code | **Pass** — Policy created and `$this->authorize()` called on both actions; `cursor-pointer` present; input-less action uses `router.patch(route(…))` | — |
| 2026-07-19 | `docs-research` | Write a research note answering a market question | Claude Code | **Pass** — closed schema, sourcing at point of claim; **14/15 cited URLs return 200**, the 15th bot-blocked (403), none fabricated | none |

Targets: a private Laravel marketplace app (25 drafts, 8 research notes) and a public standard-library
Python CLI. The Python CLI was chosen deliberately — before it, the payload had only ever met a web app and
a Markdown repo, so "stack-neutral" was an untested claim.

## What each defect was

**Ratification granularity.** The standard said a draft graduates when "the owner ratifies" it, without
saying whether that means a row or the file. Given one ratified claim inside a draft, two of three agents
`git mv`'d the entire file into `prd/` — silently promoting every *other* requirement in it into the source
of truth on the owner's authority. One agent caught it and stopped to ask. Fixed by stating the granularity
and adding it to *Stop and ask*; on re-run, all agents left the file where it was. **Lesson, now law in
this repo's `AGENTS.md`: when prose assigns authority, say over what unit. Ambiguous authority is worse
than an ambiguous rule.**

**`ADOPT.md` left a pre-existing docs system in place.** The target already kept agent docs in another
directory. Both agents adopted *alongside* it and left it, producing two homes for the same facts — the one
failure this system exists to prevent, and invisible to a linter that was never told the old directory
exists. `ADOPT.md` now has a step for folding in and deleting a prior docs home.

**`ADOPT.md` had agents author the component ontology silently.** `prd/README.md` says the components are
the owner's call and "an agent stops and asks", while `ADOPT.md` told the agent to declare them. Both agents
picked one without asking — and picked *differently*. Since IDs are permanent, a guessed ontology is the
hardest thing in the system to undo. `ADOPT.md` now requires proposing them and getting sign-off.

**The `MEMORY.md` duty did not fire at all.** Two agents hit a real guard, discovered the workaround, used
it, finished the task — and wrote nothing down. The cause was a chicken-and-egg: the always-loaded rule said
only *"Hit friction -> add a line"*, while the definition of what **counts** as friction lived in
`docs-memory.md`, which is edit-gated and therefore only read *after* an agent has already decided something
is friction. The trigger is now concrete in the always-loaded line ("anything that cost you a failed
attempt: an env var you had to discover, a guard you had to satisfy…"), and `docs-memory.md` states the test
plainly: *did it cost you an attempt?*

That fixed recognition but not routing: one agent named the friction as "worth knowing" **in its reply** and
still left the file untouched. Two further rounds followed — a *Definition of done* criterion ("friction is
in the file, or say plainly you hit none; telling the human doesn't count"), then a timing instruction
("write it the moment you find the workaround, not at the end"). **Neither worked.** Across four runs one
agent complies reliably and the other never wrote an entry, on a task where it demonstrably hit the guard,
worked around it, and reported the workaround in prose.

**Conclusion, recorded as a negative result: this duty cannot be carried by prose alone.** Every other rule
in this system is either lintable or a judgment made *while writing a doc* — this one asks an agent to
notice something mid-task and act on it later, and that is the one thing the always-loaded file cannot
reliably buy. The improved wording is kept because it moved one agent from silence to a textbook entry and
costs nothing, but a project that genuinely needs friction captured should drive it from its **harness**
(an end-of-task hook that asks the question), not from `AGENTS.md`. That is per-harness, so the payload
cannot ship it.

**Treat `MEMORY.md` as best-effort.** An empty `MEMORY.md` is not evidence that a codebase has no traps.

**A postscript worth keeping.** The fix itself shipped a bug: the completion criterion read *"friction is
in the file — or you say plainly you hit none"*, immediately followed by *"telling the human doesn't
count"*, which leaves "none" nowhere to go but the file. It would have turned `MEMORY.md` into a
changelog of non-events. No agent did it, and no lint could have caught it — the owner caught it reading
the line. **That is the third authority-shaped ambiguity in this log** (ratification granularity, the
component ontology, this). When a rule says *do X or else Y*, name where Y goes.

**`docs-agents` only described the greenfield case.** The guide said "Copy this. Fill every
`<placeholder>`" and stopped — so three things went untested and two went wrong. (1) *Ship-as-written* was
enforced by intent, not by definition: one agent kept the blocks byte-identical, the other enriched the
bullets in place with project detail, destroying the cross-repo comparability the rule exists to protect.
The rule now states the test — every shipped line present, unmodified, in order — and explicitly permits
appending project lines below them. (2) The `✅`/`❌` example was hedged as "where it helps"; neither agent
produced one, on a repo whose *existing* file already had a good one. Now every code-shape area carries a
pair, with a fenced slot in the template. (3) **The guide never covered adopting into a repo that already
has an `AGENTS.md`** — the commonest case. One agent reconciled and extended; the other rewrote from
scratch and silently lost real rules, including the one setting credential file permissions. A new
*The repo already has an `AGENTS.md`* section makes reconciliation the rule and forbids dropping anything
silently. A *Changing it later* section closes the last gap: `docs-memory.md` graduates hardened traps into
`AGENTS.md`, and nothing on this side ever said so.

**The head-to-head is the strongest evidence in this log, and its misses are the interesting part.** Given
the same repo with its `AGENTS.md` deleted, an agent rebuilt the section structure exactly — all ten, same
order — and independently found ten of fifteen real rules: the tenancy split, both migration homes, the
`ui/app/site` tiers, `useForm`, `route()`, `strict_types`, the gate command, the static-analysis level.

The five it missed were **not failures of research**. `env()` outside `config/` appears **zero times** in
that codebase, so the ban leaves no trace to find. `app/Policies/` holds **zero classes**, so the
authorization rule describes an intended pattern with nothing to discover. The rest — who runs the UI, no
legacy fallbacks, no backend/frontend drift — are workflow and taste, which are not in code at all.

**A codebase cannot tell you the rules it already obeys, the rules it has not implemented yet, or the
rules that are about people.** The guide now ends its procedure by requiring the agent to name those gaps
and ask, instead of shipping a file that looks complete. It also gained a length signal: the rewrite ran
248 lines against the original's 155, and long rulebooks stop being reread.

**`AGENTS.md` had no edit gate.** The orientation trio each end with *"Editing this file? Follow the
standard first"* — that pointer is the whole reason an agent reads a guide before rewriting a doc.
`AGENTS.md` carried no such line, and `.knowledge/README.md`'s homes table had no row for it (reasonably —
it lives at the repo root). So the one file that is the law of the project was also the one document that
could be rewritten without ever opening its own standard. It now ends with the same pointer, the map has a
row for it, and `doc-lint` checks it — the third of the three deliberately shallow `AGENTS.md` checks.

Verified on the revision path rather than assumed: asked to add a new rule, an agent put it in *Best
practices*, wrote it as a Do/Don't **with a ✅/❌ pair** in the project's own paths, left every
ship-as-written section byte-identical, and grew the file by seven lines.

**`docs-brief.md` had no discovery method at all** — no mention of read, research, find, README, ask or
owner — while being the doc whose content is *least* present in code. Story, users and refusals are not in
a repo. The earlier adoptions produced good briefs only because that repo had a rich README; cut it to
three lines and an agent is left to infer a market from a schema, which is the worst failure available
here: a brief that reads as confident, is quietly wrong, and is loaded on every task afterwards while
nobody re-checks it. The guide now ranks where the answers actually live and says the code is evidence of
what was built, never of who it is for.

The disclosure step then taught the lesson twice. Written as *"state plainly what you inferred"* it did
**not** fire — the same agent that dutifully stopped for sign-off on the component ontology reported the
brief as "verified against the code". The ontology ask worked because `ADOPT.md` makes it a **step with
explicit sign-off**; the brief's was a soft sentence in a guide. Moved into `ADOPT.md` step 4 as a required
step, it fired immediately and correctly. **A statement is not a gate — if it must happen, it is a step.**

`docs-codemap.md`'s method was sound but began at "the framework and top-level folders". It now names the
five highest-signal artifacts to read first — manifest, entry points, routing/wiring config, test layout,
build scripts — because a folder tree misleads on any repo that departs from its framework's defaults.

**`docs-overview` is the guide most shaped by testing, because a written diagram can be *wrong*.** A
generated map cannot claim a false relationship; a hand-drawn one can, and nobody proofreads a picture. The
first draft drew three arrows that did not exist — an auditing agent disproved them against the models in
minutes. The guide now requires naming the evidence for every arrow before drawing it.

The second audit failed the file on something that was **my** defect, not the writer's: the guide offered
only *Built* and *Not built yet*, so a component whose core exists but whose lifecycle does not was
presented as shipped — eight of its eleven requirements unmet, drawn as a solid box. Three states now, and
"partly built" is only honest when it names which part. Binary status marking is how a roadmap becomes a
lie.

Audience was the third correction, and it came from the owner rather than a test: the first drafts were
written in protocol vocabulary — `FORM_POST`, `TTL`, `clamp` — which is useless to the product and
marketing readers this doc exists for. The guide now bans implementation vocabulary outright and gives the
test: could a marketer read it aloud on a customer call without stopping. The re-audit passed on language.

**The first coding test, and the *Never* rules held completely** — no inline validation, no inline
`abort(403)`, no `env()` outside config, no stray `console.log`, no hardcoded URLs, from either agent. Both
also wrote `declare(strict_types=1)`, injected dependencies, kept controllers thin, and cited the
requirement ID in a doc-block. The documentation duties fired *during code*: both updated `CODEMAP.md` and
the relevant draft unprompted, one wrote to `MEMORY.md`.

The failure was in a *Do* rule, and it was phrasing. **"Authorize in the Policy via the Form Request"**
covers only actions that take input. Pause/resume takes none, so there is no Form Request — and one agent
shipped two state-changing admin endpoints with **no authorization at all**, faithfully copying a codebase
whose existing admin controllers also authorize nowhere. The other agent independently wrote a Policy and
authorized properly. Same rules, opposite outcomes, because the rule was a mechanism rather than an
obligation.

**Generalised into the guide, because it is not a Laravel problem:** a rule that routes an obligation
through a mechanism must say what happens when the mechanism is absent, and critical obligations get
"no exceptions" first, *how* second. Also logged: the one styling rule stated only in prose was missed by
**both** agents, while every gate-enforced rule was followed — so a checkable rule belongs in the gate or
inside a `✅`/`❌` example, never in a bullet list alone.

## Coverage

| Guide | Exercised by an agent | Notes |
|---|---|---|
| `docs-prd.md` | Yes — 3 runs, 8 agent-tasks | The most tested, and the most linted |
| `docs-agents.md` | Yes — written from scratch, twice | Ship-as-written sections survived verbatim both times |
| `docs-codemap.md` | Yes — written from scratch, twice | Both produced real layers with counts, not the shipped skeleton |
| `docs-brief.md` | Yes — written from scratch, twice | |
| `docs-memory.md` | Yes — 6 runs against planted friction | **The only guide that still fails.** Reliable for one agent, never fired for the other |
| `docs-research.md` | Yes — one note written and its sources verified | |
| `docs-overview.md` | Yes — 4 runs, two adversarial audits | Written, not generated, so it is the one guide where an audit is mandatory |

## Known limits of this evidence

- Every task so far has been a **documentation** task. No run has tested whether an agent still follows
  these conventions at hour three of writing application code, which is when conventions actually break.
- The adoption runs used a repo the agent could read in full. A large codebase may defeat `CODEMAP.md`'s
  "survey it layer by layer" instruction in a way a small one cannot.
- The friction used was *planted*. It was real and non-obvious, but an agent meeting a trap it half-expects
  is not the same as one meeting a surprise at hour three.
