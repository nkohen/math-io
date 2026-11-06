# math-io — agent operating guide

This is a math-io workspace, owned by the person named in `project.toml` (`[project] owner`;
"the owner" below) and worked on by AI agents under the owner's direction. Read this file
first in every session. It is short on purpose: each rule here names the moment it applies,
and the longer reasoning lives in [docs/discipline/](docs/discipline/README.md), which you open
when that moment comes. Words with a specific meaning here are defined in
[GLOSSARY.md](GLOSSARY.md); look a term up rather than guessing: `bin/glossary <term>` prints just its entry. If you know an idea but not
this project's word for it, check [SEARCH-ALIASES.md](SEARCH-ALIASES.md).

You are the coordinator unless your brief says you are a worker (see the worker agent file and
[docs/discipline/tiers.md](docs/discipline/tiers.md)). "Brick", "strong tier", "worker tier" and "long job" are defined in
[GLOSSARY.md](GLOSSARY.md).

## Ground rules

- **Work from this folder.** The project's skills, hooks, agents and settings load only in a
  session started in this folder (the one holding this file), trusted, with its hooks trusted via
  `/hooks`. If you reached this file through another folder's instructions, or your session started
  elsewhere, tell the owner at once how to restart here, and do not imitate the missing
  pieces by hand (running hook scripts yourself, pasting agent files into briefs).
  `bin/doctor` checks what is loaded; run it in a session's first turn of work.
- **Durable state lives on disk, never only in your context.** Results, checks, decisions
  and progress logs are files in this repository. Your
  context window is scratch: it may be summarized or reset at any time. Before you hold a
  decision in your head across steps, write it down where the next session will find it.
- **Every working file has a home: the document it serves.** Each document you verify,
  review, read or write has a folder, `documents/<slug>/` (made with `bin/doc new`), holding
  its `document.toml`, its README (plan, RESUME HERE, outcome), text someone else wrote in
  `source/` (never edited), your own writing at its top, and briefs and throwaway files
  (never a manuscript) in `scratch/`, which git ignores. `notes/` is only for standing notes
  on how the workspace works. Details: [documents.md](docs/discipline/documents.md).
- **Some levers belong to the owner alone.** Only the owner may: approve a change to this file proposed as
  ASK (a change only the owner may approve; see [notes/reflect-autonomy-heuristics.md](notes/reflect-autonomy-heuristics.md)) by the reflection loop, edit the standing procedures in [notes/procedures.md](notes/procedures.md), or publish anything outside this repository. You may
  *propose* any of these; never do them yourself.
- **Report what is true, at the scope the evidence supports.** A result measured on one
  family is a conjecture about other families. A finite computation is evidence, not a
  proof. "Done" means verified: name the check you ran.
- **The owner's statements and framings are claims too.** Test them like any other, and report
  evidence against one plainly and early. Against an informal idea, weigh the evidence; it
  rarely refutes outright.
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
- This project is set up for **Codex CLI**. Agents are in `.codex/agents/`, skills in
  `.agents/skills/`, hook registrations in `.codex/hooks.json` (trust them once with `/hooks`).

## Where things are

| Path | What it holds |
|---|---|
| `wiki/known-results/` | what the literature already proves |
| `wiki/raw/`, `wiki/inbox/`, `wiki/concepts/` | sources (never edited), sources not yet read, synthesized articles |
| `documents/` | one folder per document: `document.toml`, its README (plan, RESUME HERE, outcome), `source/` (text you did not write), your own writing, a git-ignored `scratch/`; `bin/doc list` lists them |
| `docs/discipline/` | the reasoning behind the rules below |
| `docs/OWNER.md` | the owner's manual: what only the owner does, and how to tune this setup |
| `notes/workflow-journal.md`, `logs/` | the reflection loop's record of friction and failures (`logs/*.jsonl` and `.gates/*.jsonl` are created on first use) |
| `project.toml` | the project's settings (stack commands, model tiers, gate policy) |
| `bin/` | the project's scripts; run `bin/selftest` after you change a hook or the settings |

## The four tasks

Each is a skill; load the one the owner's request matches (they may ask in plain words):
`verify` (check proofs and record what was found), `review-draft` (feedback on a draft, for
its author), `guided-reading` (help the owner read a text), `write` (the owner's own writing,
in LaTeX, built with `bin/pdf`).

## Checking a document

- What was checked, by whom, and what was found lives in the document's check record,
  `documents/<slug>/checks.md`, filled with `bin/checks`. Every verdict cites the
  proof-referee stamp behind it; the commit gate refuses one that does not match.
- Someone else's text is checked through unit files (`units/<id>.md`: Uses, Statement,
  Proof, word for word, nothing else); your own draft is reviewed as the draft file.
- `checked` means checked by reviewers, with what was found; `accepted` is the owner's.
- Rules, verdicts and the order: [docs/discipline/checking.md](docs/discipline/checking.md).

## Known results

- Before testing or proving anything, look up the object in `wiki/known-results/` (filed
  by object of study): it may already be settled.
- Record every result with its source, section or theorem number, and date accessed. A
  claim with no source you have read is a seed to verify, not a fact.
- Why and how: [docs/discipline/known-results.md](docs/discipline/known-results.md).

## Check records

- **A record's `accepted` status is the owner's.** Propose it with `bin/checks report <slug>`;
  never set it, and never write an `accepted-by:` line.
- **To mark a record `checked`:** status and `bin/checks summary` → `git add` → the
  claim-auditor on the staged record (does the summary and coverage follow from the rows; does
  each note justify its verdict?) → stamp → commit.
- Details: [docs/discipline/checking.md](docs/discipline/checking.md).

## Literature wiki

- Sources live in `wiki/`: `raw/` (immutable copies), `inbox/` (still to read),
  `concepts/` and `references/` (our synthesis). Read a folder's `_index.md` before
  scanning it, and append each operation to `wiki/log.md`.
- **When a source enters the project, load the `ingest` skill**: the raw record, an article in `concepts/`, its results in `known-results/`, in one commit. A link in a notes file is not an ingest; never edit `raw/`.
- Before committing an ingest: `bin/wiki-check` (exits 1 on a raw file nothing synthesizes).
- Why and how: [docs/discipline/literature-wiki.md](docs/discipline/literature-wiki.md).

## Review gates

- **The moment you record or report a finding, load the `gate-chain` skill.** A finding stated in a message counts.
- **In guided reading** (the `guided-reading` skill), explaining what the text says or does is not a finding. Your own claim that a step holds or fails is one: do not make it in passing; offer to have the referee check that unit (the `verify` skill).
- Reviewers: `claim-auditor` (does it follow?), `proof-referee` (is the proof right?), `red-team` (is it true?). Fresh context, one path each.
- Cheapest gate first, one at a time per document; apply each gate's fixes before the next.
- Scale review to the claim, and limit it: one computed fact gets one recheck, an argued claim one claim-auditor pass, any gate three reviews.
- An argument that convinces but is not a proof is an **argued claim**: labelled, evidence and never a result. Write it with [docs/templates/informal-argument.md](docs/templates/informal-argument.md).
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
- A claim that decides work or enters a record gets one check of your own first: read a cited theorem yourself; search the whole library by name before saying it lacks something; scout before calling a task too hard.
- Verify a premise before handing it to an agent. Never say "recorded" unless the write happened.

Rules: [docs/discipline/firsthand-checks.md](docs/discipline/firsthand-checks.md).

## Model tiers and workers

- **Direction and review: strong tier (gpt-6-astra). Execution: workers (gpt-6-luna).** Dispatch a whole brick, not a one-line fix.
- **A worker ends DONE, PARTIAL or NEED-DIRECTION** and hands back at an escalation trigger (3 failed attempts at one goal, an error unchanged after 2, a route choice, a known-answer check still failing after 1 fix attempt; full list: docs/discipline/tiers.md), never judging its own stuckness.
- **The coordinator owns every long job** (anything over about two minutes: a full build, a sweep, a probe); a worker validates on a seconds-scale case and returns the command.
- Triggers, briefs, best-of-n: [docs/discipline/tiers.md](docs/discipline/tiers.md).

## Keep going; stop only at a real boundary

- **No continue signal: finish the task you were given**, including the cheap independent threads inside it, then stop and report. Ask before starting work the owner did not ask for.
- **With a continue signal** (the owner's latest message says keep going, or a standing mandate they have not withdrawn): do each concrete next step and report inline. Never end on "is this a good checkpoint?". The continue-nudge hook notices only a bare "continue"/"keep going" message; honoring a standing mandate is your own responsibility.
- **Before calling work "deep" or "multi-session", list it as numbered bricks** (the cheapest informative steps first: a base case, the smallest parameter), attempt the cheapest, and stop only with a stated reason none is cheap.
- **Blocked on a hard step? Reduce first:** state it as an explicit hypothesis and finish everything around it.
- Multi-step work keeps a RESUME HERE on disk. Details: [docs/discipline/stopping.md](docs/discipline/stopping.md).

## Offline mode

- When `project.toml` says `[web] offline = true`, use no web search or fetch and download
  nothing (a hook refuses them; never work around it). Work from what the workspace holds,
  and mark a citation or attribution you could not check "not verified (offline)".
- Only the owner switches it (`bin/offline on|off`).

## Safety guard

- A hook refuses recursive deletes (`rm -r`, `find -delete`), a force push or delete of a main branch, and a download piped into a shell. Delete named files; write scratch into a fresh timestamped directory so nothing needs cleaning up.
- **`sudo` / `doas` and a world-writable `chmod` (777, 666, `o+w`) are the owner's steps.** When refused, do not retry or work around it: give the owner step-by-step instructions for only the steps they must perform (what each changes, its risk, how to undo it), then continue with what does not need them.
- **Never set `GATE_OK` or pass `--no-verify`**: those bypasses are the owner's. The hook refuses and logs the attempt.
- Stage exact paths, not `git add -A`; edit docs with the edit tool, not `sed -i`. Details: [docs/discipline/guard.md](docs/discipline/guard.md).

## Reflection loop

- **Log friction the turn you notice it** (a failed or repeated step, a wrong assumption, a misleading doc): `bin/journal --add friction "<one line>"`. A correction from the owner about how you work: `--add feedback … --kind correction`.
- **Run a reflection pass (the `reflect` skill) at a stopping point** when a nudge suggests it or friction has piled up; never mid-task, never as a worker.
- **AUTO fixes are applied and committed (`chore(reflect auto):`); ASK fixes wait for the owner's yes**: AGENTS.md, permissions, automatic or blocking behaviour, taste. Queue each with `bin/journal --propose` and put the pending ones (`bin/journal --pending`) to the owner as a numbered list; a "continue" is not a yes.
- Formats, ladder, routing: [docs/discipline/reflection-loop.md](docs/discipline/reflection-loop.md).

## Retrospective

- **End a session in which the owner corrected or redirected you with a one-line retro offer**; if accepted (`retro` skill): label each correction, log it, and propose 2–4 standing changes that would have produced that feedback without the owner (queued with `bin/journal --propose`, put to the owner numbered). Apply none unprompted.
- Background: [docs/discipline/reflection-loop.md](docs/discipline/reflection-loop.md).

## Usage statistics

- A hook copies token **counts** (never text) per model and agent role from the harness's session record into `logs/usage.jsonl` at each end of turn; nothing to do by hand.
- **Before proposing a model-tier or delegation change, look at `bin/usage-report`** (e.g. `--by role`, `--since <date>`): argue from the measured main-thread vs subagent split, not from impressions.
- What is recorded, how to read it, how to switch it off: [docs/discipline/usage.md](docs/discipline/usage.md).

