# math-io — agent operating guide

This is a math-io workspace, owned by the person named in `project.toml` (`[project] owner`;
"the owner" below) and worked on by AI agents under the owner's direction. Read this file
first in every session. It is short on purpose: each rule here names the moment it applies,
and the longer reasoning lives in [docs/discipline/](docs/discipline/README.md), which you open
when that moment comes. Words with a specific meaning here are defined in
[GLOSSARY.md](GLOSSARY.md); look a term up rather than guessing: `bin/glossary <term>` prints just its entry. If you know an idea but not
this project's word for it, check [SEARCH-ALIASES.md](SEARCH-ALIASES.md).

The **coordinator** is the main session, the one talking to the owner; an agent dispatched by
another agent never is. The coordinator's own rules are in
[COORDINATOR.md](COORDINATOR.md), which a hook adds to the main session's context at its start
and after each summary. If you are the coordinator and those rules are not in your context,
read COORDINATOR.md before your first action. If your brief says you are a worker, see the
worker agent file and [docs/discipline/tiers.md](docs/discipline/tiers.md); "brick", "strong tier", "worker tier" and
"long job" are defined in [GLOSSARY.md](GLOSSARY.md).

## Ground rules

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
- **Some decisions belong to the owner alone** (the list is in COORDINATOR.md). A dispatched agent
  never makes one and never edits a record to do so; it reports, and the coordinator proposes.
- **Report what is true, at the scope the evidence supports.** A result measured on one
  family is a conjecture about other families. A finite computation is evidence, not a
  proof. "Done" means verified: name the check you ran.
- **The owner's statements and framings are claims too.** Test them like any other, and report
  evidence against one plainly and early. Against an informal idea, weigh the evidence; it
  rarely refutes outright.
- This project is set up for **Claude Code**. Agents are in `.claude/agents/`, skills in
  `.claude/skills/`, hook registrations in `.claude/settings.json`.

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

## Literature wiki

- Sources live in `wiki/`: `raw/` (immutable copies), `inbox/` (still to read),
  `concepts/` and `references/` (our synthesis). Read a folder's `_index.md` before
  scanning it, and append each operation to `wiki/log.md`.
- Why and how: [docs/discipline/literature-wiki.md](docs/discipline/literature-wiki.md).

## Review gates

- An argument that convinces but is not a proof is an **argued claim**: labelled, evidence and never a result. Write it with [docs/templates/informal-argument.md](docs/templates/informal-argument.md).

## Firsthand checks

- A claim that decides work or enters a record gets one check of your own first: read a cited theorem yourself; search the whole library by name before saying it lacks something; scout before calling a task too hard.
- Never say "recorded" unless the write happened.

Rules: [docs/discipline/firsthand-checks.md](docs/discipline/firsthand-checks.md).

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

