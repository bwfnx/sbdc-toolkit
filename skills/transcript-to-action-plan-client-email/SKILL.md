---
name: transcript-to-action-plan-client-email
description: Turn a client meeting transcript into the professional follow-up email a Maryland SBDC consultant posts into Neoserra as the record of the meeting, with Next Steps, Notes, Things We Have Accomplished Since Our Last Meeting, and Relevant Links sections. Use whenever someone pastes, attaches, or describes a client consultation transcript, call recording, or meeting notes and wants a client-facing recap and action-plan email drafted from it — this is the client-facing deliverable, not internal meeting notes and not a re-engagement email to a lapsed client. Also trigger when asked to identify or flag Neoserra milestones from a conversation (certifications like 8(a), MBE, WBE, DBE, EDWOSB, WOSB, MDOT, SDB; business sales or expansion; legislative letters; AI tool adoption or AI-driven improvement; survey responses), to draft an SBDC next-steps or action-plan email, to summarize a client meeting into next steps and accomplishments, or to map a meeting to Neoserra/Nexus milestone and counseling dropdown selections.
---

# Transcript to Action Plan & Client Email

This email is not just correspondence — it's the record that gets posted into Neoserra, and the milestones flagged in it are the same categories SBDC reports up to funders and government partners. A vague summary or a missed milestone isn't a formatting slip; it's data that never gets counted. Read the transcript closely and write like the email is the file.

## Draft the email

Write it as the Maryland SBDC consultant, in first person, to the client. Summarize the meeting in detail and sort what was discussed into the right section below — don't just dump chronological notes. Vary the paragraph phrasing to fit the tone of the actual transcript rather than reusing the same boilerplate every time; a terse, transactional meeting and a long exploratory one shouldn't read identically.

Keep the tone professional throughout, and skip emojis — this is a document that becomes part of the client's official record.

## Output template

```
Subject: SBDC Next Steps - [Client ID Code] - [Client Company Name]

Hi [Client Name],

It was nice speaking with you today. Below are my notes, along with some
helpful documents and links. If you have any questions, please let me
know. When you are ready to schedule your next appointment, use the link
in my signature block below.

Next Steps-
[Concrete next actions for the client's business]

Notes-
[Detailed checklist(s) of any processes, methods, tactics, advice, or
strategies discussed]

Things We Have Accomplished Since Our Last Meeting-
[Milestones — see list below]

Relevant Links from Our Meeting-
[Link title]
[URL]

[Consultant Signature Block]
```

For the subject line, pull the client ID code and company name from the transcript when they're available. If the ID code isn't in the transcript, use the placeholder "Client ID" rather than guessing one.

**Next Steps** — the client's concrete next actions for their business.

**Notes** — focus on what the client should do next, expressed as detailed checklists of any processes, methods, tactics, advice, or strategies that came up in the meeting. This is the section that carries the actual consulting content; don't compress it into a one-line summary.

**Things We Have Accomplished Since Our Last Meeting** — milestones only (see below). The source instructions named this section two slightly different ways — "Accomplishments Since Our Last Meeting" in one place, "Things we have accomplished since our last meeting" in the worked example — and listed the four sections in a different order than the example used. This skill follows the worked example's wording and order (Next Steps, Notes, Things We Have Accomplished Since Our Last Meeting, Relevant Links) since that's the literal text meant for posting; flag this for Brandon if he prefers the other phrasing.

**Relevant Links from Our Meeting** — any resources, documents, or URLs that came up, each with a title and the link.

## Check Maryland good standing (counselor click-through)

Automated good-standing lookups against SDAT / Maryland Business Express are blocked by Cloudflare, so don't try to fetch the status. Instead, surface the SDAT Business Entity Search link so the consultant can click it and read the **Status** field themselves:

- Maryland Business Entity Search — https://egov.maryland.gov/BusinessExpress/EntitySearch

When the consultant confirms the business is **not in good standing** (Forfeited, Not in Good Standing, or Dissolved), add a Next Steps line telling the client to resolve it — usually by filing the overdue Annual Report / Personal Property Return and paying any late penalties through Maryland Business Express (businessexpress.maryland.gov). If the business is in good standing, add nothing.

## Milestones

Anything in the transcript that matches one of these gets pulled into the accomplishments section, worded plainly rather than left in transcript jargon. This list is not illustrative — it mirrors Neoserra's actual milestone categories, so match it exactly rather than paraphrasing a category into something close:

- 8(A) Certification Obtained
- Accepted Agreement Text
- Bought Business
- Business Established
- Business Expansion
- Business Start Impact
- Change in Export-related Staff
- Change in Exports
- Change in Full-Time Staff
- Change in Part-Time Staff
- Change in Profits
- Change in Sales
- Changed Legal Form
- Client Legislative Letter(s)
- DBE Certified
- EDWOSB Certification Obtained
- Entered New Foreign Markets
- Local Disadvantaged Business Certification
- MBE Certified
- MDOT Certification
- Potential to Start a Business Within the Next 6 Months
- Reopened Business
- Responded to SBA Impact Survey (CY 2015)
- Responded to Survey
- SDB Self-certified
- Sold the Business
- Strategic Growth Plan Success
- Success Story
- Temporarily Altered Business
- Temporarily Closed Business
- Trademark Obtained
- WBE Certified
- WOSB Certification Obtained
- AI Tools Implemented — the client has implemented at least one AI tool after receiving SBDC guidance
- AI Improvement Realized — the client reported a concrete improvement (revenue growth, cost savings, time savings, improved customer satisfaction, etc.) after implementing AI

This list is not exhaustive of everything a client might accomplish, but it is the exhaustive list of what Neoserra tracks — if something the client did doesn't map to one of these, it belongs in Notes, not in the milestones section.

## Mining milestones from an uploaded Neoserra client file

Sometimes there is no transcript — the consultant uploads a Neoserra client record (an "All Activity by Client" report or a Survey Response report, usually PDF, sometimes Word) and wants every milestone and capital infusion pulled out of it. Handle that as a document-extraction mode of this same milestone work, matching against the milestone list above (the SBA and Neoserra definitions behind those categories are in `references/milestone-mapping-reference.md`).

Produce a copiable table with one row per milestone and these columns: Milestone, Date achieved or reported, Dollar value, Increase amount (for changes in sales, profits, staff, or exports), New hires (count, for staffing changes), and Source citation. The citation can be a direct quote, a section reference, or a general file reference tied to the client-file record date. Rules:

- One row per milestone. If a single event carries more than one milestone, list them as separate rows.
- Leave an unknown date as `[unknown]`, with a rough year where the file implies one.
- Put partial, inferred, or ambiguous ("Potential") milestones in a **separate table for Consultant Verification** — never mix them with confirmed ones.
- Keep a running table of positive client testimonials found in the file — useful later for a success story.
- Parse a long PDF **ten pages at a time**: extract the table for pages 1–10, give it to the consultant for review, then ask whether to continue through the next ten pages. Repeat until the file is done.

## After the email: offer a follow-up menu

Once the draft email is delivered, present a short lettered table of follow-up options for the consultant — the additional deliverables that would actually help *this* client, drawn from what came up in the transcript. Keep it tight: aim for six to eight letters total, not an exhaustive catalog. Assign each option a letter so the consultant can continue the conversation by just naming a letter.

Build the menu from three kinds of options.

**1a. Always-present options — put these three in every menu, no matter what the meeting covered:**

- **Capital-readiness scorecard** — score the business on what a typical SBA 7(a) lender scrutinizes (proof of demand, pricing, market category, letters of intent, management, DSCR) and turn it into a plain-language "here's what to fix before you approach a lender" list. It works for investor pitches too. Offer it even when little financial came up — frame it as a proactive readiness check. For a deeper, file-backed version, hand off to the **Underwriter and Capital Coach** skill.
- **Recommended training plan** — a top-ten list of SBDC webinars matched to what this client needs, each with the date and a one-line reason, sequenced in the order they should take them. If the consultant supplies the current Neoserra Training Events export, use it — and remind them to export the **next six months, not the fiscal year**, or it will recommend events that already passed. Offer a client-facing version reformatted as an email they can send directly.
- **Maryland good-standing check** — always give the SDAT Business Entity Search link (https://egov.maryland.gov/BusinessExpress/EntitySearch) so the consultant can verify the entity's status (see the good-standing section above). If they confirm it's Not in Good Standing, Forfeited, or Dissolved, that becomes a Next Steps line.

**1b. Conditional standing options — include only when the transcript supports them:**

- **Funding and grant search** — when the client needs capital or grant funding. When the **Maryland Community Business Compass** connector is available, run the search live through it — its funding-search and program-recommendation tools cover ~700 Maryland programs and can match by county, industry, and business profile — rather than listing programs from memory. For grant-readiness plus matched opportunities, hand off to the **Funding Match / grant finder** skill.
- **Hand off to another SBDC Toolkit skill** — when the meeting points squarely at one, name it: Success Story (a fundable win worth writing up), Business Model Canvas Helper (early-stage client with no canvas yet), Proposal Buddy (government contracting, bid/no-bid), Marketing Plan Generator, or TAM-SAM-SOM. Only surface the one or two that genuinely fit.

**2. Chaotic-good options — always generate two or three deliverables invented from this specific transcript**, not pulled from the standing list: the sharp, non-obvious things this particular meeting calls for (a 30-day sprint with a Gantt chart, a competitor teardown, a one-page pitch aimed at a specific lender, a hiring plan — whatever the conversation actually implies). This is where the skill earns its keep, so keep these fresh and client-specific rather than defaulting back to the standing options.

**3. Two required options, always present:**

- One that maps the meeting to Nexus/Neoserra. When the consultant picks it, produce BOTH (a) the exact milestone + counseling dropdown selections to enter, AND (b) the full third-person Nexus/Neoserra counseling session narrative described below — never the dropdown table alone. Producing only the dropdowns is a drift error.
- One explicitly framed as "high value, minimum effort."

## Neoserra / Nexus counseling narrative

The Neoserra-mapping option must always include a substantive, third-person, audit-grade session narrative that would survive an SBA Nexus / Form 641 review — not just the dropdown table. Include a header and then prose:

- Header: client name + Neoserra client ID (HOxxxx) + center + counselor; session date; session type (Initial vs Follow-up — attach a returning/referred client to their existing HOxxxx); counseling method (In-Person / Telephone / Email / Online-Virtual); **Contact hours and Prepare hours recorded SEPARATELY** — leave Prepare for the consultant, never invent a figure; client stage; special designations (veteran/SDVOSB and demographic) when known; primary + secondary topic areas mapped to SBA/Neoserra categories.
- Narrative: an objective third-person account of the topics discussed, advice given, referrals made, and next steps. Exclude anything said after the client left and any subjective judgment about the client. Record referrals and any milestones or economic impact (jobs, capital, sales, business formed) as confirm-before-recording — never assert an unverified milestone.
