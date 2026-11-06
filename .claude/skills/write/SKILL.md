---
name: write
description: Help the owner write mathematics — a paper draft, lecture notes, a survey, an exposition of someone else's result — in LaTeX (or Markdown) in its document folder, built into a PDF with bin/pdf, with every proof reviewed before it is committed and the reader reviewers before it is called finished. Load it when the owner wants to start, continue or finish a piece of writing.
---

# Writing

The owner's writing lives at the top of its document folder and is theirs: you draft, revise
and propose, in their voice and at their direction. A proof you write is a claim like any
other, and it is reviewed before it is committed.

## Starting

- A new piece: `bin/doc new <slug> --title "<title>" --whose mine`. A draft kept elsewhere
  stays there: `--external <path>` (its proofs are then checked through unit files, the
  `verify` skill, since the commit gate cannot see it).
- Ask once, before writing much: **who is the intended reader** (and what they already know),
  what the piece is for, and which **model text** sets its voice (the owner's earlier papers,
  or a book they admire: `docs/discipline/exposition.md`). Record the answers in the
  document's README.
- The main file is `documents/<slug>/main.tex` (one top-level `.tex` with `\documentclass`),
  with its bibliography beside it. `bin/pdf <slug>` builds it into `build/` (git-ignored) and
  says plainly where LaTeX stopped.

## The rhythm with the commit gate

Every edit inside a proof (`\begin{proof}` ... `\end{proof}`, or from a line starting with
the word "Proof" to an end-of-proof mark or the next heading) is refused at commit until the `proof-referee` and the `claim-auditor` have
stamped the draft file as staged. So:

- **Commit text outside proofs as often as you like**: introductions, definitions,
  statements, remarks.
- **An unfinished proof stays outside a proof environment**, as a paragraph headed
  "Sketch (in progress)." (not "Proof sketch": the gate treats any line starting with the
  word "Proof" as a proof). It is committed like any other text, and nobody mistakes it for a
  proof.
- **When a proof is meant to stand**, put it in a proof environment, run
  `bin/math-hygiene-scan`, review it (the `gate-chain` skill: author check, then the referee
  and the claim-auditor, naming the draft file in each brief), stamp, and commit. Batch the
  proofs that are ready into one review where you can.
- If this is still too slow for the owner, the gate can refuse once instead of every time
  (`[gates] refuse = "once"` in `project.toml`). That is the owner's setting to change, never
  yours; mention it once if the friction is real.

## Citations and attribution

- Every result you did not prove here is cited: author, work, and theorem number. Find the
  right source firsthand (the literature wiki, `wiki/known-results/`, the `lit-search`
  agent); never cite from memory.
- An exposition of someone else's result says so plainly, and the `provenance` reviewer
  checks it.
- The referee asks for a source for every standard fact. In the owner's own writing that
  stands: a citation request is fixed (cite it, or prove it), not waved through.

## Finishing

A piece is finished when the owner says so after these, in order (the `gate-chain` skill's
order for a reader-facing write-up):

1. Every proof reviewed and stamped. Then **offer the strict pass**: every citation request
   the referee made is treated as a defect, and each is fixed or answered in the text.
2. `provenance` (what is new, what is the owner's earlier work, what is classical),
   `expositor` (can the intended reader learn from it?), and `cold-reader` (can a stranger
   follow it?), each naming the intended reader in its brief. Apply each one's fixes before
   the next.
3. For a write-up drafted from an internal staging record: the fidelity check, a fresh
   `claim-auditor` given both (does the write-up state anything more strongly than the
   record?).
4. `bin/pdf <slug>` builds cleanly. Set the README's `status: done` and write its Outcome.

Publishing it (a preprint, a journal, a website) is the owner's step, never yours.
