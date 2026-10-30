# Design: SBA business status check for transcript-to-action-plan

**Date:** 2026-10-30
**Skill:** `skills/transcript-to-action-plan-client-email`
**Status:** Approved design, not yet implemented

## Why

The MD SBDC program analyst reviewed recent business starts and reversed several of them. The causes:

1. Session notes did not state the client's business status at the first session in SBA terms, so the business start could not be validated.
2. A client was recorded as pre-venture while the notes showed it already operating (vehicle on the road, a third-party contract, a completed first week of operations).
3. An investment secured before the first SBDC session was reported as impact.
4. Admin time spent reviewing survey responses was logged as client follow-up sessions.

She asked that, when the AI agent does not capture it, the counselor add an explicit status note using the SBA definition: **registration AND (sales OR hires OR investment OR operating expenses)**. Example wording: "Client registered the business but does not have sales or hires and has made no investment or business expenses."

The skill should capture this so the counselor does not have to remember to add it by hand.

## Scope

In scope: SKILL.md, `references/milestone-mapping-reference.md`, `references/gpt-assistant-instructions.md` (kept in sync with SKILL.md).

Out of scope: other skills, the docs site page for this skill (update in a follow-up once the change ships).

## 1. Business status check (every email)

For every transcript, the skill records what the transcript shows for each SBA criterion:

| Criterion | What to record |
|---|---|
| Registration | Registered or not; entity type and date if stated |
| Sales | Any revenue yet |
| Hires | Any employees |
| Investment | Any capital in, with its date relative to the first SBDC session |
| Operating expenses | Any business spending |

Output goes in two places:

- **Client email.** One neutral line at the end of **Notes-**: `Business status as of this meeting: <one-sentence status in the SBA wording>.` Because the email is BCC'd to the Neoserra postbox, this line lands in the session record automatically.
- **Consultant verification note** (after the email, alongside potential milestones): the full criterion-by-criterion breakdown, each with the transcript evidence or `not mentioned`.

If the transcript is silent on a criterion, the skill does not guess. It marks it `not mentioned` in the verification note and adds "confirm with client" there. The client-email line states only what the transcript supports.

## 2. Initial status (first sessions)

On a first session, the skill labels the client:

- **Pre-venture** only when the transcript shows no sales, no hires, no investment and no operating expenses.
- **In business** otherwise.

If the counselor or transcript calls the client pre-venture but the transcript shows operating evidence, the verification note flags it:
"Transcript shows the client operating (<evidence>). Initial status should likely be Start-up / In business, not Pre-venture."

## 3. Business Start rule

Replaces the current rule in `milestone-mapping-reference.md` ("Business Start Impact when SBA's role is clearly mentioned").

The skill flags **Business Start Impact** as a *potential* milestone only when all three hold:

1. The client was Pre-venture at the first SBDC session.
2. The client is now registered.
3. At least one of sales, hires, investment or operating expenses is present now that was absent at intake.

It goes in the consultant verification note only, never the client email, and names which criterion changed. Otherwise a newly registered entity is at most **Business Established**.

## 4. Capital infusion timing

For any investment the transcript mentions (TEDCO, angel, loan, grant):

- Secured **before** the first SBDC session → not reportable. Mention as background in Notes; never flag as a milestone.
- Date **unclear** → verification note asks the counselor to confirm timing before logging.
- Secured **after** the first session → handled as today.

## 5. Intake status on follow-up sessions

On a follow-up, the skill needs the first session's status to know which criteria are new. It checks sources in this order and stops at the first that answers:

1. **Uploaded Neoserra client file**, if attached. Authoritative: it reflects any status corrections made in Neoserra.
2. **Email search**, if a mail connector is available. Search sent mail for prior session emails by the client ID exactly as it appears in the current transcript or subject line, in whatever format (HO4158, MO1234, another state's format). Never assume a center prefix or validate the ID's pattern. If there is no ID, search by company and client name and flag the match as "matched by name, confirm it is the same client". Use the earliest matching email; pull its status line, or for older emails without one, the operating evidence in its Notes.
3. **Ask the counselor** one question: "What was the client's status at the first session?"

The verification note names the source used (e.g. "Intake status from 03/12/26 email: operating, one vehicle, one contract"). If two sources disagree, show both and do not pick.

If email search finds nothing (new ID, or a session logged by another counselor), fall through to asking. Email search is optional; the skill must work for SBDCs with no mail connector.

## 6. Center-neutral client IDs

Replace the Howard-only `HOxxxx` in the Nexus narrative header (SKILL.md and gpt-assistant-instructions.md) with: `Neoserra client ID (center code + number, e.g. HO4158, MO1234)`, and "attach returning clients to their existing client ID".

## 7. Guardrails to add

- Never flag a Business Start for a client who was in business at the first session.
- Never count a capital infusion secured before the first SBDC session.
- Never guess a missing business-status criterion; mark it `not mentioned`.
- Survey-response review is non-reportable admin time, not a client follow-up session (applies to client-file mode and "Responded to Survey").

## Test cases

Run the edited skill against these and check the output:

1. **Operating client tagged pre-venture.** First session, client describes one vehicle, one driver, a third-party contract, first full week of operations. Expect: status line shows operating; verification note flags "should likely be In business"; no Business Start.
2. **Pre-funded startup.** First session, client is incorporated and already has an investment from before the session. Expect: investment in Notes as background; no Capital Infusion or Business Start flag.
3. **True pre-venture to start.** Follow-up; intake status pre-venture (supplied by counselor); client now registered with first sales. Expect: potential Business Start Impact in verification note naming "sales" as the new criterion; nothing in client email's milestone section.
4. **Silent transcript.** First session that never mentions sales or hires. Expect: those criteria marked `not mentioned` with "confirm with client"; status line does not claim "no sales".
5. **Non-Howard ID.** Follow-up for client MO1234 with email connector available. Expect: search uses MO1234; narrative header has no "HO".
