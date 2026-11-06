---
name: getting-started
description: Walk the owner through the first session in this workspace, one step at a time, instead of having them read docs/OWNER.md — the self-check, the four things they can ask for (verify, review a draft, guided reading, write), where their documents go, and how working with the agents goes. Load it when the owner asks to get started, asks what to do first, or seems unsure how to begin.
---

# Getting started

The owner has just set up this workspace, or is coming back to it unsure where to begin.
Walk them through the first session, using `docs/OWNER.md` ("Day one" and "Later, when
needed") as your source, so they do not have to read it themselves.

How to walk them through it:

- **One step at a time.** Say what the step is and why it matters in two or three
  sentences, do the part that is yours, and wait for the owner's answer before the next
  step.
- **Plain words.** The owner is a mathematician who may be new to agents and terminals.
  Explain a term from `GLOSSARY.md` the first time it comes up, in one sentence.
- **Their decisions stay theirs.** You may explain, propose and do the steps they agree
  to.
- Skip any step that is already done, and say so in one line.

## 1. Check the setup

First run `bin/doctor`. It checks the live session, not the files: that this session
started in the project's own folder, that the project's hooks (its automatic checks) ran
for that very command, and, once there are any, that subagents run as the project's own agents.
For each FAIL, tell the owner in plain words what is not loaded and how to fix it (each
line says how), and stop here until it passes: work done in a session that fails it runs
without the project's reviewers, checks and settings, and nothing else would tell them.
If the owner tells you to go on anyway (the check may misfire on an unusual folder
arrangement), go on, but first say which protections are missing, one per FAIL line, and
log the failure as a setup problem (`bin/journal --add friction "doctor FAIL, continued on the owner's say-so: <the FAIL lines>"`).
Typical fixes: start the agent again from the project folder (in a terminal, `cd` into it
first; in VS Code, File > Open Folder… and choose the project folder itself, not a folder
above it); on Windows, from Ubuntu rather than the Windows side. If the project's path starts with
`/mnt/`, it is on the Windows drive, where it runs slowly; mention that moving it into the
Linux home folder helps.

Run `bin/selftest`. If every line says PASS, tell them the setup is healthy in one
sentence. If a line says FAIL, run `bin/selftest -v`, explain what is broken, and offer to
fix it before going on.

## 2. What they can ask for

Name the four things this workspace is for, one line each, with how to start each one
(they can also just say it in plain words):

- **Verify** (`/verify`): check a proof, a section or a whole paper; every verdict comes from
  a separate reviewer and goes into the document's check record, and a whole paper can be
  checked unattended, ending in a report.
- **Review a draft** (`/review-draft`): feedback on their own draft or a colleague's, written
  for its author in `review.md`.
- **Guided reading** (`/guided-reading`): work through a paper or a chapter at their pace,
  picking up where the last sitting stopped.
- **Write** (`/write`): drafts, notes or an exposition in LaTeX, built into a PDF, with each
  proof reviewed before it is committed.

## 3. Where their documents go

Explain in a few sentences: each document gets a folder (`documents/<slug>/`, made with
`bin/doc new`, or by asking you); someone else's text goes in its `source/` and is
committed, so **the workspace should only ever be pushed to a private repository**, never a
public one (`docs/OWNER.md`, "Your documents"). Offer to set up a folder for something they
want to work on now.

## 4. How the work goes from here

In a few sentences, explain what a working session looks like:

- The owner says what they want; you propose a concrete step and say what it is for
  before doing anything long.
- Before a verdict or a proof is recorded, separate reviewer agents check it; you never mark
  something correct on your own reading.
- What only the owner does: accepting a check record, setting priorities, and approving the
  changes to the setup that the reflection loop asks about (`docs/OWNER.md`, "What only
  you do").
- When something in the setup gets in their way, they can just say so: you log it
  (the `friction` skill), and the `reflect` skill later turns recurring problems into
  fixes. Any reminder that annoys them can be switched off (`docs/OWNER.md`, "Switching
  off a nudge").
- Coming back another day: open a terminal, `cd` into this folder, start the agent, and
  ask where things stand. The files hold the state; nothing depends on this session.

Ask whether they have questions about any of it.

## 5. Things that can wait

From "Later, when needed" in `docs/OWNER.md`, mention only the items that apply to this
project, in one line each, and offer to do any of them now:
- their own papers and a model text for the write-up reviewers
  (`docs/discipline/exposition.md`), if they will write;
- `bin/setup` in any new copy (clone) of this repository;
- the models and what they cost (`docs/OWNER.md`, "Models" and "What this costs").

## 6. First real step

Ask what they would like to work on first, propose one concrete step, and wait for their
go-ahead before starting.
