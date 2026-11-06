# The commit gate

A git pre-commit check (`.githooks/pre-commit`) that refuses to commit a finding until the
reviewers it needs have seen the exact text being committed. The review procedure itself
is the `gate-chain` skill; this page explains the mechanism.

## Why

Prose rules about reviewing ("run the claim-auditor before you record a result") are
followed most of the time and skipped exactly when an agent is tired, rushed or confident.
An agent's own report that "the auditor passed it" is also not evidence: the text may have
changed after the review, or the review may never have run. So the gate asks for evidence:
a log that the reviewer was dispatched on this content, and a recorded passing verdict for
the same content.

It is a reminder with evidence, not security. Anyone can edit `.gates/` by hand; the gate
exists to make skipping a review a deliberate act rather than an oversight.

## What needs a review

Set in `project.toml` under `[gates]`:

- **Proof edits** (`[gates.proof]`): any added or removed line inside a proof block —
  `\begin{proof}`…`\end{proof}`, or a line starting "Proof." up to an end-of-proof mark
  (∎, □, `\qed`) or the next heading — in a matching `.md` or `.tex` file. Default
  reviewers: `proof-referee` and `claim-auditor`.
- **Any rule you add**: `[[gates.rules]]` with `paths` (globs), `gates`, and optionally
  `status` (without it, any change to a matching file triggers the rule), `exclude` (globs
  to skip), `when` / `unless` (a regex the staged file must or must not contain), and
  `last_look` (reviewers whose last look is needed too). Every
  name in `gates` must be a key of `[gates.verdicts]`: `bin/gate-stamp` refuses any other
  name, so a rule naming one could never be satisfied. `[gates.proof] enabled = false`
  switches off the proof-block check.

Every other commit passes the review check untouched.

## The flow

1. Dispatch the reviewer with the **target file's path named in its brief**. The hook
   `hooks/gate-dispatch-log.py` records `{gate, path, content hash}` in
   `.gates/dispatches.jsonl`.
   It fires when a new reviewer agent is spawned (the agent
   type names the gate; failing that, exactly one reviewer name must appear in the brief),
   and it records each existing project file the brief names.
   A follow-up message to a
   reviewer that is already running is **not** a dispatch and is not recorded: spawn the
   reviewer again on the new text. If you give the reviewer a section extract, still name
   the target file in the brief, so the dispatch is recorded against it.
2. When it returns, run `bin/gate-stamp <gate> <path> <VERDICT> -` with
   the reviewer's full reply, word for word, on standard input, whatever the verdict:

   ```bash
   bin/gate-stamp claim-auditor documents/chapter-two/lemma-3.md SOUND - <<'EOF'
   <the reviewer's full reply, word for word>
   EOF
   ```

   The stamp in `.gates/stamps.jsonl` keeps the text, so no verdict file is written (a file
   path in place of `-` still works). Only a passing word (`[gates.verdicts]`) satisfies the
   commit gate; a failing one (`[gates.failing]`) is recorded as review history, so
   `bin/gate-stamp --list <path>` shows every review of the file, and a dispatch with no
   verdict recorded shows as a hole. It refuses if that gate was never dispatched on the
   file's current content, if the word is neither passing nor failing for that gate (a
   typo), or if a passing excerpt holds a caveat phrase (below).
3. Stage and commit. The pre-commit check hashes the **staged** content of each file that
   needs review and wants a dispatch and a passing stamp for that exact content.

**A passing stamp over the reviewer's own caveat.** If the excerpt of a passing verdict
holds a caveat phrase (`[gates] caveat_phrases`: "sketched", "not verified", "incorrect",
"from memory" and the like), the stamp is refused: a reviewer that writes "Step 4 is
sketched" and then "SOUND" has not passed it. If a line does not apply (a gap the author
closed, a phrase about something else), stamp with
`--caveat-ok "<the line, word for word> — <why it does not apply>"`; the script checks that
the reason contains each such line, keeps the reason, and `--list` prints it, so the owner
sees it in the review summary. The scan stops at the red-team's "Attack surface" line, which
lists what is uncovered by design, and skips a line the reviewer marks minor, except under the
proof-referee's `CLEAN`, which says nothing is left to fix (minor points belong under `CLEAN-MINOR`). It checks only what you give it, which is why
the stamp takes the reviewer's whole reply, not lines you choose: a caveat left out would
not be caught.

**Kinds and cycles.** `--kind last-look` or `--kind exchange` marks a review that does not
count toward the re-review limit (`docs/discipline/gate-chain.md`); the default is
`review`. An exchange is a fresh full review, so a passing one satisfies the gate like a
review. A last look answers one question, so it never stands in for the reviewer's review;
it satisfies only a `last_look` requirement. `bin/gate-stamp --new-cycle <path> "<what is new>"` starts a new count for a file:
run it when you record the claim at the end of a cycle, or when new evidence or a new proof
arrives. `--list <path>` prints each gate's reviews this cycle.

If you edit the file after the review, the stamp is stale and the commit is refused: the
reviewer has not seen what you are committing. Re-dispatch on the new text. This is the
mechanical form of the rule "never write a verdict label until the reviewer re-ran on the
revised text".

When refused, the message names each file, the missing or stale review, and what to do.
`refuse = "always"` (the default) refuses every time; `refuse = "once"` lets an identical
retry through, for projects that prefer a nudge.

## Owner levers

- **`GATE_OK=1 git commit …`** commits despite the gate and logs `{kind: bypass}` to
  `logs/feedback.jsonl`. It is the owner's override, for a commit the owner judges does not
  need review. An agent never sets it (the guard hook refuses and
  logs the attempt).
- **`git commit --no-verify`** skips every git hook, this one included. Same rule: the owner
  only.
- It runs `bin/hedge-scan --diff` and prints what it reports: a hedge ("heuristically", an
  argued label) removed with no new evidence, an argued verdict
  with an unknown label or no premises. Shown, never enforced (the owner's decision).

## Setup, and the per-clone hazard

Git reads hooks from the directory in `core.hooksPath`, a per-clone setting that is not
committed. `bin/setup-hooks` sets it to `.githooks`; run it once in every new clone and in
any worktree with its own configuration. Until then that clone **skips the gate silently**.
`bin/selftest` reports a clone where it is not set; `bin/setup-hooks --check` tells you
directly.

A fresh clone has the gate off until `bin/setup` (through `bin/setup-hooks`) sets
`core.hooksPath`, which is what switches it on; math-io's own files arrive by the clone and
need no reviews.
`[gates] enabled = false` in `project.toml` turns the gate off even where `core.hooksPath`
is set; `enabled = true` (the default) only takes effect in a clone that has run
`bin/setup-hooks`.

## Merging branches

`.gates/dispatches.jsonl`, `.gates/stamps.jsonl` and `.gates/cycles.jsonl` are append-only
and union-merged, so two branches that both reviewed files merge without conflict. Rows may
then appear twice or out of order; the scripts match rows as a set and de-duplicate by `id`.

## If the check crashes

It lets the commit through (fails open) and prints a WARNING, with the traceback in
`logs/state/hook-errors.log`. A gate that wedges every commit would be switched off; a gate
that fails silently would be trusted when it should not be. Fix the cause and re-run
`bin/selftest`.
