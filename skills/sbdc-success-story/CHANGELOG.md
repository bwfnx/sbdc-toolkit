# Changelog

## 2026-11-19 — Client Authorization

- Adds client approval of a finished story by email, which also serves as the Publicity Release. An emailed approval with the client's typed full name and date counts as the signed release (ref BAT-452).
- New `references/client-authorization.md`: the step-by-step workflow, from internal-or-public through regional review.
- New `scripts/build_authorization_email.py`: fills the branded email template.
  - Escapes all text and builds the Approve and Request changes buttons.
  - Refuses dollar amounts and web addresses.
  - Has a built-in self-test: `--self-test`.
- New `assets/authorization-email.html`, built with the Maryland SBDC Design System values.
- New `assets/sbdc-maryland-logo.png`: the logo from the 2024 Publicity Release form.
- New `references/publicity-release.md`: the release text, word for word, as the single source.
- Round 1 of the guided walkthrough now asks "public or internal?" instead of an unenforced "do you have a signed release?"
- The Follow-Up Menu leads with Client Approval.
- Based on Luis Diaz-Colorado's authorization workflow.
