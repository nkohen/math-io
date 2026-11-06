---
name: ingest
description: Ingest one source (a paper, preprint, chapter or talk) into the literature wiki so the next session can use it without opening it again — the raw record, the synthesis, the known-result entries, the indexes and the log, in one commit. Load it whenever a source enters the project: an inbox item, a reference a task turned up, a paper the owner mentions. A link pasted into a notes file is not an ingest.
---

# Ingesting a source

An ingest is finished when the next reader can use what the source says without opening it
again. Until then the source is only a link, and the next session reads it again or, worse,
works from memory. One source at a time; all of the steps below go into one commit.

## 1. The raw record: `wiki/raw/<slug>.md`

- **Pin the version** in the frontmatter (`title`, `source`, `ingested`, `summary`, as
  `wiki/raw/_index.md` says): an arXiv id with its version (`2401.14659v2`), a DOI, an
  edition and its page numbers. Results move between versions.
- **The text, when its license allows.** Commit the source's text below the frontmatter
  with `kind: text` when its license permits redistribution (a Creative Commons license, the
  public domain, the owner's own paper). For an arXiv paper the license is named on its
  abstract page. arXiv's own license (the arXiv.org perpetual, non-exclusive license) lets
  only arXiv distribute the paper, so a paper under it gets a pointer; commit the text only
  under a Creative Commons or public-domain (CC0) notice. `pdftotext -layout` (if
  installed) turns a PDF into text.
- **Otherwise a pointer, with its reason**: `kind: pointer` and `pointer-reason:` (the
  license does not permit redistribution, a paywall, a binary file). The body then records,
  as short quotes with their numbers, every statement the project uses: theorem, lemma and
  equation numbers, their hypotheses, the page. A pointer that only says "read Section 2"
  is not an ingest. Save the PDF or extracted text you read in `wiki/raw/local/<slug>.pdf`
  (or `.txt`), which git ignores, so a later session on this machine can read it without
  fetching it again; the pointer and its quotes remain the record.
- Never edit a raw file afterwards: if the extraction was bad, ingest it again as a new
  file and say so in the log. Add its row to `wiki/raw/_index.md`.

## 2. The synthesis: an article in `wiki/concepts/`

Skip this step for a source used for one stated result: the raw record's quote of it, with
its hypotheses and page, is enough, once the result is filed in step 3. Write the article when the project uses the source's method or a
second of its results.

What this project takes from the source, in the project's terms: each result it uses with
its hypotheses, the idea of the proof or method, how it bears on the work
that brought it in, and a `confidence` with its one-line reason. Cite the raw file under `## Sources`. Extend an
existing article when the idea already has one. A page in `wiki/references/` (a reading
list, a comparison table) may link the source too, but it collects sources; it does not
replace the article.

## 3. Known results: `wiki/known-results/`

File every result the source proves or observes about an object this project studies:
under that object's entry (create it from the template if there is none), with the theorem
number, the version, and the date accessed. This is what an agent looks up before trying
to prove something that is already known, so a result used only in `notes/` is lost.

## 4. Indexes, log, inbox

- A row in the `_index.md` of every folder you added a file to.
- One entry in `wiki/log.md`: `## [YYYY-MM-DD] ingest | <citation>`.
- If the source came from `wiki/inbox/`, delete its inbox note (never the raw file).

## Check, then commit

Run `bin/wiki-check`: it lists raw files that no concept article or known result cites, and
pointers with no reason. Fix what it lists, or, for a source deliberately left
unsynthesized, add its file name to `.wikiignore` with the reason in a comment. Then commit
the whole ingest together.

Why and the wider rules: [docs/discipline/literature-wiki.md](../../../docs/discipline/literature-wiki.md).
