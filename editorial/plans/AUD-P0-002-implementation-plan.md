# AUD-P0-002 implementation plan

- **Status:** published and resolved
- **Approved:** 2026-07-12
- **Verified:** 2026-07-12
- **Published:** 2026-07-12
- **Released edition:** 2026.07.12.5

## Objective

Replace the textlog-derived German display with an accountable critical reading
based on *Gesammelte Schriften* II.1; preserve the reported T1–T4 evidence;
synchronize the English translation, commentary, epilogue, bibliography,
README, colophon, and revision records; and publish no intermediate state.

The evidence and recommendations are recorded in
`editorial/reviews/AUD-P0-002A-collation-research-findings.html` and its three
linked memoranda.

## Approved readings

- Adopt GS at ED/GS divergence IDs 1–8 and 10–16.
- Retain Genesis 1:11 at ¶14 as a declared edition emendation of GS 1:14.
- At ¶3, restore unanimous T1–T4 `in` as a declared departure from GS’s
  conjectural `in einer Sprache`.
- Retain the sensible GS conjectures `Einsichten. –` and `die einzige`, while
  recording the reported T1–T4 readings internally.
- Restore `der menschliche Namen` and `Genetiv` as marked historical forms;
  do not silently standardize them.
- Restore every visually confirmed GS emphasis boundary in the German reading.

## Translation policy for this revision

- ¶1: “to impart its content” becomes “to impart its quintessential content.”
- ¶3: “imparts itself in a language and not through a language” becomes
  “imparts itself in, and not through, a language.”
- Retain the English full stop at the end of ¶5: Reclam and Jephcott support it,
  while the German reading follows the GS colon.
- Retain Genesis 1:11 in English and identify it as an emendation.
- `Namen` and `Genetiv` require no English lexical change.
- Carry German emphasis into English where the correspondence is direct and
  philosophically functional. Partial-word and non-isomorphic cases require an
  explicit translation judgment rather than mechanical copying; every such
  decision is recorded in the internal collation.

## Implementation sequence

1. Create `edition/german-gs.md`, `edition/german-reading.md`,
   `edition/textual-apparatus.yml`, and `edition/collation.md` before changing
   the public display.
2. Encode all sixteen former ED/GS divergences, the ¶3 T1/GS decision, the
   three GS conjectures, later-witness conflicts, and the complete emphasis
   layer.
3. Update the 26 German paragraphs and the two required English readings.
4. Synchronize exact German commentary quotations in wording, punctuation,
   and emphasis; update English quotation headers where the translation
   changes.
5. Rewrite the ¶1, ¶2, ¶3, ¶4, ¶8, ¶14, and ¶16 textual commentary affected
   by the new evidence; remove every stale “GS pending” claim.
6. Revise the translator’s note, epilogue, bibliography, README, and colophon
   so they preserve the edition’s actual history while naming GS as the current
   base and textlog as provenance only.
7. Add the compact public apparatus: ¶3 `in` and ¶14 Genesis 1:11 are the two
   departures from GS; explain `Namen`, `Genetiv`, GS’s critical constitution,
   and the emphasis policy.
8. Record the net reader-visible revision under `Unreleased` until deployment;
   on publication, create the matching on-site Revision History entry, version,
   commit, and tag.

## Verification gates

- Maintained reading text and all 26 displayed German paragraphs agree in
  wording, punctuation, and emphasis.
- The maintained GS source accurately represents the printed GS reading and
  does not masquerade as a diplomatic T1 transcription.
- Every exact German commentary quotation is a verified excerpt of the adopted
  reading after explicit ellipsis and editorial terminal-punctuation handling.
- The public apparatus exposes both edition departures from GS; the internal
  collation contains all sixteen ED/GS divergences and all reported GS
  interventions.
- ¶1 and ¶3 English text and quotations agree with the revised translation;
  the English quintessence-family count is recomputed.
- No stale `fourteen`, `fifteen`, `99.7%`, `GS pending`, “GS will settle,” or
  nonexistent German-frontmatter claim remains in current documentation.
- README, bibliography, epilogue, translator’s note, colophon, Revision
  History, and `CHANGELOG.md` report one provenance and one edition state.
- Existing paragraph and sentence fragment identifiers remain stable.
- Desktop, mobile, keyboard, German-toggle, apparatus, and accessibility
  checks pass before publication.

## Publication boundary

Implementation may proceed locally as one coordinated unreleased change.
Publication is a separate terminal step: do not commit, tag, push, or deploy
until every gate passes and the complete reader-visible state is ready at once.

## Verification record

All gates passed locally on 2026-07-12. The maintained German and the 26
displayed paragraphs match exactly; the adopted reading differs from GS only
at ¶3 and ¶14; 125 German and 125 English commentary excerpts match their
paragraph sources; and the English reading contains 62 quintessence-family
occurrences. Desktop and 390px mobile browser checks found no document
overflow, console error, or page error; German toggle, commentary sheet,
apparatus anchors, and j/k/g/Escape handlers passed. The complete state was
published as Edition 2026.07.12.5.
