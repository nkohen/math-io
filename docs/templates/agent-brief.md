# Agent brief: <one line naming the task>

For ONE fresh agent doing ONE bounded task in a single turn. For several independent
threads use [dispatcher-brief.md](dispatcher-brief.md); for a brick list worked while the
owner is present use [worker-handoff.md](worker-handoff.md).

RUN ON: <strong tier (opus) | worker tier (sonnet)>, because <...>.

## Ground rules for this run

- **Run to completion in this turn.** Run every command in the foreground and wait for it.
  If a computation will not finish in time, make it smaller (fewer cases, a tighter limit);
  never detach it.
- **Write your summary early.** Create `<path to summary file>` near the start and update
  it as you go, so an interrupted run still leaves its findings on disk.
- **Stay in your lane.** Touch only `<paths>`. Other agents may be working on other files
  at the same time.
- Commit with an explicit path list, if this brief allows commits at all: <yes | no>.

## Front-loaded facts (verified)

<facts the task relies on, each with how it was checked>

## Task

Known (from the literature pass): <facts, conventions and named techniques, each sourced; the
status of the problem only as a fact>
Sub-goal: <the concrete statement to prove, construct or refute>

<what to do, item by item, each with its finish line>

## Discipline

- Check a tool on a known-answer case before trusting it on new cases.
- Keep raw values next to every derived pass/fail.
- Say exactly what your evidence covers and what it does not.

## Wrap-up (end your run with this)

1. A verdict per item: what was found, with the evidence.
2. The single most interesting finding.
3. The cheapest next step.
4. Honest coverage: what was checked, what was capped or skipped, and why.
