# no-slop-type

A short, opinionated catalog of free typefaces that don't make a site look AI-generated, tagged by feel
and use so an agent (or you) can pick the right one fast. Every font is free for commercial use and meant
to be **self-hosted**: no Google Fonts CDN, no third-party requests. The repo stores no font files.

- **Agents:** start at [`AGENTS.md`](AGENTS.md). From any project, `/find-font <brief>` runs it.
- **Humans:** browse the catalog below, grouped by use and by feel.
- **Editing:** change [`fonts.json`](fonts.json) only, then run `python3 scripts/build.py`. It validates the
  data and regenerates the catalog part of this README.

| File | What it is |
|---|---|
| `fonts.json` | The catalog: tag vocabulary, fonts, and the avoid list. The only file you edit by hand. |
| `AGENTS.md` | How an agent picks a font from a brief. |
| `scripts/build.py` | Validates `fonts.json` and regenerates this README's catalog. `--check` to verify only. |
| `scripts/no-google-fonts.sh` | Fails if a project hotlinks Google Fonts or the Fontshare CDN. |
| `scripts/eval.py` | Runs the briefs in `evals/briefs.json` through `/find-font` and checks the picks. Uses Claude calls. |
| `scripts/check_links.py` | Checks every font link is alive and Fontshare facts still match. Needs the internet. |
| `tests/` | Validator tests: `python3 -m unittest discover -s tests` |
| `starter/fonts.css` | Copy-paste `@font-face` setup for self-hosting. |

After cloning, run `git config core.hooksPath .githooks` once. The pre-commit hook then blocks commits with an
invalid or out-of-date catalog.

**When to run what:** the hook covers every commit. Run `scripts/eval.py` after changing `AGENTS.md`, the tag
vocabulary or many tags at once. Run `scripts/check_links.py` every month or so.

---

## Why not Google Fonts?

In January 2022 the Munich Regional Court (LG München I, case 3 O 17493/20) ruled that a site loading
Google Fonts from Google's servers broke the GDPR. Every page view sends the visitor's IP address to
Google, and the visitor hasn't consented. The court awarded the visitor €100, and a wave of cease-and-desist
letters followed.

The ruling is about **hotlinking** (`fonts.googleapis.com` / `fonts.gstatic.com`), not the fonts. An OFL font
that also appears on Google Fonts is fine when you serve the files from your own domain. This repo still
prefers each font's upstream source (the foundry or its GitHub) over the Google copy.

If you have no choice but a CDN, [Bunny Fonts](https://fonts.bunny.net) is a GDPR-oriented drop-in
replacement with the same API. Self-hosting is still better.

---

## Fontshare rules

Fontshare fonts (license `FFL`) are not open source. They use the ITF Free Font License (v2.0, August 2026),
which ships as `License/FFL.txt` in every download. In short:

- **Allowed:** personal and commercial use in any medium; self-hosting with `@font-face` on your own sites
  and apps; logos and wordmarks (which you can trademark); embedding in PDFs and apps. Credit is optional.
- **Not allowed:** redistributing the files anywhere (public git repos, npm packages, other font sites);
  modifying them, including subsetting, format conversion or renaming; handing the files to a contractor
  (they download their own copy); offering the font as a selectable option in a tool other people use.

That means:

- Never commit Fontshare files to a public repo. Keep them out of version control, or in a private repo
  used only for your own site.
- Use the `.woff2` files from the zip's `Fonts/WEB/fonts/` folder as they are. Don't subset or convert them.
- Don't use Fontshare's own CDN (`api.fontshare.com`) either. It sends visitor IPs to a third party, the
  same problem as the Google Fonts ruling. Self-hosting is explicitly allowed and recommended in the license.

---

## Where to find more

- [Velvetyne](https://velvetyne.fr): French libre foundry; weird, expressive, all OFL. Sources also on [GitLab](https://gitlab.com/velvetyne)
- [Collletttivo](https://www.collletttivo.it): Italian open-source type collective
- [The League of Moveable Type](https://www.theleagueofmoveabletype.com): the original open-source foundry
- [Use & Modify](https://usemodify.com): curated libre fonts
- [Uncut](https://uncut.wtf): free and open-source typefaces
- [Badass Libre Fonts by Womxn](https://www.design-research.be/by-womxn/): libre fonts designed by women
- [Fontshare](https://www.fontshare.com): Indian Type Foundry's free catalog (see the rules above)
- [Fontsource](https://fontsource.org): npm packages for self-hosting open fonts
- [tfam.io/type](https://tfam.io/type): good for *finding* a vibe, but it searches the Google catalog. Self-host whatever you pick.

---

## Using a font

1. Download the `.woff2` files from the font's source into your own project (e.g. `fonts/`).
2. OFL fonts: keep the license file next to them. Fontshare fonts: follow the rules above.
3. Copy `starter/fonts.css` into your project, edit it, and link it from your page.
4. Run `scripts/no-google-fonts.sh path/to/your/project` to check nothing still hotlinks Google or Fontshare.

Licenses can change. Check the font's own license before you ship.

---

<!-- catalog:start (generated by scripts/build.py, do not edit) -->

## By use

Fonts whose *primary* use is the job are listed first.

### body

Long reading text: articles, docs.

- [Source Sans 3](https://github.com/adobe-fonts/source-sans): *sans*, neutral, warm. Adobe's calm humanist workhorse with wide language support. An alternative to Open Sans.
- [Ranade](https://www.fontshare.com/fonts/ranade): *sans*, neutral, editorial (FFL). Neo-grotesque with high-contrast diagonals, a little kick that sets it apart from Helvetica clones.
- [Author](https://www.fontshare.com/fonts/author): *sans*, warm, literary (FFL). Slightly wide humanist sans made for publications. Roomy, readable, a sans that likes books.
- [Plein](https://www.fontshare.com/fonts/plein): *sans*, warm, neutral (FFL). Monolinear humanist sans with open, pleasant forms. An alternative to DM Sans.
- [Source Serif 4](https://github.com/adobe-fonts/source-serif): *serif*, literary, neutral. Sturdy transitional serif with an optical-size axis, so it looks right from captions to headlines.
- [IBM Plex Serif](https://github.com/IBM/plex): *serif*, technical, literary. A serif with an engineer's precision; pairs naturally with Plex Sans and Plex Mono.
- [Libertinus](https://github.com/alerque/libertinus): *serif*, literary. Classic old-style book face with huge language coverage and a math companion. For essays, papers, long reads.
- [Junicode](https://github.com/psb1558/Junicode-font): *serif*, literary, retro (unreviewed). A scholar's serif built for medievalists, with weight and width axes. Old-world without being a costume.
- [Sorts Mill Goudy](https://github.com/theleagueof/sorts-mill-goudy): *serif*, literary, warm. A revival of Goudy Oldstyle: warm, bookish, early-20th-century American printing.
- [Linden Hill](https://github.com/theleagueof/linden-hill): *serif*, literary, elegant. A revival of Goudy's Deepdene: graceful, slightly calligraphic old-style serif.
- [Gambetta](https://www.fontshare.com/fonts/gambetta): *serif*, editorial, literary (FFL). Text serif with diagonal stress and contrast that grows with weight. Newspaper-grade reading.
- [Sentient](https://www.fontshare.com/fonts/sentient): *serif*, literary, warm (FFL). Slightly wide, robust serif for immersive long reading. Holds up at small sizes.
- [Recia](https://www.fontshare.com/fonts/recia): *serif*, neutral, literary (FFL). Low-contrast, slightly condensed contemporary serif with true cursive italics. A serif that works on screens.
- [Bespoke Serif](https://www.fontshare.com/fonts/bespoke-serif): *serif*, literary, neutral (FFL). Wedge-serif text face with big open counters, designed for reading.
- [iA Writer Mono / Duo / Quattro](https://github.com/iaolo/iA-Fonts): *mono*, literary, neutral. Plex Mono reworked for writing. Duo and Quattro are duospace and quattrospace, so prose reads more naturally than in a true mono.
- [Atkinson Hyperlegible Next](https://www.brailleinstitute.org/freefont): *sans*, warm, neutral. Made for low-vision readers: every confusable letter (I l 1, O 0) is distinct. A humane alternative to Inter for UI.
- [Public Sans](https://github.com/uswds/public-sans): *sans*, neutral. The U.S. government's plain, dependable grotesque. An alternative to Inter or Roboto with less baggage.
- [IBM Plex Sans](https://github.com/IBM/plex): *sans*, technical, neutral. Corporate-engineered grotesque with small quirks that keep it from being bland. Pairs with Plex Serif and Plex Mono.
- [Switzer](https://www.fontshare.com/fonts/switzer): *sans*, neutral (FFL). Classic neo-grotesque with 9 weights and true italics. The quieter, less-seen alternative to Inter and Satoshi.
- [Synonym](https://www.fontshare.com/fonts/synonym): *sans*, warm, editorial (FFL, no italics). Humanist sans with visible stroke contrast; personality without losing legibility. Made for branding and editorial.
- [Alpino](https://www.fontshare.com/fonts/alpino): *sans*, editorial, warm (FFL, no italics). Magazine humanist sans: small x-height, long ascenders, oldstyle figures, softly rounded corners.
- [Happy Times at the IKOB](https://gitlab.com/velvetyne/Happy-Times-at-the-IKOB): *serif*, playful, editorial (unreviewed). A cheeky riff on Times New Roman with odd, joyful details. Times, but it smiles.
- [Zodiak](https://www.fontshare.com/fonts/zodiak): *serif*, editorial (FFL). Sturdy Century-style serif. Middle weights set text; the extreme thin and black weights make great display pairs.
- [Erode](https://www.fontshare.com/fonts/erode): *serif*, editorial, elegant (FFL). Contrasty serif with long ascenders and open counters. Made for pull quotes and eye-catching headlines.
- [Mona Sans / Hubot Sans](https://github.com/github/mona-sans): *sans*, neutral, technical. GitHub's variable grotesque with a width axis, so one family covers condensed headlines and normal UI. Hubot Sans is its squarer, more mechanical sibling.
- [Red Hat Display / Text](https://github.com/RedHatOfficial/RedHatFont): *sans*, warm, neutral. Friendly geometric-humanist pair: Display for big sizes, Text for small. An alternative to Poppins or Montserrat.
- [IBM Plex Mono](https://github.com/IBM/plex): *mono*, technical, warm. Mono with a slightly humanist italic. Works for code and for tech-flavoured UI labels.

### ui

App interfaces, dashboards, small labels.

- [Public Sans](https://github.com/uswds/public-sans): *sans*, neutral. The U.S. government's plain, dependable grotesque. An alternative to Inter or Roboto with less baggage.
- [Mona Sans / Hubot Sans](https://github.com/github/mona-sans): *sans*, neutral, technical. GitHub's variable grotesque with a width axis, so one family covers condensed headlines and normal UI. Hubot Sans is its squarer, more mechanical sibling.
- [IBM Plex Sans](https://github.com/IBM/plex): *sans*, technical, neutral. Corporate-engineered grotesque with small quirks that keep it from being bland. Pairs with Plex Serif and Plex Mono.
- [Red Hat Display / Text](https://github.com/RedHatOfficial/RedHatFont): *sans*, warm, neutral. Friendly geometric-humanist pair: Display for big sizes, Text for small. An alternative to Poppins or Montserrat.
- [Overpass](https://github.com/RedHatOfficial/Overpass): *sans*, technical, neutral. Based on US highway signage (Highway Gothic): open, legible, a little civic. Has a matching mono.
- [Switzer](https://www.fontshare.com/fonts/switzer): *sans*, neutral (FFL). Classic neo-grotesque with 9 weights and true italics. The quieter, less-seen alternative to Inter and Satoshi.
- [Supreme](https://www.fontshare.com/fonts/supreme): *sans*, technical, neutral (FFL). Straight-sided, monolinear engineer's grotesque. An alternative to Space Grotesk without the trend.
- [Source Sans 3](https://github.com/adobe-fonts/source-sans): *sans*, neutral, warm. Adobe's calm humanist workhorse with wide language support. An alternative to Open Sans.
- [Ranade](https://www.fontshare.com/fonts/ranade): *sans*, neutral, editorial (FFL). Neo-grotesque with high-contrast diagonals, a little kick that sets it apart from Helvetica clones.
- [Plein](https://www.fontshare.com/fonts/plein): *sans*, warm, neutral (FFL). Monolinear humanist sans with open, pleasant forms. An alternative to DM Sans.
- [Recia](https://www.fontshare.com/fonts/recia): *serif*, neutral, literary (FFL). Low-contrast, slightly condensed contemporary serif with true cursive italics. A serif that works on screens.
- [Commit Mono](https://commitmono.com): *mono*, neutral, technical. Neutral, anonymous coding font with smart kerning. Configurable on the site before download. An alternative to JetBrains Mono.
- [Monaspace](https://github.com/githubnext/monaspace): *mono*, technical, playful. Five metric-compatible monos (Neon, Argon, Xenon, Radon, Krypton) you can mix in one editor, e.g. a handwriting-style mono for comments.
- [Recursive](https://github.com/arrowtype/recursive): *mono*, playful, warm. One variable font that slides from sans to mono and from linear to casual brush. Great for friendly dev brands.
- [IBM Plex Mono](https://github.com/IBM/plex): *mono*, technical, warm. Mono with a slightly humanist italic. Works for code and for tech-flavoured UI labels.
- [Atkinson Hyperlegible Next](https://www.brailleinstitute.org/freefont): *sans*, warm, neutral. Made for low-vision readers: every confusable letter (I l 1, O 0) is distinct. A humane alternative to Inter for UI.

### headlines

Section titles and large text inside a page.

- [Karrik](https://velvetyne.fr/fonts/karrik/): *sans*, experimental, technical (unreviewed). A grotesque with odd notches cut into its strokes; reads as normal from afar and strange up close.
- [Sporting Grotesque](https://gitlab.com/velvetyne/Sporting-Grotesque): *sans*, retro, editorial (no italics, unreviewed). A wide, slightly old-fashioned grotesque with sporty swagger. Feels like a vintage club badge.
- [League Spartan](https://github.com/theleagueof/league-spartan): *sans*, loud, retro (no italics). Bold geometric in the Futura tradition; the heaviest weights are the reason to use it.
- [Synonym](https://www.fontshare.com/fonts/synonym): *sans*, warm, editorial (FFL, no italics). Humanist sans with visible stroke contrast; personality without losing legibility. Made for branding and editorial.
- [Technor](https://www.fontshare.com/fonts/technor): *sans*, technical, retro (FFL, no italics). Constructed sans with flat sides and rounded tops. Sci-fi and industrial without being a cliché.
- [Alpino](https://www.fontshare.com/fonts/alpino): *sans*, editorial, warm (FFL, no italics). Magazine humanist sans: small x-height, long ascenders, oldstyle figures, softly rounded corners.
- [Cormorant](https://github.com/CatharsisFonts/Cormorant): *serif*, elegant, literary. Delicate Garamond-style display serif with long, sharp details. Luxurious at large sizes.
- [Bagnard](https://github.com/sebsan/Bagnard): *serif*, retro, editorial (no italics). Based on graffiti carved by a Napoleonic-era prisoner: rough, heavy, unusual serif with real character.
- [Avara](https://gitlab.com/velvetyne/Avara): *serif*, experimental, editorial. A curveless serif: every curve drawn as straight segments. Classic silhouette, faceted up close.
- [Happy Times at the IKOB](https://gitlab.com/velvetyne/Happy-Times-at-the-IKOB): *serif*, playful, editorial (unreviewed). A cheeky riff on Times New Roman with odd, joyful details. Times, but it smiles.
- [Zodiak](https://www.fontshare.com/fonts/zodiak): *serif*, editorial (FFL). Sturdy Century-style serif. Middle weights set text; the extreme thin and black weights make great display pairs.
- [Erode](https://www.fontshare.com/fonts/erode): *serif*, editorial, elegant (FFL). Contrasty serif with long ascenders and open counters. Made for pull quotes and eye-catching headlines.
- [Gambarino](https://www.fontshare.com/fonts/gambarino): *serif*, elegant, editorial (FFL, no italics). Condensed post-modern Garalde for headlines. Pair it with a quieter text serif or sans.
- [Boska](https://www.fontshare.com/fonts/boska): *serif*, elegant, editorial (FFL). High-contrast Didone with a pointed-pen flourish. Fashion-magazine elegance. An alternative to Playfair Display.
- [Trench Slab](https://www.fontshare.com/fonts/trench-slab): *serif*, technical, editorial (FFL, no italics). Slab serif with big, prominent ink traps that become a visible style at large sizes.
- [Hoover](https://www.fontshare.com/fonts/hoover): *serif*, retro, loud (FFL, no italics). Monolinear slab with no curves at all. Pure American collegiate and varsity-jacket lettering.
- [Basteleur](https://gitlab.com/velvetyne/basteleur): *display*, experimental, elegant (no italics, unreviewed). Medieval-inspired serif with wild, sharp details; Moonlight is delicate, Bold is gothic drama.
- [Sligoil](https://gitlab.com/velvetyne/sligoil): *display*, experimental, technical (no italics, unreviewed). Based on slug-shaped, gel-like forms; monospace-ish and alien. Ships a variable font.
- [Kola](https://www.fontshare.com/fonts/kola): *display*, technical, playful (FFL, no italics). Rounded techno stencil sans, a bit like LED signage. Large x-height keeps it readable.
- [Melodrama](https://www.fontshare.com/fonts/melodrama): *display*, elegant, editorial (FFL, no italics). Sans with extreme contrast that grows with weight. Glamorous and theatrical.
- [Steps Mono](https://github.com/raphaelbastide/steps-mono): *mono*, experimental, retro (no italics, unreviewed). Stepped, angular mono. More art piece than coding font.
- [Mona Sans / Hubot Sans](https://github.com/github/mona-sans): *sans*, neutral, technical. GitHub's variable grotesque with a width axis, so one family covers condensed headlines and normal UI. Hubot Sans is its squarer, more mechanical sibling.
- [Red Hat Display / Text](https://github.com/RedHatOfficial/RedHatFont): *sans*, warm, neutral. Friendly geometric-humanist pair: Display for big sizes, Text for small. An alternative to Poppins or Montserrat.
- [Overpass](https://github.com/RedHatOfficial/Overpass): *sans*, technical, neutral. Based on US highway signage (Highway Gothic): open, legible, a little civic. Has a matching mono.
- [Supreme](https://www.fontshare.com/fonts/supreme): *sans*, technical, neutral (FFL). Straight-sided, monolinear engineer's grotesque. An alternative to Space Grotesk without the trend.
- [Author](https://www.fontshare.com/fonts/author): *sans*, warm, literary (FFL). Slightly wide humanist sans made for publications. Roomy, readable, a sans that likes books.
- [Source Serif 4](https://github.com/adobe-fonts/source-serif): *serif*, literary, neutral. Sturdy transitional serif with an optical-size axis, so it looks right from captions to headlines.
- [IBM Plex Serif](https://github.com/IBM/plex): *serif*, technical, literary. A serif with an engineer's precision; pairs naturally with Plex Sans and Plex Mono.
- [Junicode](https://github.com/psb1558/Junicode-font): *serif*, literary, retro (unreviewed). A scholar's serif built for medievalists, with weight and width axes. Old-world without being a costume.
- [Linden Hill](https://github.com/theleagueof/linden-hill): *serif*, literary, elegant. A revival of Goudy's Deepdene: graceful, slightly calligraphic old-style serif.
- [Gambetta](https://www.fontshare.com/fonts/gambetta): *serif*, editorial, literary (FFL). Text serif with diagonal stress and contrast that grows with weight. Newspaper-grade reading.
- [Terminal Grotesque](https://github.com/StudioTriple/Terminal-Grotesque): *display*, retro, experimental (no italics). Rough pixel grotesque, cyberpunk zine energy.
- [Le Murmure](https://gitlab.com/velvetyne/murmure): *display*, editorial, experimental (no italics). Tall, narrow display face with alternate letters. Made for a Paris agency; fashion-poster attitude.
- [League Gothic](https://github.com/theleagueof/league-gothic): *display*, loud, retro (no italics). Tall condensed gothic (an Alternate Gothic revival) with a width axis. Classic newspaper and poster shout. An alternative to Bebas Neue and Oswald.
- [Ostrich Sans](https://github.com/theleagueof/ostrich-sans): *display*, loud, playful (no italics). Ultra-condensed caps with rounded, inline and dashed variants. Fun, tall and skinny.
- [Tanker](https://www.fontshare.com/fonts/tanker): *display*, loud, experimental (FFL, no italics). Condensed caps-only sans: the lowercase keys type classic caps and the uppercase keys type dynamic, experimental ones.
- [Panchang](https://www.fontshare.com/fonts/panchang): *display*, loud, technical (FFL, no italics). Ultra-wide, almost panoramic sans. Industrial and very confident.
- [Departure Mono](https://departuremono.com): *mono*, retro, technical (no italics, unreviewed). Pixel monospace inspired by old computers and NASA. Charming at its native pixel sizes.
- [Switzer](https://www.fontshare.com/fonts/switzer): *sans*, neutral (FFL). Classic neo-grotesque with 9 weights and true italics. The quieter, less-seen alternative to Inter and Satoshi.
- [Ranade](https://www.fontshare.com/fonts/ranade): *sans*, neutral, editorial (FFL). Neo-grotesque with high-contrast diagonals, a little kick that sets it apart from Helvetica clones.
- [Zina](https://www.fontshare.com/fonts/zina): *display*, elegant, retro (FFL, no italics). Stately inline Didone with ball terminals. Early-1800s grandeur.
- [Recursive](https://github.com/arrowtype/recursive): *mono*, playful, warm. One variable font that slides from sans to mono and from linear to casual brush. Great for friendly dev brands.

### posters

Hero text, covers, one-word big moments.

- [Ouroboros](https://gitlab.com/velvetyne/ouroboros): *display*, experimental (no italics, unreviewed). Looping, snake-like letterforms. Strange, organic, impossible to mistake for a template.
- [Terminal Grotesque](https://github.com/StudioTriple/Terminal-Grotesque): *display*, retro, experimental (no italics). Rough pixel grotesque, cyberpunk zine energy.
- [Le Murmure](https://gitlab.com/velvetyne/murmure): *display*, editorial, experimental (no italics). Tall, narrow display face with alternate letters. Made for a Paris agency; fashion-poster attitude.
- [League Gothic](https://github.com/theleagueof/league-gothic): *display*, loud, retro (no italics). Tall condensed gothic (an Alternate Gothic revival) with a width axis. Classic newspaper and poster shout. An alternative to Bebas Neue and Oswald.
- [Ostrich Sans](https://github.com/theleagueof/ostrich-sans): *display*, loud, playful (no italics). Ultra-condensed caps with rounded, inline and dashed variants. Fun, tall and skinny.
- [Knewave](https://github.com/theleagueof/knewave): *display*, playful, loud (no italics). Bold brush script with skate and surf energy.
- [Tanker](https://www.fontshare.com/fonts/tanker): *display*, loud, experimental (FFL, no italics). Condensed caps-only sans: the lowercase keys type classic caps and the uppercase keys type dynamic, experimental ones.
- [Panchang](https://www.fontshare.com/fonts/panchang): *display*, loud, technical (FFL, no italics). Ultra-wide, almost panoramic sans. Industrial and very confident.
- [Segment](https://www.fontshare.com/fonts/segment): *display*, retro, technical (FFL, no italics). LCD-style letters built from segments. Digital clocks, transit boards, calculators.
- [Karrik](https://velvetyne.fr/fonts/karrik/): *sans*, experimental, technical (unreviewed). A grotesque with odd notches cut into its strokes; reads as normal from afar and strange up close.
- [Avara](https://gitlab.com/velvetyne/Avara): *serif*, experimental, editorial. A curveless serif: every curve drawn as straight segments. Classic silhouette, faceted up close.
- [Boska](https://www.fontshare.com/fonts/boska): *serif*, elegant, editorial (FFL). High-contrast Didone with a pointed-pen flourish. Fashion-magazine elegance. An alternative to Playfair Display.
- [Basteleur](https://gitlab.com/velvetyne/basteleur): *display*, experimental, elegant (no italics, unreviewed). Medieval-inspired serif with wild, sharp details; Moonlight is delicate, Bold is gothic drama.
- [Sligoil](https://gitlab.com/velvetyne/sligoil): *display*, experimental, technical (no italics, unreviewed). Based on slug-shaped, gel-like forms; monospace-ish and alien. Ships a variable font.
- [Aktura](https://www.fontshare.com/fonts/aktura): *display*, retro, experimental (FFL, no italics). Modern blackletter with ornate Lombardic capitals. Newspaper nameplate, diploma or metal band.
- [Zina](https://www.fontshare.com/fonts/zina): *display*, elegant, retro (FFL, no italics). Stately inline Didone with ball terminals. Early-1800s grandeur.
- [Melodrama](https://www.fontshare.com/fonts/melodrama): *display*, elegant, editorial (FFL, no italics). Sans with extreme contrast that grows with weight. Glamorous and theatrical.
- [Steps Mono](https://github.com/raphaelbastide/steps-mono): *mono*, experimental, retro (no italics, unreviewed). Stepped, angular mono. More art piece than coding font.
- [League Spartan](https://github.com/theleagueof/league-spartan): *sans*, loud, retro (no italics). Bold geometric in the Futura tradition; the heaviest weights are the reason to use it.
- [Technor](https://www.fontshare.com/fonts/technor): *sans*, technical, retro (FFL, no italics). Constructed sans with flat sides and rounded tops. Sci-fi and industrial without being a cliché.
- [Zodiak](https://www.fontshare.com/fonts/zodiak): *serif*, editorial (FFL). Sturdy Century-style serif. Middle weights set text; the extreme thin and black weights make great display pairs.
- [Hoover](https://www.fontshare.com/fonts/hoover): *serif*, retro, loud (FFL, no italics). Monolinear slab with no curves at all. Pure American collegiate and varsity-jacket lettering.
- [Departure Mono](https://departuremono.com): *mono*, retro, technical (no italics, unreviewed). Pixel monospace inspired by old computers and NASA. Charming at its native pixel sizes.

### logos

Wordmarks and brand marks.

- [Aktura](https://www.fontshare.com/fonts/aktura): *display*, retro, experimental (FFL, no italics). Modern blackletter with ornate Lombardic capitals. Newspaper nameplate, diploma or metal band.
- [Zina](https://www.fontshare.com/fonts/zina): *display*, elegant, retro (FFL, no italics). Stately inline Didone with ball terminals. Early-1800s grandeur.
- [Sporting Grotesque](https://gitlab.com/velvetyne/Sporting-Grotesque): *sans*, retro, editorial (no italics, unreviewed). A wide, slightly old-fashioned grotesque with sporty swagger. Feels like a vintage club badge.
- [League Spartan](https://github.com/theleagueof/league-spartan): *sans*, loud, retro (no italics). Bold geometric in the Futura tradition; the heaviest weights are the reason to use it.
- [Technor](https://www.fontshare.com/fonts/technor): *sans*, technical, retro (FFL, no italics). Constructed sans with flat sides and rounded tops. Sci-fi and industrial without being a cliché.
- [Cormorant](https://github.com/CatharsisFonts/Cormorant): *serif*, elegant, literary. Delicate Garamond-style display serif with long, sharp details. Luxurious at large sizes.
- [Bagnard](https://github.com/sebsan/Bagnard): *serif*, retro, editorial (no italics). Based on graffiti carved by a Napoleonic-era prisoner: rough, heavy, unusual serif with real character.
- [Gambarino](https://www.fontshare.com/fonts/gambarino): *serif*, elegant, editorial (FFL, no italics). Condensed post-modern Garalde for headlines. Pair it with a quieter text serif or sans.
- [Trench Slab](https://www.fontshare.com/fonts/trench-slab): *serif*, technical, editorial (FFL, no italics). Slab serif with big, prominent ink traps that become a visible style at large sizes.
- [Hoover](https://www.fontshare.com/fonts/hoover): *serif*, retro, loud (FFL, no italics). Monolinear slab with no curves at all. Pure American collegiate and varsity-jacket lettering.
- [Ouroboros](https://gitlab.com/velvetyne/ouroboros): *display*, experimental (no italics, unreviewed). Looping, snake-like letterforms. Strange, organic, impossible to mistake for a template.
- [Knewave](https://github.com/theleagueof/knewave): *display*, playful, loud (no italics). Bold brush script with skate and surf energy.
- [Kola](https://www.fontshare.com/fonts/kola): *display*, technical, playful (FFL, no italics). Rounded techno stencil sans, a bit like LED signage. Large x-height keeps it readable.
- [Segment](https://www.fontshare.com/fonts/segment): *display*, retro, technical (FFL, no italics). LCD-style letters built from segments. Digital clocks, transit boards, calculators.
- [Synonym](https://www.fontshare.com/fonts/synonym): *sans*, warm, editorial (FFL, no italics). Humanist sans with visible stroke contrast; personality without losing legibility. Made for branding and editorial.
- [Boska](https://www.fontshare.com/fonts/boska): *serif*, elegant, editorial (FFL). High-contrast Didone with a pointed-pen flourish. Fashion-magazine elegance. An alternative to Playfair Display.
- [Tanker](https://www.fontshare.com/fonts/tanker): *display*, loud, experimental (FFL, no italics). Condensed caps-only sans: the lowercase keys type classic caps and the uppercase keys type dynamic, experimental ones.
- [Panchang](https://www.fontshare.com/fonts/panchang): *display*, loud, technical (FFL, no italics). Ultra-wide, almost panoramic sans. Industrial and very confident.
- [Melodrama](https://www.fontshare.com/fonts/melodrama): *display*, elegant, editorial (FFL, no italics). Sans with extreme contrast that grows with weight. Glamorous and theatrical.

### code

Code blocks, terminals, data tables.

- [Commit Mono](https://commitmono.com): *mono*, neutral, technical. Neutral, anonymous coding font with smart kerning. Configurable on the site before download. An alternative to JetBrains Mono.
- [Monaspace](https://github.com/githubnext/monaspace): *mono*, technical, playful. Five metric-compatible monos (Neon, Argon, Xenon, Radon, Krypton) you can mix in one editor, e.g. a handwriting-style mono for comments.
- [Departure Mono](https://departuremono.com): *mono*, retro, technical (no italics, unreviewed). Pixel monospace inspired by old computers and NASA. Charming at its native pixel sizes.
- [Intel One Mono](https://github.com/intel/intel-one-mono): *mono*, neutral, warm. Coding font designed with and for low-vision developers. Clear, open and calm.
- [Recursive](https://github.com/arrowtype/recursive): *mono*, playful, warm. One variable font that slides from sans to mono and from linear to casual brush. Great for friendly dev brands.
- [Iosevka](https://github.com/be5invis/Iosevka): *mono*, technical. Narrow, highly configurable coding font. Fits lots of columns; build your own variant.
- [Victor Mono](https://rubjo.github.io/victor-mono): *mono*, playful, technical. Narrow mono with a cursive italic. Comments and keywords look handwritten.
- [IBM Plex Mono](https://github.com/IBM/plex): *mono*, technical, warm. Mono with a slightly humanist italic. Works for code and for tech-flavoured UI labels.
- [iA Writer Mono / Duo / Quattro](https://github.com/iaolo/iA-Fonts): *mono*, literary, neutral. Plex Mono reworked for writing. Duo and Quattro are duospace and quattrospace, so prose reads more naturally than in a true mono.

### accessible

Built for legibility: low vision, dyslexia, small sizes.

- [Atkinson Hyperlegible Next](https://www.brailleinstitute.org/freefont): *sans*, warm, neutral. Made for low-vision readers: every confusable letter (I l 1, O 0) is distinct. A humane alternative to Inter for UI.
- [Intel One Mono](https://github.com/intel/intel-one-mono): *mono*, neutral, warm. Coding font designed with and for low-vision developers. Clear, open and calm.

## By feel

### neutral

Quiet, Swiss, gets out of the way.

- [Public Sans](https://github.com/uswds/public-sans): *sans*, for ui, body
- [Mona Sans / Hubot Sans](https://github.com/github/mona-sans): *sans*, for ui, headlines, body
- [Source Sans 3](https://github.com/adobe-fonts/source-sans): *sans*, for body, ui
- [Switzer](https://www.fontshare.com/fonts/switzer): *sans*, for ui, body, headlines
- [Ranade](https://www.fontshare.com/fonts/ranade): *sans*, for body, ui, headlines
- [Recia](https://www.fontshare.com/fonts/recia): *serif*, for body, ui
- [Commit Mono](https://commitmono.com): *mono*, for code, ui
- [Intel One Mono](https://github.com/intel/intel-one-mono): *mono*, for code, accessible
- [Atkinson Hyperlegible Next](https://www.brailleinstitute.org/freefont): *sans*, for accessible, body, ui
- [IBM Plex Sans](https://github.com/IBM/plex): *sans*, for ui, body
- [Red Hat Display / Text](https://github.com/RedHatOfficial/RedHatFont): *sans*, for ui, headlines, body
- [Overpass](https://github.com/RedHatOfficial/Overpass): *sans*, for ui, headlines
- [Supreme](https://www.fontshare.com/fonts/supreme): *sans*, for ui, headlines
- [Plein](https://www.fontshare.com/fonts/plein): *sans*, for body, ui
- [Source Serif 4](https://github.com/adobe-fonts/source-serif): *serif*, for body, headlines
- [Bespoke Serif](https://www.fontshare.com/fonts/bespoke-serif): *serif*, for body
- [iA Writer Mono / Duo / Quattro](https://github.com/iaolo/iA-Fonts): *mono*, for body, code

### warm

Friendly, human, soft edges.

- [Atkinson Hyperlegible Next](https://www.brailleinstitute.org/freefont): *sans*, for accessible, body, ui
- [Red Hat Display / Text](https://github.com/RedHatOfficial/RedHatFont): *sans*, for ui, headlines, body
- [Synonym](https://www.fontshare.com/fonts/synonym): *sans*, for headlines, body, logos
- [Author](https://www.fontshare.com/fonts/author): *sans*, for body, headlines
- [Plein](https://www.fontshare.com/fonts/plein): *sans*, for body, ui
- [Source Sans 3](https://github.com/adobe-fonts/source-sans): *sans*, for body, ui
- [Alpino](https://www.fontshare.com/fonts/alpino): *sans*, for headlines, body
- [Sorts Mill Goudy](https://github.com/theleagueof/sorts-mill-goudy): *serif*, for body
- [Sentient](https://www.fontshare.com/fonts/sentient): *serif*, for body
- [Intel One Mono](https://github.com/intel/intel-one-mono): *mono*, for code, accessible
- [Recursive](https://github.com/arrowtype/recursive): *mono*, for code, ui, headlines
- [IBM Plex Mono](https://github.com/IBM/plex): *mono*, for code, ui, body

### technical

Engineered, precise, a bit cold.

- [IBM Plex Sans](https://github.com/IBM/plex): *sans*, for ui, body
- [Overpass](https://github.com/RedHatOfficial/Overpass): *sans*, for ui, headlines
- [Supreme](https://www.fontshare.com/fonts/supreme): *sans*, for ui, headlines
- [Technor](https://www.fontshare.com/fonts/technor): *sans*, for headlines, logos, posters
- [IBM Plex Serif](https://github.com/IBM/plex): *serif*, for body, headlines
- [Trench Slab](https://www.fontshare.com/fonts/trench-slab): *serif*, for headlines, logos
- [Kola](https://www.fontshare.com/fonts/kola): *display*, for headlines, logos
- [Monaspace](https://github.com/githubnext/monaspace): *mono*, for code, ui
- [Iosevka](https://github.com/be5invis/Iosevka): *mono*, for code
- [IBM Plex Mono](https://github.com/IBM/plex): *mono*, for code, ui, body
- [Mona Sans / Hubot Sans](https://github.com/github/mona-sans): *sans*, for ui, headlines, body
- [Karrik](https://velvetyne.fr/fonts/karrik/): *sans*, for headlines, posters
- [Sligoil](https://gitlab.com/velvetyne/sligoil): *display*, for headlines, posters
- [Panchang](https://www.fontshare.com/fonts/panchang): *display*, for posters, headlines, logos
- [Segment](https://www.fontshare.com/fonts/segment): *display*, for posters, logos
- [Commit Mono](https://commitmono.com): *mono*, for code, ui
- [Departure Mono](https://departuremono.com): *mono*, for code, headlines, posters
- [Victor Mono](https://rubjo.github.io/victor-mono): *mono*, for code

### literary

Bookish, classic, made for reading.

- [Source Serif 4](https://github.com/adobe-fonts/source-serif): *serif*, for body, headlines
- [Libertinus](https://github.com/alerque/libertinus): *serif*, for body
- [Junicode](https://github.com/psb1558/Junicode-font): *serif*, for body, headlines
- [Sorts Mill Goudy](https://github.com/theleagueof/sorts-mill-goudy): *serif*, for body
- [Linden Hill](https://github.com/theleagueof/linden-hill): *serif*, for body, headlines
- [Sentient](https://www.fontshare.com/fonts/sentient): *serif*, for body
- [Bespoke Serif](https://www.fontshare.com/fonts/bespoke-serif): *serif*, for body
- [iA Writer Mono / Duo / Quattro](https://github.com/iaolo/iA-Fonts): *mono*, for body, code
- [Author](https://www.fontshare.com/fonts/author): *sans*, for body, headlines
- [IBM Plex Serif](https://github.com/IBM/plex): *serif*, for body, headlines
- [Cormorant](https://github.com/CatharsisFonts/Cormorant): *serif*, for headlines, logos
- [Gambetta](https://www.fontshare.com/fonts/gambetta): *serif*, for body, headlines
- [Recia](https://www.fontshare.com/fonts/recia): *serif*, for body, ui

### editorial

Magazine confidence, opinionated serif or grotesque.

- [Alpino](https://www.fontshare.com/fonts/alpino): *sans*, for headlines, body
- [Gambetta](https://www.fontshare.com/fonts/gambetta): *serif*, for body, headlines
- [Zodiak](https://www.fontshare.com/fonts/zodiak): *serif*, for headlines, body, posters
- [Erode](https://www.fontshare.com/fonts/erode): *serif*, for headlines, body
- [Le Murmure](https://gitlab.com/velvetyne/murmure): *display*, for posters, headlines
- [Sporting Grotesque](https://gitlab.com/velvetyne/Sporting-Grotesque): *sans*, for headlines, logos
- [Synonym](https://www.fontshare.com/fonts/synonym): *sans*, for headlines, body, logos
- [Ranade](https://www.fontshare.com/fonts/ranade): *sans*, for body, ui, headlines
- [Bagnard](https://github.com/sebsan/Bagnard): *serif*, for headlines, logos
- [Avara](https://gitlab.com/velvetyne/Avara): *serif*, for headlines, posters
- [Happy Times at the IKOB](https://gitlab.com/velvetyne/Happy-Times-at-the-IKOB): *serif*, for headlines, body
- [Gambarino](https://www.fontshare.com/fonts/gambarino): *serif*, for headlines, logos
- [Boska](https://www.fontshare.com/fonts/boska): *serif*, for headlines, posters, logos
- [Trench Slab](https://www.fontshare.com/fonts/trench-slab): *serif*, for headlines, logos
- [Melodrama](https://www.fontshare.com/fonts/melodrama): *display*, for headlines, posters, logos

### elegant

High contrast, refined, a little luxurious.

- [Cormorant](https://github.com/CatharsisFonts/Cormorant): *serif*, for headlines, logos
- [Gambarino](https://www.fontshare.com/fonts/gambarino): *serif*, for headlines, logos
- [Boska](https://www.fontshare.com/fonts/boska): *serif*, for headlines, posters, logos
- [Zina](https://www.fontshare.com/fonts/zina): *display*, for logos, posters, headlines
- [Melodrama](https://www.fontshare.com/fonts/melodrama): *display*, for headlines, posters, logos
- [Linden Hill](https://github.com/theleagueof/linden-hill): *serif*, for body, headlines
- [Erode](https://www.fontshare.com/fonts/erode): *serif*, for headlines, body
- [Basteleur](https://gitlab.com/velvetyne/basteleur): *display*, for headlines, posters

### loud

Heavy, condensed or wide, poster energy.

- [League Spartan](https://github.com/theleagueof/league-spartan): *sans*, for headlines, logos, posters
- [League Gothic](https://github.com/theleagueof/league-gothic): *display*, for posters, headlines
- [Ostrich Sans](https://github.com/theleagueof/ostrich-sans): *display*, for posters, headlines
- [Tanker](https://www.fontshare.com/fonts/tanker): *display*, for posters, headlines, logos
- [Panchang](https://www.fontshare.com/fonts/panchang): *display*, for posters, headlines, logos
- [Hoover](https://www.fontshare.com/fonts/hoover): *serif*, for headlines, logos, posters
- [Knewave](https://github.com/theleagueof/knewave): *display*, for posters, logos

### playful

Quirky, bouncy, fun.

- [Happy Times at the IKOB](https://gitlab.com/velvetyne/Happy-Times-at-the-IKOB): *serif*, for headlines, body
- [Knewave](https://github.com/theleagueof/knewave): *display*, for posters, logos
- [Recursive](https://github.com/arrowtype/recursive): *mono*, for code, ui, headlines
- [Victor Mono](https://rubjo.github.io/victor-mono): *mono*, for code
- [Ostrich Sans](https://github.com/theleagueof/ostrich-sans): *display*, for posters, headlines
- [Kola](https://www.fontshare.com/fonts/kola): *display*, for headlines, logos
- [Monaspace](https://github.com/githubnext/monaspace): *mono*, for code, ui

### experimental

Weird, art-school, rule-breaking.

- [Karrik](https://velvetyne.fr/fonts/karrik/): *sans*, for headlines, posters
- [Avara](https://gitlab.com/velvetyne/Avara): *serif*, for headlines, posters
- [Ouroboros](https://gitlab.com/velvetyne/ouroboros): *display*, for posters, logos
- [Basteleur](https://gitlab.com/velvetyne/basteleur): *display*, for headlines, posters
- [Sligoil](https://gitlab.com/velvetyne/sligoil): *display*, for headlines, posters
- [Steps Mono](https://github.com/raphaelbastide/steps-mono): *mono*, for headlines, posters
- [Terminal Grotesque](https://github.com/StudioTriple/Terminal-Grotesque): *display*, for posters, headlines
- [Le Murmure](https://gitlab.com/velvetyne/murmure): *display*, for posters, headlines
- [Tanker](https://www.fontshare.com/fonts/tanker): *display*, for posters, headlines, logos
- [Aktura](https://www.fontshare.com/fonts/aktura): *display*, for logos, posters

### retro

Clearly from an era: pixel, terminal, LCD, collegiate, medieval.

- [Sporting Grotesque](https://gitlab.com/velvetyne/Sporting-Grotesque): *sans*, for headlines, logos
- [Bagnard](https://github.com/sebsan/Bagnard): *serif*, for headlines, logos
- [Hoover](https://www.fontshare.com/fonts/hoover): *serif*, for headlines, logos, posters
- [Terminal Grotesque](https://github.com/StudioTriple/Terminal-Grotesque): *display*, for posters, headlines
- [Aktura](https://www.fontshare.com/fonts/aktura): *display*, for logos, posters
- [Segment](https://www.fontshare.com/fonts/segment): *display*, for posters, logos
- [Departure Mono](https://departuremono.com): *mono*, for code, headlines, posters
- [League Spartan](https://github.com/theleagueof/league-spartan): *sans*, for headlines, logos, posters
- [Technor](https://www.fontshare.com/fonts/technor): *sans*, for headlines, logos, posters
- [Junicode](https://github.com/psb1558/Junicode-font): *serif*, for body, headlines
- [League Gothic](https://github.com/theleagueof/league-gothic): *display*, for posters, headlines
- [Zina](https://www.fontshare.com/fonts/zina): *display*, for logos, posters, headlines
- [Steps Mono](https://github.com/raphaelbastide/steps-mono): *mono*, for headlines, posters

## All fonts

| Font | Category | Feel | Use | Weights | Italics | Scripts | License |
|---|---|---|---|---|---|---|---|
| [Atkinson Hyperlegible Next](https://www.brailleinstitute.org/freefont) | sans | warm, neutral | accessible, body, ui | 200–800 var | yes | latin | OFL |
| [Public Sans](https://github.com/uswds/public-sans) | sans | neutral | ui, body | 100–900 var | yes | latin, vietnamese | OFL |
| [Mona Sans / Hubot Sans](https://github.com/github/mona-sans) | sans | neutral, technical | ui, headlines, body | 200–900 var | yes | latin, vietnamese | OFL |
| [IBM Plex Sans](https://github.com/IBM/plex) | sans | technical, neutral | ui, body | 100–700 var | yes | latin, cyrillic, greek, vietnamese | OFL |
| [Red Hat Display / Text](https://github.com/RedHatOfficial/RedHatFont) | sans | warm, neutral | ui, headlines, body | 300–900 var | yes | latin | OFL |
| [Overpass](https://github.com/RedHatOfficial/Overpass) | sans | technical, neutral | ui, headlines | 100–900 var | yes | latin, cyrillic, vietnamese | OFL |
| [Source Sans 3](https://github.com/adobe-fonts/source-sans) | sans | neutral, warm | body, ui | 200–900 var | yes | latin, cyrillic, greek, vietnamese | OFL |
| [Karrik](https://velvetyne.fr/fonts/karrik/) ⚠︎ | sans | experimental, technical | headlines, posters | 400 | yes | latin | OFL |
| [Sporting Grotesque](https://gitlab.com/velvetyne/Sporting-Grotesque) ⚠︎ | sans | retro, editorial | headlines, logos | 400–700 | no | latin | OFL |
| [League Spartan](https://github.com/theleagueof/league-spartan) | sans | loud, retro | headlines, logos, posters | 100–900 var | no | latin, vietnamese | OFL |
| [Switzer](https://www.fontshare.com/fonts/switzer) | sans | neutral | ui, body, headlines | 100–900 var | yes | latin | FFL |
| [Supreme](https://www.fontshare.com/fonts/supreme) | sans | technical, neutral | ui, headlines | 100–800 var | yes | latin | FFL |
| [Synonym](https://www.fontshare.com/fonts/synonym) | sans | warm, editorial | headlines, body, logos | 200–700 var | no | latin | FFL |
| [Technor](https://www.fontshare.com/fonts/technor) | sans | technical, retro | headlines, logos, posters | 200–900 var | no | latin | FFL |
| [Ranade](https://www.fontshare.com/fonts/ranade) | sans | neutral, editorial | body, ui, headlines | 100–700 var | yes | latin | FFL |
| [Author](https://www.fontshare.com/fonts/author) | sans | warm, literary | body, headlines | 200–700 var | yes | latin | FFL |
| [Plein](https://www.fontshare.com/fonts/plein) | sans | warm, neutral | body, ui | 300–900 var | yes | latin | FFL |
| [Alpino](https://www.fontshare.com/fonts/alpino) | sans | editorial, warm | headlines, body | 100–900 var | no | latin | FFL |
| [Source Serif 4](https://github.com/adobe-fonts/source-serif) | serif | literary, neutral | body, headlines | 200–900 var | yes | latin, cyrillic, greek, vietnamese | OFL |
| [IBM Plex Serif](https://github.com/IBM/plex) | serif | technical, literary | body, headlines | 100–700 var | yes | latin, cyrillic, vietnamese | OFL |
| [Libertinus](https://github.com/alerque/libertinus) | serif | literary | body | 400–700 | yes | latin, cyrillic, greek, hebrew, vietnamese | OFL |
| [Cormorant](https://github.com/CatharsisFonts/Cormorant) | serif | elegant, literary | headlines, logos | 300–700 var | yes | latin, cyrillic, vietnamese | OFL |
| [Junicode](https://github.com/psb1558/Junicode-font) ⚠︎ | serif | literary, retro | body, headlines | 300–700 var | yes | latin, greek | OFL |
| [Bagnard](https://github.com/sebsan/Bagnard) | serif | retro, editorial | headlines, logos | 400 | no | latin | OFL |
| [Avara](https://gitlab.com/velvetyne/Avara) | serif | experimental, editorial | headlines, posters | 700–900 | yes | latin | OFL |
| [Happy Times at the IKOB](https://gitlab.com/velvetyne/Happy-Times-at-the-IKOB) ⚠︎ | serif | playful, editorial | headlines, body | 400–700 | yes | latin | OFL |
| [Sorts Mill Goudy](https://github.com/theleagueof/sorts-mill-goudy) | serif | literary, warm | body | 400 | yes | latin | OFL |
| [Linden Hill](https://github.com/theleagueof/linden-hill) | serif | literary, elegant | body, headlines | 400 | yes | latin | OFL |
| [Gambetta](https://www.fontshare.com/fonts/gambetta) | serif | editorial, literary | body, headlines | 300–700 var | yes | latin | FFL |
| [Zodiak](https://www.fontshare.com/fonts/zodiak) | serif | editorial | headlines, body, posters | 100–900 var | yes | latin | FFL |
| [Erode](https://www.fontshare.com/fonts/erode) | serif | editorial, elegant | headlines, body | 300–700 var | yes | latin | FFL |
| [Sentient](https://www.fontshare.com/fonts/sentient) | serif | literary, warm | body | 200–700 var | yes | latin | FFL |
| [Gambarino](https://www.fontshare.com/fonts/gambarino) | serif | elegant, editorial | headlines, logos | 400 | no | latin | FFL |
| [Recia](https://www.fontshare.com/fonts/recia) | serif | neutral, literary | body, ui | 300–700 var | yes | latin | FFL |
| [Bespoke Serif](https://www.fontshare.com/fonts/bespoke-serif) | serif | literary, neutral | body | 300–800 var | yes | latin | FFL |
| [Boska](https://www.fontshare.com/fonts/boska) | serif | elegant, editorial | headlines, posters, logos | 200–900 var | yes | latin | FFL |
| [Trench Slab](https://www.fontshare.com/fonts/trench-slab) | serif | technical, editorial | headlines, logos | 300–700 var | no | latin | FFL |
| [Hoover](https://www.fontshare.com/fonts/hoover) | serif | retro, loud | headlines, logos, posters | 100–700 var | no | latin | FFL |
| [Ouroboros](https://gitlab.com/velvetyne/ouroboros) ⚠︎ | display | experimental | posters, logos | 400 | no | latin | OFL |
| [Basteleur](https://gitlab.com/velvetyne/basteleur) ⚠︎ | display | experimental, elegant | headlines, posters | 300–700 | no | latin | OFL |
| [Terminal Grotesque](https://github.com/StudioTriple/Terminal-Grotesque) | display | retro, experimental | posters, headlines | 400 | no | latin | OFL |
| [Le Murmure](https://gitlab.com/velvetyne/murmure) | display | editorial, experimental | posters, headlines | 400 | no | latin | OFL |
| [Sligoil](https://gitlab.com/velvetyne/sligoil) ⚠︎ | display | experimental, technical | headlines, posters | 400–700 var | no | latin | OFL |
| [League Gothic](https://github.com/theleagueof/league-gothic) | display | loud, retro | posters, headlines | 400 var | no | latin, vietnamese | OFL |
| [Ostrich Sans](https://github.com/theleagueof/ostrich-sans) | display | loud, playful | posters, headlines | 300–900 | no | latin | OFL |
| [Knewave](https://github.com/theleagueof/knewave) | display | playful, loud | posters, logos | 400 | no | latin | OFL |
| [Tanker](https://www.fontshare.com/fonts/tanker) | display | loud, experimental | posters, headlines, logos | 400 | no | latin | FFL |
| [Panchang](https://www.fontshare.com/fonts/panchang) | display | loud, technical | posters, headlines, logos | 200–800 var | no | latin | FFL |
| [Aktura](https://www.fontshare.com/fonts/aktura) | display | retro, experimental | logos, posters | 400 | no | latin | FFL |
| [Zina](https://www.fontshare.com/fonts/zina) | display | elegant, retro | logos, posters, headlines | 400 | no | latin | FFL |
| [Kola](https://www.fontshare.com/fonts/kola) | display | technical, playful | headlines, logos | 400 | no | latin | FFL |
| [Melodrama](https://www.fontshare.com/fonts/melodrama) | display | elegant, editorial | headlines, posters, logos | 300–700 var | no | latin | FFL |
| [Segment](https://www.fontshare.com/fonts/segment) | display | retro, technical | posters, logos | 400 | no | latin | FFL |
| [Commit Mono](https://commitmono.com) | mono | neutral, technical | code, ui | 200–700 | yes | latin | OFL |
| [Monaspace](https://github.com/githubnext/monaspace) | mono | technical, playful | code, ui | 200–800 var | yes | latin | OFL |
| [Departure Mono](https://departuremono.com) ⚠︎ | mono | retro, technical | code, headlines, posters | 400 | no | latin | OFL |
| [Intel One Mono](https://github.com/intel/intel-one-mono) | mono | neutral, warm | code, accessible | 300–700 var | yes | latin, vietnamese | OFL |
| [iA Writer Mono / Duo / Quattro](https://github.com/iaolo/iA-Fonts) | mono | literary, neutral | body, code | 400–700 var | yes | latin | OFL |
| [Recursive](https://github.com/arrowtype/recursive) | mono | playful, warm | code, ui, headlines | 300–900 var | yes | latin, vietnamese | OFL |
| [Iosevka](https://github.com/be5invis/Iosevka) | mono | technical | code | 100–900 | yes | latin, cyrillic, greek | OFL |
| [Victor Mono](https://rubjo.github.io/victor-mono) | mono | playful, technical | code | 100–700 var | yes | latin, cyrillic, greek, vietnamese | OFL |
| [IBM Plex Mono](https://github.com/IBM/plex) | mono | technical, warm | code, ui, body | 100–700 var | yes | latin, cyrillic, vietnamese | OFL |
| [Steps Mono](https://github.com/raphaelbastide/steps-mono) ⚠︎ | mono | experimental, retro | headlines, posters | 100–400 | no | latin | OFL |

⚠︎ = tags not yet reviewed by a human.

## Avoid as defaults

- **Inter**: The default of nearly every AI-generated UI and SaaS template. Try Switzer, Public Sans, Atkinson Hyperlegible Next.
- **Geist**: Vercel's font; now the default look of AI-generated Next.js apps. Try Switzer, Supreme, Mona Sans / Hubot Sans.
- **Space Grotesk**: The go-to 'techy but friendly' choice in templates. Try Supreme, Technor, Karrik.
- **Instrument Serif**: The default 'tasteful serif' in AI landing pages. Try Erode, Gambarino, Cormorant.
- **DM Sans**: Ubiquitous geometric default. Try Plein, Red Hat Display / Text.
- **Plus Jakarta Sans**: Ubiquitous in startup templates. Try Red Hat Display / Text, Synonym.
- **Manrope**: Ubiquitous in startup templates. Try Switzer, Ranade.
- **Outfit**: Ubiquitous geometric default. Try Red Hat Display / Text, League Spartan.
- **Poppins**: The most overused geometric sans on the web. Try Red Hat Display / Text, League Spartan.
- **Montserrat**: The most overused display sans on the web. Try League Spartan, Panchang.
- **Roboto**: Android and Material default; reads as 'no decision made'. Try Public Sans, Source Sans 3.
- **Open Sans**: Reads as 'no decision made'. Try Source Sans 3, Plein.
- **JetBrains Mono**: The default mono in AI-generated code UIs. Try Commit Mono, Intel One Mono, Monaspace.
- **Satoshi**: Fontshare's most-used font; the default of Framer-style templates. Try Switzer, Supreme.
- **General Sans**: Heavily used in Framer-style templates. Try Switzer, Plein.
- **Clash Display**: The default 'bold display' of Framer-style templates. Try Panchang, League Gothic, Tanker.
- **Cabinet Grotesk**: Heavily used in Framer-style templates. Try Synonym, Sporting Grotesque.

<!-- catalog:end -->
