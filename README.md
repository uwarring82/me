# uwarring82.github.io/me

Personal academic website of Ulrich Warring — experimental quantum physicist at
the University of Freiburg.

**Live page:** [https://uwarring82.github.io/me/](https://uwarring82.github.io/me/)


## What this is

An academic profile covering research, teaching, and open-science work, with a
per-paper publications registry and a canonical policy layer. Open science is
not a separate section — it is integrated into the research areas where it
belongs. Everything is hosted on GitHub Pages as plain static files. The only
local tool is a short Python aggregator that regenerates the publications
index; see [How to update](#how-to-update).


## Repository structure

```
.
├── index.html                                  Landing page (About, Research, Teaching)
├── photo.png                                   Portrait photograph
├── policy/
│   ├── index.html                              Canonical policy page (licences, tiers, invariants)
│   └── attribution-templates.html              Enumerated notice_template values
├── publications/
│   ├── index.html                              Filterable registry (fetches publications.json)
│   ├── data/
│   │   └── publications.json                   GENERATED ARTEFACT — do not hand-edit
│   └── papers/
│       └── <slug>/
│           ├── index.html                      Tier C author summary page
│           └── rights.json                     Per-paper rights manifest (source of truth)
├── tools/
│   └── build-publications-index.py             Aggregator: scans rights.json, writes publications.json
├── CONTENT-LICENCE.md                          Repo-legible mirror of the licence regime
├── LICENSE                                     MIT licence for code
├── README.md                                   This file
└── site-blueprint-v0.2.1.md                    Site architecture and governance
```

Canonical authority flows top-down from [`policy/index.html`](policy/index.html):
where anything here conflicts with it, the policy page governs. Full
architecture and tier definitions: [`site-blueprint-v0.2.1.md`](site-blueprint-v0.2.1.md).


## How to update

**Landing-page content (About, Research, Teaching).** Edit
[`index.html`](index.html) directly. Commit and push to `main`; GitHub Pages
deploys automatically. The portrait lives at `photo.png`; the CSS renders it
as a small rounded square (`border-radius: 5px`) alongside an SVG network
badge, not as a circular avatar.

**Publications registry.** The registry is driven by per-paper manifests.

1. Create `publications/papers/<slug>/rights.json` — the source of truth for
   the paper's bibliographic data, rights decisions, display tier, and audit
   record. Schema in `site-blueprint-v0.2.1.md` §3.2.
2. Create `publications/papers/<slug>/index.html` — the Tier C author summary
   page (title, authors, DOI, arXiv, 150-word summary, "why this mattered",
   related dossiers, machine-rendered rights notice). Follow the template from
   any existing paper.
3. Run the aggregator: `python3 tools/build-publications-index.py`. It scans
   every `rights.json`, validates the schema, and rewrites
   `publications/data/publications.json`. Non-zero exit on validation failure.
4. Commit the new `rights.json`, the paper `index.html`, and the regenerated
   `publications.json` together.

**Policy layer.** Changes to `policy/index.html` are governance acts, not
routine edits. Update the blueprint first (or in the same commit), and ensure
`CONTENT-LICENCE.md` still mirrors the licence portion.


## Sections on the landing page

| Section | Accent | Content |
|---|---|---|
| About | Blue | Biography, positions, Harbour introduction |
| Research | Green | Four subsections with publications and open research links |
| Teaching | Rose | Courses, pilot projects, course materials |


## Fonts

The page loads two typefaces from Google Fonts:

- **Crimson Pro** (serif) — body text
- **DM Sans** (sans-serif) — headings, navigation, labels

No fonts are bundled in the repository.


## Licence

The source code of this repository (HTML, CSS, and the aggregator script) is
licensed under the [MIT License](LICENSE).

Content licences for prose, portrait, and site schematics are declared
canonically on [`policy/index.html`](policy/index.html) and mirrored in
[`CONTENT-LICENCE.md`](CONTENT-LICENCE.md). In any conflict, the policy page
governs.
