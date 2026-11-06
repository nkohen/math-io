---
name: review-draft
description: Review a mathematical draft — the owner's own, or a colleague's they were asked to comment on — for correctness and for exposition, and write the review for its author in review.md in the document's folder. Informal review, not journal refereeing. Load it when the owner asks for feedback, comments or a review of a draft, paper or set of notes.
---

# Reviewing a draft

You are finished when `documents/<slug>/review.md` holds a review the owner could hand to
the author: what is wrong, what is unclear, what could be better, each point tied to where
it came from. Nothing is sent: the owner decides what goes to the author.

## 0. Before starting

- The folder: `bin/doc list`; if the draft has none, `bin/doc new` it, `--whose mine` for
  the owner's own and `--whose other` for a colleague's.
- Ask once:
  - **who the intended reader is** (and what they already know);
  - **what kind of feedback**: correctness, exposition, or both;
  - **how deep**: every proof, or the main ones;
  - any deadline.
- Checking every proof costs about one proof-referee run per result. Put the number in front
  of the owner before a full correctness review, as the `verify` skill says.

## 1. Correctness

Check the proofs in scope with the `verify` skill's steps, so that the document's check
record says what was checked:
- unit files for a colleague's draft;
- the draft file itself for the owner's.

The review then cites the record, and does not repeat its rows.

- **A colleague's draft:** a referee's request for a source for a standard fact is a
  **suggestion** ("you might cite ... for this"), never a defect.
- **The owner's own draft:** such requests stand, and before the draft is called finished,
  offer the strict pass (the `write` skill).

## 2. Exposition

Send the draft to the reader reviewers, naming the intended reader in each brief:
- `expositor`: can that reader learn from it, and reuse it?
- `cold-reader`: can a stranger with no context follow it?
- `provenance`: is each result's origin clear: new, the author's earlier work, or classical?

For a colleague's draft the file is in `source/`; stamp each reply anyway
(`bin/gate-stamp`), so the review's sources are on record.

## 3. The review: `documents/<slug>/review.md`

Written for the draft's author, plain and specific, kind and direct:

1. **Summary**: what the draft does, in two or three sentences, and the main concerns.
2. **Correctness**: each gap, with its place (theorem number, page) and why, as the referee
   put it. Each `unclear` point, with what would settle it.
3. **Exposition**: by section, from the reader reviewers.
4. **Minor**: typos, notation, references.
5. **Citations**: missing sources, as suggestions on a colleague's draft.

Every point comes from a review (named in a short source line: "proof-referee on Lemma 3.2")
or is marked as your own reading. Never state a point more strongly than its review did, and
never add one the reviews do not support without saying it is yours.

**One audit of the review.** When it is written, `git add` it and send the `claim-auditor` the
staged `review.md` (its question: does each point say no more than the review it names, and is
each credited to the right review?). **Stamp its verdict before touching the file**
(`bin/gate-stamp claim-auditor documents/<slug>/review.md <VERDICT> -`), whatever it is. Then
apply every point it makes, and do not send the review to it again: its fixes weaken or
re-attribute a point, which cannot make the review claim more. If a point cannot be fixed
that way (a claim no review supports), cut it or mark it as your own reading. Tell the owner
the verdict and what you changed.

## 4. Hand over

Tell the owner what the review found, in a few lines, and where it is. For a colleague's
draft, the owner sends it, edits it, or drops points; never send anything. For the owner's
own draft, offer to make the changes (the `write` skill).
