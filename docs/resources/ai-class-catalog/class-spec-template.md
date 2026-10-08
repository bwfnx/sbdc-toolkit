# Class spec template

The brief the Maryland SBDC AI Co-Working team fills in before building any Applied AI class: audience, timing, objectives, demos, exercises, handout and prompt pack. Copy the template block into a new `SPEC.md` per class.


**House rules that apply to every step.**
- Tool and model names come from `ai-landscape-2026-09.md` only; nothing from its do-not-say list appears anywhere.
- No client names or real client scenarios. House examples: the exotic-pet store in Columbia (market research), the salon (renamed once, no bank named), the food truck → restaurant → franchise (phased planning), an independent consultant. Invent others freely; never reuse a name from the old decks' client slides.
- Practical and demo-heavy: no theory slide without an applied follow-up on the next slide.
- Plain language, large type, no mental math on slides or handouts — words over figures ("about twenty minutes," not "≈18.5 min").
- Every live demo has a fallback (saved output or screenshot) named in the run-of-show.
- Voice: direct, warm, no hype, no corporate filler. Short sentences.

---

## The template

```markdown
# SPEC — <slug>

**Class title:** <working title>
**Series:** Applied AI for Small Business (Maryland SBDC)
**Source:** <the old deck or outline this replaces, if any>
**Status:** step <1|2|3|4> — <draft | approved YYYY-MM-DD>

## 1. Audience

- Who is in the room: <owner stage — idea / startup / established; industry mix; typical AI experience>
- What they walk in with: <phones only | laptops | printed handout>
- What they must be able to do when they leave (one sentence): <…>
- Format: <in person at MIC | Zoom | hybrid>; room size assumption: <n>

## 2. Length and shape

- Target length: <60 | 75 | 90> minutes
- Slide count target: <n>
- Rhythm: <e.g., teach 10 → demo 5 → do 5, repeated; or one long build>
- Prerequisite class, if any: <intro-to-ai | none>
- What this class hands off to: <next class title>

## 3. Learning objectives (three to five, each starts with a verb, each is demonstrated in class)

1. <…>
2. <…>
3. <…>

## 4. Timed agenda

| Minute | Block | What happens | Slides |
|--------|-------|--------------|--------|
| 0 | Open | <show of hands / hook> | 1–2 |
| … | … | … | … |
| <end−5> | Close | what's being sent, next class, open door | … |

Rule: the first applied moment (demo or exercise) lands inside the first ten minutes.

## 5. Live demos (three to five)

| # | Demo | Tool + account | Exact prompt (copy-ready) | Expected result | Fallback |
|---|------|----------------|---------------------------|-----------------|----------|
| 1 | <name> | <Claude Pro / ChatGPT Plus / Gemini free / Copilot> | "<…>" | <what the room sees> | <screenshot / saved output file name> |

Pick from the demo-safe list in CURRENT-LANDSCAPE.md unless you have a reason not to. Pre-run anything slow.

## 6. Hands-on exercises (one to two)

- Exercise: <what each person does, on what device, in how many minutes>
- Share-out: <how results come back to the room>
- What they keep: <the artifact that goes home — usually a section of the handout>

## 7. What survives from the old deck

| Old slide(s) | Concept | Keep as-is / rework / move to handout / cut |
|--------------|---------|---------------------------------------------|
| <n> | <…> | <…> |

List what is **cut** too, with a one-line reason, so no one re-adds it.

## 8. Open questions for the lead instructor (answered at the step-1 gate)

1. <…>

## 9. Handout / worksheet contents (filled at step 3)

- Cover: class title, date line, one-sentence promise
- Section A — <the thing they fill in during the exercise>
- Section B — <reference: the framework, in plain language>
- Section C — <the prompts used in class, copy-ready>
- Section D — next steps: book a Triage appointment, next class in the series, one resource
- Design: large type, high contrast, fits on two printed pages or one phone screen per section

## 10. Prompt pack contents (filled at step 3)

- Grouped by task, not by tool; each prompt is copy-ready with [brackets] for the owner's own details
- Each prompt names which tool it was tested in and the date
- 8–15 prompts; the demo prompts from Section 5 are included verbatim

## 11. Run-of-show (filled at step 3)

- Minute-by-minute, with the exact prompt to paste at each demo, the fallback file name, and what to say if the tool stalls
- Pre-class checklist: accounts logged in, fallback files open, Wi-Fi test, handouts counted, booking QR on the last slide
- Post-class: what gets emailed, Neoserra training record, survey

## 12. Framing prompt (filled at step 4)

- Names the SlideDeck template (`templates/slide-deck/SlideDeck.dc.html`) and the Maryland SBDC Design System project by name
- Carries: audience, the one idea, tone, design rules, out-of-scope list, "use exactly these N slides and this exact on-screen text"
- Followed by the slide script pasted whole or a few slides at a time
```

---

## Slide script format (step 2) — same as VOSBTC26

```markdown
### Slide <n> — <short name>

**Type:** <SlideDeck slide type — see list below>

**On screen:** <the exact text on the slide; one idea; three bullets is a lot>

**Visual:** <layout instruction for Claude Design; for demo slides, "prompt set as a monospaced block">

**Notes:** ≈ minute <m>. <what the presenter says; for demo slides, the exact prompt to paste and the fallback file name>
```

**SlideDeck slide types.** The authoritative list is the template's `SKILL.md` in the Claude Design project "Maryland SBDC Design System" (root of the project). Until Chat 1 confirms the exact names, use these working labels and let the framing prompt map them: `title`, `section`, `statement` (one big line), `bullets` (max three), `two-column`, `demo` (prompt block + expected result), `table`, `image`, `quote`, `exercise` (instructions + timer), `closing` (what's being sent + booking QR). **Chat 1 action:** replace this paragraph with the real type names from `SKILL.md`.

---


## Quality checklist (run before every gate; copied from the design spec)

- Every live demo in the run-of-show has a fallback.
- Every tool/model name matches `ai-landscape-2026-09.md`; nothing from the do-not-say list appears.
- Handout reads at large type; no mental-math asks; plain language.
- Framing prompt explicitly names the SlideDeck template and the Maryland SBDC Design System.
- No client names or PII; invented examples only.
