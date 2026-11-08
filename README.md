# no-slop-type

A short, opinionated list of free typefaces that don't make a site look AI-generated.
Every font here is free for commercial use and **self-hosted**: no Google Fonts CDN, no third-party requests.

- `fonts.json`: the catalog in machine-readable form
- `starter/fonts.css`: copy-paste `@font-face` setup for self-hosting
- `scripts/no-google-fonts.sh`: fails if a project hotlinks Google Fonts or the Fontshare CDN

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
Montserrat, JetBrains Mono, Roboto, Open Sans.** From Fontshare: **Satoshi, General Sans, Clash Display,
Cabinet Grotesk.**

You can still use one on purpose. Just don't let it be the font you get by not deciding.

---

## The list

License key: **OFL** = SIL Open Font License (free to use, modify and bundle). **FFL** = Fontshare's
ITF Free Font License (see [Fontshare rules](#fontshare-rules) below).

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
| Switzer | Jérémie Hornus (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Supreme | Jérémie Hornus (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Synonym | Hugo Dumont (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Technor | Jean-Baptiste Morizot (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Ranade | Easha Ranade (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Author | Satya Rajpurohit (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Plein | Inga Plönnigs (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Alpino | Alisa Nowak (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |

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
| Gambetta | Paul Troppmar (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Zodiak | Jérémie Hornus (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Erode | Nikhil Ranganathan (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Sentient | Noopur Choksi (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Gambarino | Théo Guillard (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Recia | Carlos de Toro (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Bespoke Serif | Jérémie Hornus (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Boska | Barbara Bigosinska (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Trench Slab | Shiva Nallaperumal (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Hoover | Gaetan Baehr (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |

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
| Tanker | Ruosi Huang (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Panchang | Barbara Bigosinska (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Aktura | Gaetan Baehr (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Zina | Théo Guillard (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Kola | Jean-Baptiste Morizot (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Melodrama | Shaily Patel (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |
| Segment | Frode Helland (Fontshare) | FFL | [fontshare.com](https://www.fontshare.com) |

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
- [Fontshare](https://www.fontshare.com): Indian Type Foundry's free catalog (see the rules below)
- [Fontsource](https://fontsource.org): npm packages for self-hosting open fonts, including the Google catalog
- [tfam.io/type](https://tfam.io/type): good for *finding* a vibe, but it searches the Google catalog. Self-host whatever you pick.

---

## Fontshare rules

Fontshare fonts are not open source. They use the ITF Free Font License (v2.0, August 2026), which ships
as `License/FFL.txt` in every download. In short:

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
- Fontshare also lists OFL fonts (Poppins, Montserrat, Space Grotesk and others). Those are mostly the
  Google catalog, so they aren't in this list.

---

## Using a font

This repo doesn't store any font files. It only points to where they come from.

1. Download the `.woff2` files from the font's source into your own project (e.g. `fonts/`).
2. Keep the font's license file next to them (OFL requires it if you redistribute).
3. Copy `starter/fonts.css` into your project, edit it, and link it from your page.
4. Run `scripts/no-google-fonts.sh path/to/your/project` to check nothing still hotlinks Google or Fontshare.

Licenses can change. Check the font's own license before you ship.
