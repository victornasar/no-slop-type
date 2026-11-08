# AGENTS.md

This repo is a catalog of free, self-hostable typefaces chosen to avoid the look of AI-generated sites.
`fonts.json` is the single source of truth: its `vocab` defines every tag, `fonts` holds the catalog, and
`avoid` lists the overused defaults with replacements. The repo stores no font files.

Two branches:

- **Picking a font for a brief** → follow [Picking a font](#picking-a-font).
- **Changing the catalog** → follow [Editing the catalog](#editing-the-catalog).

---

## Picking a font

You get a brief ("a cozy bakery site", "body font for our docs", "logo for a synth brand"). You return a
ranked recommendation. You recommend only: downloading files and editing the user's project are out of scope
unless the user asks afterwards.

### 1. Read the brief

Work out three things:

- **Roles**: which `use` tags the brief needs. A website usually needs two roles, `headlines` plus `body`
  (or `ui` for an app). A logo needs `logos`. A code editor needs `code`.
- **Feel**: one or two `feel` tags, inferred from the brief's words. See [Feel words](#feel-words).
- **Hard constraints**: languages (map to `scripts`), whether the project's repo is public (affects Fontshare,
  see [Licenses](#licenses)), and any font the brief names.

Ask one short question only when the roles cannot be inferred. Feel is always inferred; a wrong guess shows up
in the alternatives.

Done when: every role has a `use` tag, there are one or two `feel` tags, and constraints are listed.

### 2. Filter

For each role, keep fonts from `fonts.json` where:

- the role's `use` tag is in the font's `use`;
- every required script is in the font's `scripts`;
- for `body`: `italics` is `true` and there are at least two `weights`;
- for `ui`: at least three `weights`.

Done when: each role has a candidate list.

### 3. Rank

Order each role's candidates by, in priority:

1. **Use fit**: the role is the font's *first* `use` tag beats second beats third.
2. **Feel fit**: shares the brief's primary feel, then its secondary feel. A font's first `feel` tag counts most.
3. **Fewest caveats** that bite this brief (read `caveats`).
4. **OFL over FFL** when the repo is public or the brief needs the fonts in a shared design tool.

Fonts with `"review": true` are allowed; mention that their tags are unreviewed.

Recommend fonts from `fonts.json`. When nothing fits, say so plainly, then name at most one outside font,
marked **outside the catalog, license unverified**.

Done when: each role has a top pick and two alternatives.

### 4. Pair (only when there are two or more roles)

Build the top combination with these rules:

- **Contrast category**: serif headline with sans body, or sans headline with serif body. A single family
  with a wide weight range (Switzer, Source Serif 4, IBM Plex) is also a good pair.
- **Share a feel**: the two fonts have at least one `feel` tag in common, or one is `neutral`.
- **One voice**: at most one font in the pair is `loud`, `experimental` or `playful`. The other stays quiet.
- **Code is separate**: a `code` font sits beside the pair and follows the same "share a feel" rule.

Done when: the pair satisfies all four rules, or you state which rule it bends and why.

### 5. Answer

Use this shape, nothing longer:

```
**Top pick:** <Font> for <role> (+ <Font> for <role>)
<One sentence: why it fits the brief, in the brief's words.>

| | Font | Why | License | Get it |
|---|---|---|---|---|
| 1 | ... | ... | OFL / FFL + limit | <url> |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

**CSS**
<@font-face for the top pick + font-family with the fallback stack>

**Replaces:** <avoid-list font this stands in for, if the brief or project uses one>
**Notes:** <unreviewed tags, caveats that bite, Fontshare limits>
```

For FFL fonts the License cell always says: *"Fontshare: self-host only, keep files out of public repos."*

### Feel words

Map the brief's words to `feel` tags. Examples, not an exhaustive list:

| Brief says | Feel |
|---|---|
| cozy, friendly, approachable, human, community | `warm` |
| clean, minimal, calm, professional, trustworthy | `neutral` |
| dev tool, data, engineering, precise, infrastructure | `technical` |
| books, essays, scholarly, long reads, calm reading | `literary` |
| magazine, journalism, opinionated, culture | `editorial` |
| luxury, fashion, refined, beauty, wedding | `elegant` |
| bold, punchy, sports, events, protest, brutalist | `loud` |
| fun, kids, quirky, cheeky, games | `playful` |
| art, gallery, avant-garde, zine, music, weird | `experimental` |
| nostalgic, vintage, 8-bit, varsity, medieval, 70s | `retro` |

### Fallback stacks

Append to the `font-family` of every recommendation:

- sans: `system-ui, -apple-system, "Segoe UI", sans-serif`
- serif: `Georgia, "Times New Roman", serif`
- mono: `ui-monospace, "SF Mono", Menlo, Consolas, monospace`
- display: the sans or serif stack, whichever the letter shapes resemble

### Licenses

- **OFL**: free to use, modify, subset and redistribute. Keep the OFL license file next to the font files.
- **FFL** (Fontshare, `url` on fontshare.com): free commercial use and self-hosting. The files stay
  out of public repos and stay unmodified: use the `.woff2` from the zip's `Fonts/WEB/fonts/` folder as-is.
  Each designer or contractor downloads their own copy.
- Every recommendation is self-hosted. Font CSS points at the project's own files, never at
  `fonts.googleapis.com`, `fonts.gstatic.com` or `api.fontshare.com` (the Munich GDPR ruling; see README).

### Where the files come from

Include the matching line in the answer so the user can fetch the files:

- **fontshare.com/fonts/…**: "Download family" → zip → `Fonts/WEB/fonts/*.woff2`.
- **github.com/…**: the latest release's assets; look for a `webfonts` or `woff2` folder, plus `OFL.txt`.
- **gitlab.com/velvetyne/…**: the repo's `fonts/` folder (OTF, TTF and often WOFF2).
- **velvetyne.fr**: was redirecting to a strike notice in Nov 2026. Most families are also at gitlab.com/velvetyne.
- **Other sites** (commitmono.com, departuremono.com, brailleinstitute.org): the site's download button.

---

## Editing the catalog

1. Edit `fonts.json` only. The README catalog is generated.
2. Use tags from `vocab` only, 1–3 per `feel` and `use`, primary tag first. Adding a tag to `vocab` is a
   decision for the user; ask first.
3. Take `weights`, `italics`, `variable` and `scripts` from a source (the foundry's files, the Fontshare
   API at `api.fontshare.com/v2/fonts`, or the Fontsource API at `api.fontsource.org/v1/fonts/<id>`), never from
   memory. Set `"review": true` on any font whose tags are your judgement and haven't been checked by the user.
4. Write `note` as one or two plain sentences on what it feels like and what it's for. Name the overused
   font it replaces when there is one ("an alternative to Inter").
5. `url` is the font's source page, never a CDN.
6. Run `python3 scripts/build.py`. Done when it prints `✓` and `python3 scripts/build.py --check` passes.
