# Documents

One folder per document you verify, review, read or write: someone else's paper, a
colleague's draft, your own write-up. Each holds the document's `document.toml`, its README
(plan, RESUME HERE, outcome), text you did not write in `source/`, your own writing at its
top, and throwaway files in `scratch/`, which git ignores. Rules:
[docs/discipline/documents.md](../docs/discipline/documents.md).

To start one, run `bin/doc new <slug> --title "<title>" --whose mine|other` (with
`--arxiv`, `--url`, `--file` or `--external` for where its text comes from); it adds a row
below. When the work ends, fill in its README's **Outcome** and change the row's status.

| folder | title | whose | status | what it is for, or what it established |
|---|---|---|---|---|
