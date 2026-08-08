# SBDC Toolkit

A Claude Code plugin of 14 skills for Maryland SBDC advising work — turning client meetings into follow-up emails and file notes, coaching on capital and debt, drafting grants and government proposals, building business-model and market-sizing analyses, and producing marketing plans, success stories, referrals, and training newsletters. The skills speak in Brandon Mason's consulting voice and map to Neoserra milestones and fields.

## Install

In Claude Code, add the marketplace and install the plugin:

```
/plugin marketplace add https://github.com/bwfnx/sbdc-toolkit.git
```
```
/plugin install sbdc-toolkit@maryland-sbdc
```

That's it — the repo is public, so no GitHub account or authentication is required.

## Update

When a new version ships, pull the latest:

```
/plugin marketplace update maryland-sbdc
```

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

This public toolkit intentionally excludes the internal `sbdc-second-brain` knowledge skill, which bundles private SBDC wiki material and is distributed separately.

## License

MIT — see [LICENSE](LICENSE).
