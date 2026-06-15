# uwarring82.github.io/me

Personal landing page of Ulrich Warring — experimental quantum physicist at the
University of Freiburg.

**Live page:** [https://uwarring82.github.io/me/](https://uwarring82.github.io/me/)


## What this is

A single, minimal landing page: name, role, affiliation, portrait, a contact
block, and three links — the university group, GitHub, and ORCID. Hosted on
GitHub Pages as one plain static HTML file.


## Repository structure

```
.
├── index.html    Landing page (self-contained: HTML + inline CSS)
├── photo.png     Portrait photograph
├── LICENSE       MIT licence
└── README.md     This file
```


## How to update

Edit [`index.html`](index.html) directly, then commit and push to `main`;
GitHub Pages deploys automatically. The portrait lives at `photo.png` and is
rendered as a small rounded square (`border-radius: 5px`).


## Fonts

The page loads two typefaces from Google Fonts (a single CSS import is the only
external request the page makes):

- **Crimson Pro** (serif) — name and body text
- **IBM Plex Mono** (monospace) — role, contact, and link labels

No fonts are bundled in the repository.


## Licence

The source of this repository (HTML and CSS) is licensed under the
[MIT License](LICENSE). The portrait (`photo.png`) is © Ulrich Warring.
