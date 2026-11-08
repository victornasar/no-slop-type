# no-slop-type

A short, opinionated list of free typefaces that don't make a site look AI-generated.
Every font here is free for commercial use and **self-hosted**: no Google Fonts CDN, no third-party requests.

- `fonts.json`: the catalog in machine-readable form
- `starter/fonts.css`: copy-paste `@font-face` setup for self-hosting
- `scripts/no-google-fonts.sh`: fails if a project hotlinks Google Fonts

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

## The slop list (avoid as defaults)

These are good fonts, but AI tools and templates reach for them so often that they now read as "generated":

**Inter, Geist, Space Grotesk, Instrument Serif, DM Sans, Plus Jakarta Sans, Manrope, Outfit, Poppins,
Montserrat, Satoshi, JetBrains Mono, Roboto, Open Sans.**

You can still use one on purpose. Just don't let it be the font you get by not deciding.

---

## The list

License key: **OFL** = SIL Open Font License (free to use, modify and bundle). **FFL** = Fontshare's
free font license (free for commercial use, but read it before redistributing the files).

### Sans

| Font | Who | License | Get it |
|---|---|---|---|
| Atkinson Hyperlegible Next | Braille Institute | OFL | [brailleinstitute.org/freefont](https://www.brailleinstitute.org/freefont) |
| Public Sans | U.S. Web Design System | OFL | [github.com/uswds/public-sans](https://github.com/uswds/public-sans) |
| Mona Sans / Hubot Sans | GitHub | OFL | [github.com/github/mona-sans](https://github.com/github/mona-sans) |
| IBM Plex Sans | IBM | OFL | [github.com/IBM/plex](https://github.com/IBM/plex) |
| Red Hat Display / Text | Red Hat | OFL | [github.com/RedHatOfficial/RedHatFont](https://github.com/RedHatOfficial/RedHatFont) |
| Overpass | Red Hat / Delve | OFL | [github.com/RedHatOfficial/Overpass](https://github.com/RedHatOfficial/Overpass) |
| Source Sans 3 | Adobe | OFL | [github.com/adobe-fonts/source-sans](https://github.com/adobe-fonts/source-sans) |
| Karrik | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |
| Sporting Grotesque | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |
| League Spartan | The League of Moveable Type | OFL | [theleagueof.com](https://www.theleagueofmoveabletype.com) |
| Switzer | Indian Type Foundry | FFL | [fontshare.com](https://www.fontshare.com) |
| General Sans | Indian Type Foundry | FFL | [fontshare.com](https://www.fontshare.com) |
| Cabinet Grotesk | Indian Type Foundry | FFL | [fontshare.com](https://www.fontshare.com) |

### Serif

| Font | Who | License | Get it |
|---|---|---|---|
| Source Serif 4 | Adobe | OFL | [github.com/adobe-fonts/source-serif](https://github.com/adobe-fonts/source-serif) |
| IBM Plex Serif | IBM | OFL | [github.com/IBM/plex](https://github.com/IBM/plex) |
| Libertinus | Khaled Hosny, Caleb Maclennan | OFL | [github.com/alerque/libertinus](https://github.com/alerque/libertinus) |
| Cormorant | Christian Thalmann | OFL | [github.com/CatharsisFonts/Cormorant](https://github.com/CatharsisFonts/Cormorant) |
| Junicode | Peter Baker | OFL | [github.com/psb1558/Junicode-font](https://github.com/psb1558/Junicode-font) |
| Bagnard | Sébastien Sanfilippo | OFL | [github.com/sebsan/Bagnard](https://github.com/sebsan/Bagnard) |
| Avara | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |
| Happy Times at the IKOB | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |
| Sorts Mill Goudy | The League of Moveable Type | OFL | [theleagueof.com](https://www.theleagueofmoveabletype.com) |
| Linden Hill | The League of Moveable Type | OFL | [theleagueof.com](https://www.theleagueofmoveabletype.com) |
| Gambetta | Indian Type Foundry | FFL | [fontshare.com](https://www.fontshare.com) |
| Zodiak | Indian Type Foundry | FFL | [fontshare.com](https://www.fontshare.com) |
| Erode | Indian Type Foundry | FFL | [fontshare.com](https://www.fontshare.com) |

### Display

| Font | Who | License | Get it |
|---|---|---|---|
| Ouroboros | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |
| Basteleur | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |
| Terminal Grotesque | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |
| Le Murmure | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |
| Sligoil | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |
| League Gothic | The League of Moveable Type | OFL | [theleagueof.com](https://www.theleagueofmoveabletype.com) |
| Ostrich Sans | The League of Moveable Type | OFL | [theleagueof.com](https://www.theleagueofmoveabletype.com) |
| Knewave | The League of Moveable Type | OFL | [theleagueof.com](https://www.theleagueofmoveabletype.com) |
| Tanker | Indian Type Foundry | FFL | [fontshare.com](https://www.fontshare.com) |
| Panchang | Indian Type Foundry | FFL | [fontshare.com](https://www.fontshare.com) |

### Mono

| Font | Who | License | Get it |
|---|---|---|---|
| Commit Mono | Eigil Nikolajsen | OFL | [commitmono.com](https://commitmono.com) |
| Monaspace | GitHub Next | OFL | [github.com/githubnext/monaspace](https://github.com/githubnext/monaspace) |
| Departure Mono | Helena Zhang | OFL | [departuremono.com](https://departuremono.com) |
| Intel One Mono | Intel / Frere-Jones Type | OFL | [github.com/intel/intel-one-mono](https://github.com/intel/intel-one-mono) |
| iA Writer Mono / Duo / Quattro | iA | OFL | [github.com/iaolo/iA-Fonts](https://github.com/iaolo/iA-Fonts) |
| Recursive | Arrow Type | OFL | [github.com/arrowtype/recursive](https://github.com/arrowtype/recursive) |
| Iosevka | Belleve Invis | OFL | [github.com/be5invis/Iosevka](https://github.com/be5invis/Iosevka) |
| Victor Mono | Rune Bjørnerås | OFL | [rubjo.github.io/victor-mono](https://rubjo.github.io/victor-mono) |
| IBM Plex Mono | IBM | OFL | [github.com/IBM/plex](https://github.com/IBM/plex) |
| Steps Mono | Velvetyne | OFL | [velvetyne.fr](https://velvetyne.fr) |

---

## Where to find more

- [Velvetyne](https://velvetyne.fr): French libre foundry; weird, expressive, all OFL
- [Collletttivo](https://www.collletttivo.it): Italian open-source type collective
- [The League of Moveable Type](https://www.theleagueofmoveabletype.com): the original open-source foundry
- [Use & Modify](https://usemodify.com): curated libre fonts
- [Uncut](https://uncut.wtf): free and open-source typefaces
- [Badass Libre Fonts by Womxn](https://www.design-research.be/by-womxn/): libre fonts designed by women
- [Fontshare](https://www.fontshare.com): Indian Type Foundry's free catalog (download the files; don't use their CDN)
- [Fontsource](https://fontsource.org): npm packages for self-hosting open fonts, including the Google catalog
- [tfam.io/type](https://tfam.io/type): good for *finding* a vibe, but it searches the Google catalog. Self-host whatever you pick.

---

## Using a font

This repo doesn't store any font files. It only points to where they come from.

1. Download the `.woff2` files from the font's source into your own project (e.g. `fonts/`).
2. Keep the font's license file next to them (OFL requires it if you redistribute).
3. Copy `starter/fonts.css` into your project, edit it, and link it from your page.
4. Run `scripts/no-google-fonts.sh path/to/your/project` to check nothing still hotlinks Google.

Licenses can change. Check the font's own license before you ship.
