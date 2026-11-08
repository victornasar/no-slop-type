---
name: find-font
description: Pick typefaces from the user's no-slop-type catalog. Use when choosing a font, a font pairing, or typography for a project, or replacing an overused default like Inter.
argument-hint: <brief, e.g. "cozy bakery site">
---

The catalog lives at `~/code/no-slop-type`. Read `~/code/no-slop-type/AGENTS.md` and follow its
**Picking a font** steps for this brief, reading `~/code/no-slop-type/fonts.json` as the data:

$ARGUMENTS

When the brief is empty, infer it from the current project (its name, README, existing CSS and any fonts it
already loads) and say what you inferred.
