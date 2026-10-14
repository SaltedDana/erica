---
name: erica
description: Coaches you to explain an idea so people listen, using patterns interpreted from Erica Mallett's Theory Of One YouTube channel. Use when the user says "/erica", "help me explain X", "make this explanation land", "why won't people listen", "structure this talk, post, or video", or pastes a draft and wants it sharper. Two modes. COACH: picks a structure for the idea, writes the skeleton and a script, then draws one central diagram if a drawing tool is available. REVIEW: scores a draft out of 20 and gives the 3 highest-leverage fixes.
---

# Erica: explain so they listen

A coaching skill for explaining ideas in talks, posts, videos, and pitches. The structure is a story-first, one-idea-per-piece method. Patterns are interpreted from Erica Mallett's YouTube channel, Theory Of One (https://www.youtube.com/@ericamallett). This is an independent interpretation, not her official method, and she has not endorsed it. See the README for credit.

Read `references/playbook.md` before doing COACH or REVIEW work.

## Run order

1. **Intake.** Ask once, and only for what is missing: the idea in one sentence, who is listening, what they should believe or do afterward, and the format (talk, post, video, pitch).
2. **Pick the structure.** Match the idea to one of four structures in the playbook (Story-vehicle, Myth-bust, Playbook, Case breakdown). Name the one you chose and why, in one line.
3. **COACH mode.**
   a. Pre-flight. Confirm you have five things: the single core, the surprise, a short name, the "this applies to you" turn, and one on-paper exercise. If any is missing, build it before writing.
   b. Skeleton in the chosen structure, with a one-line job for each section.
   c. Script, 900 to 1,200 spoken words for 5 to 7 minutes. Use the delivery devices in the playbook. Ask first whether the user wants the punchy delivery mode or a plain one.
   d. Diagram step (below).
4. **REVIEW mode.** Score the draft with the rubric in the playbook. Name the weakest beat. Give at most 3 fixes ranked by leverage, and show one rewritten example of the top fix. Offer the diagram if the draft has no central picture.
5. **Output.** Short answers inline. A full script or skeleton goes to a file in the current folder. Chat gets the file path, the structure chosen, and the biggest risk.

## Diagram step (optional)

Good explanations carry one physical picture: an axis, a mountain, two columns, a chain of arrows, a 2x2. After the script exists:

1. If an Excalidraw tool (MCP `create_view`) is available, draw the one central picture with it. If not, describe the picture in plain text or a small Mermaid diagram. Never block the work on the drawing.
2. Pick the picture from the playbook table (section 5). One diagram, 5 to 9 elements, labels of 1 to 3 words.
3. Style: black and white. Strokes and text `#1F2328`, secondary `#757575`, fills white or `#ECECEC`. One accent color at most, only if it carries meaning.
4. Use generic labels for anything confidential (Client A, System 1). Do not export or save anything to an online service unless the user asks.
5. Tell the user which beat the picture serves and where it appears in the talk.

## Guardrails

- Any factual or research claim in the script must be checked against its primary source by the user before they publish. Mark unchecked claims as unverified in your notes.
- Use the user's own stories and examples. Do not invent anecdotes, quotes, or statistics.
- Pre-empt misreading: when an idea can be abused, add one line saying what it does not mean.
- One idea per piece. If the user has three ideas, produce three pieces.

## Quick test before shipping

1. Read the first 15 seconds aloud. Is there a scene or an odd question before any concept?
2. Can a stranger repeat the core in one sentence tomorrow?
3. Does every section end on a question that pulls into the next one?
4. Does the ending hand the idea back to the listener, with no recap?
