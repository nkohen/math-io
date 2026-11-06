# Coordinator brief: <one line naming the work>

RUN ON: strong tier (opus). This brief is for a coordinator that dispatches
workers; it is not itself a worker brief.

Continuation mode: report progress inline and continue through each landed milestone. End
a turn only at a genuine block (an input you lack), a fork only the owner can decide, or a
hard core you have already broken into sub-steps and attempted.

Placeholders are in angle brackets. Delete any section that does not apply.

## 0. Orient (read before anything else)

- `AGENTS.md`, then the files this work touches: <paths>.
- `git log --oneline -20` for what landed recently.

## 1. Where the work stands

<Three to six lines: what is established (with the file that records it), what is in
flight, what was tried and failed.>

## 1b. Front-loaded facts (verified only)

<Facts the workers will build on. Each one was checked by you, with the check named. A fact
you have not checked does not go here; it goes in a work item as something to verify.>

## 2. Work items

For each item:

```
### W<k>: <name>                         [cheap-parallel | deep]
Goal: <the finish line, stated so a worker can tell when it is reached>
Known (from the literature pass): <facts, conventions, named techniques, each sourced;
  status only as a fact>
Already ruled out / do not re-derive: <earlier negative results AND known symmetries or
  trivial cases of the object, so a fresh agent does not rediscover them as findings>
Bricks: 1. <...> 2. <...>
Worker or inline: <dispatch to a worker | coordinator inline, and why>
```

## 3. Operating disciplines

- **Tiers.** Dispatch execution to workers as whole bricks; keep design, analysis and
  record wording yourself. Answer a NEED-DIRECTION yourself; never forward it to the owner
  unless the choice is genuinely theirs.
- **Copy a worker's `CLAIM:` line verbatim** into your report and the record.
- **Verify returns firsthand.** Re-run a worker's check (its command, its known-answer
  case) before building on its result. A summary is not evidence.
- **Disagreements between reviewers** are settled on the facts, by you, with the fact named.
- **A result that overturns committed work** gets the hardest review available, and the
  affected records are flagged visibly until it is settled.
- **Long jobs are yours.** Workers validate and return commands; you run them.
- **Edits.** Commit with an explicit path list. Keep proven, proposed-but-unproven, and
  refuted statements visibly distinct in every record.
- **Stopping.** Before reporting any remaining work as large or blocked, list it as
  numbered bricks, attempt the cheapest, and state the hard step as an explicit hypothesis
  with everything around it finished.

## 4. First move

<The one concrete action to take first, usually: orient, then dispatch the
cheap-parallel items together.>
