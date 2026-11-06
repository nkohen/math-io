# Glossary

Terms with a specific meaning in this project. If a document uses a term that is not
here and not defined in the document itself, that is a defect: define it here, the same
turn you notice. Add a row to [SEARCH-ALIASES.md](SEARCH-ALIASES.md) when you searched
for an idea under one word and the project calls it another.

## General

- **owner**: the person who directs this workspace, named in `project.toml` (`[project] owner`). Some decisions are theirs alone (see COORDINATOR.md, "Ground rules").
- **coordinator**: the agent session talking to the owner. It plans, dispatches other agents, checks their work and records results. Its own rules are in COORDINATOR.md, which only it gets.
- **worker**: an agent the coordinator dispatches to carry out one well-specified unit of work.
- **reviewer**: a fresh-context agent whose only job is to check one document from one angle and return a verdict and a list of problems. It never edits, and it always runs on the strong tier (see `project.toml` `[tiers]`). The core three are `claim-auditor`, `proof-referee` and `red-team`.
- **durable**: written to a file in this repository (and committed), as opposed to only said in a chat or held in context.
- **harness**: the program the agents run in (claude for this project).
- **intake check**: the coordinator's list, before a long computation or a new line of work, of what the task leaves open; each item is answered from the standing procedures or asked of the owner, in one question.
- **standing procedure**: one of the owner's default answers in `notes/procedures.md`, used unless the owner says otherwise for a task.
- **genuine fork**: a choice that is the owner's to make: mutually exclusive designs, an irreversible or outward-facing action, or a scope decision. Only at one should an agent stop and ask.
- **smoke test**: a seconds-long run on a few small, hard cases that checks a script or pipeline works before anything bigger is started.
- **known-answer check**: running a tool on a case whose correct output is already known independently (a published value, a hand computation, a trivial case) before trusting it on cases that are not.

## Documents

- **document**: a piece of mathematics you verify, review, read or write: someone else's paper or draft, or your own write-up.
- **document folder**: `documents/<slug>/`, everything about one document (rules: `docs/discipline/documents.md`). Older wording, still in the reviewer briefs and the gate-chain skill, calls it the **work folder**.
- **`document.toml`**: a document folder's record of what the document is: its `title`, `whose` it is, and where its text comes from (`[source]`), with a hash (a checksum) of each file fetched.
- **whose**: `mine` for your own writing, `other` for someone else's. Rules that treat the two differently read this field.
- **source/**: the folder holding text you did not write, exactly as fetched. Never edited, outside the commit gate, and committed like everything else, unless the document was made with `--local-source` (`[source] commit = false`): then git ignores it and `bin/doc fetch` brings it back.
- **external draft**: your own draft kept outside the workspace; `document.toml` records its path (`[source] external`), and nothing copies it in.

## Check records

- **check record**: `documents/<slug>/checks.md`, what was checked in a document, by which review, and what was found (rules: `docs/discipline/checking.md`; tool: `bin/checks`).
- **unit**: one statement with its proof, checked as a whole; its row in the check record has a **unit id** (`U01`, `U02`, ...).
- **unit file**: `documents/<slug>/units/<id>.md`, a unit copied word for word (Uses, Statement, Proof, nothing else) for a reviewer. Identical unit files share a git blob id, which is how a review is reused.
- **Uses**: a unit file's list of the exact statements its proof relies on, each labelled with where it comes from.
- **coverage**: the check record's list of every numbered result in the document, with the unit that checks it or why there is none.
- **verdict (unit)**: `checked`, `gap`, `citation-missing`, `unclear` or `open`; each but `open` is backed by a proof-referee stamp.
- **assumption**: a cited result a proof relies on, `assumed` as the document quotes it, `assumed (not retrieved)`, or `checked: <where>`.
- **reuse**: filling a unit's row from a passing review of identical content elsewhere (`bin/checks reuse`).
- **checked / accepted (record)**: `checked`, every unit reviewed and the record itself reviewed by the claim-auditor (an unattended run ends here); `accepted`, the owner read it and agrees (only the owner sets it).

## Offline mode

- **offline mode**: `[web] offline = true` in `project.toml`, set with `bin/offline on` by the owner: no web search or fetch and no downloads (the `offline-guard` hook; on Codex, `web_search = "disabled"`), so nothing about the work leaves the computer. **not verified (offline)** marks a citation or attribution that could not be checked from what the workspace holds.

## Known results

- **known result**: a statement the literature proves or observes about an object of study, filed in `wiki/known-results/` with its source, scope and date accessed.
- **object of study**: what a known-results file is about and named for: a named sequence, a family of graphs, a class of curves.
- **family file**: a known-results file (`family-<topic>.md`) for results about a whole class of objects rather than one.
- **catalog id**: an identifier in an online catalog (an OEIS A-number, an LMFDB label), used in file names and recorded with the date accessed.
- **date accessed**: the day a source, especially an online page, was read. Online catalogs change, so this is the provenance.
- **seed to verify**: a claim seen without a source you have read (an unreferenced catalog formula, a remark, a summary). Not a fact until checked or sourced.
- **firsthand**: you read the statement in the source itself, not in someone's summary of it.
- **corroborated**: the source itself was out of reach, and two independent sources restate the theorem with its hypotheses; the citation stays the original source.
- **checked** (a known result): you verified the statement yourself (a proof written out, a computation) and recorded how, as `read: checked (<how>)`. A result known only from a summary is a seed to verify, not a known result.

## Literature wiki

- **raw source**: a file in `wiki/raw/` recording a source as ingested (its text, or a pointer to it). Never edited afterwards.
- **ingest**: bring a source into the project so it can be used without opening it again: its raw record, a synthesized article, its results in `wiki/known-results/`, the folder indexes and the wiki log, in one commit (the `ingest` skill). A file in `wiki/raw/` alone is not an ingest.
- **pointer file**: a raw source that records where a source is instead of its text (`kind: pointer`), because the text cannot be committed; it states why (`pointer-reason:`) and quotes every statement the project uses.
- **inbox item**: a file in `wiki/inbox/` naming one source someone wants read, and why. Deleted once the source is ingested and synthesized.
- **synthesized article**: a page in `wiki/concepts/` explaining one bounded idea in the project's terms, drawn from raw sources, with a confidence level and its reason, and a `## Sources` list.
- **reference page**: a page in `wiki/references/` collecting sources or results: a reading list, an annotated bibliography, a comparison table.
- **synthesize before relying**: the rule that a source's result or method is written up as an article before work relies on it.
- **folder index**: the `_index.md` in each wiki folder, listing its files. Read it before scanning the folder.
- **wiki log**: `wiki/log.md`, one appended entry per operation on the wiki, never edited.

## Review gates

- **finding**: any result you record or report: a measured verdict, a proof, a negative result. Stating it in a message counts. Findings go through the review gates before they are promoted or committed.
- **finding-bearing change**: a change that records a finding, or adding or changing a proof in a document.
- **gate**: a review step a finding passes before it is promoted or relied on — a scan script or a reviewer agent.
- **verdict**: a reviewer's one-word result, e.g. `SOUND`, `OVER-CLAIMED`, `CLEAN`, `CLEAN-MINOR`, `NEEDS-WORK`, `SURVIVED`, `REFUTED`, `NARROWED`, `INCONCLUSIVE`.
- **crux** (load-bearing step): the single condition a whole argument or proof turns on, used exactly once; the proof-referee re-derives it first and reports `CRUX-UNVERIFIED` if it cannot.
- **proxy / target**: a cheap quantity measured in place of the quantity a claim is really about. A proxy supports a claim only where it is shown to track the target.
- **claim-strength self-audit**: the questions an author asks before writing a status or verdict (rigorous invariant or proxy? what is the scope gap? is the sample capped?); see `docs/discipline/gate-chain.md`.
- **scope gap**: the difference between what the evidence covers and what the claim asserts.
- **two-step promotion**: claim-auditor `SOUND` on the new wording, then red-team `SURVIVED`; only then is the change proposed to the owner, who makes it.
- **section extract**: the part of a long document under review, plus a short preamble of trusted definitions and results, given to a reviewer instead of the whole file.
- **canonical draft**: the one document where a finding is written and reviewed first; other records copy from it after it passes.
- **informal argument**: an argument offered for a claim that is not a proof: a heuristic, a "morally" story, a plausibility count, an argument inside an idealized model, an analogy. How to write and test one: `docs/discipline/informal-arguments.md`.
- **argued claim**: a claim whose support includes a non-deductive step or an open premise. It is evidence, never a result, and carries its **labels** (`heuristic`, `moral`, `conditional`, `model-only (<model>)`, `analogy (hint)`, `analogy (relay: ...)`, combined with `+`).
- **handle**: the step that does the work in an argument, separated from ancillary detail.
- **perturbation**: a cheap test of an argument by changing it (drop a hypothesis, the false variant, corrupt a step, delete an ingredient, a nearby case, the distinguishing feature). It *bites* when the changed argument still "works" or the support disappears.
- **brief**: the message that dispatches a reviewer: the file and lines, the claim, the statements of cited results, what changed. It withholds who wrote the claim, the exploration behind it, the author's confidence and earlier verdicts.
- **last look**: one fresh claim-auditor check before a proof is proposed, asking only whether the headline ignores anything the document's own gaps section lists.
- **re-review limit**: three reviews of one document by one reviewer per cycle; at the limit the claim is recorded at the strength the last review supports, with its open issues listed.
- **review miss**: a claim that passed a gate and was later refuted, narrowed or retracted; recorded as a `review-miss:` line for each gate that passed it.
- **standing disagreement**: two gates, or a gate and the author, still disagreeing on a fact after one exchange; recorded under `## Disagreements`, given to an **adjudicator** (a fresh agent that must run a checkable step; the losing side is shown the step, not the ruling), and if still standing put to the owner, whose answer is an `owner-decision:` line.

## Writing for readers

- **reader-facing write-up**: a document people outside the project will read to learn from and reuse, such as a paper draft or a wiki article.
- **staging document**: the internal record a write-up is drafted from; it keeps every result, positive and negative, with full hedging, and is what the honesty reviewers check.
- **fidelity check**: comparing a write-up against its staging document so that nothing is stated more strongly in the write-up than the staging document records.
- **intended reader**: the person a write-up is written for, with what they already know; the expositor judges motivation relative to them.
- **role motivation / insight motivation**: a step is role-motivated when the reader can see what it does in the argument, and insight-motivated when the reader can see where it could have come from.
- **cite out**: replace a re-derivation with a citation. Done only for the owner's own prior work, which the intended reader is assumed to know.
- **prior work**: results the owner published or wrote before this project, listed in `docs/discipline/exposition.md`.

## Mechanical scans

- **scan**: a zero-model script in `bin/` that greps a document for one kind of mechanical defect. Scans are cheap and run before a reviewer; they never replace one.
- **strength word**: a word that asserts certainty or generality ("proved", "always", "for all", "settled"); `bin/hedge-scan` lists them, headlines first.
- **high-visibility line**: a header, a bold lead or a summary line ("Verdict:", "Status:"); read in isolation, so it must carry the hedges of the body it summarizes.
- **finding code**: a private label invented inside one piece of work (F12, SB2). Fine inside the document that defines it; meaningless in a shared index.
- **orphan**: an artifact on disk (a known result, a document folder) that its store's `_index.md` never names. `.orphanignore` lists intentional ones.
- **difficulty estimate**: a phrase like "multi-week", "from scratch" or "out of scope" that can stop work; it needs a real search or attempt behind it.
- **stale claim**: an old wording of a claim left elsewhere after the claim was corrected.
- **correction marker**: a sign that a line is a corrected form (the warning sign, REFUTED, CORRECTED, SUPERSEDED, a strikethrough).
- **setting hygiene**: using a fact or language valid in one setting in another (analytic language for formal power series, a finite-dimensional fact in infinite dimension).
- **field rules**: this project's own proof conventions, in `project.toml` `[hygiene] rules`.

## Commit gate

- **commit gate**: the git pre-commit check in `.githooks/pre-commit` that refuses a commit recording a finding until the required reviews are on file for the staged text.
- **dispatch record**: a line in `.gates/dispatches.jsonl`, written automatically when a reviewer is dispatched, saying which reviewer was sent which file in which version.
- **stamp**: a line in `.gates/stamps.jsonl`, written by `bin/gate-stamp`, recording a reviewer's verdict on one version of one file. Only a passing stamp satisfies the commit gate; the others are the review history.
- **caveat phrase**: a phrase in a reviewer's report saying something is not established ("sketched", "not verified"); `bin/gate-stamp` refuses a passing stamp whose excerpt holds one unless `--caveat-ok` quotes the line and says why it does not apply.
- **review cycle**: the stretch in which one reviewer's reviews of one file are counted against the re-review limit; `bin/gate-stamp --new-cycle` starts a new one.
- **content hash (blob id)**: the identifier git gives a file's exact content; any edit changes it. Dispatch records and stamps are tied to it.
- **stale stamp**: a stamp for an earlier version of a file. The file changed after the review, so the review no longer counts.
- **staged text**: the version of a file that `git add` put in the index, which is what a commit records (it can differ from the file on disk).
- **hooksPath**: the git setting naming the directory git runs hooks from; set per clone by `bin/setup-hooks`.

## Firsthand checks

- **prior-art search**: looking for an existing treatment before building something. Its internal half searches the project's own record; its external half searches the published literature (the `lit-search` agent).
- **load-bearing claim**: a claim that decides what work happens (build or reuse, continue or stop) or that is about to enter a durable record.
- **durable record**: a file that outlives the session and that others will rely on: a commit, a known-results file, a report, a handoff.
- **firsthand check**: one cheap check you run yourself (one command, one search, one reading of the source) before passing a claim on.
- **placement claim**: a claim about where a question stands in the literature ("open", "studied by X", "the best known result is Y"), as opposed to a specific theorem attribution.
- **reading**: an interpretation of a source, or a theorem number, that has not been checked against the source's exact words.
- **absence claim**: a claim that something does not exist (in a library, in the literature, in this project). It needs a search whose scope is stated.
- **scope verdict**: a judgment that a task is too hard, out of scope, or blocked, which would stop or redirect work.
- **scout**: one search of the libraries, literature or project for the missing piece, run before a scope verdict.
- **exclusion list**: in a brief to an agent, what it should not report again: past failures, and the known trivialities, symmetries and invariances of the object.
- **lit report**: the report a literature-search agent returns, tagged `[VERIFIED-FIRSTHAND]`, `[READING]` or `[PLACEMENT]` claim by claim.

## Model tiers and workers

- **strong tier / worker tier**: the two model settings in `project.toml` `[tiers]` (see there for the models in use). The strong tier (opus) does direction, design and review; the worker tier (sonnet) does execution.
- **brick**: one self-contained unit of work with a stated finish line: a lemma to prove, a script to write and validate, a table to fill. Remaining work is always written as a numbered list of bricks.
- **DONE / PARTIAL / NEED-DIRECTION**: the three ways a worker ends. DONE: the brick is finished and checked. PARTIAL: some of it landed, the rest is listed. NEED-DIRECTION: the worker hit an escalation trigger and hands back the facts without choosing.
- **escalation trigger**: a mechanical condition (for example "the same goal failed 3 attempts") at which a worker must stop and return NEED-DIRECTION instead of judging whether it is stuck.
- **best-of-n**: answering a stuck search by running several attempts with deliberately different approaches and keeping the best one. It is for finding an argument, never for deciding whether one is correct.
- **step audit**: checking an argument step by step (by a reviewer), as opposed to comparing final answers across attempts.
- **attempt**: one edit-plus-check cycle on a goal. Escalation counts are in attempts.
- **CLAIM line**: the extra line a proof or construction brick's return carries (`PROVED`, `COUNTEREXAMPLE`, `GAPS (core: ...; routine: ...)`, `ARGUED (<labels>; premises: ...)`, `NOT-PROVED` or `NONE (escalated: ...)`), saying what the brick established.
- **long job**: a build, sweep or computation that may run longer than about two minutes; only the coordinator starts one.
- **ARGUED**: the CLAIM verdict for an argument that convinces but is not a proof: a non-deductive step or an open premise. Its labels say what kind (`heuristic`, `moral`, `conditional`, `model-only (<model>)`, `analogy (hint)`, `analogy (relay: ...)`, combined with `+`). An argued claim is evidence, never a result.

## Stopping and resuming

- **deep core**: the genuinely hard, open part of a piece of work, the step no known method handles directly. Calling something a deep core is a claim that must be earned by listing the bricks around it first.
- **reduce (before reporting blocked)**: restate a problem so that its hard step appears as one explicit, named hypothesis, and finish everything else. The hard step is then isolated, often smaller than it looked, and the work around it is done.
- **design progress doc**: the `README.md` of a document folder (`documents/<slug>/README.md`) that holds a multi-step effort's plan, its RESUME HERE section and its progress log (template: `docs/templates/design-progress-doc.md`).
- **RESUME HERE**: the short section at the top of a design progress doc that names the exact next step, so a fresh session can continue from the file alone.
- **progress log**: the dated, append-only list at the bottom of a design progress doc, one entry per checkpoint.
- **continue signal**: either the owner's most recent message says "continue", "keep going" or similar, or a standing mandate from earlier in the session that the owner has not withdrawn. With one, keep working through milestones; without one, finish the task you were given and stop (see `docs/discipline/stopping.md`).
- **autonomous mandate**: an explicit owner instruction to keep working for a long stretch without them ("keep going until blocked or done"). A standing mandate is one kind of continue signal. It is a standing mode, not a grant for one step.

## Safety guard

- **hard block**: a hook refusing a tool call outright, every time. The guard hard-blocks recursive deletes, force pushes or deletes of a main branch, downloads piped into a shell, `sudo`/`doas`, and a `chmod` that makes files writable by everyone; the owner can lift these by starting the agent with `GUARD_OFF=1` in its environment.
- **owner bypass**: an override that only the owner may use, such as `GATE_OK=1` on a commit or `git --no-verify`. The guard refuses it from an agent and logs the attempt to `logs/feedback.jsonl`.
- **cd drift**: a `cd` made for a one-off lookup that silently changes the working directory of every later shell call.

## Reflection loop

- **friction**: anything in the way the work went that wasted effort or went wrong — a failed or repeated step, a wrong assumption, a misleading doc. Logged one line per event in `logs/friction.jsonl`. A proof found wrong is a result about the mathematics, not friction.
- **feedback**: the owner's reaction to how the work was done — a correction, praise, or a gate bypass — logged in `logs/feedback.jsonl`.
- **watched command**: a program listed in `project.toml` `[stack] research_commands` (none at first); only these are watched for failures.
- **failure signature**: a label for a kind of failure, either a pattern from `[[stack.failure_signatures]]` that matched the output, or `<program>-exit-nonzero`. Recurrence is counted per signature.
- **hook**: a small script in `hooks/` that the harness runs automatically at a fixed moment (before or after a command, at the end of a turn).
- **nudge**: a hook response that does not forbid anything for good. Either it refuses a tool call once with a reason, and the identical call re-issued proceeds (used where the call is usually a mistake but sometimes right), or, at the end of a turn, it reminds the agent of something (for example to log friction). The safety guard's hard blocks are not nudges. `HOOKS_QUIET=1` silences all nudges.
- **workflow journal**: `notes/workflow-journal.md`, prose notes on how the work is going and the record of each reflection pass.
- **reflection pass**: a periodic review (the `reflect` skill) of everything logged since the last review, ending in a few small workflow fixes.
- **reviewed marker**: the line `<!-- reviewed YYYY-MM-DD -->` in the journal, and the matching per-row review state kept by `bin/journal` in `logs/state/`; together they say what a pass has already read.
- **AUTO / ASK**: the two routes for a reflection fix. AUTO fixes (small, additive, tested, revertible) are applied in the pass; ASK fixes are proposed and wait for the owner. Rules in `notes/reflect-autonomy-heuristics.md`.
- **`[auto-applied]`**: the journal tag (with the commit prefix `chore(reflect auto):`) on a fix applied without asking, so AUTO routing can be audited later.
- **ladder**: the order in which a fix escalates — prose, then a nudge, then a hard check — climbing one rung only when the previous one demonstrably did not hold.
- **proposal queue**: `logs/proposals.jsonl`, the changes waiting for the owner's yes or no (`bin/journal --propose` queues one, `--pending` lists them, `--decide` records the answer). A proposal stays pending until the owner answers; a "continue" is not an answer.

## Retrospective

- **retro**: an end-of-session review of the feedback the owner had to give, asking what standing structure would have made it unnecessary (the `retro` skill).
- **pre-emptive guardrail**: an instruction the owner writes into a prompt to prevent a mistake before it happens; in a retro, the strongest evidence that a rule is missing.
- **counterfactual (retro)**: a proposed change to the project's docs, checks or workflow, stated as a prediction of which feedback items it would have made unnecessary.

## Usage statistics

- **usage row**: one line of `logs/usage.jsonl`: for one transcript, model, agent role and UTC day, how many API responses (`calls`) and how many input, cache-read, cache-write, output and reasoning tokens a stretch of work used. Counts only, never text.
- **main thread / subagent**: the conversation the owner talks to, versus an agent it dispatched; usage is split by this `role`, and subagents also by their agent type.
- **cache read / cache write**: input tokens served from, or written to, the provider's prompt cache; usually priced differently from ordinary input, so they are counted apart.
- **reasoning tokens**: hidden thinking tokens some models report (Codex); already included in the output count, never added to it.
- **plan limits**: the share of a subscription's usage window already spent, as the harness reports it (Codex: a 5-hour and a weekly window); logged as a `limits` row when it changes.
- **backfill**: `bin/usage-report --backfill`, which imports sessions the hook did not see from the harness's own transcript store, skipping what is already logged.

