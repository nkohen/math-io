# The known-results catalog

Open this before you test or try to prove something, when you read a paper or a catalog
page about an object the project studies, and when you are about to say "this is new".
The catalog lives in [wiki/known-results/](../../wiki/known-results/_index.md); terms are in
[GLOSSARY.md](../../GLOSSARY.md).

## Why a catalog

This catalog records what is already known about the objects we study.
Without it, the same search is run again every few weeks, a settled question gets a week
of work, and a classical result gets written up as new.

## Rules

**File results by the object they are about.** One file per object of study (a named
sequence, a family of graphs, a class of curves), named for the object plus its catalog id
when it has one (an OEIS A-number, an LMFDB (the L-functions and modular forms database) label, a House of Graphs id). Results about a
whole class go in a family file, `family-<topic>.md`.
*Why:* a lookup starts from the object you are computing on ("what is known about this
sequence?"), not from a paper.
*Anti-scope:* a general method or technique with no particular object is not a known result
about anything here; it belongs with the sources it came from.

**Record the source, the theorem or section, and the date accessed.** For a paper: authors,
title, year, and the theorem number or section. For an online catalog page: the id, the
date accessed, and the part of the page the fact came from (comments, formulas,
references).
*Why:* the reader must be able to find the exact statement. Online catalogs change, so the
date is the provenance.
*Anti-scope:* the project's own results do not go here; they live with their evidence
in the project's own notes.

**State the result with the source's hypotheses, never stronger.** Copy the scope exactly:
the parameter range, the conditions, "for all sufficiently large n", "assuming GRH", where GRH is the generalized Riemann hypothesis.
*Why:* a result whose scope grows one notch in each retelling ends up "settling" cases it
never covered.
*Anti-scope:* you may restate it in the project's notation, as long as the content is
unchanged.

**A claim with no source you have read is a seed to verify, not a fact.** Catalog comments
and formulas with no reference, a remark in a talk, a sentence in a survey, and a search
agent's summary of a paper all go under "Seeds to verify", with where each was seen. Move
one up to Results only after you have read the statement in its source, corroborated it, or
checked it yourself (the `read:` values below).
*Why:* crowd-sourced and second-hand statements are often right and sometimes wrong, and
the wrong ones are expensive once something is built on them.
*Anti-scope:* a seed is still useful: it can suggest where to look, or a quick check.

**Mark how you read the statement.** `read: firsthand` means you opened the source and read
the theorem (the owner reading it for you counts: `read: firsthand (the owner, <date>)`).
`read: corroborated (<A>; <B>)` means the source was out of reach (a textbook with no
copy at hand) and two independent sources restate the theorem with its hypotheses: a paper
or preprint that quotes it, a MathSciNet or zbMATH review, a reference work such as the
Stacks Project or the LMFDB. `read: checked (<how>)` means
you verified the statement yourself (a proof written out, a computation) and say how. A
result known only from someone's summary is not a Result: it stays under Seeds to verify.
*Why:* a theorem number attributed by a summary is a reading of the paper, not a fact. Two
restatements that agree on the hypotheses are a check on the reading; one is not.
*Anti-scope:* the citation stays the original source in every case: a corroborated
textbook theorem is cited to the textbook, and the restatements are how it was checked,
recorded here, never cited in its place. A firsthand or corroborated
reading is required before a result is quoted to a reviewer or cited in a write-up. None of this is needed before a claim is filed under Seeds to verify.
The general rule for checks like this is in `docs/discipline/firsthand-checks.md`.

**Look here before testing, proving, or claiming novelty.** Search the catalog for the
object and for the property before designing a check, and before writing that a result
is new. A general lemma, inequality or method has no object, so it is not here: search
the literature articles in `wiki/concepts/` for the statement or method too. If the catalog has nothing, that is not proof the result is unknown: it means the
literature search has not been done yet.
*Why:* re-deriving a known theorem costs a session, and calling it new costs credibility.
*Anti-scope:* a quick sanity computation (seconds) does not need a catalog search first.

**Add to entries; do not rewrite them.** When a source turns out wrong, superseded, or
narrower than recorded, add a dated note to the entry and keep the original line. When the
note says the result is wrong, superseded or narrower, also prefix its heading with
`SUPERSEDED <date>:` or `NARROWED <date>:` (the original wording stays).
*Why:* the history of what was believed explains past decisions, and the prefix stops a
reader who scans only the headings from picking up a statement since found wrong.
*Anti-scope:* typos and formatting can be fixed in place.
