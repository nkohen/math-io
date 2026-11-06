# The check record: what was checked, by whom, and what was found

Open this when you check a proof or a document: one lemma for the owner, a draft, or a
whole paper with no one watching. The record is `documents/<slug>/checks.md`; the tool is
`bin/checks` (`bin/checks --help`); the template is
[docs/templates/check-record.md](../templates/check-record.md).

## Why

"I checked it" is worth nothing a week later unless it says what text was checked, by which
review, and with what result. The record ties every verdict to a stamp
(`bin/gate-stamp`), and a stamp to the exact text the reviewer saw (its git blob id). So a
verdict cannot be recorded without the review behind it, and a verdict on text that has
since changed shows as stale.

## What the reviewer is sent

- **Someone else's document, or your draft kept outside the workspace: unit files.** A
  **unit** is one statement with its proof (a lemma, proposition, theorem, or a claim inside
  a proof worth checking alone). Write each as `documents/<slug>/units/<id>.md` (ids `U01`,
  `U02`, ...) with three sections, copied word for word from the document:
  - `## Uses`: the exact statements the proof relies on (earlier results, definitions, cited
    theorems as the document quotes them), each labelled with where it comes from;
  - `## Statement`;
  - `## Proof`.

  Put no id, page or line number in the file: those go in the record's `where` column. Then
  the same lemma with the same proof and the same dependencies gives an identical file in
  any document, and `bin/checks reuse` finds an earlier review of it.
  *Why:* a reviewer judges one named file, and the file is what makes "this exact text"
  checkable and reusable.
  *Anti-scope:* never fix, shorten or modernize the document's text in a unit file. A unit
  file that differs from the document checks something the document does not say. From a
  PDF-only source the file is a transcription: say so in the row's note.
- **Your own draft in the workspace: the draft file.** Your draft's proofs are under the
  commit gate, which stamps the draft file itself. Send the proof-referee the draft, naming
  the draft file in the brief (for a long draft, also the section to review: the gate-chain's
  section extract), and record its stamp, which is on the draft file. There are no unit files and no
  reuse: your draft changes as you write.

`units/` and `source/` are outside the commit gate's proof rule: they are copies of text,
and a unit with a gap must still be recordable.

## Filling the record

1. `bin/checks init <slug>`.
2. Make **Coverage** list every numbered result in the document (theorem, lemma,
   proposition, corollary, claim), each with the unit that checks it or why it has none
   ("immediate from Thm 2.3", "no proof given").
   *Why:* without it, a run that made units of 12 of 30 results could honestly reach
   `checked`, and the record would overstate what was checked.
3. For each unit: write its unit file, `bin/checks add <slug> <id> --where "<where>"`, try
   `bin/checks reuse <slug> <id>`, and otherwise run the proof-referee on it (the gate-chain
   order), stamp the verdict, and `bin/checks set <slug> <id> <verdict> [--note "<quote>"]`.
   Before any review, `bin/checks fidelity <slug> <id>` confirms a unit's Statement and Proof
   are word for word in `source/` (LaTeX or text; a PDF-only source cannot be compared, so say
   "transcribed from the PDF" in the row's note).
4. List in **Assumptions** every cited result a proof relies on.
5. `bin/checks summary <slug>`, then the status (below).

**Unit verdicts** (`bin/checks set` refuses a verdict its stamp does not back):

| verdict | means | needs |
|---|---|---|
| `checked` | the proof holds | a passing proof-referee stamp (`CLEAN`, `CLEAN-MINOR`) on the text as it is now |
| `gap` | a real error or missing argument, including a cited result that does not apply (hypotheses fail, the statement does not cover the use) | a failing stamp; a note quoting the hit |
| `citation-missing` | sound, except that a standard fact is used without a source | a failing stamp whose only major hits ask for a source; a note quoting them |
| `unclear` | could not be confirmed either way: notation, an illegible step, a cited statement that could not be retrieved | a failing stamp; a note saying what would settle it |
| `open` | not reviewed yet | nothing |

**On someone else's document, `citation-missing` is not a failure**: published papers
leave standard facts uncited, and the referee asks for a source every time. On your own
draft it stands as the referee gave it, and before a draft is called finished, offer the
owner a strict pass that treats every citation request as a failure.

**Offline** (`bin/offline`), a cited statement the workspace does not already hold cannot
be retrieved: the unit is `unclear` and its assumption `assumed (not retrieved)`, the same as
when a search finds nothing.

**Assumptions** have one of three statuses: `assumed` (taken as the document quotes it; the
referee checks the quoted statement against its use, not the real theorem), `assumed (not
retrieved)` (the statement could not be found to quote), or `checked: <where>` (read
firsthand: a known-results file, a unit in another document).

## The red-team on main theorems

The red-team asks whether a statement is true; the referee whether its proof is right. The
`verify` skill sends it the main theorems. Its stamp goes on the unit file, and its verdict
in a line of the Summary's prose. A unit's row stays the referee's. A **REFUTED** statement
whose counterexample holds up (check it yourself) goes back to the referee: start a new
review cycle (`bin/gate-stamp --new-cycle`), send the unit again with the counterexample in
the brief, and record the row from that failing stamp. A counterexample that does not hold
goes under `## Disagreements`.

## Statuses

- `open`: checking in progress.
- `checked`: every unit has a verdict other than `open`; Coverage accounts for every
  numbered result; the summary's counts match; and the claim-auditor returned `SOUND` on the
  record itself. Its question there: does the summary and the coverage follow from the rows,
  and does each note justify its verdict? **An unattended run ends here.** `checked` means
  checked by reviewers, not correct: the summary says what was found, gaps included.
- `accepted`: the owner read the record and agrees. **Only the owner sets it**, with an
  `accepted-by:` line in the front matter (name, date). Propose it; never set it.

**The order for `checked`:** set `status: checked`, run `bin/checks summary`, `git add` the
record, dispatch the claim-auditor naming `documents/<slug>/checks.md`, stamp its verdict
**before editing the file again**, then commit. A `SOUND` with minor wording points is
committed as it is, and the points applied in a following commit (the gate's rule fires only
when the status becomes `checked`). An edit before the stamp makes the review stale and
spends one of the cycle's three reviews.

## What enforces it

- **`bin/checks verify`**, which the commit gate runs (`--staged`) on every staged record. It
  fails on a verdict its stamp does not back, a missing note, a unit file without a row or a
  row without its unit file, an open row or a coverage hole under `checked`, summary counts
  that do not match, and `accepted` without `accepted-by`. A unit whose text changed after its
  review fails under `checked` and warns while `open`. The gate runs it on any commit that
  touches a document folder with a record, not only on a commit of the record: **to edit a
  draft whose record is `checked`, set the record back to `open` in the same commit** (its
  rows go stale and are reviewed again), so the record never claims more than it covers.
- **A gate rule** (`[[gates.rules]]` in `project.toml`): a record whose status becomes
  `checked` needs a passing claim-auditor stamp on its staged content.
- **The record is stale, not false, when the document changes:** `bin/doc check` warns when
  someone else's text changes upstream (its hashes in `document.toml`), and `bin/checks
  verify` when a draft outside the workspace changes (`checked-text`). Re-extract the units
  whose text changed and review them again; the others keep their verdicts.
