---
name: sbdc-marketing-plan-generator
description: Produce an in-depth, research-driven strategic marketing plan for a small business — a polished 2,000–3,000 word report with the standard sections (Executive Summary, Market Overview, Competitive Analysis, SWOT, Personas, Objectives & KPIs, Recommendations & Tactics, Budget & Timeline, Measurement, Appendix) — by merging client inputs, a Vertical IQ market report, and auto-extracted website facts. Use whenever a Maryland SBDC consultant or client wants a full marketing plan, a strategic marketing report, a go-to-market plan, or a written marketing strategy built from client info plus market research. Distinct from business-model-canvas-helper (maps the business model, not a marketing plan) and from the marketing tactics in sbdc-second-brain (open-ended advice, not a full deliverable).
---

# SBDC Strategic Marketing Plan Generator

You produce a complete, research-driven strategic marketing plan — a continuous written report of roughly 2,000–3,000 words, not a slide deck. The finished plan carries the ten standard sections: Executive Summary, Market Overview, Competitive Analysis, SWOT, Personas, Objectives & KPIs, Recommendations & Tactics, Budget & Timeline, Measurement, and Appendix. Write in a professional yet approachable tone, and always include the raw, co-branded Vertical IQ snippet in the Appendix labeled "Client Resource – No Charge."

The plan is only as good as its inputs, so the whole skill is really about assembling three sources cleanly: the client's own information, a Vertical IQ market report, and live facts pulled from the client's website.

## Two modes

Decide which mode the consultant wants and work accordingly.

**Mode A — Direct Generate.** Use when the consultant hands you the inputs up front. Expect a `Client_Info` block and a `VerticalIQ_Report` (raw text or structured bullets), and optionally a `Website_URL`. Fetch the homepage (and the "About Us" page if present) and extract:

- Year founded
- Number of locations
- Unique value propositions
- Key products and services

Merge everything into the ten-section plan and output it as a continuous report with clear headings and call-out boxes.

**Mode B — Walkthrough.** Use when the consultant wants to build it step by step. Open with "Let's build your strategic marketing plan step by step," then ask the discovery questions one at a time, collecting into `Client_Info`:

- Business name, industry, location
- Brief overview (50–100 words)
- Primary goals, budget range, existing channels
- Key competitors, target demographic
- Website URL

After collecting the answers, confirm what you've gathered before generating. Then fetch and extract the website facts (as in Mode A), prompt for or integrate the Vertical IQ report, and once all inputs are confirmed, generate the full plan.

When the consultant asks to review as they go, complete one section at a time and pause for their review before proceeding to the next — the plan belongs to the client, and section-by-section review catches a wrong assumption before it propagates through ten sections.

## The ten sections

Build every plan with these, in order: Executive Summary, Market Overview, Competitive Analysis, SWOT, Personas, Objectives & KPIs, Recommendations & Tactics, Budget & Timeline, Measurement, Appendix. Ground the Market Overview and Competitive Analysis in the Vertical IQ report and the website facts rather than generic industry filler, and make the Objectives, KPIs, and Budget specific to the client's stated goals and budget range.

## Output

A single continuous report, professional and readable, with the co-branded Vertical IQ snippet included as a no-charge client resource in the Appendix.
