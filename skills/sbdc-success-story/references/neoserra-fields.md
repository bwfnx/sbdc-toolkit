# Neoserra Field Reference

This reference helps the skill extract the right information from Neoserra "All Activity by Client" reports and other common SBDC document formats.

## About Neoserra Reports

Neoserra is the CRM used by SBDCs nationwide to track client interactions. The "All Activity by Client" report is the most common export consultants will upload. It contains session logs, notes, milestones, and activity records for a single client.

## Where to Find Key Fields

### Client Identity
- **Business name**: Usually appears in the report header or first section
- **Client contact name**: Header section, often paired with business name
- **Neoserra client code**: Alphanumeric code, typically in the header or filename (e.g., "MD-12345")
- **Business address**: Client profile section — critical for legislative letter lookups

### Session Records
Each counseling session typically includes:
- **Date** of the session
- **Consultant name** who conducted it
- **Session type** (in-person, phone, email, virtual)
- **Duration** in hours
- **Session notes** — free-text field where the richest narrative detail lives

Look for session notes that describe:
- What the client asked for or was struggling with
- What advice or resources the consultant provided
- Referrals made to other organizations
- Tools or programs recommended (LivePlan, market research databases, etc.)
- Follow-up actions agreed upon

### Milestones and Outcomes
Neoserra tracks predefined milestones. Common ones relevant to success stories:
- Business started
- Jobs created / retained
- Loans or capital obtained (report general category, never dollar amounts)
- Contracts awarded (government or private)
- Certifications obtained (MBE, WBE, 8(a), HUBZone, etc.)
- Revenue increase (describe in general terms only)
- Business plan completed
- New market entered

### Client Quotes
Direct client quotes may appear in:
- Session notes (consultant recorded what the client said)
- Email correspondence attached to the record
- Survey responses linked to the client profile
- Testimonial fields if the center uses them

When extracting quotes, always note the source: session date, document title, or email date.

### Programs and Tools
Look for references to:
- LivePlan (business planning software)
- Market research tools (IBISWorld, ReferenceUSA, etc.)
- Training programs or workshops attended
- Referrals to SCORE, TEDCO, DORS, WBC, or other partners
- Funding programs (SBA loans, TEDCO grants, county programs)

## Other Document Types

Consultants may also upload:
- **Email threads** — scan for client quotes, outcome descriptions, and timeline details
- **Client intake forms** — business name, industry, reason for seeking help
- **Consultant notes** (Word docs, plain text) — treat like session notes
- **Previously drafted stories** — extract and improve rather than starting over

## Extraction Priority

When a document is messy or inconsistent:
1. Extract the primary fields first (business name, issue, actions, outcomes)
2. Flag anything ambiguous rather than guessing
3. Present what you found as a bulleted summary for confirmation
4. Ask targeted follow-up questions only for gaps that block the draft
