# AUD-P0-002 — adversarial full-text recollation

**Date:** 2026-07-12
**Scope:** Independent recollation of all 26 displayed German paragraphs against *Gesammelte Schriften* II.1, pp. 140–157; comparison with the current textlog transcription, the official 2019 Reclam reading text where its sample is available, the critical report in *GS* II.3, and Edmund Jephcott's canonical English translation as a control only.
**Status:** Research complete; no German, English, commentary, or provenance text changed.
**Confidence convention:** High = directly visible or explicitly reported by the critical edition; medium = strong multi-witness inference whose manuscript basis was not directly inspected; low = unresolved without a facsimile or another historical witness.

## Executive conclusion

The first review's fifteen ED/GS divergences were not the whole textual problem.

1. **One additional word-level ED/GS divergence was missed:** ¶8 has `Genitiv`, while the visually inspected *GS* p. 144 and Fred Lönker's official 2019 Reclam edition both have `Genetiv`. Duden records `Genetiv` as a valid but now obsolete spelling. Under the approved policy of following *GS* in spelling, it should be restored, not silently modernized.
2. **A much larger class was omitted:** the displayed German has zero emphasis markup, while *GS* contains extensive italics and its critical report identifies at least one passage as double-underlined in all four typescripts. The official Reclam sample exposes 56 italic XML fragments through only its printed p. 25 (approximately through *GS* p. 152), and the remaining *GS* page images add further emphasized words. Emphasis is textual data here, not merely house styling.
3. **The initial Genesis recommendation should be reversed.** *GS* and, by implication from the apparatus, T1 read `1,14`, but ED's `1,11` is supported separately by Jephcott (1978) and Reclam (2019), and it alone fits Benjamin's immediate claim that only the fiat occurs in that creation act. Retain `1,11` as a declared editorial emendation of the *GS* base.
4. **The initial `Name` recommendation should also be reversed.** *GS*, the authorial typescript by implication, textlog, and Reclam all read `der menschliche Namen`. Modern `Name` is commoner, but IDS Grammis records nominative `der Namen` as an attested rare variant produced by the same historical declensional reanalysis. The authorial and later critical agreement defeats the premise that `Namen` is simply a typo. Restore `Namen` and, if desired, gloss its rarity in the apparatus.
5. **The web witnesses are not independent.** textlog and Projekt Gutenberg reproduce numerous identical rare corruptions and share *GS*'s editorial conjectures. They are best treated as descendants of one defective electronic transcription of a Suhrkamp text, not as corroborating witnesses.
6. **The declared base is already an edited text.** *GS* II.3 says T1 is the `Druckvorlage`, but explicitly records *GS* conjectures at 142,8 (`in einer Sprache` for unanimous T1–T4 `in`), 143,21 (`Einsichten. –` for `Einsichten.!`), and 150,12 (`die` for unanimous `das`). An accountable edition should preserve the distinction between authorial T1 and the editorial constitution of the chosen *GS* base.

The revised lexical/punctuation count is therefore **sixteen ED/GS divergences**: adopt *GS* in fifteen, retain ED `1,11` as one declared emendation, and restore the omitted emphasis layer separately. This conclusion is provisional only in the sense that the 1955 printing and T1–T4 facsimiles were not obtained; it is not provisional about what the inspected *GS* pages print.

## Materials and method

### Witnesses actually inspected

- **GS reading text (visual):** Walter Benjamin, “Über Sprache überhaupt und über die Sprache des Menschen,” in *Gesammelte Schriften* II.1, ed. Rolf Tiedemann and Hermann Schweppenhäuser (Suhrkamp, 1977), pp. 140–157. Every one of the eighteen page images was inspected at high resolution. The embedded OCR was used only to locate passages and generate challenge lists; readings reported as visual were checked against the scan. [Public scan](https://www.kritiknetz.de/images/stories/texte/walter-benjamin-gesammelte-schriften-ii.pdf)
- **GS critical report (visual and extracted):** *GS* II.3, printed pp. 931–936, especially p. 935 for `Überlieferung` and `Lesarten`. It identifies T1–T4, declares T1 the printing copy, and discloses the editors' conjectures. This was visually checked, not accepted from OCR alone. [Same volume scan](https://www.kritiknetz.de/images/stories/texte/walter-benjamin-gesammelte-schriften-ii.pdf)
- **ED:** the 26 German `<div class="de">` paragraphs currently embedded in `index.html`, plus all 125 German commentary blockquotes and rights/bibliographic statements.
- **TL:** the current [textlog transcription](https://www.textlog.de/benjamin/essays/metaphysisch/sprache-ueberhaupt-und-sprache-des-menschen), retrieved during this pass.
- **Reclam 2019:** Walter Benjamin, *Über Sprache überhaupt und über die Sprache des Menschen*, ed. Fred Lönker, Reclam Universal-Bibliothek 19607 (2019). The publisher describes it as a critical edition; its official product record identifies Lönker, publication date, and ISBN. The available sample contains the reading text from the opening through part of the Fall discussion. Its PDF is born-digital, so both visible text and font-level emphasis were examined. [Official product page](https://www.reclam.de/produktdetail/ueber-sprache-ueberhaupt-und-ueber-die-sprache-des-menschen-9783150196076), [sample PDF](https://www.lesejury.de/media/samples/076/9783150196076_leseprobe.pdf)
- **Jephcott control:** the seven-page scan at `/Users/jesse/Desktop/Benjamin-3-11-On Language as Such (2).pdf`, pp. 62–74 of *Selected Writings* I / the received Jephcott translation. All pages were visually inspected. It is evidence for how a prior editor or translator understood difficult readings, not authority over the German.
- **Projekt Gutenberg control:** its page labels the source “Suhrkampverlag” and year “1996,” but the text contains the same distinctive electronic corruptions as textlog. [Page](https://projekt-gutenberg.org/authors/walter-benjamin/books/ueber-sprache-ueberhaupt-und-ueber-die-sprache-des-menschen/chapter/2/)
- **Lexical controls:** Duden's entry for [`Genetiv`](https://www.duden.de/rechtschreibung/Genetiv) marks the form obsolete but valid; IDS Grammis describes nominative variants including [`der Name (der Namen)`](https://grammis.ids-mannheim.de/kontrastive-grammatik/3635).

### What was not inspected

- No facsimile of T1, T2, T3, or T4 was available. Statements about their readings are limited to what the *GS* critical report explicitly records or, where clearly marked, what follows from its declaration that T1 was the printing copy.
- The 1955 *Schriften* II reading text was not obtained. Its table of contents and publication facts are documented elsewhere in the repository, but they cannot establish individual readings.
- The 2019 Reclam sample stops before the end of the essay. It is therefore an authoritative later comparator for only the part it exposes.
- No surviving manuscript or archival image was requested from an institution; no external outreach was performed.

### Procedure

1. Extracted the 26 ED German paragraphs and their repeated commentary quotations.
2. Visually read *GS* pp. 140–157 in sequence, checking words, punctuation, paragraph transitions, biblical numbers, quotations, and emphasis.
3. Used OCR/token comparison only to generate possible mismatches; every retained mismatch was checked against the image.
4. Compared the first eighteen ED paragraphs with Reclam's born-digital sample, separating modern spelling from substantive/editorial readings.
5. Read *GS* II.3's transmission report to test whether the printed *GS* reading was authorial or conjectural.
6. Inspected the canonical English scan for consequences and prior editorial choices, without treating translation as a German witness.
7. Searched the 125 German commentary blockquotes for every affected string and for display/quotation disagreement.

## Witness genealogy

### T1–T4 and GS

The critical report provides the only documented stemma-like evidence obtained in this pass:

| Siglum | Description in *GS* II.3 p. 935 | Evidentiary consequence |
|---|---|---|
| T1 | Typescript with Benjamin's handwritten corrections, Benjamin Archive Ts 93–115 | Declared `Druckvorlage`; strongest surviving authorial witness reported by the editors. |
| T2 | Typescript copy of a lost original; perhaps early, perhaps made by Gretel Adorno in America after T1 | Its independence and date are uncertain. |
| T3, T4 | Carbon typescripts from the same lost original, Ts 134–169 | Sibling copies, not independent authorial revisions. |
| GS | Printed from T1, with explicit editorial conjectures | A critical reading text, not a diplomatic transcript of T1. |

The three explicit *GS* conjectures are editorial facts the new source architecture should preserve:

- *GS* 142,8 `in einer Sprache` for T1–T4 `in`.
- *GS* 143,21 `Einsichten. –` for T1–T4 `Einsichten.!`.
- *GS* 150,12 `die` for T1–T4 `das` in `(Es ist dies nicht die/das einzige …)`.

The report also says the passage beginning `Das` and ending `Sprache.` at 142,22f. was double-underlined in all four typescripts. The printed visual emphasis and the later Reclam emphasis are therefore not decorative inventions.

### The electronic branch

textlog and Projekt Gutenberg share, among many others, the highly diagnostic corruptions `seinen Inhalt` (lost `geistigen`), `in selbst`, `zwischen Geist, und`, `existentester.`, `in den Namen Das`, `»in der Mitteilung`, `hervor-, In`, `Obersetzung`, `Manschen`, `er kennen`, and longer broken clauses around `Der Inbegriff …`. They also reproduce *GS* conjectural readings such as `in einer Sprache` and `die einzige`.

That pattern is incompatible with two independent transcriptions. It supports one defective electronic ancestor, or direct copying between the sites, downstream of a Suhrkamp reading text. Projekt Gutenberg's own “Suhrkampverlag | 1996” label makes a post-*GS* Suhrkamp source especially plausible. The exact direction of copying cannot be proved from the public pages, so this report does not assert whether textlog copied Gutenberg, Gutenberg copied textlog, or both imported a third file.

ED began from this branch and corrected many of its errors, but not all. The previous “99.7% agreement with a second online witness” therefore provides no independent confirmation.

## Revised disposition of all sixteen ED/GS divergences

The numbering preserves the first review's fifteen items and appends the newly found word-level item as 16.

| ID | Locus | ED | Visually inspected GS | Other evidence | Fresh recommendation | Confidence |
|---|---|---|---|---|---|---|
| 1 | ¶1; *GS* 141 | `seinen Inhalt mitzuteilen` | `seinen geistigen Inhalt mitzuteilen` | Reclam retains `geistigen`; TL shares the omission. Jephcott gives “mental nature/content” in this clause. | Restore `geistigen`; change English “its content” under the settled `geistiges Wesen` policy; update the German blockquote. | High |
| 2 | ¶1; *GS* 141 | `ist eine Idee: aber` | `ist eine Idee; aber` | Reclam has the semicolon. | Adopt semicolon; update quoted German. | High |
| 3 | ¶2; *GS* 141 | `und über ihm, gerade über ihm sich schwebend zu erhalten, ist ihre Aufgabe` | `und über, gerade über ihm sich schwebend zu erhalten ist ihre Aufgabe` | Reclam follows *GS*. The *GS* syntax is a deliberate-looking suspension rather than an accidental omission. | Restore *GS*; keep clarifying English syntax. | High for reading; medium-high for interpreting the suspension as deliberate |
| 4 | ¶3; *GS* 142 | `sprachlichen Wesen: Das geistige Wesen` | `sprachlichen Wesen. Das geistige Wesen` | Reclam has the full stop. | Adopt full stop and make the quotation boundary explicit. | High |
| 5 | ¶4; *GS* 142 | `jede Sprache teilt sich in selbst mit` | `jede Sprache teilt sich in sich selbst mit` | Reclam and the English control support the full reflexive construction. | Restore second `sich`; update the blockquote. | High |
| 6 | ¶5; *GS* 143 | `daß er die Dinge benennt.` | `daß er die Dinge benennt:` | Reclam changes this to a full stop, but *GS*/T1's colon opens the next questions `Wozu benennt? Wem …?` and is the declared base reading. | Adopt *GS* colon; preserve the rhetorical transition. | High for base; medium-high against Reclam's later punctuation |
| 7 | ¶11; *GS* 146 | `zwischen Geist, und Sprache` | `zwischen Geist und Sprache` | Reclam agrees with *GS*. | Remove comma. | High |
| 8 | ¶11; *GS* 146 | `der sprachlich existentester. d. h. fixierteste Ausdruck` | `der sprachlich existenteste, d. h. fixierteste Ausdruck` | Reclam agrees with *GS*. | Adopt *GS* morphology and comma. | High |
| 9 | ¶14; *GS* 148 | `Genesis 1,3; 1,11` | `1,3; 1,14` | The critical report does not list this as a conjecture, so `1,14` is inferentially T1. TL follows it. Jephcott 1978 and Reclam 2019 both read 1:11. Genesis 1:11 is the act in which the speech alone initiates creation; 1:14 is followed by God's making the lights at 1:16. | **Retain `1,11` as a declared emendation of *GS*/T1.** Rewrite commentary that currently says *GS* will settle the question: *GS* creates the disagreement, while Jephcott, Reclam, and the argument support the emendation. | High that *GS* reads 1:14; medium-high that 1:11 is the correct editorial reading |
| 10 | ¶16; *GS* 149 | `der menschliche Name` | `der menschliche Namen` | Not listed as a *GS* conjecture, hence inferentially T1; TL and Reclam preserve `Namen`; scholarship routinely quotes it. IDS Grammis documents rare nominative `der Namen`. Jephcott's “human name” cannot decide German morphology. | **Restore `Namen`; do not emend an attested authorial form merely because `Name` is commoner.** A brief apparatus gloss may prevent readers mistaking it for a transcription error. | High on witnesses; medium-high on retaining the marked form |
| 11 | ¶16; *GS* 150 | `Dinge selbst; aus denen` | `Dinge selbst, aus denen` | Reclam follows the semicolon rather than *GS*; the current commentary blockquote already silently has the *GS* comma. | Adopt base comma and synchronize display/quotation. | High for *GS*; medium-high editorially |
| 12 | ¶18; *GS* 151 | `in den Namen Das ist also` | `in den Namen. Das ist also` | Reclam and the current German blockquote already have the stop. | Restore full stop. | High |
| 13 | ¶19; *GS* 154 | `Diese Unmittelbarkeit »in der Mitteilung` | `Diese Unmittelbarkeit in der Mitteilung` | Stray guillemet is confined to the electronic branch/ED. | Remove guillemet. | High |
| 14 | ¶21; *GS* 155 | `sie hervor-, In der Sprache` | `sie hervor. In der Sprache` | Evident electronic corruption; the commentary omits this exact segment rather than reproducing it. | Adopt *GS*. | High |
| 15 | ¶22; *GS* 156 | `eine Obersetzung` | `eine Übersetzung` | The commentary blockquote already silently corrects it. | Restore `Übersetzung`. | High |
| 16 | ¶8; *GS* 144 | `wenn der Genitiv nicht …` | `wenn der Genetiv nicht …` | Reclam also has `Genetiv`; Duden marks it obsolete, not erroneous. TL/ED silently normalize it. | Restore `Genetiv` under the policy of following *GS* spelling; update the blockquote. | High |

### Net disposition

- Fifteen changes return ED to *GS*: 1–8, 10–16.
- One reading, 9, deliberately remains different from *GS* and must be publicly declared: `GS/T1 1,14; ED em. 1,11`.
- `Namen` is no longer a proposed edition emendation. Under the evidence now available, changing it to `Name` would itself be the emendation.
- *GS*'s own three conjectures remain part of the base text unless the editor separately decides to prefer T1. They belong in the internal collation record even if the public compact apparatus is limited to this edition's departures from *GS*.

## The omitted emphasis layer

### Finding

The German in `index.html` contains **zero** `<em>`, `<i>`, or `<strong>` descendants. That is not a neutral web normalization. Emphasis is structurally active throughout the essay: it distinguishes `in` from `durch`, draws out the `-bar` in `mitteilbar`, sets propositions apart, and marks quotations and pivots.

The official Reclam sample, inspected at the XML/font level, contains **56 italic fragments** before the sample ends. Line wrapping splits some logical emphases into multiple XML fragments, so 56 is not a count of independent editorial units. It is nevertheless a reproducible lower bound showing that the omission is systematic, not occasional.

Representative *GS*/Reclam emphasis includes:

- ¶2: `Sprache`, `durch`, `sich`, `λόγος`;
- ¶3–4: `in`, `durch`, `sofern`, the suffix `bar`, `was`, the full proposition `Jede Sprache teilt sich selbst mit`, `mitteilbar`, `ist`, `erscheint`, `an`, `Unmittelbarkeit` (Reclam encodes only the stem `Unmittel` in italics), and the opposed `durch` / `in` terms;
- ¶5–7: `benennt`, `benennende`, the full `Das sprachliche Wesen des Menschen ist also, daß er die Dinge benennt`, pronouns `er` / `sie`, and `durch` / `in`;
- ¶8–10: the full `im Namen teilt das geistige Wesen des Menschen sich Gott mit`, `durch`, `in`, `die`, `daß die Sprache schlechthin`, `heißen`, the full proposition `Der Mensch allein hat die nach Universalität und Intensität vollkommene Sprache`, and `in` before `die Mitteilbarkeit`;
- ¶10: the entire proposition beginning `Einen Inhalt der Sprache gibt es nicht` and ending `eine Mitteilbarkeit schlechthin mit`;
- ¶11–18: selected words in the Hamann quotation (`Sprache, die Mutter`, `Offenbarung`), `zunächst`, `Gabe`, `ihm`, `aber`, `schöpferischen`, and `die` in `in die Sprache`;
- later *GS* page images: `menschlichen` in `des menschlichen Wortes`, `etwas`, `bloßen Zeichen`, `Zeichen`, and `Menschen` in the parenthesis on nature's redemption.

Most decisively, *GS* II.3 p. 935 reports that the `Das … Sprache.` proposition at 142,22f. was **double-underlined in T1–T4**. The emphasis is authorial transmission evidence.

### Recommendation

1. Treat emphasis as a separate collation dimension, not as part of generic typography normalization.
2. Encode the complete *GS* emphasis in `edition/german-gs.md` and the adopted emphasis in `edition/german-reading.md` before revising `index.html`.
3. Preserve partial-word emphasis (`mitteil` + emphasized `bar`) when visually confirmed; it is philosophically meaningful.
4. Synchronize the German commentary blockquotes with the adopted emphasis wherever they quote emphasized language.
5. Add automated comparison that checks inline emphasis boundaries as well as plain text. A plain-text equality test will miss the present failure completely.

Because T1–T4 facsimiles were not inspected, this report does not claim that every printed *GS* italic is a literal transcription of the same manuscript mark. It does establish that deleting all of them is not faithful to the declared base.

## Repeated German quotation audit

The site has 125 `<blockquote class="deq">` elements. They are not currently generated from the German reading text and fall into three categories:

### Quotations that repeat a corrupt display reading

- ¶1 quotation omits `geistigen`.
- ¶1 closing quotation has the ED colon where *GS* has a semicolon.
- ¶2 quotation repeats the supplied first `ihm` and added comma.
- ¶4 quotation repeats `in selbst`.
- ¶8 quotation repeats normalized `Genitiv` rather than base `Genetiv`.
- ¶16 quotation repeats ED `Name` rather than the now-recommended `Namen`.

### Quotations that silently correct the display

- The ¶3 quotation boundary supplies a full stop where the display has a colon.
- The ¶5 excerpt closes with a full stop where the *GS* transition has a colon; if it remains an excerpt, the editorial terminal punctuation should be identified as such.
- The ¶16 quotation already has `Dinge selbst, aus denen`, while the display has a semicolon.
- The ¶18 quotation already has `in den Namen. Das`, while the display lacks the stop.
- The ¶22 quotation already has `Übersetzung`, while the display has `Obersetzung`.

### A commentary claim that is now false

The ¶14 commentary says that both online German witnesses have `1,14`, that the printed English has `1:11`, and that “GS II-1 will settle it finally.” The first two clauses are substantially right; the conclusion is not. Visual inspection shows that *GS* itself reads `1,14`. The note should instead state that ED emends *GS*/T1 to `1,11`, supported by Jephcott, Reclam, and the internal Genesis logic.

The safest implementation is to generate exact German quotation spans from the maintained reading source and mark ellipses/editorial terminal punctuation explicitly. Until then, a mechanical substring/emphasis check should be part of every textual release.

## English consequences

The German recollation directly requires only one wording change and one factual/apparatus correction in the current English:

1. ¶1 `seinen geistigen Inhalt mitzuteilen`: “to impart its content” loses the adjective. Under the already approved lexicon, the minimal correction is “to impart its quintessential content.” Jephcott's received translation also marks the phrase as mental/spiritual rather than bare content, but the governing authority is the German.
2. ¶14 should continue to show Genesis 1:11, but the textual note must identify it as an edition emendation rather than as the settled German witness.

Restoring `Namen`, `Genetiv`, punctuation, and emphasis does not require changing the corresponding English semantic wording, although the English display may benefit from matching emphasis where Benjamin's argument depends on it.

## Cross-check against the repository bibliography

- The bibliography correctly calls *GS* II.1 the critical text and gives pp. 140–157, but its statement that “fourteen transcription defects” were patched is obsolete. The current ED still has fifteen readings to return to *GS*, one deliberate Genesis emendation, and a systematically omitted emphasis layer.
- The epilogue's statement that only physical-book collation remained is obsolete because the print collation is now complete. What remains is editorial decision and implementation, plus any optional archival comparison with T1–T4.
- The colophon correctly says collation was pending; after an approved implementation it should name *GS* as the base and link the apparatus.
- The bibliography's Maler Müller title, `Adams erstes Erwachen und erste selige Nächte`, agrees with the *GS* critical report's source identification. Reclam's reading text abbreviates the title at one point; that later editorial difference is not a reason to change the bibliography.
- The critical report supplies the exact source locators the bibliography can add to its internal collation record: Hamann in Nadler III, p. 32; Maler Müller 1779, pp. 49 and 51; Kierkegaard/Haecker 1914, p. 44; and the Luther Bible edition cited at *GS* II.3 p. 935.

## Recommended implementation policy after review

1. Keep *GS* II.1 as the declared base, but describe it accurately as a T1-based critical text containing disclosed editorial conjectures.
2. Create the approved diplomatic, reading, apparatus, and collation sources before touching the display.
3. Encode all sixteen ED/GS divergences and the emphasis layer.
4. Adopt *GS* for IDs 1–8 and 10–16.
5. Record only ID 9 as this edition's substantive departure from *GS*: `1,14] 1,11 ED em.` Include the reason and supporting witnesses.
6. Preserve `Namen` and `Genetiv`; neither is demonstrated corruption.
7. Add a source-note layer for the three *GS* conjectures from unanimous T1–T4 readings. Whether all three need space in the compact public apparatus is a presentation decision, but none should be lost internally.
8. Generate or mechanically validate every German commentary quotation, including emphasis.
9. Revise the ¶14 commentary, German-source bibliography, epilogue, colophon, counts, and Revision History together.
10. Do not describe textlog, Projekt Gutenberg, or their agreement as independent confirmation.

## Acceptance tests suggested by this pass

- Plain German reading source equals the 26 displayed German paragraphs after intentional HTML normalization.
- Inline emphasis boundaries in the maintained source equal the displayed German emphasis.
- Every exact German commentary quotation is a source substring after explicit ellipsis normalization; no quotation contains a superseded reading.
- Apparatus contains sixteen ED/GS entries, with fifteen resolved to *GS* and one `ED em.` Genesis entry.
- Internal source notes contain the three *GS* conjectures over T1–T4.
- `geistigen`, `in sich selbst`, `existenteste, d. h.`, `Namen`, `Genetiv`, `in den Namen. Das`, `hervor. In`, and `Übersetzung` are present at their loci.
- `zwischen Geist, und`, `existentester.`, `»in der Mitteilung`, `hervor-, In`, `Obersetzung`, and bare `seinen Inhalt mitzuteilen` are absent from the maintained German and its quotations.
- Genesis is displayed as 1:11 and expressly identified as an emendation of *GS*/T1 1:14.
- Bibliography, colophon, textual note, epilogue, README, and Revision History report one consistent base, count, and status.

## Bottom line

The first pass was directionally right about the electronic corruption but too quick to equate “what *GS* prints” with “what Benjamin's typescript reads,” and too quick to treat unusual German as error. The decisive upgrade is not merely adding a sixteenth variant. It is moving to a layered record:

```text
T1 authorial reading
  → GS critical constitution (with disclosed conjectures)
    → this edition's critical reading (with one declared Genesis emendation)
      → generated display and synchronized quotations (including emphasis)
```

That structure makes the edition both readable and reversible. It also prevents the next online transcription from mistaking inherited corruption, authorial markedness, editorial conjecture, and typographic emphasis for the same kind of thing.
