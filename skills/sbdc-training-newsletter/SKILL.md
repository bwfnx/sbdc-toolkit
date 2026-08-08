---
name: sbdc-training-newsletter
description: Build the Maryland SBDC monthly training newsletter end to end — parse a Neoserra training-events export into a single clean, chronological course table, merge that table into the Constant Contact newsletter template, and then generate one course-themed image at a time on request. Use whenever a consultant wants to assemble the monthly SBDC training newsletter, turn a list or PDF of upcoming training events into a formatted newsletter, aggregate Neoserra course data into a table for the newsletter, or generate images for each course in the newsletter. Covers both halves of the workflow — the data aggregation and the newsletter-plus-images production.
---

# SBDC Training Newsletter

This skill builds the Maryland SBDC monthly training newsletter in three stages: aggregate the raw training-event data into one clean table, render that table into the newsletter, and generate a themed image per course on demand. The two halves used to be separate tools; they are one pipeline — the table the aggregation step produces is exactly what the newsletter step consumes. Data integrity is the throughline: every date, time, fee, and instructor has to survive from the Neoserra export to the finished newsletter unchanged.

## Stage 1 — Aggregate the events into one table

Input is a Neoserra training-events export (PDF or text) for the target month, plus any user-provided corrections or updates. Parse every event and produce a **single, chronological table** with these columns:

| Date | Time | Event Title | Fee | Format | Topic | Location | Instructor | Course Description (from source) |

Rules:

- Normalize date and time to a consistent, human-readable format (e.g., "March 5, 2026", "1:00PM – 2:00PM").
- Put the fee in the Fee column, or "No Fee" if unspecified.
- Reflect online / in-person / hybrid status in the Format column.
- Use the exact source text for the Course Description column.
- If the user supplies an external list or correction that overrides the export (e.g., $20 vs. $25), incorporate it, resolving discrepancies to the best-known value.
- For any missing field, write "(Not listed)" or "(No data)" rather than leaving it blank — never drop the rest of a row over one missing field.
- Sort ascending by date, then time. Ensure no event is duplicated.

Output the aggregated table on its own first, so the consultant can confirm the data before it goes into the newsletter.

## Stage 2 — Merge the table into the newsletter

Take the confirmed course table and the newsletter template (the consultant provides the Constant Contact template, or asks you to use the standard monthly layout) and produce the final, consolidated newsletter:

- Fill each course section of the template from the table.
- Keep the template's headings, bullet points, "Register Here" placeholders, and formatting intact.
- Verify every course's date, time, instructor, fee, and description matches the table exactly — this is the step where transcription errors creep in, so double-check.

Present the complete newsletter as a single, final piece of text.

## Stage 3 — Generate course images one at a time

Image generation is part of the deliverable, not an afterthought. After the newsletter is assembled, wait for the consultant to say **"Next"**, and then generate an image for one course at a time, in newsletter order:

1. Identify which course is next in sequence.
2. Write a short text-to-image prompt describing a scene or concept that visually represents that course's topic — name the style, key objects, and background.
3. Produce the image (or the image prompt, if the surface has no image model), then confirm and offer to proceed to the next course.

Only generate one course image per "Next" so the consultant can review and request changes before moving on. Keep the visual style consistent across the set so the newsletter reads as one piece.

## Throughout

Keep responses clear and user-friendly. The two failure modes to guard against are data drift (a fee or instructor that changed between the export and the newsletter) and formatting drift (a course section that doesn't match the template) — check for both before calling the newsletter done.
