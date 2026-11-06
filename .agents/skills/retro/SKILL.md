---
name: retro
description: End-of-session retrospective — list the feedback the owner had to give (corrections, guardrails written into prompts, reasons only they knew), log it, and ask what standing structure would have produced that feedback without them. Offer it in one line at the end of every session in which the owner corrected or redirected you; load it when the owner accepts, or asks for a retro. Never mid-task.
---

# Retrospective

A reflection pass (the `reflect` skill) works from what was *logged*. A retro works from
what the owner had to *say*: every correction, prompt guardrail or missing reason is a
place where the project's standing structure fell short. At the end of every session in
which the owner corrected or redirected you, offer one in a single line ("You corrected me
on N points this session; run a retro?") and run it if the owner accepts; an unanswered
offer is declined. Run it at a stopping point. If, once you look, the owner gave no
substantive feedback, say so in one line and stop; never log an empty retro.

## 1. Gather the owner's messages

The main evidence is this session's conversation.
This harness's saved-session format is not documented, so earlier sessions are not read
directly. For them, use what was recorded: read `logs/feedback.jsonl`, the
`logs/friction.jsonl` rows with `"source": "owner"`, and `notes/workflow-journal.md`
directly (not with `bin/journal --show-new`, which belongs to the reflection pass). Since
the last retro means since the last `RETRO` line, or the project's first commit date if there
is none.

Skip anything already in `logs/feedback.jsonl` or logged as friction: the reflection loop
already has it, and counting it twice inflates the cluster.

## 2. Label each item

One line per item, faithful to the owner's words (no softening — the list is evidence).
Start each with one label:

- **Pre-emptive guardrail** — the owner wrote an instruction into a prompt to stop
  something *before* it happened ("read each file before moving it", "ask me before
  deciding X"). The most valuable kind: the fix arrives already stated.
- **Rationale** — the owner supplied a reason recorded nowhere (why an artifact is kept,
  what a step is for). The decision was answerable only because they were present.
- **Reactive** — a correction or complaint after the fact.
- **Self-observed** — you noticed it, the owner did not complain, but it shaped what they
  decided (a wrong premise they acted on).

An item that fits none is written without a label; a wrong label is worse than none.

## 3. Ask the counterfactual question

> What reasonable change to this project's standing structure would have made it likely
> that this feedback was produced without the owner?

- **Structure, not instances.** "Fix the thing they pointed at" is not an answer (that
  presumably happened). Name the class: which doc, check, template field, convention or
  workflow step would have caught every comment of this kind.
- **Each answer names the items it would have absorbed.** An answer mapping to none is
  speculation; drop it.
- **They are predictions.** Present them as untested hypotheses, not findings.

## 4. Log before presenting

So nothing is lost if the session ends now:

```bash
bin/journal --add feedback "<item text>" --kind correction --label <preemptive|rationale|reactive|self-observed>
bin/journal --propose "<change> — would have absorbed: <items> — costs: <cost>" --source retro
```

One `feedback` row per item, one proposal per counterfactual (`--propose` queues it for
the owner's decision and writes its `RETRO` journal line). Item type to
`--kind`: pre-emptive guardrail, rationale, reactive and self-observed items are
`--kind correction` (with `--label` preemptive, rationale, reactive, self-observed);
something the owner said worked well is `--kind praise`; a gate bypass is `--kind bypass`.
An item that fits no label goes in as a `journal` line instead.

Then mark the retro done, even when it proposed nothing, so the next retro starts here:

```bash
bin/journal --add journal "retro done: <n> items, <m> proposals" --kind RETRO
```

## 5. Present 2–4 changes

Rank by how many items each would have absorbed. For each: what would improve, what it
costs, and whether it is AUTO or ASK under `notes/reflect-autonomy-heuristics.md`. **Apply
none of them unprompted** — the owner decides, and an endorsed change is ordinary directed
work from there. Reread your list as the owner will, without this session's context, and
spell out every reference to its events.

Present them numbered, with the proposal ids, at the end of your reply, so the owner can
answer "yes to 1 and 3"; then run `bin/journal --shown`. Record each answer with
`bin/journal --decide <id> yes|no`. A "continue" is not an answer: the proposals stay
pending and come back at a later stop. The journal, the proposal queue and your message
are the retro's record: do not write it up in a separate notes file, where no one will
decide it.
