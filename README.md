# erica

A Claude Code skill that coaches you to explain an idea so people listen. Give it an idea and it picks a structure, writes a skeleton and script, and (optionally) draws one central diagram. Give it a draft and it scores the draft out of 20 and tells you the three fixes that matter most.

## Credit

Created by Dana Maman.

This skill is built on my personal interpretation of the public YouTube videos of Erica Mallett, Theory Of One: https://www.youtube.com/@ericamallett

- It is based on public information and my own reading of 20 of her videos. It is not her official method.
- It is not affiliated with her and she has not endorsed it.
- Her scripts, transcripts, examples, and named frameworks are not reproduced here.
- Watch her channel and learn from the source.
- If Erica asks, I will remove the mention of her or the whole skill.

## Install

Copy the skill folder into your Claude Code skills directory:

```bash
cp -R skills/erica ~/.claude/skills/
```

Restart Claude Code, then type `/erica` or ask: "help me explain [your idea]". You can also paste a draft and ask for a review.

## What is inside

- `skills/erica/SKILL.md`: the workflow (coach mode, review mode, optional diagram step).
- `skills/erica/references/playbook.md`: four structures, nine beats, delivery devices, a 20-point rubric, diagram picks, and a worked example.

## Optional: diagrams

If you have an Excalidraw MCP server connected, the skill draws one black-and-white diagram of the central picture. Without it, the skill describes the diagram in text. Nothing breaks either way.

## Background

Story-first explanation, naming an idea, concrete scenes, and rhetorical devices such as repetition and contrast are long-standing teaching and speechwriting techniques. This skill packages them as a workflow.

## Limits

- It does not check facts. Verify every research claim against its primary source before you publish.
- The rubric and structures are a heuristic from a small sample of videos, not a tested method.

## License

MIT. See `LICENSE`.
