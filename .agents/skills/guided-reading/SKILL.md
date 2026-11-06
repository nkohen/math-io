---
name: guided-reading
description: Guide the owner through reading a paper, a chapter or a set of notes — explaining what the text says and does, filling in background, checking their understanding when they want — at their pace, picking up where the last sitting stopped. Load it when the owner wants to read, understand, study or work through a mathematical text with help.
---

# Guided reading

The owner reads; you guide. The point is their understanding, not a summary of the text.

## Starting, and coming back

- The folder: `bin/doc list`; if the text has none, `bin/doc new` it (`--whose other`) and
  `bin/doc fetch` its text into `source/`.
- **Coming back:** read RESUME HERE in the document's README. It says where the last sitting
  stopped and what was left open; start there, in a sentence.
- **First time:** ask what they want from the text (the main theorem's statement? its
  proof? a technique? enough to cite it?), what they already know, and how they like to work
  (you explain, or they read and ask). Record that in the README.

## While reading

- **Work from the text itself**, in `source/`. Quote statements exactly, and refer to them
  by their numbers.
- **Explaining is not a finding.** Saying what a passage says or does, why a step is there,
  where a definition comes from, or working an example is guiding, and needs no review.
  **Your own claim that a step holds, or fails, is a finding.** Do not make one in passing.
  Offer instead: "I can have the referee check that lemma" (the `verify` skill, on that one
  unit). **A worked example that settles the step is a verdict too**: set it as an exercise
  for the owner ("try $S_3$ with ..."), or offer `verify`; do not work it out for them.
- **Mark what goes beyond the text.** When you add a gloss, an intuition or a different
  route, say it is yours ("my reading, not the paper's"). A background fact you state comes
  from a source you have read, or is marked "from memory".
- **When they think something is wrong**, take it seriously, and offer `verify` on that
  unit instead of judging it yourself.
- **Check understanding when they want it**, never as a quiz they did not ask for: ask them to
  predict the next step, to try a small case, or to say the argument back in their own words.
- **Keep to their pace.** One section, or one proof, per sitting, unless they want more.
  Stop at natural breaks and ask whether to go on.

## Ending a sitting

Update RESUME HERE in the document's README, in a few lines:
- where you stopped (section, page or result);
- what they now understand;
- the questions left open.

That is the only record kept. The conversation itself is the reading. **Take notes only when
they ask**, in `documents/<slug>/notes.md`.
