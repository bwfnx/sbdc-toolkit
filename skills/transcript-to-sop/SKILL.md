---
name: transcript-to-sop
description: Turn a meeting or process-walkthrough transcript into a clean, repeatable Standard Operating Procedure (SOP) for Maryland SBDC consultants, aggressively extracting every distinct process — tasks, systems, decisions, handoffs, exceptions — into an operational playbook across Gmail, Outlook, Neoserra, and typical business tools. Use whenever someone pastes, uploads, or describes a transcript and wants an SOP, a process document, a repeatable playbook, a how-to a new consultant could follow, or a documented workflow. Distinct from transcript-to-action-plan-client-email (a client-facing meeting recap) and transcript-to-meeting-notes (an internal file record of what was said) — this skill produces reusable operating procedures, not a record of one meeting.
---

# Transcript to SOP

A transcript of someone explaining how they do their work is raw material, not a procedure. The job is to convert it into SOPs a new consultant could follow without guessing — extracting every distinct process, and being honest about what the transcript does not say rather than inventing steps to fill the gaps.

Audience is Maryland SBDC consultants. The primary systems are Gmail, Outlook, and Neoserra; also handle other standard business systems when the transcript references them (calendars, shared drives, Zoom/Teams, CRM exports, PDFs, e-sign, forms). Write steps that are tool-agnostic when the transcript is vague and tool-specific when the transcript names a specific feature or field.

Work in four passes, in order. Do not skip ahead to writing the SOP before the inventory is done — the inventory is what keeps blended workflows from collapsing into one mushy procedure.

## 1. Process inventory (first — do not write the SOP yet)

Produce a table titled **"Process Inventory"**, one row per distinct process detected:

| Process Name | Trigger | Owner/Role | Inputs | Systems Used | Outputs | Frequency/SLA | Dependencies/Handoffs | Risks/Failure Points | Open Questions |

Rules while building it:

- Split a process into two if it has a different trigger, owner, or outcome.
- If the transcript blends multiple workflows together, untangle them into separate rows.
- Do not assume policy. Anything the transcript leaves unstated goes in **Open Questions**, not into an invented step.

## 2. Clarify ambiguities (only after the inventory)

List **only** the minimum critical clarifying questions needed to make the SOPs executable — at most 10. Where information is missing but a sensible default exists, supply it and label it **"Default assumption (editable)"** rather than blocking on a question.

## 3. Write the SOPs

For each process in the inventory, write an SOP with exactly this structure:

**SOP #[X]: [Process Name]**

- **Purpose**
- **Scope** (what's included and excluded)
- **Trigger**
- **Owner & backup**
- **Definitions** (only if needed)
- **Prerequisites / Access**
- **Inputs**
- **Systems & locations** (e.g., specific Neoserra fields, email folder labels, shared-drive paths)
- **Step-by-step procedure** — numbered, unambiguous, one action per step
  - Decision points as **If / Then / Else**
  - Handoffs stated explicitly: "Send to / Notify / Assign to"
  - Where to record the work in **Neoserra**, when applicable
- **Quality checklist ("Done means…")** — 5 to 10 check items
- **Time standards / SLA** (if mentioned; otherwise "Not specified")
- **Exceptions & edge cases**
- **Templates / copy-paste text** (email snippets, follow-up language, log-note templates)
- **Metrics to track** (optional but recommended)
- **Version notes** (what in the transcript this SOP is based on)

## 4. Consultant-friendly artifacts

After all SOPs, add:

- **Master Checklist** — one combined checklist across all SOPs, grouped by system (Gmail / Outlook / Neoserra / Calendar / Other).
- **RACI-lite** — who is Responsible, Approver, Consulted, Informed, where it can be inferred.
- **Neoserra Logging Guide** — only for what the transcript actually mentions; list the rest as open items.

## Style

Write like a practical internal playbook: clear, direct, no fluff. Use consistent action verbs — Log, Email, Schedule, Update, Attach, Tag, Assign. Avoid vendor-specific instructions unless the transcript explicitly names a feature. When the transcript contradicts itself, call it out and propose the safest interpretation.

## Strict mode (on request)

When the consultant needs extremely exact SOPs, work in strict mode: do not invent steps or fields. If a required detail is missing (e.g., which Neoserra field to update), write `[MISSING]` and add it to Open Questions.

## Optional condensed version

Offer, after the full SOP set, a one-page **"Consultant Quickstart"** — the same content condensed — when the consultant wants a fast reference alongside the full procedures.
