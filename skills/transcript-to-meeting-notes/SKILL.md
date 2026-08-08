---
name: transcript-to-meeting-notes
description: Use this to write up a meeting after it happens — turn what was said in a client call, advising session, or consultation into the advisor's own internal file record. Trigger on any ask to log, document, record, recap, or write up a call — "notes for the file," "internal write-up," "log this consultation," "categorized meeting notes" — and on any request naming the pieces wanted from a meeting — action items, what the client accomplished, discussion topics grouped under subheaders, resources or links mentioned. Trigger whether the transcript is pasted, attached, or merely described. Produces one fixed four-section note — Action Items, Milestones Achieved, Key Discussion Points, Resources. Not for anything someone else reads — a follow-up or recap email to the client, a success story, marketing copy, or outreach — and not for answering business questions. Internal record, never correspondence.
---

# Transcript to Meeting Notes

A transcript is a wall of talk; a file note is what an advisor can scan in ten seconds before the next call. The job is to turn a raw meeting transcript into a structured, categorized internal record, sorted into the same four buckets every time so a client's notes stay comparable meeting to meeting. This is not a client-facing document — no one but the advisor sees it — so favor scanability over politeness. If the ask is instead for something to send the client, see "Not this skill" below.

## Extract four things, every time

Every transcript gets read for:

1. **Action items** — with checklists and deadlines
2. **Milestones achieved** — matched against the Neoserra taxonomy in `references/neoserra-milestones.md`
3. **Key discussion topics and advice**
4. **Resources and links mentioned**

## Output template

Use this structure exactly, including the emoji in the section headers — they're scan markers, not decoration, and the source GPT treats them as part of the format rather than dropping them the way other conversions here do (see "After delivering the notes" for when to remove them).

```
# Meeting Notes - [Client ID] - [Client Company Name]

## 🎯 Action Items
- **Category/Process** (e.g., Certifications, Pipeline Management):
  - [ ] Task 1 (Deadline: [date])
    - Subtask 1
    - Subtask 2
  - [ ] Task 2

## 🏆 Milestones Achieved
- **MBE Certification** approved on [date]
- Business Expansion: [Details, e.g., "Opened second location in Baltimore"]
- Change in Sales: Increased by 15% QoQ

## 📝 Key Discussion Points
### Government Contracting
- Reviewed eligibility for 8(a) Certification.
- Next step: Submit DBE application by [date].

### Intern Program
- MTIP enrollment requires HR alignment by [date].

## 🔗 Resources
- [USAspending Advanced Search](https://www.usaspending.gov/search)
- [MDOT Certification Portal](https://www.mdot.maryland.gov/tso/pages/index.aspx?pageid=90)
```

**Action Items.** Convert every "Next Steps" the transcript surfaces into a checklist item. Group items under a bolded Category/Process label (Certifications, Pipeline Management, or whatever the meeting actually covered), and nest sub-tasks under the task they belong to.

**Milestones Achieved.** List accomplishments pulled from the taxonomy in `references/neoserra-milestones.md`, and bold certifications and other quantifiable wins so they stand out from ordinary discussion notes — plain business changes (like the sales-increase example above) don't need bolding, only the named certifications and hard numbers do.

**Key Discussion Points.** Group under topic subheaders (`### Government Contracting`, `### Intern Program`, etc.) rather than one flat list, using whatever categories the transcript actually raised.

**Resources.** Turn every document, tool, or website named in the transcript into a markdown link.

## How to find each category in the transcript

**Milestones.** Scan for language like "certified," "expanded," or "hired" — anything signaling a completed accomplishment rather than a plan still in progress. Example: transcript says "We finalized the MBE Certification" → note reads "- **MBE Certification** finalized on [date]."

Read `references/neoserra-milestones.md` and use its exact wording for anything that matches. Neoserra reporting keys off the category names, so "got certified as a minority business" does not register where "MBE Certified" does. That file also covers the pairs that get confused — certification obtained versus self-certified, full-time versus part-time staff changes, sales versus profits — and says to flag ambiguity rather than pick a side, since a miscategorised milestone is harder to catch later than a flagged one.

**Action items.** Convert phrases like "need to," "next step," or "will do" into checklist items. If a deadline is mentioned, even a relative one, resolve it to an actual date rather than repeating the relative phrase: "Submit by Friday" becomes "(Deadline: 2023-10-20)," not "(Deadline: Friday)."

**Key discussions.** Group by category (Certifications, Marketing, whatever the meeting covered) and pull out the actual advice given, not just the topic name — "recommended using GovWin for pipeline tracking" is worth keeping; "discussed pipeline tracking" is not.

## Worked example

Input transcript snippet:

> "We got the MBE approval last week. Next, we need to apply for the 8(a) Certification by November. Also, remember to review the intern onboarding checklist with HR by Friday."

Output:

```
## 🎯 Action Items
- **Certifications**
  - [ ] Apply for 8(a) Certification (Deadline: 2023-11-30)
- **Intern Program**
  - [ ] Review onboarding checklist with HR (Deadline: 2023-10-20)

## 🏆 Milestones Achieved
- **MBE Certification** approved on 2023-10-10
```

## After delivering the notes

Ask whether emojis should be used to increase readability. If the answer is no, redo the section headers as plain text (`## Action Items`, `## Milestones Achieved`, `## Key Discussion Points`, `## Resources`) and keep everything else the same.

## Not this skill

If the request is a client-facing follow-up email — something to post into Neoserra with Next Steps, Accomplishments Since Our Last Meeting, Notes, and Relevant Links sections, addressed to the client — that's `transcript-to-action-plan-client-email`, not this skill. This skill's output is the advisor's internal file note: it stays in third person, is never addressed "Hi [Client]," and is not meant to be sent anywhere.
