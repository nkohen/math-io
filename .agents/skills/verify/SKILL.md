---
name: verify
description: Check mathematics for correctness and record what was found — one proof the owner points at, a section, a draft, or a whole paper with no one watching. Every verdict comes from the proof-referee and goes into the document's check record (documents/<slug>/checks.md); main theorems also get the red-team. Load it when the owner asks to verify, check or referee a proof, a lemma, a paper or a draft, or asks whether something in a document is right.
---

# Verifying a document

You are finished when the document's check record says, for every numbered result in scope,
what was checked, by which review, and what was found, and (for a whole document) its status
is `checked` with the claim-auditor's review of the record. Your own reading never decides a
verdict: the proof-referee's does. Rules and verdicts: `docs/discipline/checking.md`.

## 0. Before starting

- **The folder.** `bin/doc list`; if the document has none, `bin/doc new` it (someone else's
  paper is `--whose other`). Then `bin/checks init <slug>` if it has no record.
- **Scope, with the owner** (the intake check): one result, a section, or the whole
  document? With them, or unattended ("check the whole paper and report")?
- **Put the size in front of them once**, before a section or a whole document: how many
  numbered results, and roughly what it costs. Measured on API pricing: one proof-referee run
  is about $0.50–1, and a whole run comes to **about $2 per result all told** (a three-result
  test paper cost $5.80, including the red-team, a literature search and the record's
  review), a few minutes each. On a subscription it comes out of the usage allowance in the
  same proportions. Wait for the go-ahead; an unattended run is a standing mandate to work
  through to `checked` and the report.

## 1. Coverage first

Read the document (`source/`; LaTeX when there is a choice) and list **every numbered result**
in the record's Coverage table, in order: theorems, lemmas, propositions, corollaries,
numbered claims. Every result with a proof in the document becomes a unit. One without a proof
gets a reason ("cited from [12]", "stated as known", "left to the reader"). "Immediate" and
"left to the reader" are where errors hide: name them in the report.

## 2. One unit at a time

**Someone else's document, or your draft kept outside the workspace: write the unit file**
`documents/<slug>/units/<id>.md` (ids `U01`, `U02`, ...), and nothing else in it:

```markdown
## Uses
- Lemma 2.4: <its statement, word for word>
- [12, Thm 3] (Banach-Alaoglu, as the document cites it): <the statement it relies on>

## Statement
<word for word>

## Proof
<word for word>
```

- **Word for word means copied, not retyped.** From LaTeX, copy the source's lines between
  `\begin{lemma}` and `\end{proof}` (the environment lines themselves may go). Never fix a
  typo, modernize notation, shorten or complete a step: a unit that differs from the document
  checks something the document does not say.
- **Uses** quotes each statement the proof relies on: earlier results and definitions from
  the document, and cited results as the document states them. If the document only cites
  ("by [12, Lemma 2.4]"), find the statement firsthand (the literature wiki, `lit-search`)
  and quote it with where you read it. If it cannot be found, write "not given in the
  document, not retrieved": the row will be `unclear`, and its Assumptions entry
  `assumed (not retrieved)`.
- **Check it mechanically:** `bin/checks fidelity <slug> <id>` confirms the Statement and
  Proof are word for word in `source/`. A FAIL is fixed before any review. A PDF-only source
  cannot be checked this way: say "transcribed from the PDF" in the row's note.
- **Many units?** You may hand extraction to workers in batches (a whole section per brief:
  "copy, never retype"). Run `fidelity` on every unit they return, and read one per batch
  against the source yourself.
- Then `bin/checks add <slug> <id> --where "Lemma 2.4 (Section 2, p. 7)"`, and try
  `bin/checks reuse <slug> <id>`: if identical content was already reviewed, the row is done.

**Your own draft in the workspace:** no unit files. `bin/checks add` a row per lemma, and send
the referee the draft file, naming the lemma and its lines in the brief.

## 3. The review

1. `bin/math-hygiene-scan <the unit file or draft>`: cheap, and it goes before every referee
   run.
2. The author check from the `gate-chain` skill, written into the document's `README.md`,
   never into the brief.
3. Dispatch the `proof-referee`, naming the unit file (or the draft) in the brief. Load the
   `gate-chain` skill for what a brief holds and withholds: no opinion of yours, no earlier
   verdict.
4. Stamp its full reply: `bin/gate-stamp proof-referee <path> <VERDICT> -`.
5. **Classify from the text of its major hits**, and record with `bin/checks set <slug> <id>
   <verdict> --note "<the hit, quoted>"`:

   | the referee returned | verdict |
   |---|---|
   | `CLEAN` or `CLEAN-MINOR` | `checked` (minor points may go in the note) |
   | `NEEDS-WORK`, and every major hit only asks for a source for a standard fact | `citation-missing` |
   | `NEEDS-WORK`, a hit says a cited statement was not supplied | `unclear`; try once to retrieve it and review again |
   | `NEEDS-WORK`, a hit says a cited result does not apply (hypotheses fail, the statement does not cover the use) | `gap` |
   | `NEEDS-WORK`, a hit names an error or a missing argument | `gap` |
   | `NEEDS-WORK`, it cannot decide (notation, an illegible step) | `unclear`, with what would settle it |

   On someone else's document, `citation-missing` is not a failure. On the owner's own draft,
   it stands, and before the draft is called finished, offer a strict pass that treats each
   citation request as a gap.
6. **Never review again hoping for a better word.** A second review of unchanged text is a
   second opinion, not a correction. If you think a hit is wrong, write why under
   `## Disagreements` and follow the `gate-chain` rules for a standing disagreement; the
   referee's verdict stands until resolved.
7. **A unit file is never edited after its review.** If the document itself changes, write
   the unit again; its old stamp no longer matches, and it is reviewed again.

## 4. The main theorems: the red-team

The red-team asks whether a statement is true; the referee whether its proof is right. Send it
the unit files of the document's **main theorems** (those the abstract or the introduction
announces; for a draft, those the owner names), and any unit the owner asks for. Stamp its
reply on the unit file (`bin/gate-stamp red-team <path> <VERDICT> -`), and add a line to the
Summary's prose: "Red-team on the main theorems: U04 SURVIVED (s:...), U09 REFUTED (s:...)".

**REFUTED** needs three steps before anything is recorded:
1. Check the counterexample yourself.
2. If it holds, start a new review cycle (`bin/gate-stamp --new-cycle <path> "red-team
   counterexample"`) and send the referee the unit again with the counterexample in the
   brief.
3. Its failing stamp makes the row a `gap`.

If the counterexample does not hold, record why under `## Disagreements`.

## 5. Assumptions, then close

- List every cited result a proof relies on in Assumptions: `assumed` (as the document quotes
  it), `assumed (not retrieved)`, or `checked: <where>` when it was read firsthand.
- `bin/checks summary <slug>`, and add a short prose summary under the count lines: the gaps
  in a sentence each, and what Coverage left out.
- For a whole document: set `status: checked`, `git add` the record, send the
  `claim-auditor` the staged `documents/<slug>/checks.md` (its question: do the summary and
  Coverage follow from the rows, and does each note justify its verdict?), and **stamp its
  verdict before touching the file**, whatever the verdict.
  - `SOUND`, with or without minor wording points: commit as it is. Apply the minor points in
    a following commit; that needs no new review, since the gate's rule fires only when the
    status becomes `checked`.
  - A failing verdict: fix what it names, then review again. That is the review's second
    of three this cycle, so write the summary carefully the first time. Every sentence in it
    is a claim the auditor checks against the rows.
- **Report** from `bin/checks report <slug>`, in plain words. Never "the paper is correct":
  "the referee passed 27 of 30 results; it found a gap in Lemma 3.2 (...)", and what was not
  checked. Propose `accepted` to the owner; never set it.

## Unattended

- After every unit, update RESUME HERE in the document's README (the next unit, anything
  open). A fresh session continues from it.
- Ask only at a genuine fork. Stop at the re-review limit or an escalation trigger, record
  what is known, and go on to the next unit.
- The run ends at `checked` and the report, never at `accepted`.
