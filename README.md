# math-io

A workspace in which AI agents help you **verify**, **review**, **read** and **write**
mathematics: check a proof or a whole paper, review a draft (yours or someone else's), work
through a paper or a book with a guide, and write up mathematics in LaTeX. It is not set up
for new research.

Agents propose and check; you decide. Separate reviewer agents check every claim before it
is recorded, and git keeps the history of everything.

## Get it

You need git, Python 3.11 or newer, and one of two agent programs. TeX is optional, needed
only to build PDFs.

| You use | Clone |
|---|---|
| Claude Code | `git clone https://github.com/nkohen/math-io.git` |
| Codex CLI | `git clone --branch codex https://github.com/nkohen/math-io.git` |

Then, in a terminal:

```
cd math-io
bin/setup
```

`bin/setup` asks your name, turns on the commit check, looks for TeX, runs the workspace's
self-check, and tells you how to start the agent and get going.

**Keep your copy private.** Your workspace will hold copies of the papers you add, which
you usually may not redistribute. Push it only to a private repository, never a public one.

## Learn more

- [docs/OWNER.md](docs/OWNER.md): your manual (the agent walks you through the first session,
  so you need not read it first).
- [AGENTS.md](AGENTS.md): the rules the agents follow.

math-io is built on [init-math](https://github.com/nkohen/init-math). MIT licensed; the
workspace and what you add to it are yours ([LICENSE](LICENSE)).
