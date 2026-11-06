# When a reflection fix is applied directly, and when it is asked first

A reflection pass ([reflection loop](../docs/discipline/reflection-loop.md)) drafts fixes
for recurring friction. This file decides, per fix, whether the agent applies it in the
pass (**AUTO**) or proposes it and waits for the owner's yes (**ASK**). It starts as a
default and is tuned by this project's own record: the tables below start empty and fill
as passes happen.

## AUTO: apply in the pass, report afterwards, when ALL hold

("AUTO-n" in a journal line means the n-th numbered clause below.)

1. **Additive and dismissible** — an advisory nudge, a scan or linter that only reports,
   a selftest, an edit to a template, a skill, a discipline doc, an agent file or the
   GLOSSARY. Never a blocking check on a path agents hit often.
2. **Narrow** — it fires only on the friction's own pattern; it adds no check to every
   commit or every turn.
3. **A repair or a recurrence** — it repairs an existing mechanism (a false positive
   narrowed, a pattern widened, a bug fixed), or it answers a friction that recurred **at
   least twice** despite existing prose. Never a new rule inferred from one incident.
4. **Tested and reversible** — self-tested through its real entry point (all four branches
   for a hook, [hook authoring](../docs/discipline/hook-authoring.md)) and undone by
   reverting one commit.
5. **When in doubt, nudge more rather than less** — a dismissible nudge that fires a little
   too often is cheaper than a missed failure; do not add "only when confident" exemptions.

## ASK: propose with the tradeoff, do not apply, when ANY holds

1. It edits **AGENTS.md** beyond a one-line pointer to a doc that carries the rule.
2. It **widens what runs unattended or what an agent may do**: permissions, allowlists,
   settings, anything an injected instruction could ride on.
3. It **adds automatic or scheduled behaviour** (a cadence, an end-of-turn hook that acts
   rather than reminds) or a **blocking** check.
4. It **encodes the owner's taste or the direction of the work** (what a good summary,
   exposition or next task is). Derive such rules with the owner from a concrete case first.
5. It **generalizes from one incident** onto a path everyone hits, or its collateral cost
   cannot be named.
6. It **removes or replaces** an existing mechanism.
7. It edits **notes/procedures.md**, the owner's standing procedures.

A fix on the boundary is ASK.

## Record

Fill these at each pass. They are what makes the rule above trustworthy (or not) for this
project.

**Outcomes per pass**

| date | AUTO applied | AUTO later reverted / narrowed | ASK accepted | ASK declined | ASK deferred |
|---|---|---|---|---|---|

**Every non-acceptance, by class**

| date | what was proposed or applied | what happened | class |
|---|---|---|---|

Classes:

- **A** — one incident turned into a rule on a frequent path.
- **B** — wrong place: the rule belonged in a doc or a template, not AGENTS.md.
- **C** — widened a permission.
- **D** — added automatic or scheduled behaviour.
- **E** — encoded taste or direction without the owner.
- **F** — timing: right idea, moot by then.
- **G** — redundant, or an agent error in applying it.
- **H** — the proposal did not state its cost.

## Keeping the rule honest

`git log --oneline --grep='reflect auto'` lists every auto-applied fix. If an auto-applied
fix draws a class A or C objection, AUTO was too loose for that kind of change: tighten the
clause above (an ASK-class edit to this file), don't just revert the fix. If, over several
passes, ASK proposals of some kind are always accepted unchanged, propose moving that kind
to AUTO — also an ASK.
