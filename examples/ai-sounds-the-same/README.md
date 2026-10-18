# Example: why AI-written posts all sound the same

This folder holds one real run of the skill, from a fresh install with no personal setup.

- `script.md`: the spoken script the skill wrote, with a Mermaid diagram.
- `sources.md`: every claim in the script with its status.
- `raw/`: the 8 saved model outputs behind the numbers (`plain-1` to `plain-5`: no context; `context-1` to `context-3`: with a made-up consultant's voice sample).

Test details: one model (claude-sonnet-5-5), one prompt, 2026-10-18, 5 runs without context and 3 with. The prompt was: "Write a LinkedIn post of about 90 words for a business owner on why teams need a shared knowledge base. Output only the post." For the context runs the prompt began with three short lines of a made-up consultant's writing and two facts about her firm.

The sample is small. Treat the counts as an illustration, not a measurement.
