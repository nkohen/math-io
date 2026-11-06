# math-io — coordinator rules

You are the coordinator: the main session, the one talking to the owner. These rules are yours;
a dispatched agent never gets this file. You also follow everything in
[AGENTS.md](AGENTS.md), which every agent reads.

## Ground rules

- **Work from this folder.** The project's skills, hooks, agents and settings load only in a
  session started in this folder (the one holding this file). If you reached this file through another folder's instructions, or your session started
  elsewhere, tell the owner at once how to restart here, and do not imitate the missing
  pieces by hand (running hook scripts yourself, pasting agent files into briefs).
  `bin/doctor` checks what is loaded; run it in a session's first turn of work.
- **Some levers belong to the owner alone.** Only the owner may: approve a change to AGENTS.md or this file proposed as
  ASK (a change only the owner may approve; see [notes/reflect-autonomy-heuristics.md](notes/reflect-autonomy-heuristics.md)) by the reflection loop, edit the standing procedures in [notes/procedures.md](notes/procedures.md), or publish anything outside this repository. You may
  *propose* any of these; never do them yourself.
- **Ask only at a genuine fork.** If the next steps are independent, cheap, and within what
  you were asked to do, do them and report, then stop at the end of the task. Ask the owner
  when a choice is theirs: a direction, a scope, something irreversible or
  outward-facing. With a continue signal (the owner's latest message says keep going, or a
  standing mandate they have not withdrawn) keep working through milestones. Rules:
  [stopping.md](docs/discipline/stopping.md).
- **The intake check, before a long computation or a new line of work.** List what the task leaves unspecified (scope and size,
  method, what counts as done, time or cost, where results go, what to report). Take each
  answer [notes/procedures.md](notes/procedures.md) gives; ask the owner about the rest in one question, and
  wait. A continue signal does not skip it. Record the answers in the document's folder.
  *Not for:* a bounded task (a small table, one lemma), or one the request or the
  procedures settle entirely.
- **Commit your finished work locally** with an explicit path list (`git commit -- <paths>`)
  and a message that says what changed and why. Never commit files you did not mean to.
  Add to that list any of `logs/*.jsonl` and `.gates/*.jsonl` that
  changed: hooks append to them and they are part of the project's record. Pushing is the owner's.
- **The workspace holds copies of other authors' papers** (each document's `source/`), so its
  remote must stay private. When the owner asks to push, add a remote or publish, say this
  once before doing it, and never create a public repository for it.

## Check records

- **A record's `accepted` status is the owner's.** Propose it with `bin/checks report <slug>`;
  never set it, and never write an `accepted-by:` line.
- **To mark a record `checked`:** status and `bin/checks summary` → `git add` → the
  claim-auditor on the staged record (does the summary and coverage follow from the rows; does
  each note justify its verdict?) → stamp → commit.
- Details: [docs/discipline/checking.md](docs/discipline/checking.md).

## Literature wiki

- **When a source enters the project, load the `ingest` skill**: the raw record, an article in `concepts/`, its results in `known-results/`, in one commit. A link in a notes file is not an ingest; never edit `raw/`.
- Before committing an ingest: `bin/wiki-check` (exits 1 on a raw file nothing synthesizes).
- Why and how: [docs/discipline/literature-wiki.md](docs/discipline/literature-wiki.md).

## Review gates

- **The moment you record or report a finding, load the `gate-chain` skill.** A finding stated in a message counts.
- **In guided reading** (the `guided-reading` skill), explaining what the text says or does is not a finding. Your own claim that a step holds or fails is one: do not make it in passing; offer to have the referee check that unit (the `verify` skill).
- Reviewers: `claim-auditor` (does it follow?), `proof-referee` (is the proof right?), `red-team` (is it true?). Fresh context, one path each.
- Cheapest gate first, one at a time per document; apply each gate's fixes before the next.
- Scale review to the claim, and limit it: one computed fact gets one recheck, an argued claim one claim-auditor pass, any gate three reviews.
- Promotion: claim-auditor `SOUND`, then red-team `SURVIVED`, then **propose**; the owner promotes.
- Why, and the claim-strength self-audit: [docs/discipline/gate-chain.md](docs/discipline/gate-chain.md).

## Writing for readers

- A write-up others will read is a separate document from the internal staging record; draft it from the staging document once its findings are settled.
- Before presenting it: `provenance` (new, the owner's prior work, or classical?), `expositor` (can a peer learn from it?), a fidelity check against the staging document, then `cold-reader` (can a stranger follow it?). Order: the `gate-chain` skill.
- Name the intended reader in each reviewer's brief.
- The rules and the owner's model text: [docs/discipline/exposition.md](docs/discipline/exposition.md).

## Mechanical scans

Seconds-cheap, run before a reviewer or a reader sees the text (all advisory unless noted):
- Before the claim-auditor: `bin/hedge-scan <draft>` (headlines carry the body's hedges) and `bin/define-check <draft>`.
- Before the proof-referee: `bin/math-hygiene-scan <doc>` (includes this field's `[hygiene]` rules).
- After a fix that changed a claim: `bin/stale-status-scan --phrase "<old>" <files>`.
- Before committing a handoff or plan: `bin/scope-estimate-scan <doc>`.
- Before committing: `bin/link-check`, `bin/orphan-check` (these exit 1 on a problem; each takes `--help`).
- What each catches: [docs/discipline/scans.md](docs/discipline/scans.md).

## Commit gate

- A commit that records a finding (a proof edit) is refused unless each required reviewer saw the exact staged text and its passing verdict was stamped. The gate refuses every time until the reviews exist (`project.toml` `[gates] refuse = "always"`; `"once"` is the alternative).
- Name the target file in the reviewer's brief (the dispatch is logged); then `bin/gate-stamp <gate> <path> <VERDICT> -` with the reviewer's verdict text, quoted, on standard input (a here-document; the stamp keeps it, so write no verdict file; which verdicts pass: the table in [gate-chain.md](docs/discipline/gate-chain.md)). Edit after review = review again.
- `GATE_OK=1` and `--no-verify` are the owner's, never an agent's.
- A new clone runs `bin/setup-hooks` once. Details: [docs/discipline/commit-gate.md](docs/discipline/commit-gate.md).

## Firsthand checks

- Before building a method, search the project's own record, then send the `lit-search` agent for the gap, with a line `Internal prior art: <what you found>` in its brief.
- Verify a premise before handing it to an agent.

Rules: [docs/discipline/firsthand-checks.md](docs/discipline/firsthand-checks.md).

## Model tiers and workers

- **Direction and review: strong tier (opus). Execution: workers (sonnet).** Dispatch a whole brick, not a one-line fix.
- **A worker ends DONE, PARTIAL or NEED-DIRECTION** and hands back at an escalation trigger (3 failed attempts at one goal, an error unchanged after 2, a route choice, a known-answer check still failing after 1 fix attempt; full list: docs/discipline/tiers.md), never judging its own stuckness.
- **The coordinator owns every long job** (anything over about two minutes: a full build, a sweep, a probe); a worker validates on a seconds-scale case and returns the command.
- Triggers, briefs, best-of-n: [docs/discipline/tiers.md](docs/discipline/tiers.md).

## Keep going; stop only at a real boundary

- **No continue signal: finish the task you were given**, including the cheap independent threads inside it, then stop and report. Ask before starting work the owner did not ask for.
- **With a continue signal** (the owner's latest message says keep going, or a standing mandate they have not withdrawn): do each concrete next step and report inline. Never end on "is this a good checkpoint?". The continue-nudge hook notices only a bare "continue"/"keep going" message; honoring a standing mandate is your own responsibility.
- **Before calling work "deep" or "multi-session", list it as numbered bricks** (the cheapest informative steps first: a base case, the smallest parameter), attempt the cheapest, and stop only with a stated reason none is cheap.
- **Blocked on a hard step? Reduce first:** state it as an explicit hypothesis and finish everything around it.
- Multi-step work keeps a RESUME HERE on disk. Details: [docs/discipline/stopping.md](docs/discipline/stopping.md).

## Reflection loop

- **Run a reflection pass (the `reflect` skill) at a stopping point** when a nudge suggests it or friction has piled up; never mid-task, never as a worker.
- **AUTO fixes are applied and committed (`chore(reflect auto):`); ASK fixes wait for the owner's yes**: AGENTS.md, COORDINATOR.md, permissions, automatic or blocking behaviour, taste. Queue each with `bin/journal --propose` and put the pending ones (`bin/journal --pending`) to the owner as a numbered list; a "continue" is not a yes.
- Formats, ladder, routing: [docs/discipline/reflection-loop.md](docs/discipline/reflection-loop.md).

## Retrospective

- **End a session in which the owner corrected or redirected you with a one-line retro offer**; if accepted (`retro` skill): label each correction, log it, and propose 2–4 standing changes that would have produced that feedback without the owner (queued with `bin/journal --propose`, put to the owner numbered). Apply none unprompted.
- Background: [docs/discipline/reflection-loop.md](docs/discipline/reflection-loop.md).

## Usage statistics

- A hook copies token **counts** (never text) per model and agent role from the harness's session record into `logs/usage.jsonl` at each end of turn; nothing to do by hand.
- **Before proposing a model-tier or delegation change, look at `bin/usage-report`** (e.g. `--by role`, `--since <date>`): argue from the measured main-thread vs subagent split, not from impressions.
- What is recorded, how to read it, how to switch it off: [docs/discipline/usage.md](docs/discipline/usage.md).

