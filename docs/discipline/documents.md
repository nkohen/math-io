# Document folders: where each file goes

Open this when you are about to create a file and it is not obviously a source for the
literature wiki or a known result. The index is
[documents/_index.md](../../documents/_index.md).

## Why

A workspace that runs for months gathers hundreds of working files: papers being checked,
drafts, notes on a proof, briefs, check scripts. Dropped into one flat folder they cannot
be navigated: the next session cannot tell a live file from a superseded one, which
document a file belongs to, or what a finished piece of work established. Each kind of
file therefore has one home, and the home is the document it serves.

## Where each file goes

| What | Where |
|---|---|
| a document you verify, review, read or write | its own folder, `documents/<slug>/`, made with `bin/doc new` |
| what the document is, whose it is, where its text comes from | `documents/<slug>/document.toml` |
| the plan, RESUME HERE and progress log | `documents/<slug>/README.md` |
| text you did not write (a paper's LaTeX or PDF, a colleague's draft) | `documents/<slug>/source/`, filled by `bin/doc fetch` |
| your own writing: a draft, a write-up, proofs in progress, a staging record | the top of `documents/<slug>/` |
| what was checked, by whom, and what was found | `documents/<slug>/checks.md`, the check record (`bin/checks`; rules: [checking.md](checking.md)) |
| one statement and its proof, copied word for word for a reviewer | `documents/<slug>/units/<id>.md` |
| a small script that checks a computation for it | `documents/<slug>/checks/` |
| a brief for an agent, a throwaway note or check (never a manuscript) | `documents/<slug>/scratch/` (git ignores it) |
| a reviewer's verdict text | nowhere: pipe it into `bin/gate-stamp ... -`, which keeps it in `.gates/stamps.jsonl` |
| what a source says and what we take from it | the literature wiki (the `ingest` skill) |
| a standing note about how the workspace works | `notes/` (the workflow journal) |

**One folder per document, named for the document** (`documents/hartshorne-ch2/`,
`documents/my-survey-draft/`), not for a date or a session. A second pass over the same
document is a new section in the same README, not a new folder.
*Why:* a folder per document is what lets the next reader find everything about it in one
place.
*Anti-scope:* a one-step task that produces a single file does not need a folder; put the
file in the folder of the document it serves.

**`source/` holds only text someone else wrote, as they wrote it.** Never edit a file in it:
it is the text being checked or read, and `document.toml` records a hash of each file so a
changed copy shows. Your notes, corrections and write-ups go at the folder's top.
`source/` is committed like the rest of the workspace, so the workspace holds copies of
other authors' work and its remote must stay private (see COORDINATOR.md, "Ground rules").
A document made with `--local-source` (`commit = false` in `document.toml`) keeps its text
out of the history: git ignores its `source/`, and `bin/doc fetch` brings it back in a
fresh clone. `source/` is outside the commit gate.
The literature wiki keeps its own, stricter rule for background sources (`wiki/raw/`: the
text only when its license allows, else a pointer; the `ingest` skill): a document you work
on lives here, a source you only cite lives there.
*Why:* a clone should have every paper it works on, without a network; and text you did
not write is checked through the document's record, not by stamping reviews before a
commit.

**A draft kept outside the workspace** (`bin/doc new <slug> --external <path>`) is not
copied: `document.toml` records its path, and `bin/doc check` says when it is missing.
The commit gate cannot see it; its folder still holds the plan and every record about it.

**Keep the README current.** Its RESUME HERE names the exact next step; its `## Files`
section says what each file holds and whether it is a draft, reviewed or superseded.
*Why:* the README is what a fresh session reads instead of opening every file.

**Close a folder when its work ends.** Set `status: done` or `parked` in the README and in
`documents/_index.md`, and write the **Outcome**: what was established and at what
strength, what failed and why, and where each result now lives. A result that exists only
inside a document folder's scratch is not yet part of the workspace's record.
*Why:* an open folder whose work stopped weeks ago reads as live, and the next agent resumes
it.
*Anti-scope:* do not delete a closed folder's files; they are the record of how the result
was reached.

**Scratch is scratch.** Nothing in a `scratch/` folder may be cited or relied on: it is not
committed. Anything worth keeping moves out of it into the document folder; a manuscript
never starts there. A reminder fires when a `.tex` or `.bib` file is created in a
`scratch/` folder, and `bin/doctor` and the commit gate warn about a manuscript or a
week-old file left in one.
*Why:* git ignores `scratch/`, so a draft kept there is in no commit: it is lost with the
folder and invisible to every review.
