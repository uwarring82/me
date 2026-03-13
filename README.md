# uwarring82.github.io/me

Personal academic website of Ulrich Warring — experimental quantum physicist at
the University of Freiburg.

**Live page:** [https://uwarring82.github.io/me/](https://uwarring82.github.io/me/)


## What this is

A single-page academic profile covering research, teaching, and open-science
work. Open science is not a separate section — it is integrated into the
research areas where it belongs. The page is hosted on GitHub Pages and requires
no build step — it is plain HTML and CSS served directly.


## Repository structure

```
.
├── index.html      Main (and only) page
├── photo.png       Portrait photograph (displayed within an SVG network topology)
├── README.md       This file
└── LICENSE         MIT licence for code
```


## How to update

1. Edit `index.html` directly. All content, styles, and structure are in this
   single file.
2. Commit and push to the `main` branch. GitHub Pages will deploy automatically.
3. To replace the portrait, overwrite `photo.png` with a new file of the same
   name. The image is clipped to a circle by CSS.


## Sections

The page has three sections, coloured in spectral order (blue → green → rose):

| Section | Colour | Content |
|---|---|---|
| About | Blue | Biography, positions, Harbour introduction |
| Research | Green | Five subsections with publications and open research repos |
| Teaching | Rose | Courses, pilot projects, course materials |


## External links

The page links to several external resources. If any of these change, update the
corresponding `href` in `index.html`:

| Destination | Current URL |
|---|---|
| Group page | https://www.qsim.uni-freiburg.de/members-en/uwarring |
| Open-Science Harbour | https://uwarring.gitbook.io/ions-in-freiburg |
| Harbour Architecture (Root) | https://harbour-architecture.github.io/root/ |
| Google Scholar | https://scholar.google.com/citations?user=33v2gBkAAAAJ |
| ORCID | https://orcid.org/0000-0001-8081-9718 |
| GitHub profile | https://github.com/uwarring82 |
| CCUF (Zenodo) | https://doi.org/10.5281/zenodo.17948436 |
| Quantum Relaxation Ordering | https://deep-relaxation-ordering.github.io/q-root/ |
| Stroboscopic Travelling Waves | https://strobo-travels-deep.github.io/root/ |
| Undetected Modes | https://threehouse-plus-ec.github.io/undetected-modes/ |
| Generator Layers (GLHC) | https://threehouse-plus-ec.github.io/GLHC/ |
| Amazon Seasonal Discharge | https://amazon-breakwater.github.io/root/ |
| Numerical Clock Networks | https://adv-labs-ufr.github.io/numerical_clock_networks/ |
| One Propagator, Three Regimes | https://uwarring82.github.io/advlab_bsm/ |


## Photo

The portrait is sourced from the University of Freiburg group page. It is
displayed inside an SVG network topology (one node among peers). The image is
not covered by the MIT licence below — see the licensing note.


## Fonts

The page loads two typefaces from Google Fonts:

- **Crimson Pro** (serif) — body text
- **DM Sans** (sans-serif) — headings, navigation, labels

No fonts are bundled in the repository.


## Licence

Unless otherwise noted, the source code of this repository (HTML, CSS) is
licensed under the [MIT License](LICENSE).

Text content and images remain © Ulrich Warring, all rights reserved.
