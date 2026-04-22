# Site Blueprint — `uwarring82.github.io/me`

**Version:** 0.2.1 (editorial harmonisation)
**Drafted:** 2026-04-22
**Supersedes:** v0.2 (2026-04-22), v0.1 (2026-04-22)
**Stance:** Guardian (lead) · Architect (consult, endorsed) · Scout (review, endorsed)
**Scope:** Full site architecture, including the publication registry, rights layer, and policy layer. Covers existing pages and planned additions.
**Endorsement marker:** *v1.0 candidate — implementation-ready pending final Architect and Integrator sign-off. Editorial harmonisation applied per Scout review (2026-04-22): top-level `publications.json` envelope made explicit, `YYYY-MM-01` fallback clarified as sorting surrogate, `discriminant_action` required-cases enumerated, coauthors references aligned to full schema path, §11 build-step wording normalised to "Option A+". Phase 0 implementation under way in parallel.*

---

## Changelog from v0.1

1. **Schema split.** `rights.json` now separates `rights` (what is permitted), `display` (what the site chooses to show), `site_policy` (preconditions imposed by site, not by law), and `audit` (provenance of checks).
2. **Source-of-rights provenance** added; `last_audit` retained but reframed as audit timestamp, not rights timestamp.
3. **Third-party material flag** added at article level.
4. **Discriminant action** required wherever `licence: "unverified"` appears.
5. **ISO 8601 `date_published`** added for deterministic chronology.
6. **Co-author consultation reframed** as site-policy precondition, not a claim about external permissibility.
7. **Site-level invariants** lifted out of tier definitions into their own section (§10), including the no-mirrored-publisher-HTML rule.
8. **`publications.json` is now a generated artefact** produced by a minimal local aggregator script; never hand-edited.
9. **Phases 2 and 3 swapped:** arXiv linking precedes manuscript layer.
10. **14-day Tier B fallback:** if co-author consultation receives no response, the paper defaults to Tier C.
11. **Single-auditor limitation** documented explicitly in §8.
12. **All six §9 open decisions closed.** Old §9 retained as §11 changelog appendix.
13. **`display_status`** added (planned / live / audit-hold).
14. **`policy/index.html` declared canonical;** `CONTENT-LICENCE.md` mirrors.
15. **Build-step migration trigger** specified as a measurable threshold.

---

## 0. Governing Principles

The site is treated as a **public-facing Coastline**: it expresses invariant facts about a person's research, teaching, and affiliations. Interpretive material (the "why this matters" prose around each paper) sits as **Sail** content — free to evolve. The Lock-Key Rule applies: bibliographic facts and rights metadata are locks; framings and summaries are keys.

Three principles govern every design decision below.

1. **Map, not territory.** The site documents what exists; it does not claim authority over the underlying physics. External Coastlines (publishers, ORCID, Scholar) remain the source of record.
2. **Audit over scalability.** Every page must be able to answer the question *"why is this content here, and under what licence?"* without recourse to memory.
3. **Restraint by default.** The current site's typographic restraint is itself a signal. New layers earn their place by removing friction for the reader, not by adding ornament.

---

## 1. Site Map

```
/ (root)
├── index.html                          [existing — landing + thematic research overview]
├── publications/                       [new — Phase 1]
│   ├── index.html                      [registry: filterable list]
│   ├── data/
│   │   └── publications.json           [GENERATED ARTEFACT — do not hand-edit]
│   └── papers/
│       ├── <slug>/
│       │   ├── index.html              [author summary page — Tier C default]
│       │   ├── rights.json             [per-paper rights manifest]
│       │   ├── figures/                [only if Tier A/B]
│       │   └── manuscript.html         [only if Tier A/B, opt-in]
│       └── ...
├── policy/                             [new — Phase 0, must precede Phase 1]
│   ├── index.html                      [CANONICAL: site-wide content licence + tier definitions + invariants]
│   └── attribution-templates.html      [machine-checked notice templates]
├── tools/                              [new — local-only, may be in repo or separate]
│   └── build-publications-index.py     [minimal aggregator: scans rights.json → publications.json]
├── photo.png                           [existing portrait]
├── LICENSE                             [existing — MIT, code only]
└── CONTENT-LICENCE.md                  [new — mirrors policy/index.html; HTML governs in conflict]
```

Top-level navigation gains one item — **Publications** — and one footer link — **Policy**. Nothing else changes.

---

## 2. Section Blueprints

### 2.1 Header / Navigation

**Current.** Name plate, identity badges (ORCID, Scholar, GitHub, Group, Harbour, Harbour Root), contact line.

**Proposed change.** Add `Publications` to the in-page nav (after `Research`, before `Teaching`). Move the badge row's visual weight unchanged.

**Guardian note.** The portrait `photo.png` carries an explicit licence statement on the new `CONTENT-LICENCE.md` page (default: *all rights reserved*; see §4).

### 2.2 About

**Current.** Biographical narrative, positions list. No structural change.

**Proposed minor edit.** Add one sentence near the close acknowledging the Open-Science Harbour ecosystem as the documentary substrate of the site itself, not only of the research.

### 2.3 Research

**Current.** Thematic overview, four research sub-areas, each with selected publications inline (DOI links) and links to open-research dossiers.

**Proposed change.** *None to the prose.* Inline DOI listings remain. Add a single line at the head of each "Selected publications" block: *"Author summaries and rights metadata: see [Publications registry](../publications/)."*

**Guardian note.** Resist migrating inline DOIs into the registry. Redundancy here is a feature.

### 2.4 Teaching

**Current.** Course list, philosophy paragraph, two pilot project links. No change for v0.2.

### 2.5 Publications (new — Phase 1)

This is the substantive addition. See §3 for detailed schema.

**Default tier for every paper: Tier C** (author summary + DOI + arXiv link where available). Tier A and Tier B are *per-paper exceptions*, opted into individually with explicit rights verification.

**Page anatomy (Tier C).**
- Title, authors (with ORCID where known), journal, year, DOI as primary link.
- arXiv ID and link if a preprint exists.
- 150-word author summary in the site's voice.
- One "why this mattered" paragraph (the Sail layer).
- Optionally: one redrawn explanatory schematic, marked *"Website figure, not from the article."*
- Related Harbour dossiers / repositories.
- Footer block: machine-rendered rights notice from `rights.json`.

**Page anatomy (Tier B — accepted manuscript).** Adds a `manuscript.html` link with banner: *"Author-accepted manuscript. Not the typeset version of record. Refer to the DOI for the published article."* Figures hosted only after panel-by-panel rights verification.

**Page anatomy (Tier A — version of record under open licence).** Full text + figures permitted. Banner carries CC BY (or other) attribution string in the form required by the licence.

### 2.6 Policy & Rights (new — Phase 0)

`policy/index.html` is the **canonical Coastline document** for the publication layer. Where any conflict arises between it and `CONTENT-LICENCE.md` in the repository, the HTML page governs.

Contents:
- Site-wide content licence regime (see §4).
- Tier A / B / C definitions with worked examples.
- Site-level invariants (see §10) listed and numbered.
- Statement on figure rights: *figures are evaluated panel by panel*.
- Statement on co-author courtesy: *for multi-author works, co-author notification precedes any manuscript-tier hosting on this site* (site-policy precondition, not a claim about general permissibility).
- Statement on embargoes: *applies separately to preprint, accepted manuscript, and version of record*.
- Governance: present limitations (single-auditor, annual cadence, no second pair of eyes — declared, not disguised).
- Contact for rights queries.

`policy/attribution-templates.html` holds the machine-checked notice templates referenced by `rights.json` (see §3.3).

### 2.7 Footer

**Current.** Affiliation line, Harbour ecosystem statement, *"Maps, not territory."*

**Proposed change.** Add a single link: `Policy & Rights`. Nothing more.

---

## 3. Publications Registry — Detailed Schema

### 3.1 `publications.json` — generated index

This file is **never hand-edited**. It is produced by `tools/build-publications-index.py` (or equivalent), which scans every `papers/*/rights.json`, extracts the index fields, and writes the aggregate. The top-level shape is:

```json
{
  "_warning": "GENERATED ARTEFACT. Do not edit. Source: papers/*/rights.json. Regenerate with tools/build-publications-index.py.",
  "schema_version": "0.2",
  "entries": [ /* see entry shape below */ ]
}
```

The aggregator runs locally before any commit that touches a paper page. CI verifies that the committed `publications.json` matches what would be generated from the current `rights.json` files; any mismatch fails the check.

Index entry shape (one element of `entries`):

```json
{
  "slug": "energy-level-renormalisation-2025",
  "doi": "10.1038/s41467-025-57840-4",
  "title": "Observing time-dependent energy level renormalisation in an ultrastrongly coupled open system",
  "date_published": "2025-03-12",
  "journal": "Nature Communications",
  "tier": "A",
  "display_status": "live",
  "themes": ["open-quantum-systems", "quantum-thermodynamics"]
}
```

`date_published` uses ISO 8601. If the exact day is unknown, default to `YYYY-MM-01` and note in the per-paper `audit.auditor_note`. This fallback is a sorting surrogate, not a claim that the publication date is the first day of the month.

### 3.2 `rights.json` — per-paper manifest (v0.2 schema)

The schema separates **what the law/publisher permits** from **what the site chooses to do** from **preconditions imposed by site policy** from **the audit trail of who checked what when**.

```json
{
  "schema_version": "0.2",
  "doi": "10.1038/s41467-025-57840-4",
  "arxiv_id": null,
  "canonical_url": "https://doi.org/10.1038/s41467-025-57840-4",
  "date_published": "2025-03-12",
  "title": "Observing time-dependent energy level renormalisation in an ultrastrongly coupled open system",
  "journal": "Nature Communications",
  "themes": ["open-quantum-systems", "quantum-thermodynamics"],

  "rights": {
    "text_version_allowed": "version_of_record",
    "licence": "CC-BY-4.0",
    "embargo_until": null,
    "third_party_material_present": false,
    "source_of_rights": {
      "type": "publisher-licence",
      "url": "https://www.nature.com/articles/s41467-025-57840-4",
      "checked_on": "2026-04-22"
    },
    "figures": [
      {
        "id": "fig1",
        "source": "original",
        "rights_holder": "authors",
        "licence": "CC-BY-4.0",
        "can_host": true
      },
      {
        "id": "fig3-panel-c",
        "source": "adapted_from",
        "external_doi": "10.xxxx/xxxxx",
        "rights_holder": "third_party",
        "licence": "unverified",
        "can_host": false,
        "discriminant_action": "Awaiting response to clearance request submitted to publisher portal on 2026-04-22; if not received by 2026-07-22, replace with redrawn schematic."
      }
    ]
  },

  "display": {
    "tier": "C",
    "host_manuscript": false,
    "show_figures": false,
    "display_status": "planned",
    "notice_template": "summary-only"
  },

  "site_policy": {
    "coauthors": {
      "lead_author_consulted": true,
      "consultation_date": "2026-04-15",
      "consultation_method": "email",
      "consultation_outcome": "approved",
      "fallback_applied": false
    }
  },

  "audit": {
    "last_audit": "2026-04-22",
    "auditor": "U.W.",
    "auditor_note": "Tier C summary only; manuscript layer deferred pending figure-rights resolution."
  }
}
```

**Key change of meaning:** `display.tier` is the operational decision for this site. `rights.text_version_allowed` records what could legally be hosted. The two need not match — permission is not obligation.

### 3.3 Notice templates

`policy/attribution-templates.html` enumerates allowed `notice_template` values, e.g.:
- `cc-by-4.0-standard` — CC BY 4.0 with structured author / title / source / licence / modifications fields, rendered by a deterministic template.
- `aps-accepted-manuscript` — APS author-accepted manuscript notice.
- `springer-nature-accepted-manuscript` — Springer Nature equivalent with embargo statement.
- `summary-only` — Tier C: DOI-link only, no manuscript content hosted.

Notices are not free text in `rights.json`; they are template references. Drift is structurally prevented.

### 3.4 Tier definitions (operational)

| Tier | Text | Figures | Required precondition |
|---|---|---|---|
| **C** (default) | Author summary in site's voice, DOI link | Optionally one redrawn website schematic, clearly labelled | None beyond accurate metadata |
| **B** | Accepted manuscript, hosted as document or HTML conversion with banner | Author-owned panels only, after panel-by-panel verification | (i) publisher self-archiving rules permit; (ii) any embargo expired; (iii) co-author consultation logged with outcome `approved` (see §8 fallback) |
| **A** | Version of record | All figures whose `can_host: true` | Article licence explicitly permits reuse (CC BY or equivalent); third-party panels handled separately via `discriminant_action` |

### 3.5 Discriminant Conditions (Breakwater alignment)

A `discriminant_action` field is **required** in every one of the following cases: (i) any entry with `licence: "unverified"`; (ii) uncertain figure clearance (a per-figure `licence` or `can_host` that is not definitively settled); (iii) uncertain self-archiving status (a `text_version_allowed` value that is not definitively settled, including pending-embargo cases). The field must state in operational terms what observation or action will resolve the ambiguity. This aligns the publication registry with the Breakwater Claim Analysis Ledger's mandatory Discriminant Conditions on UNDERDETERMINED entries.

Examples of well-formed discriminant actions:
- *"Awaiting publisher portal clearance response, deadline 2026-07-22; on no-response, replace with redrawn schematic."*
- *"Pending email confirmation from co-author; default to Tier C if no response by 2026-05-06."*
- *"Embargo expires 2026-10-01; tier may be promoted to B at that date."*

A `licence: "unverified"` entry without a `discriminant_action` fails CI validation.

---

## 4. Site-wide Rights & Licensing (decisions closed)

The current `LICENSE` (MIT) governs **code only**. The site declares three further regimes in `CONTENT-LICENCE.md` (mirrored to canonical `policy/index.html`):

1. **Prose / written content: CC BY-SA 4.0.** Reuse permitted with attribution and share-alike. Aligns with Open-Science Harbour reciprocity ethos.
2. **Portrait photograph (`photo.png`): all rights reserved.** No reuse without written permission. Personality rights and copyright both protected. This is the Option A wording from the v0.1 review.
3. **Redrawn schematics on publication pages: CC BY 4.0**, attributable to U. Warring, with per-figure caption stating the licence inline.

A single visible link in the footer (`Policy & Rights`) reaches the canonical page that lays all four regimes (code, prose, portrait, schematics) out side by side.

---

## 5. Visual Identity

The current site's visual restraint is part of its meaning. Constraints for new pages:

- **Typography.** Match existing: serif body, sans-serif headings (or whatever the live stylesheet specifies — verify during Phase 0).
- **Colour.** Reserve a single accent colour drawn from the Construction III emblem palette (sea-blue) for primary links and section markers. Signal-red reserved for *audit warnings on policy pages* — not decorative use.
- **Density.** Each publication page should fit on a single laptop screen for the summary block. Anything below the fold is Sail content (extended discussion) or rights-notice apparatus.
- **No badges, no metrics widgets, no altmetric counts.** These introduce third-party data flows and violate the audit-first principle without commensurate reader benefit.

---

## 6. Build & Deployment

**Decision: no-build static site, with one local aggregator script.** The aggregator is not a content-transformation pipeline; it is a ledger-keeping tool that prevents duplicate-edit drift between `rights.json` files and `publications.json`.

**Aggregator contract (`tools/build-publications-index.py` or equivalent):**
- Reads every `publications/papers/*/rights.json`.
- Extracts the index-relevant fields (slug, doi, title, date_published, journal, tier, display_status, themes).
- Writes `publications/data/publications.json` with the `_warning` sentinel as the first entry.
- Exits non-zero if any `rights.json` fails schema validation or contains an unresolved `licence: "unverified"` without a `discriminant_action`.
- Total length expected: well under 100 lines; no external dependencies beyond the standard library.

**Workflow per new paper page:**
1. Author summary written in `papers/<slug>/index.html`.
2. `rights.json` populated, with `audit.last_audit`, `audit.auditor_note`, and `rights.source_of_rights.checked_on` completed.
3. Run aggregator locally; commit both the new `rights.json` and the regenerated `publications.json`.
4. CI re-runs the aggregator and confirms idempotence (committed `publications.json` matches regenerated output).
5. Pull request includes a one-line statement: *"Tier C, no rights questions"* or *"Tier B, accepted-manuscript, co-author consulted <date>, outcome approved."*

**Migration trigger to a full generator (Option B → light static-site generator):**
The threshold is **measurable**, not heuristic. Migrate when *any one* of the following holds:
- More than 30 paper pages exist.
- Per-paper page-creation time exceeds 30 minutes for routine Tier C entries (measure on three consecutive entries).
- Schema migration touches more than five `rights.json` files in a single revision (signals duplication has become a maintenance burden).

Until one of those triggers, stay no-build.

---

## 7. Phasing (revised)

**Phase 0 — Policy first.** Build `policy/index.html`, `policy/attribution-templates.html`, and `CONTENT-LICENCE.md`. Add footer link. *No publication pages yet.* This phase exists to prevent every future page from improvising against an unstated standard.

**Phase 1 — Summary-first registry.** Three to five Tier C author-summary pages plus the aggregator script. Suggested seed: the 2025 Nature Communications paper, one PRL from the NIST era (Microwave quantum logic gates, Nature 2011 — Tier C), and one recent open-research-linked paper. Build `publications/index.html` as the filterable registry.

**Phase 2 — arXiv layer (was Phase 3 in v0.1).** Populate `arxiv_id` fields in all existing `rights.json` files. Surface arXiv links prominently on each paper page. Lowest friction, lowest rights exposure; should logically precede the manuscript layer.

**Phase 3 — Per-paper manuscript layer (was Phase 2 in v0.1, opt-in).** Only after Phase 2 is stable. Begin with the 2025 Nature Communications paper as Tier A pilot — but only after panel-by-panel figure rights verification. Each subsequent paper is a discrete decision, not a default.

---

## 8. Audit & Governance

Each paper page must, on inspection, answer three questions visibly:

- *What is hosted here?* (text version, figures present)
- *Under what licence or policy?* (CC BY, accepted-manuscript self-archiving, summary-only)
- *When was this last audited, and against what?* (`audit.last_audit` + `rights.source_of_rights.checked_on`, both surfaced in page footer)

A single annual audit pass refreshes `last_audit` and `checked_on` and re-checks publisher policies for any tier change.

**Tier B co-author consultation fallback.** For Tier B, `site_policy.coauthors.lead_author_consulted: true` with `site_policy.coauthors.consultation_outcome: "approved"` is a site-policy precondition. If consultation receives no response within **14 calendar days**, the paper defaults to Tier C, `site_policy.coauthors.fallback_applied: true` is recorded, and `audit.auditor_note` documents the deferral. This prevents Tier B from being indefinitely blocked by unanswered email.

**Site-policy framing, not legal claim.** Co-author consultation is required by *this site's policy* for Tier B hosting. It is not a claim that consultation is generally legally required. The distinction is recorded in `policy/index.html`.

**Present governance limitations (declared, not disguised).** The site currently operates with:
- A single auditor (U.W.).
- No second pair of eyes on rights decisions.
- An annual audit cadence.
- No formal escalation path if the auditor is unavailable.

These are acceptable for the present scale but are documented in `policy/index.html` under *"Governance: present limitations"* so that readers can calibrate trust appropriately. Audit-first applied to the audit system itself.

---

## 10. Site-Level Invariants

Numbered, listed in `policy/index.html`, never silently relaxed.

1. **No publisher-generated HTML is mirrored.** Hosted text must be one of: (a) author-written summary, (b) author-accepted manuscript (under self-archiving rules), (c) lawfully reusable open-access full text prepared for this site under its licence.
2. **Figures are evaluated panel by panel.** A document-level licence does not automatically clear embedded third-party material.
3. **No third-party tracking, badges, or metrics widgets.** No external data flows beyond direct DOI / arXiv / ORCID / Scholar links the reader chooses to follow.
4. **Permission is not obligation.** A paper that *could* be hosted at Tier A may be hosted at Tier C for editorial restraint.
5. **Every `licence: "unverified"` carries a `discriminant_action`.** No silent ambiguities.
6. **`policy/index.html` is canonical** for any rights, licence, or governance question. Repository files mirror; HTML governs in conflict.
7. **`publications.json` is a generated artefact.** Hand-editing it is forbidden; CI enforces idempotence.

---

## 11. Decisions Closed (changelog from v0.1 §9)

| # | Question | Decision | Date | Authority |
|---|---|---|---|---|
| 1 | Prose content licence | CC BY-SA 4.0 | 2026-04-22 | Supervisor (delegated to Guardian on reviewer recommendation) |
| 2 | Portrait wording | All rights reserved; no reuse without written permission | 2026-04-22 | Supervisor (delegated, Option A) |
| 3 | arXiv inventory timing | Deferred to Phase 2; not a Phase 0 blocker | 2026-04-22 | Supervisor (delegated) |
| 4 | Audit cadence | Annual | 2026-04-22 | Supervisor (delegated) |
| 5 | Build step | No-build static site with minimal local aggregator script (Option A+, local tooling only) | 2026-04-22 | Supervisor ("1B") |
| 6 | Top-level naming | `publications/` | 2026-04-22 | Supervisor (delegated) |
| 7 | Phase 2/3 swap (arXiv before manuscript) | Accepted | 2026-04-22 | Supervisor ("3OK") |

---

## 12. Endorsement & Next Steps

This blueprint is a **revised draft Coastline document** for the site, with all v0.1 open decisions closed and convergent revisions from Architect and Scout integrated.

**Stance sign-off status:**
- **Guardian:** endorsed (this draft).
- **Architect:** endorsed in principle (Option B selected, schema separation accepted); confirmation pending on final schema text in §3.2.
- **Integrator:** endorsement pending; phasing revised per Scout's signal and is conservative.

**Recommended next steps:**
1. Architect confirms §3.2 schema text matches the rights/display separation as proposed.
2. Integrator reviews phasing and the 14-day Tier B fallback.
3. On three-stance endorsement, this becomes v1.0 (ratified).
4. Phase 0 implementation begins: build `policy/index.html`, `policy/attribution-templates.html`, `CONTENT-LICENCE.md`, and the aggregator script. *No paper pages yet.*

*Drafted under Guardian stance. Convergent revisions integrated. No standing-order veto raised. Returning to Council for Architect and Integrator endorsement.*
