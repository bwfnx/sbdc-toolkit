# SBDC Toolkit

14 skills for SBDC advising work — turning client meetings into follow-up emails and file notes, coaching on capital and debt, drafting grants and government proposals, building business-model and market-sizing analyses, and producing marketing plans, success stories, referrals, and training newsletters. Written for Maryland SBDC practice, in Brandon Mason's consulting voice, mapped to Neoserra milestones and fields.

**A skill here is a plain Markdown file, not an app.** Each one is instructions an assistant reads and follows, so the same file works in Claude Code, the Claude desktop app, or ChatGPT — and in anything else that accepts custom instructions. Pick whichever you already pay for; the outputs are the same.

**[How to actually use each skill →](https://bwfnx.github.io/sbdc-toolkit/)** — one guide per skill: what to have ready, what to say, what comes back, and what it will never do.

Other SBDCs are welcome to use and adapt these (MIT). They encode Maryland practice, so check anything touching your own CRM, programs, or reporting rules before you rely on it.

## Use it where you already work

### ChatGPT
No install. Open any skill file in [`skills/`](skills/) — for example [`skills/tam-sam-som/SKILL.md`](skills/tam-sam-som/SKILL.md) — copy the whole file, and paste it into a **Project**'s instructions (or a custom GPT). Start a chat and say what you want. One skill per Project keeps them from bleeding together.

### Claude desktop app
Download `sbdc-toolkit.plugin` from the [latest release](https://github.com/bwfnx/sbdc-toolkit/releases/latest), drag it into a chat, click **Accept**. No GitHub account needed.

### Claude Code

```
/plugin marketplace add https://github.com/bwfnx/sbdc-toolkit.git
```
```
/plugin install sbdc-toolkit@maryland-sbdc
```

The repo is public, so no authentication is required.

### Anything else
Copy the skill text into whatever system prompt, project instruction, or agent config your assistant uses. There is nothing vendor-specific inside the files.

## Update

Claude Code: `/plugin marketplace update maryland-sbdc`. Desktop app: download the newer `.plugin` from the [latest release](https://github.com/bwfnx/sbdc-toolkit/releases/latest) and Accept again. ChatGPT: re-paste the changed skill file.

## The 14 skills

| Skill | What it does |
|---|---|
| `transcript-to-action-plan-client-email` | Turns a meeting transcript into the client-facing follow-up email you post into Neoserra (Next Steps, Notes, Accomplishments, Links); flags milestones. |
| `transcript-to-meeting-notes` | Turns a transcript into your internal file record (Action Items, Milestones, Discussion Points, Resources). |
| `transcript-to-sop` | Turns a walkthrough or transcript into a reusable standard operating procedure. |
| `client-follow-up-and-reengagement` | Writes a warm re-engagement email to a client who has gone quiet, from their record alone. |
| `sbdc-underwriter-and-capital-coach` | Reviews a business plan or financials for lending feasibility like an SBA underwriter; risk-and-mitigation analysis and capital-readiness coaching. |
| `mdsbdc-debt-helper` | Guides a debt-workout / creditor-negotiation conversation. |
| `sbdc-grant-advisor` | Helps identify and pursue grant opportunities. |
| `business-model-canvas-helper` | Builds or interprets a Business Model Canvas block by block. |
| `tam-sam-som` | Sizes a market — total addressable, serviceable, and obtainable. |
| `sbdc-marketing-plan-generator` | Produces a structured marketing plan for a client. |
| `proposal-buddy` | Government proposal assistant on the Shipley Model — RFP analysis, bid/no-bid, capture, compliance matrix, writing, review. |
| `sbdc-success-story` | Crafts success stories, press releases, legislative letters, and social posts from client wins. |
| `business-service-provider-referral-engine` | Matches clients to the right service providers and partners. |
| `sbdc-training-newsletter` | Drafts training and workshop newsletters. |

## Notes

The guides in [`docs/`](docs/) are generated; they are published at <https://bwfnx.github.io/sbdc-toolkit/>.

This public toolkit intentionally excludes the internal `sbdc-second-brain` knowledge skill, which bundles private SBDC wiki material and is distributed separately.

## License

MIT — see [LICENSE](LICENSE).
