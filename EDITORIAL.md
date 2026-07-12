# Editorial Process

This repository maintains *On Language as Such and on the Language of Man* as a living scholarly edition. The edition may change, but it must never change opaquely.

The process below governs every substantive correction or revision arising from [AUDIT.md](AUDIT.md) and any later editorial review.

## Governing principle

Every substantive issue moves through a gated sequence:

> document → present → discuss → decide → implement → verify → record → publish

No audit remediation is applied to the edition before its issue has been presented in a dedicated internal HTML review and explicitly approved.

## The three records

The project keeps three complementary histories:

1. **Revision History** is the curated, reader-facing account embedded in `index.html`. It records dated, published, reader-visible changes.
2. **Textual apparatus** records every adopted reading of the German witness and every editorial emendation, with source reading, adopted reading, authority, and rationale.
3. **Git history** is the exhaustive implementation record. It may contain mechanical, formatting, and maintenance changes that do not belong in the public Revision History.

`CHANGELOG.md` is the maintained repository source for the public Revision History. Until the site is generated from structured sources, its published entries must be copied into `index.html` as part of the same change and checked for agreement.

## Versioning

Published editions use calendar versions:

```text
YYYY.MM.DD
```

If more than one public edition is released on the same day, append a sequence:

```text
YYYY.MM.DD.2
```

Each published edition should have:

- the version displayed in the colophon;
- a corresponding dated entry in `CHANGELOG.md` and the on-site Revision History;
- a durable Git commit and, for substantive releases, a tag named `vYYYY.MM.DD`;
- enough information for a reader to identify the state consulted.

## Issue identifiers and internal review pages

Audit issues use stable identifiers:

```text
AUD-P0-001
AUD-P0-002
AUD-P1-001
```

Their internal review pages live under `editorial/reviews/` and use the identifier in the filename. They are not linked from the published edition and must contain:

- issue status and priority;
- the complete current claim or behavior;
- affected files, passages, and selectors;
- verified facts and supporting sources;
- uncertainties and facts still requiring verification;
- consequences of leaving the issue unresolved;
- viable resolution options and their tradeoffs;
- a provisional recommendation;
- exact proposed language or code where useful;
- explicit questions requiring an editorial decision;
- acceptance criteria and a verification plan;
- a decision and implementation record once resolved.

Internal HTML pages include `noindex, nofollow`. Because the repository root is also the GitHub Pages source, this makes them unlisted and discourages indexing but does **not** provide access control. Truly confidential material must not be committed to the publishing branch.

## Status lifecycle

Every issue passes through these statuses:

1. **Open** — documented but not yet presented.
2. **In discussion** — review page presented; edition remains unchanged.
3. **Approved** — an explicit decision has been recorded.
4. **Implemented** — the approved change has been applied locally.
5. **Verified** — textual and/or browser checks have passed.
6. **Published** — the public edition, Revision History, changelog, and version marker agree.
7. **Resolved** — the audit checklist and internal review record are closed.

If new evidence undermines an approved resolution, the issue is reopened rather than silently rewritten.

## Per-issue workflow

### 1. Select

Take the highest-priority unresolved issue in `AUDIT.md`. Closely related findings may be grouped only when resolving them requires the same editorial decision.

### 2. Present

Create or update the issue's internal HTML page. Present the page for review without modifying the affected edition text or behavior.

### 3. Discuss

Work through the facts, uncertainties, options, and wording. Research may continue during this phase. Read-only investigation does not constitute implementation.

### 4. Decide

Record the chosen option and exact scope in the review page. Implementation begins only after explicit approval.

### 5. Implement

Apply only the approved resolution. Newly discovered adjacent problems are documented separately rather than silently folded into the change.

### 6. Verify

Verification is proportional to the change:

- textual changes are checked against the maintained witness and apparatus;
- translation changes are checked across every repeated term and commentary quotation;
- citation changes are opened and checked against the claimed source;
- interface changes are tested at desktop and mobile widths, with keyboard and deep-link checks;
- rights and license changes are checked for consistency across README, LICENSE, bibliography, colophon, and metadata.

### 7. Record

Before publication:

- update `CHANGELOG.md` under `Unreleased`;
- add the matching entry to the public Revision History;
- update the current-edition marker;
- update the issue's decision and verification record;
- update the corresponding `AUDIT.md` checklist item.

Meaningful translation changes record the old wording, new wording, paragraph or sentence identifier, and a concise reason. German-text changes additionally belong in the textual apparatus.

### 8. Publish and close

After publication, move the changelog entry from `Unreleased` to the released calendar version, add the permanent commit/tag, mark the issue Published and Resolved, and proceed to the next audit item.

## What belongs in the public Revision History

Record:

- changes to the German reading text;
- changes in translation wording or policy;
- substantive commentary, epilogue, or bibliography revisions;
- corrected factual claims or citations;
- rights and licensing changes;
- interface changes that affect reading, navigation, accessibility, or citation;
- significant structural changes to the edition.

Usually group rather than enumerate:

- typographic cleanup;
- formatting-only changes;
- mechanical refactoring with no reader-visible effect;
- test and build maintenance.

Do not record a proposed change as though it were published. Proposals remain in their internal review pages; completed local work remains under `Unreleased` until deployed.

Every public-facing entry, including `Unreleased`, describes the net reader-visible difference from the most recent published edition. Do not narrate intermediate local states, reverted experiments, or changes to work that readers never saw. Those details belong in internal review records and Git history.

## Changelog entry form

```markdown
## YYYY.MM.DD

### German text
- ¶14: `Genesis 1:11` → `Genesis 1:14`, corrected against *GS* II.1,
  p. 148.

### Translation
- ¶21.16: “the hundred languages of man” → “hundreds of human
  languages,” restoring `hunderten Menschensprachen`.

### Commentary
- Added the verified Hamann letter locus to ¶11.

### Interface
- Repaired the mobile apparatus and paragraph keyboard navigation.
```

Categories with no changes are omitted.
