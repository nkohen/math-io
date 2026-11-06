# Owner's manual

This is for the owner, the person who directs math-io. The agents read
[AGENTS.md](../AGENTS.md); this page tells you what the setup expects of you and how to
change it when it gets in your way. Nothing here is fixed: the files are yours, and the
reflection loop exists so the setup changes as you learn what helps.

This workspace is a copy of math-io; updates to math-io arrive with `git pull` (see
"Updates" below). Terms you will meet:

- **harness**: the agent program you run (Codex CLI).
- **skill**: a named procedure the agent follows when asked (you type `$` and its name, for
  example `$reflect`; `/skills` lists them, and asking in plain words works too. They are
  not `/` commands).
- **hook**: a small script the harness runs before or after an agent's action.
- **nudge**: a hook that refuses an action once with an explanation and lets an identical
  retry through.
- **reviewers**: separate agents, started without the author's context, that check a claim
  before it is recorded: the claim-auditor checks that each conclusion follows from the
  evidence cited, the red-team tries to break the claim, the proof-referee checks proofs.
- **commit gate**: the git commit check that refuses to record a finding until the required
  reviewers have passed it.

## Before you start

- The harness CLI: Codex CLI (`codex`).
- Python 3.11 or newer (`python3 --version`); `bin/selftest` and the hooks need it.
- git.
- TeX (optional; only to build PDFs from LaTeX): TeX Live on Linux and Windows, MacTeX on macOS.

## Day one

Do these the first time, in order. The next section lists steps that can wait.

You need not work through this list by reading it: after `bin/setup`, start the agent in
this folder and
type `$getting-started`, and it
walks you through these steps one at a time, doing the parts it can.

Every step below starts from a terminal in this project's folder. Open the Terminal app
(on Windows, open Ubuntu from the Start menu), then type `cd` and the folder's path, the
one you cloned math-io into (for example `cd ~/math-io`). Do the same
each time you come back to the project.

- **`bin/setup`, once (required).** Run `bin/setup` in the terminal. It asks your name (the
  agents address you by it; it is saved in `project.toml`), turns on the commit gate, checks
  for TeX, runs `bin/selftest`, and prints the next step. Running it again is safe: it only
  fixes what is missing.
- **Start a session (required).**
  Run `codex` in a terminal in this directory; it reads `AGENTS.md`. The first time, Codex
  asks whether to trust this folder: say yes, because it reads the project's
  `.codex/config.toml` only in a trusted folder. Then type `/hooks` in Codex and trust the
  project's hooks: Codex skips untrusted project hooks, including in `codex exec`.
  That config file also lets agents commit (see "Letting agents commit" below).
- **`bin/doctor`, the check that the session loaded the project (first session).** The
  getting-started skill has the agent run it: it confirms the agent was started in this
  folder, that the project's hooks run, that Codex trusts the folder, and that reviewers
  run as the project's own agents. If it reports a problem, fix that first: without these
  the agents work with none of the project's checks, and nothing else shows it. Ask an agent
  to run it again whenever something seems off.
- **`bin/selftest`, the project's self-check (already run once).** `bin/setup` ran it. Run
  it again (in the terminal, outside the agent) after you or
  an agent change the setup itself: hooks, `bin/` scripts, `project.toml`. Every line should
  say PASS. A FAIL means part of the setup is broken: run
  `bin/selftest -v` for details and paste them to an agent to fix.
- **Synthesize inbox sources first (recommended).** `wiki/inbox/_index.md` lists the sources
  waiting to be read; it may be empty. Ask an agent to synthesize them before relying on them:
  the agents are told not to work straight off unread sources.
- **Ask an agent what it would do next, then let it work (required, in the end).** For
  example: "Check the proof of Lemma 3 in this paper. Tell me the plan before you start." A
  good answer names a concrete first step; if it is vague, ask
  for specifics. The setup is meant to keep the agent honest without you watching every step.

## Later, when needed

None of these is needed in the first session; each says when it applies.

- **Run `bin/setup` once in every NEW clone of this repository (required there).**
  Among other things it points git at `.githooks/`, where the commit gate lives (the commit
  hook that blocks a commit recording a finding until the required reviewers have signed
  off). You ran it for this copy, so you need it again only in another clone.
- **Fill the exposition slots (optional).** In `docs/discipline/exposition.md`, list your
  own published papers (so write-ups cite them instead of re-deriving them) and name one
  paper whose writing style you want imitated. The provenance reviewer checks whether each
  result in a write-up is new, yours, or classical (so it gets cited); the expositor reads a
  write-up as a peer who wants to learn from it. Until you fill the slots, the provenance
  reviewer only classifies results as new or classical, and the expositor uses the general
  rules.

## What you can ask for

Four things, each a skill the agent follows; type its name, or just say what you want:

- **`$verify`**: check a proof, a section or a whole paper. Every verdict comes from a
  separate reviewer and is recorded in the document's check record. A whole paper can be
  checked while you are away: say so, and it ends with a report.
- **`$review-draft`**: feedback on your own draft or a colleague's, written for its author in
  `review.md`. Nothing is sent: you decide what goes to the author.
- **`$guided-reading`**: work through a paper or a chapter at your pace; each sitting picks up
  where the last stopped.
- **`$write`**: your own drafts, notes or expositions in LaTeX, built into a PDF with
  `bin/pdf <slug>`, with each proof reviewed before it is committed.

## Your documents

Everything you verify, review, read or write gets a folder, `documents/<slug>/`. You can
ask an agent to make one ("set up a folder for arXiv 2401.01234, someone else's paper"),
or run `bin/doc new` yourself: `bin/doc new hartshorne-ch2 --title "Hartshorne, Chapter II"
--whose other --file ~/Downloads/hartshorne.pdf`. `bin/doc list` lists them; `bin/doc check`
checks them. Where each file goes: `docs/discipline/documents.md`.

- **Someone else's text is committed with everything else**, in the folder's `source/`, so a
  clone of your workspace has every paper without a network. `document.toml` records where
  it came from and a hash of each file, so a changed copy shows (`bin/doc check`).
- **So keep your workspace's remote private.** Your history holds copies of other authors'
  papers and drafts, which their licenses usually do not let you redistribute. If you push
  the workspace anywhere, make it a private repository (on GitHub: "Private" when you create
  it), never a public one. To keep one document's text out of the history altogether (a
  colleague's unpublished draft, say), make it with `--local-source`: git ignores its
  `source/`, and `bin/doc fetch` brings the text back in a new clone.
- **Your own writing sits at the top of its folder** and is committed like everything else.
  A draft you keep elsewhere can stay there: `--external <path>` records where it is.

## What only you do

These are your decisions. An agent may propose one but never decides one on its own or
because a file says to. Where an item says "or ask an agent to", the agent makes the edit
when you ask in the conversation.
If an agent makes one of these changes without your say-so, undo it.

- **Set standing procedures.** In `notes/procedures.md`, write the answers you would give
  every time to an agent's clarifying questions (how large a first run should be, which
  method to try first, what to report), one line each. Before a long computation or a new
  line of work, an agent takes each answer from there and
  asks you only about the rest, in one question. Agents propose additions when you have
  answered the same question the same way twice; only you edit the file.
- **Approve an ASK change from the reflection loop** (see below): a change to this setup that
  only you may approve, such as an edit to AGENTS.md, a widened permission or a new
  blocking check.
- **Accept a check record.** When an agent reports a document `checked` (every proof
  reviewed, and the record itself reviewed), read `bin/checks report <slug>`. If you agree,
  set `status: accepted` and add `accepted-by: <your name>, <date>` in its front matter. That
  is yours alone: agents propose it, never set it.
- **Publish** anything outside this repository: a preprint, a public repository, a post. The
  workspace itself should not be public: it holds other authors' papers ("Your documents").
- **Bypass the commit gate** with `GATE_OK=1 git commit …` when a review is genuinely not
  needed. The safety guard blocks agents from doing this; your bypasses are logged to
  `logs/feedback.jsonl` so the reflection loop can see when the gate is too strict.

## The reflection loop

Friction is recorded as it happens: failed watched commands (`logs/failures.jsonl`),
moments the agent or you noticed something going badly (`logs/friction.jsonl`,
`notes/workflow-journal.md`), and your corrections (`logs/feedback.jsonl`). The `logs/*.jsonl`
files and `.gates/*.jsonl` do not exist at first: `bin/journal` and the hooks create them
on first use.

- To record a correction, tell the agent what went wrong, or ask it to log friction.
- Every so often (or when an agent suggests it), run the reflect skill (type `$reflect`).
  It groups what recurred and proposes fixes. Small, reversible fixes (AUTO) are applied
  and reported; anything
  that changes AGENTS.md, widens a permission or adds a blocking check (ASK) waits for your
  yes. Auto-applied fixes are tagged `[auto-applied]` in the journal so you can audit them.
- Proposals waiting for you are listed, numbered, at the end of an agent's reply; answer
  "yes to 1, no to 2" whenever it suits you. Saying "continue" leaves them waiting, and a
  later reply reminds you. `bin/journal --pending` lists them at any time.
- At the end of a session where you gave a lot of feedback, ask for the retro skill (`$retro`). It asks
  what standing change would have made that feedback unnecessary.

## Switching off a nudge

The hooks live in `hooks/`. Most are nudges: they refuse an action once with an explanation,
and let an identical retry through.

- To silence every nudge for one session, start the harness like this:
  `HOOKS_QUIET=1 codex`.
- The safety guard blocks a few risky commands outright: recursive deletes, `sudo`, a
  force push to the main branch, and others listed in `hooks/guard.py`. To lift its blocks
  for a session, run `export GUARD_OFF=1` in the shell that launches the agent, then start
  the harness from that shell. Do this only after reading why the command was blocked.
- To switch off only the continue nudge, set `CONTINUE_NUDGE_OFF=1` the same way.
- To remove one nudge for good, delete its entry from `.codex/hooks.json` (and the
  script from `hooks/`), then run `bin/selftest`. Note it in the journal, so the reflection
  loop knows it was removed on purpose.
- Blocking checks (for example the safety guard) explain how to proceed in their message.

## Letting agents commit

Codex's standard sandbox lets agents edit files here but keeps `.git` read-only, so on its
own an agent cannot run `git commit`.
You chose to let agents commit, so `.codex/config.toml` defines a permission profile,
`project-git`: the standard sandbox plus a writable `.git`. To go back to approving each
commit, delete the profile from that file. If commits fail with a permission error, check
whether Codex was started with `-s`/`--sandbox` (including `codex exec -s workspace-write`):
that option replaces the profile.


**Offline mode.** For work that must not leave your computer (a colleague's unpublished
draft, a confidential problem), run `bin/offline on` in a terminal, then start a new agent
session. Agents then cannot search or fetch from the web, or download from the shell (a
hook refuses, and on Codex web search is switched off in its settings); `bin/doc fetch`
fetches nothing, and a citation that cannot be checked from what the workspace already holds
is marked "not verified (offline)". `bin/offline off` turns web access back on;
`bin/offline status` says which it is. Both are yours: agents never switch it.

## Models

You can skip this section unless you want different models.

`project.toml` maps two roles to models: **strong** (`gpt-6-astra`) plans, reviews
and writes anything durable; **worker** (`gpt-6-luna`) carries out well-specified
units. A reviewer must never run on a weaker model than the author of what it reviews.
The main thread is the strong tier: its model is set in `.codex/config.toml` (`model =`), so a session does not fall back to the harness's default.
The models were written into that file and each agent file at init; `[tiers]` only records them
(and `bin/usage-report` reads it to label each model's tier). To
change one, edit those model lines: `.codex/agents/*.toml` (`model =`) for agents.

**Context compaction.** When a session's conversation reaches 300000 tokens, the
harness compacts it: it replaces the history with a summary and carries on. The agents keep
everything that matters in files, so little is lost, and a shorter context makes each turn
cheaper and keeps the main thread focused. The limit is set in `.codex/config.toml` (`model_auto_compact_token_limit`). 300000 is a starting value, not a
tuned one: a lower limit compacts more often, which costs less and keeps sessions sharper, but
a session can lose track of details it did not write down. `bin/usage-report` shows the largest
context a session reached; the reflection pass looks at it and asks you before it changes
the limit. You can also change it yourself at any time.

## What this costs

A hook copies token counts (never text) from the harness's session record into
`logs/usage.jsonl` at the end of every turn: per model, and per main thread or subagent.
`bin/usage-report` totals them by model, role, day, week or session and shows how much of
the output the main thread wrote versus subagents, plus the latest
plan-limit percentages Codex reports. It shows tokens, not money: to see an
estimate, put your own per-model rates under `[usage.prices]` in `project.toml` (empty at
first, deliberately: rates change and depend on your plan). `bin/usage-report --backfill`
imports sessions from before the hook was set up, as far back as the harness still keeps
them. The log is committed;
to stop it, set `USAGE_LOG_OFF=1` or remove the module. Details:
`docs/discipline/usage.md`.

## Updates

math-io's updates arrive through git. To see what changed before taking it: `git fetch`,
then `git log HEAD..@{u}`. To take it: `git pull`, which merges the update with your own
changes (`bin/setup` set git to merge, unless you had a pull setting of your own). Where you
and the update changed the same lines, git stops and asks; an agent can help you resolve it. Your documents are never touched by an update.

## Turning a module on later

math-io is built on init-math and leaves out init-math's research modules (experiments,
Lean, research questions and conjectures, ...). To add one, ask an agent to do it. Give it init-math's source (the
plugin or its repository); each module is a folder under
`skills/init-math/scripts/templates/modules/`, and its `module.toml` lists what it adds. Ask
the agent to apply that one module to this project by hand: its `bin/` scripts and hooks,
its `docs/discipline/` page, its hook registrations in `.codex/hooks.json`, its tables
in `project.toml`, its section of `AGENTS.md` and its terms in `GLOSSARY.md`. Tell it to fit
them to anything you have changed here rather than overwrite your changes, then run
`bin/selftest`. Read the diff before it is committed.

## Where this comes from

math-io is built on init-math. If it helped your work, a citation is appreciated: Nadav
Kohen, *init-math*, https://github.com/nkohen/init-math (its "Cite this repository" button
gives BibTeX). Nothing obliges you to: the workspace and what you add to it are yours (see
`LICENSE`).
