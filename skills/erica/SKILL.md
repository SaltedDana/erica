---
name: erica
description: Coaches you to explain an idea so people listen, using patterns interpreted from Erica Mallett's Theory Of One YouTube channel. Use when the user says "/erica", "help me explain X", "make this explanation land", "why won't people listen", "structure this talk, post, or video", or pastes a draft and wants it sharper. Two modes. COACH: picks a structure for the idea, writes the skeleton and a script, then draws one central diagram if a drawing tool is available. REVIEW: scores a draft out of 20 and gives the 3 highest-leverage fixes.
last_update: 2026-10-19 09:42
---

# Erica: explain so they listen

Last updated: 2026-10-19 09:42

A coaching skill for explaining ideas in talks, posts, videos, and pitches. The structure is a story-first, one-idea-per-piece method. Patterns are interpreted from Erica Mallett's YouTube channel, Theory Of One (https://www.youtube.com/@ericamallett). This is an independent interpretation, not her official method, and she has not endorsed it. See the README for credit.

Read `references/playbook.md` before doing COACH or REVIEW work.

## Run order

1. **Intake.** If the user gave only the idea, ask for the missing items in one message before writing anything: who is listening, what they should believe or do afterward, the format (talk, post, video, pitch), and how long it should be (a target or a maximum, if any). Do not assume them. If you cannot ask (non-interactive run), state your assumptions on the first line of the output and continue.
2. **Find the insight first.** Before any structure, write a working brief: the observation (what odd thing was noticed, the "that's weird"), the core claim, the tension (what the obvious explanation misses), the anchor example the listener can inspect, and the payoff for the listener. The source videos start from a noticed oddity and an example that breaks an expectation, never from a framework. If the idea has no observation yet, ask for one.
3. **Pick the structure.** Match the idea to one of four structures in the playbook (Story-vehicle, Myth-bust, Playbook, Case breakdown). Name the one you chose and why, in one line.
4. **COACH mode.**
   a. Pre-flight. Confirm you have six things: the single core, the surprise, a short name, the "this applies to you" turn, one on-paper exercise, and the anchor example from step 2. If any is missing, build it before writing. The name must map parts of the idea (a mountain with base camp, tents and a first step), not only sound good.
   b. Skeleton in the chosen structure, with a one-line job for each section.
   c. Metaphor check on the central vehicle or picture: what maps to what, what the listener might wrongly infer, and whether the explanation still stands without it. The mechanism beat must explain the real relationship, not restate the metaphor as fact.
   d. Script in the user's language. Length has no fixed target: the idea sets it. If the user gave a duration, write to it. If they gave none, write the shortest version that still carries every beat (scene, name, steps, exercise, hand back) and offer to expand. Lean short: when a script runs over, cut repetition, decoration and extra terms first. Protect the anchor example and the beats, and never pad. For reference, the source videos run 5 to 7 minutes; other speakers differ, so ask for the speaker's pace or time a paragraph aloud. Count the spoken words (leave out headings and notes) and report the estimated speaking time. Use the delivery devices in the playbook. Ask first whether the user wants the punchy delivery mode or a plain one, or state which you chose.
   e. Specificity pass. Read the draft sentence by sentence. Mark every sentence that any other speaker could say about this topic. Replace each with a specific detail (a number, name, place, mistake, or the user's own observation) or cut it. If the detail has to come from the user's life, ask for it. Do not fill the gap with an invented one.
   f. Diagram step (below).
5. **REVIEW mode.** Score the draft with the rubric in the playbook. Name the weakest beat. Give at most 3 fixes ranked by leverage, and show one rewritten example of the top fix. Offer the diagram if the draft has no central picture.
6. **Output.** Short answers inline. A full script or skeleton goes to a file in the current folder. Chat gets the file path, the structure chosen, and the biggest risk.

## Diagram step (optional)

Good explanations carry one physical picture: an axis, a mountain, two columns, a chain of arrows, a 2x2. After the script exists:

1. If an Excalidraw tool (MCP `create_view`) is available, draw the one central picture with it. If not, put a small Mermaid diagram of the picture in the script file at the point where it appears, not just a sentence about it. Never block the work on the drawing.
2. Pick the picture from the playbook table (section 5). One diagram, 5 to 9 elements, labels of 1 to 3 words.
3. Style: black and white. Strokes and text `#1F2328`, secondary `#757575`, fills white or `#ECECEC`. One accent color at most, only if it carries meaning.
4. Use generic labels for anything confidential (Client A, System 1). Do not export or save anything to an online service unless the user asks.
5. Tell the user which beat the picture serves and where it appears in the talk.

## Guardrails

- Any factual or research claim in the script must be checked against its primary source by the user before they publish. List each claim with a status (verified against a source you opened, or unverified) in a separate sources file, never inside the script. Claims about a product, plan, or price need a source you opened in this session. If you have web tools, open the vendor's official documentation and check them before writing the script; if you cannot, mark them unverified.
- Use the user's own stories and examples. Do not invent anecdotes, quotes, or statistics. Never invent a personal story, client scene, or lived experience, in first person or second: personal stories are proof in the source videos, so a made-up one breaks the method. If the opening needs a scene and the user has none, write it as an explicit hypothetical ("imagine...") and say so, or ask for a real one.
- Pre-empt misreading: when an idea can be abused, add one line saying what it does not mean.
- One idea per piece. If the user has three ideas, produce three pieces.

## Quick test before shipping

1. Read the first 15 seconds aloud. Is there a scene or an odd question before any concept?
2. Can a stranger repeat the core in one sentence tomorrow?
3. Does every section end on a question that pulls into the next one?
4. Does the ending hand the idea back to the listener, with no recap?
5. Could a different speaker say every sentence? If yes, run the specificity pass again.
6. Is there an example the listener can inspect, not only a metaphor about the topic?
