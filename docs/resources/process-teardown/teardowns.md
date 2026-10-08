# VOSBTC26 — Hook and Teardowns

*Anonymized. Source mapping in source-notes.md.*

## Hook

Show of hands: who's paying for an AI tool right now? Keep it up if you're paying for two.

I sat with an owner last spring who had her hand all the way up. Solo consultant, real
credentials, a business she was good at. Two paid subscriptions. She had built a capability
statement, market research on her top three buyers, a pricing workbook, a proposal template.
Genuinely good work — better than what most people bring me.

I asked her where all of it lived. She said, "I ain't working with nothing."

It existed. It was scattered across dozens of chats and an external drive. She couldn't find
it, couldn't build on it, couldn't hand it to anybody. Her words: "Nothing was ever set up
from the beginning correctly. Now I'm going back trying to put fillers in all the stuff I
didn't do." She was still working Sundays.

So here's the mystery. She had the tools. She had the skill. She was working Sundays anyway.
What was actually broken?

Not the tools. She never wrote down what she did. She'd sit down, describe the problem fresh
every time, get a good answer, and lose it. Every session started at zero.

Roughly 90% of the owners who come to me for AI don't know what they need yet, and what they
usually need isn't AI — it's a process.

AI doesn't fix a process you can't describe.

## Teardown 1 — Floor: compliance matrix from an RFP

### The process

Turning a solicitation's proposal instructions and evaluation criteria into a compliance
matrix, before anybody writes a word of the proposal.

### The steps

1. Pull Section L and list every instruction on volumes, order, page counts, and format.
2. Pull Section M and list every evaluation factor and sub-factor.
3. Pull Section C or the SOW and list every "shall" statement as a separate requirement.
4. Line up each requirement against the Section L instruction that says where it goes and the
   Section M factor that says how it gets scored.
5. Build the outline: volume, section number, section title.
6. Mark each row Compliant / Intend to Comply / Partial Compliant / NON-COMPLIANT, with a risk
   level and a one-line justification.
7. Assign an owner and an action to every row that isn't already compliant.
8. Re-read the solicitation against the matrix and fix what you missed the first pass.

### J or R

| Step | J/R | Why |
|---|---|---|
| 1. List Section L instructions | R | Transcription. Same job on every solicitation. |
| 2. List Section M factors | R | Transcription. |
| 3. Pull every "shall" as a requirement | R | Pattern-matching against a rulebook, not a call. |
| 4. Map requirement → L instruction → M factor | R | Mechanical once all three lists exist. |
| 5. Build the outline | R | Section L already dictated it. |
| 6. Compliance status, risk, justification | **J** | This is you betting your bid. Nobody else. |
| 7. Assign owner and action | **J** | You know who can actually write it by Thursday. |
| 8. Second pass against the matrix | **J** | Judgment is the whole point of a review. |

### The first R step

Step 3 — pulling every "shall" out of the SOW. Not because it's the biggest. Because it's the
one you're most likely to do badly at 11 p.m. and the one where missing a single line gets you
thrown out on compliance before anyone reads your technical approach. It's also self-checking:
you can spot-count the "shall" statements yourself and see whether the list is complete.

### What I'd paste

> Here is [Sections L, M, and C of a solicitation, pasted]. Turn it into [a proposal compliance
> matrix] in this format: [Outline # | Proposal Section Title | Section in Proposal | RFP Section
> L | Section # | RFP Section M | Section # | RFP Section C/SOW | Compliance Status | Risk Level
> | Justification | Action | Owner]. One row per requirement. Leave Compliance Status, Risk
> Level, Justification, Action, and Owner blank — I fill those in. Flag anything that looks off
> [conflicting page limits, a Section M factor with no matching Section L instruction, a "shall"
> you couldn't place anywhere].

That output drops straight into the compliance matrix template we hand out in the GovCon
series. Same columns, same order.

### What went sideways

The first version I ran filled in the Compliance Status column for me. Every row said
"Compliant." It had no idea whether we could actually do any of it — it was pattern-matching on
what a finished matrix looks like. That's why the prompt now says leave those columns blank.
Second thing: it silently merged compound requirements. One "shall" with three clauses came back
as one row, so three obligations shared one owner and one status. Now I ask it to split
compound requirements into separate rows and I still eyeball the count.

## Teardown 2 — Middle: client follow-up

### The process

Following up on an invoice that's past due, without setting the relationship on fire.

### The steps

1. Pull the open invoices and the aging from the accounting file.
2. Pull the last email thread with that customer so you know what was already said and when.
3. Check what else is in play with them — open work, a pending change order, a renewal.
4. Draft the nudge.
5. Decide the tone, and decide whether this one escalates.
6. Send it.
7. Log the date and set the next touch.

### J or R

| Step | J/R | Why |
|---|---|---|
| 1. Pull open invoices and aging | R | The report is the report. |
| 2. Pull the last thread | R | Retrieval. |
| 3. Check what else is in play | R | Look-up. You're gathering facts, not weighing them. |
| 4. Draft the nudge | R | Fourth time this month you've written this email. |
| 5. Decide tone and whether to escalate | **J** | The single most expensive decision in the process. |
| 6. Send | R | Once you've decided, sending is sending. |
| 7. Log it and set the next touch | R | Bookkeeping. |

### The first R step

Step 4 — draft the nudge. It's the step you avoid, which is why the invoice is 45 days old
instead of 20. Handing the draft to AI removes the reason you procrastinate: staring at a blank
reply box trying to sound firm and friendly at the same time. You keep step 5 completely. The
draft shows up, you read it, you decide whether this is a soft reminder to a good customer or
the last email before you stop work.

### What I'd paste

> Here is [the invoice details: number, amount, date sent, days past due, and the last email
> thread with this customer]. Turn it into [a short follow-up email, four sentences maximum, in
> the tone I mark below] in this format: [one line of context, one line stating amount and
> original due date, one specific ask with a date, one line offering to talk]. Give me three
> versions: friendly reminder, firm, and final notice before we pause work. Flag anything that
> looks off [I already said something contradictory in the thread, the amount doesn't match what
> was quoted, there's an open dispute I'd be stepping on].

Three versions is the trick. You're not asking AI to pick the tone. You're asking it to lay out
the options so your judgment call takes ten seconds instead of ten avoided days.

### What went sideways

Two ways I've watched this go bad, both on the judgment step.

An owner in a cash crunch signed with an offshore working-capital lender. She was three days
late on one payment. The lender's collection process — fully automated, no human deciding
anything — called every customer it could find and told them to pay their bills. She kept none
of those customers, and because the lender was offshore there was nothing anyone could do about
it. That is what "automate the escalation decision" looks like at full scale.

The quieter version: an owner told me she'd been in the same tool so long that its voice had
become her voice. She'd tried a second tool and quit inside the trial because it didn't sound
right to her. Her customer emails were fluent and warm and completely generic, and my read was that her
repeat customers could tell. Automating the draft is fine. Automating the decision about *how you
sound to a customer who owes you money* is not.

## Teardown 3 — Ceiling: weekly action report

### The process

Every Friday at 4 p.m., a scheduled job reads my week out of three systems and writes an entry
to my action log so I stop losing track of my own open loops.

### The steps

1. Set the date range: Monday through today.
2. Pull the past seven days of email — sent and received — and note commitments, follow-ups, and
   decisions.
3. Pull the calendar for the week: who I met, what type of meeting, anything recurring.
4. Read my own AI session transcripts for the week: what got built, what changed, what got
   decided.
5. Write the entry in a fixed six-part shape: Synthesis, client meetings by day, email activity,
   sessions, personal, open loops.
6. Append it to the action log. Never overwrite — read the file, add to the bottom, write it back.
7. I read it Friday evening and correct it.

### J or R

| Step | J/R | Why |
|---|---|---|
| 1. Set the date range | R | It's Monday through Friday. Every time. |
| 2. Pull the week's email | R | Retrieval, with a filter I already wrote down. |
| 3. Pull the calendar | R | Retrieval. |
| 4. Read the session transcripts | R | Retrieval. |
| 5. Write the six sections | R | Same shape every week, which is the only reason it works. |
| 6. Append to the log | R | And the rule is in writing: append, never overwrite. |
| 7. Read it and correct it | **J** | The whole thing is worthless without this step. |

### The first R step

Step 3, the calendar pull. Smallest possible piece, one clean source, and I could check it in
30 seconds. That's where this started — not with the scheduled job. The scheduled job came
later, once the manual version was boring.

### What I'd paste

> Here is [my calendar for this week and the past seven days of email]. Turn it into [a weekly
> action log entry] in this format: [Synthesis — one paragraph, three to five sentences; Client
> Meetings — one line per meeting grouped by day as Day: Name / Company — meeting type
> (brief context); Email Activity — one line each, skip routine; Sessions — one line each;
> Personal — one line each, skip if empty; Open Loops — one line each, things carrying into next
> week]. Plain language, no corporate filler, one line per bullet, not mini-paragraphs. Flag
> anything that looks off [a source that came back empty, a meeting you couldn't identify, a
> commitment with no owner].

### What went sideways

This took about six weeks to get right, and it is still not hands-off.

The instructions lived in two places — the copy the scheduler reads and the copy in version
control — and nothing kept them in sync or compared them. They drifted. A related audit job ran
more than a month behind while pointing at the wrong source folder, and nobody noticed, because a wrong
answer looks exactly like a right answer in a file you skim on a Friday night. Separately, three
articles got published and rendered nowhere at all, with no alarm.

The failure mode nobody warns you about: when the tool that reads the instruction file drops its
connection, the job stops instead of guessing. That's the correct behavior, and it also means
some Fridays nothing happens and nothing tells you. Silence is not success.

What I still check by hand every week: every name and company in the meeting list, because
attribution errors are the ones that embarrass you, and the Open Loops section, because it
regularly lists things I finished on Wednesday. It never catches the thing I decided in a hallway
and didn't put anywhere.

Roughly 80% automated is where this lives. I'm not chasing the last 20%. I've never had an
employee who was right 100% of the time either.
