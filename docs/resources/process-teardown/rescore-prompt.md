# Prompt — re-score the updated VOSBTC26 deck

Paste everything below the line into a new chat in the **VOSBTC26 Workshop** project, attach the updated deck HTML, and send.

---

I'm an SBDC business advisor at Maryland SBDC at UMD. On September 17, 2026 I'm giving Session 4 at the 4th Annual Veteran-Owned Small Business Training & Conference (VOSBTC26), Maritime Conference Center: "Using AI to Increase Business Productivity, Efficiency & Growth." 60 minutes, established veteran-owned business owners, many in GovCon. Design basis is a conversation with a VBOC partner: effective AI use comes from understanding your own processes first, then implementing efficiently. Mechanics/hands-on setup is deliberately deferred to a separate nClouds/AWS workshop.

**The deck's model:** write the steps of one process (4–8), mark each Judgment (J) or Repetition (R), hand the first R step to AI, keep the J. Three worked "teardowns" — floor (GovCon compliance matrix from Section L/M/C), middle (past-due invoice nudge, three tones), ceiling (Friday 4 p.m. scheduled weekly action log) — each with process, steps, J/R table, first R step, "what I'd paste" prompt, and "what went sideways." Then a 15-minute worksheet exercise, share-outs, SBDC one-on-one pitch, and a Triage booking CTA.

**Two project docs already exist — read both first:**
- `claude/VOSBTC26-workshop-rubric.md` — the 10-criterion, 100-point rubric (weights 4/3/3/4/3/3/2/3/2/2; ship line 80+, no criterion at 1; a 1 in Audience Fit, Demos, or Time Design auto-fails).
- `claude/VOSBTC26-deck-scorecard.md` — the first scoring. Result 86/100, held by criterion 9 (Risk, cost, trust) scored 1. Four fixes were prescribed: (1) add a "don't paste this" risk slide with three rules of thumb, (2) fix the worksheet CTA href, which was the literal placeholder `{{TRIAGE_BOOKING_URL}}`, (3) run the Teardown 2 prompt live with a recorded backup, (4) write minute marks into speaker notes and name Teardown 3 as the cut block.

**How to read the deck file:** it's a bundled single-file HTML, ~1 MB, and the slide content is NOT in the visible body. It lives in `<script type="__bundler/template">` as a JSON string. Extract it with Python: regex out that script block, `json.loads` it, then strip `<script>`/`<style>` and tags to get slide text. Speaker notes are in elements matching `speaker-notes`; last time they were empty (title only) — check whether that changed. Font sizes are inline px on a 1920-wide canvas; 24px ≈ 12pt on a projector, and the rubric bar is 28pt. The worksheet is `worksheet.html` in this folder — read it and check the Triage CTA href specifically.

**What I want:**
1. Re-score the attached deck and the worksheet against the rubric. Same 10 criteria, same table format as the existing scorecard, with a "what earned it / what's missing" note per row.
2. For each of the four prescribed fixes, state whether it was made, partially made, or not made, with the evidence (slide text, href value, note contents).
3. Show the delta: previous score → new score per criterion, and the new total.
4. Anything new that got worse or broke.
5. Updated fix order, if anything is still open.
6. Save the result to the project as `claude/VOSBTC26-deck-scorecard-v2.md` and give me the file.

Don't repeat these instructions back. Data before opinions. Plain language, no corporate filler. One prioritized recommendation at the end, not a menu.
