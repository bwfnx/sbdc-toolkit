# Session 3 class file (copied from the sbdc-workshops session1_example.py). Build:  py build.py  (run from this folder)
import pathlib, sys
sys.path.insert(0, str(pathlib.Path.home() / ".claude" / "skills" / "sbdc-workshops" / "scripts" / "deck"))
import engine
engine.setup("[YOUR-FORM-URL]")
from engine import *

# The practice solicitation used all class. Fill from SAM.gov; everything below reads from here.
PR = {
    "title": "Janitorial and Carpet Cleaning Services",
    "number": "W912DR26QA051",
    "agency": "U.S. Army Corps of Engineers, Baltimore District",
    "place": "125 recruiting offices, 29 in Maryland",
    "setaside": "Total Small Business Set-Aside",
    "naics": "561720 Janitorial Services",
    "due": "July 13, 2026 (awarded Sept.)",
    "url_label": "Link is in the Zoom chat (DoD's PIEE site, no login)",
}

# ============================ SLIDES ============================

slide("dark title", f'''
  <img class="logo r" alt="America's SBDC Maryland" src="data:image/png;base64,{LOGO}">
  <div class="title-grid">
    <div>
      <p class="eyebrow light r">Winning That Government Contracting Award &middot; Session 3 of 4</p>
      <h1 class="r">How to Read a Federal RFP</h1>
      <div class="band r"></div>
      <p class="byline r">Your Name &middot; Maryland Small Business Development Center<br>Friday, October 2, 2026</p>
    </div>
    <div class="qr-card r">{QR_FORM}<span>Scan now: your worksheet</span></div>
  </div>''',
  "Welcome back. Monday was the lifecycle, Wednesday was the team. Today we get into the actual document. A federal RFP can run 100 to 200 pages of legal language and cross-references, and it looks designed to confuse you. It isn't. It's organized in a very logical way once you know the structure, and once you know what to read first it goes from overwhelming to manageable. Today we practice on a real, open janitorial solicitation here in Maryland. Scan the code: that's today's worksheet. Fill in page 1, keep the tab open, and don't hit Submit until the last slide.", label="Title")

slide("light scan", f'''
  <div class="scan-grid">
    <div>
      <ol class="steps">
        <li class="r"><b>Point your phone camera at the code.</b> Or click the link in the Zoom chat.</li>
        <li class="r"><b>Fill in page 1 now.</b> Name, email, business, where you are today.</li>
        <li class="r"><b>Open today's practice solicitation too.</b> Its link is in the chat.</li>
      </ol>
      <p class="url ink r">{FORM_LABEL}</p>
      <p class="fine r">Don't hit Submit until the last slide. When you do, the slides, the compliance matrix template and every link land in your inbox.</p>
    </div>
    <div class="qr-card big r">{QR_FORM}</div>
  </div>''',
  "Give them 90 seconds. New worksheet, so everyone scans again. Two tabs today: the worksheet and the practice solicitation on SAM.gov, both linked in the chat. Repeat: don't hit Submit until the last slide, the email fires on submit.",
  eyebrow="Before we start", title="Scan your worksheet")

slide("light", '''
  <ol class="agenda">
    <li class="r"><span>01</span>The anatomy of an RFP: Sections A through M</li>
    <li class="r"><span>02</span>The reading order that actually works</li>
    <li class="r"><span>03</span>The five sections that drive your proposal</li>
    <li class="r"><span>04</span>Sections that still need a response</li>
    <li class="r"><span>05</span>Building the compliance matrix</li>
    <li class="r"><span>06</span>Traps that catch small businesses</li>
  </ol>''',
  "Here's the plan. The full structure first, all 13 sections. Then the order you actually read them in, because front to back is one of the worst things you can do. Then the five sections that drive your proposal, and how Sections L and M become a compliance matrix, the tool we've mentioned in both earlier sessions. You got the template Wednesday; today it ties everything together.",
  eyebrow="Today", title="What we're covering")

slide("light", f'''
  <div class="cols2 wide-left">
    <div class="card r"><p class="card-k">Today's practice solicitation</p>
      <h3 class="next-h">{PR["title"]}</h3>''' + bullets([
        f"<b>Solicitation:</b> {PR['number']}",
        f"<b>Buyer:</b> {PR['agency']}",
        f"<b>Where:</b> {PR['place']}",
        f"<b>Set-aside:</b> {PR['setaside']}",
        f"<b>Due:</b> {PR['due']}"]) + f'''</div>
    <div class="callout r"><p>Real, and awarded.</p><span>{PR["url_label"]}. We read it together all class.</span></div>
  </div>''',
  "This is a real Maryland solicitation, not a made-up example: the Army Corps of Engineers, Baltimore District, buying janitorial and carpet cleaning for 125 leased recruiting offices across Maryland, Pennsylvania, Virginia, Delaware and West Virginia. It closed July 13 and was awarded in September, and at the end of class I'll show you who won. Janitorial because nearly every agency buys it, it's a classic small-business set-aside, and you don't need to be a cleaning company to learn how to read it. The documents are on the Defense Department's PIEE site, linked in the chat, no login. Don't read it now; I'll tell you exactly where to look.",
  eyebrow="Our practice RFP", title="We read a real one today")

slide("light", '''
  <table class="compare r">
    <thead><tr><th>Group</th><th>Sections</th><th>What you do with them</th></tr></thead>
    <tbody>
      <tr><td><b>Drive your proposal</b></td><td>A &middot; B &middot; C &middot; L &middot; M</td><td>Cover page, pricing, the work, instructions, evaluation</td></tr>
      <tr><td><b>Need a response</b></td><td>H &middot; J &middot; K</td><td>Special requirements, attachments, reps &amp; certs</td></tr>
      <tr><td><b>Read, then sign</b></td><td>D &middot; E &middot; F &middot; G &middot; I</td><td>Packaging, inspection, delivery, admin, FAR clauses</td></tr>
    </tbody>
  </table>
  <p class="statement center r">13 sections. About 5 drive what you write.</p>''',
  "This is the Uniform Contract Format that most negotiated federal RFPs use: Army, Navy, HHS, DHS, Sections A through M. Some agencies rename or combine sections, but the pattern holds. Notice the grouping. Five sections drive what you write: A, B, C, L and M. Three need a response: H, J and K. The rest are contractual and administrative. You read them because they become your contract, but they're not where your win strategy lives. The first RFP is the hardest. After that you know where to look.",
  eyebrow="Part 1 &middot; Anatomy", title="Sections A through M")

slide("light", '''
  <div class="cols2 wide-left">
    <div class="roles r">
      <div><b>A &rarr; Solicitation memo</b><span>number, dates, contact, set-aside</span></div>
      <div><b>B &rarr; Price Schedule.xlsx</b><span>priced by region, every site in the region</span></div>
      <div><b>C &rarr; Performance Work Statement</b><span>20 pages, 125 addresses</span></div>
      <div><b>L &rarr; Instructions to Offerors</b><span>three volumes, how to submit</span></div>
      <div><b>M &rarr; Evaluation Criteria</b><span>how they pick the winner</span></div>
    </div>
    <div class="callout r"><p>Different labels.</p><span>Same five questions. Ours arrives as separate attachments.</span></div>
  </div>''',
  "Heads up, because this trips people up on their first real one. Services like janitorial are usually bought as commercial services under FAR Part 12. Those solicitations use the SF 1449 instead of the SF 33, and they don't carry the Section A through M labels. The instructions live in an addendum to FAR clause 52.212-1, and the evaluation criteria in an addendum to 52.212-2, sometimes titled Basis for Award. Same logic, different labels. When you can't find Section L, search the document for 52.212-1, or look for an attachment called Instructions. Ours is a combined synopsis and solicitation: the pieces arrive as separate files. Here's how they map.",
  eyebrow="Part 1 &middot; Anatomy", title="Our RFQ, mapped to A through M")

section("Part 2", "The reading order that actually works",
  "Here's the part that changes everything for people reading their first RFP.")

slide("light", '''
  <div class="tiles">
    <div class="r"><span>1</span><b>A &middot; Cover page</b>Two minutes: number, due date, who to ask</div>
    <div class="r"><span>2</span><b>L &middot; Instructions</b>The recipe: volumes, page limits, format</div>
    <div class="r"><span>3</span><b>M &middot; Evaluation</b>How they score you: where to put your effort</div>
    <div class="r"><span>4</span><b>C &middot; The work</b>Every "shall" is a requirement</div>
    <div class="r"><span>5</span><b>B &middot; Pricing</b>How they want the money presented</div>
    <div class="r"><span>6</span><b>Then everything else</b>D through K, before you sign</div>
  </div>
  <p class="takeaway r">Stop. Don't read A through M.</p>''',
  "The single most practical thing I'll tell you this week: do not read an RFP front to back. You'll drown in contract clauses before you reach the parts that tell you what to write and how you'll be scored. Section A orients you in two minutes. Then straight to L, your instruction manual: if you don't follow it, you can be thrown out before anyone reads a word. Then M, how they score you. Then C, the actual work, because you can't write an approach until you know the requirements. Then B, the pricing structure. Everything else after.",
  eyebrow="Part 2 &middot; Reading order", title="A &rarr; L &rarr; M &rarr; C &rarr; B")

section("Section A", "The cover page",
  "Let's walk through each one. Starting with the cover page.")

slide("light", '''
  <div class="cols2 wide-left">''' + bullets([
    "<b>Solicitation number</b>: goes on every question and every page you submit",
    "<b>Type</b>: sealed bid (IFB), RFP, or RFQ",
    "<b>Issue date and due date</b>: your clock starts",
    "<b>Contracting officer</b>: the one person you ask questions",
    "<b>Issuing office</b>: who is buying",
    "<b>Page count</b>: how big a lift this is"]) + '''
    <div class="callout r"><p>Check the type box.</p><span>Sealed bid = price decides. RFP = they score your approach too.</span></div>
  </div>''',
  "The cover page is your orientation. SF 33 on a negotiated RFP, SF 1449 on a commercial buy like ours. The solicitation number goes on everything. The type matters: under sealed bidding, award goes to the lowest-priced responsive, responsible bid. An RFP is negotiated, and they evaluate your approach, past performance and price, with weights that vary. The contracting officer, or the contract specialist named with them, is the person you're allowed to ask. The page count gives you a sense of complexity before you read a word.",
  eyebrow="Section A &middot; Cover page", title="Two minutes, five facts")

section("Section L", "Your instruction manual",
  "Section L is where the rubber meets the road. The most important section for preparing your proposal.")

slide("light", '''
  <div class="cols2 wide-left">''' + bullets([
    "How many volumes: technical, price, past performance",
    "What goes in each, and in what order",
    "Page limits per volume",
    "Format: font, size, margins",
    "How and where to submit, and by when",
    "What <em>not</em> to send"]) + '''
    <div class="callout r"><p>If L says it, you do it.</p><span>No exceptions. 51 pages on a 50-page limit can be thrown out.</span></div>
  </div>''',
  "Section L is not a suggestion. If it says the technical volume is 50 pages, Times New Roman 10-point, one-inch margins, you do exactly that. Submit 51 pages or squeeze to 9-point and they can throw it out. I've seen it happen. L also gives you the structure; the evaluators' scoring sheet maps to it, so if your proposal doesn't match they can't find your answers. Print L and keep it next to your keyboard. And when it says don't submit information that wasn't requested, they mean it. No brochures. On a commercial buy like ours, look for the addendum to FAR 52.212-1.",
  eyebrow="Section L &middot; Instructions", title="The recipe")

checkpoint("Section A", "Read the cover page and the instructions",
  "Open the practice solicitation. In Section A of the worksheet: the due date and time, how to submit, and one instruction you could get wrong.",
  "Three minutes, full pause. They should be clicking into the SAM.gov page and the solicitation attachment. Ask one or two people to read out the due date including time zone, and the submission method. If someone finds a page limit or format rule, praise it loudly. Remind: don't hit Submit yet.")

section("Section M", "How they'll score you",
  "You know how to prepare it. Now let's talk about how they're going to judge it.")

slide("light", '''
  <div class="split r">
    <div class="half cap"><p>Best value trade-off</p><h3>Quality can beat price</h3><span>A stronger proposal at a higher price can win</span></div>
    <div class="divider"><span>OR</span></div>
    <div class="half prop"><p>LPTA</p><h3>Pass, then cheapest</h3><span>Meet the technical bar; lowest price wins</span></div>
  </div>''' + bullets([
    "The factors, their weights, and the sub-factors in order"]) + '<p class="takeaway r">Ours: LPTA. Technical, past performance, price.</p>',
  "Section M tells you what the government actually cares about, so it tells you where to spend your energy. If it says technical is significantly more important than price, write the best technical proposal you can, even at a slightly higher price. If it says Lowest Price Technically Acceptable, meet the minimum and compete on price. Same company, completely different proposal. Tie back to Wednesday: your win themes should map to the factors in M, one per factor. On a commercial buy, look for the addendum to FAR 52.212-2, or a paragraph called Basis for Award. Ours is LPTA: technical and past performance are pass or fail, then the lowest evaluated realistic price wins. That tells you how to write it: clear, complete, compliant, and priced sharp.",
  eyebrow="Section M &middot; Evaluation", title="Two ways to win")

section("Section C", "The work",
  "Now you know the rules and the scoring. Let's look at what they actually want done.")

slide("light", '''
  <div class="cols2">
    <div class="roles r">
      <div><b>From our PWS, para. 1</b><span>"The Contractor shall establish a complete Quality Control Program ... no later than 30 calendar days after contract award."</span></div>
      <div><b>From our PWS, para. 3</b><span>"Once a month ... the Contractor shall post in each building ... an inspection form."</span></div>
      <p class="fine">A SOW tells you how; a PWS tells you the result. Either way, every shall gets an answer.</p>
    </div>''' + bullets([
    "Every <b>\"the contractor shall\"</b> is a requirement",
    "Performance standards and how they're inspected",
    "Where, when, and how often",
    "Period of performance: base + option years",
    "Required staff, clearances, certifications"]) + '</div>',
  "Section C is the substance. A Statement of Work is prescriptive: it tells you how. A Performance Work Statement is results-based: it tells you the outcome and leaves the how to you, and your approach becomes your differentiator. Either way, the magic words are the contractor shall. Every one is a requirement, and your proposal has to answer every single one. Miss one and the evaluators will find the gap. This is also where you spot labor, locations and frequency, which all feed your price.",
  eyebrow="Section C &middot; The work", title="Find every \"shall\"")

section("Section B", "The pricing structure",
  "Last of the big five. Section B tells you how to present your price.")

slide("light", '''
  <table class="compare r">
    <thead><tr><th>Pricing region (ours)</th><th>What you price</th></tr></thead>
    <tbody>
      <tr><td>MD / Northern Virginia</td><td>Every site in the region, every line</td></tr>
      <tr><td>Eastern PA / DE</td><td>Every site in the region, every line</td></tr>
      <tr><td>Western PA &middot; Central PA &middot; WV</td><td>Bid only the regions you can serve</td></tr>
    </tbody>
  </table>''' + bullets([
    "Contract type: ours is firm fixed price",
    "Labor rates by category &times; hours, at or above the wage determination",
    "Leave a line blank and you're incomplete"]),
  "Section B is the money side. CLINs, contract line item numbers, break the work into pieces the government pays for separately, and each should map to work in Section C. The contract type drives your risk: firm fixed price means overruns are yours. Ours is priced by region: you may bid only the regions you can serve, but you must price every site in each region you bid, and every line has to be filled in. For janitorial, watch the Service Contract Act wage determination in the attachments: it sets the minimum wages and fringe benefits you must pay, so it sets the floor on your price. In an LPTA buy, that floor is where the competition happens.",
  eyebrow="Section B &middot; Pricing", title="How they want the money")

checkpoint("Section B", "Find the scoring and the \"shalls\"",
  "Section B of the worksheet: how this one is evaluated, two \"the contractor shall\" statements from the PWS, and one question you'd ask the contracting officer.",
  "Three minutes, full pause. Ask: best value or LPTA? Who found it, and where? Then take one or two shall statements and one CO question aloud. Good answer to push toward: anything ambiguous about square footage, frequency, or the wage determination. Remind: don't hit Submit yet.")

section("Don't skip these", "Sections that still need a response",
  "Before the compliance matrix, three more sections that need a response even though they don't drive your strategy.")

slide("light", '''
  <div class="four r">
    <div><b>H &middot; Special requirements</b><span>Key personnel, security, local-office rules. Can change your staffing plan.</span></div>
    <div><b>J &middot; Attachments</b><span>Forms to fill and return: past performance questionnaires, pricing sheets, the wage determination.</span></div>
    <div><b>K &middot; Reps &amp; certs</b><span>Your size and status. Mostly in SAM.gov, but some come with the proposal.</span></div>
    <div><b>D&ndash;G, I &middot; Read, then sign</b><span>Inspection, delivery, invoicing, FAR clauses. These become your contract terms.</span></div>
  </div>
  <p class="takeaway r">Check every attachment for an action item.</p>''',
  "Easy to overlook, and missing them is a compliance failure. H is where the special requirements hide: a facility within 30 miles, key personnel who can't be swapped without approval. J is the attachments: don't assume they're FYI. For janitorial, J is often where the wage determination and the site list live. K is reps and certs, mostly handled when you register in SAM.gov, but read it and check the boxes. The rest, D through G and I, you don't answer in the proposal, but they become your contract. Section I is usually the longest: FAR clauses by reference. Look them up at acquisition.gov.",
  eyebrow="Part 4 &middot; Response required", title="Don't skip these")

section("Part 5", "Building the compliance matrix",
  "Now let's put it all together. The tool that connects all three sessions.")

slide("light", '''
  <table class="compare r">
    <thead><tr><th>RFP ref</th><th>Requirement</th><th>Instruction (L)</th><th>Scored under (M)</th><th>Proposal section</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>PWS 1</td><td>Quality Control Program in 30 days</td><td>Vol I: staffing &amp; mgmt plan</td><td>Technical</td><td>1.2 QC program</td><td>Draft</td></tr>
      <tr><td>PWS 1.2</td><td>Keep inspection records</td><td>Vol I: technical approach</td><td>Technical</td><td>1.3 QA/QC</td><td>Outline</td></tr>
      <tr><td>PWS 10</td><td>Provide all equipment &amp; supplies</td><td>Vol I: equipment list</td><td>Technical</td><td>1.4 Equipment</td><td>Not started</td></tr>
      <tr><td>Wage det.</td><td>Pay SCA rates</td><td>Vol III: price</td><td>Price</td><td>Price schedule</td><td>In review</td></tr>
    </tbody>
  </table>
  <p class="statement center r">If only one tool leaves with you, make it this one.</p>''',
  "This is the compliance matrix. If you take one tool from the whole series, make it this. Every shall from C gets a row. L tells you where in your proposal it gets answered. M tells you how it's scored. Now you have one document that says: here's what they want, here's where I answer it, here's how they'll grade it. It guarantees compliance, it tells your writers exactly what to address, and it powers your red team review. It's the template from Wednesday's email. These four rows come straight from our practice RFQ. Your homework is to add more.",
  eyebrow="Part 5 &middot; Compliance matrix", title="Every requirement, one row")

slide("light", '''
  <div class="tiles">
    <div class="r"><span>1</span><b>Read L</b>List every instruction: volumes, limits, format</div>
    <div class="r"><span>2</span><b>Read M</b>List every factor and sub-factor</div>
    <div class="r"><span>3</span><b>Read C</b>One row per "shall"</div>
    <div class="r"><span>4</span><b>Map</b>Each row to its L location and M factor</div>
    <div class="r"><span>5</span><b>Outline</b>Your proposal outline falls out of the matrix</div>
    <div class="r"><span>6</span><b>Track</b>Writing status and review, row by row</div>
  </div>
  <p class="takeaway r">Build the matrix before you write a single word.</p>''',
  "The process. Start with L because it's the structure of your proposal. Then M for what's scored. Then C: every shall gets a row, mapped to where it goes and how it's scored. Once it's built you can allocate pages: if technical approach is weighted most and has 12 requirements in 30 pages, that's about two and a half pages each, and more for the heavy ones. It takes a day, maybe two. It saves you a week of rewriting.",
  eyebrow="Part 5 &middot; Compliance matrix", title="Six steps to build it")

slide("light", '''
  <div class="cols2 wide-left">''' + bullets([
    "Evaluation Criteria: <b>3</b> similar projects in the past <b>5</b> years",
    "Past performance questionnaire: <b>2</b> references in the past <b>3</b> years",
    "The questionnaire calls relevant work \"crane support and inspection\""]) + '''
    <div class="callout r"><p>Ask. In writing.</p><span>That's what the question deadline is for.</span></div>
  </div>''',
  "Something real I found reading our RFQ, and it's why you read it three times. The Evaluation Criteria ask for three similar projects in the past five years. The past performance questionnaire, a different attachment, asks for two references within three years, and describes relevant work as crane support and inspection. That was pasted from another solicitation. Which one do you follow? You don't guess. You send a written question to the contracting officer before the question deadline, and the answer goes to every offeror. When documents conflict, the Q&amp;A period is your friend.",
  eyebrow="Found in our RFQ", title="Spot the conflict")

slide("light", '''
  <table class="compare r">
    <thead><tr><th>Awardee</th><th>Based in</th><th>BPA value on the award notice</th></tr></thead>
    <tbody>
      <tr><td>Crystal Cleanz LLC</td><td>Germantown, MD</td><td>$4,956,097</td></tr>
      <tr><td>Greenfield International Corp.</td><td>Woodbridge, VA</td><td>$4,979,445</td></tr>
      <tr><td>Integrity Core Alliance LLC</td><td>Austell, GA</td><td>$2,853,298</td></tr>
    </tbody>
  </table>
  <p class="statement center r">Three small businesses. One is from Germantown.</p>''',
  "How it ended. The Corps awarded three master blanket purchase agreements in mid-September. The amounts are the values on the public award notices, most likely ceilings, not money already paid. One winner is a Maryland small business from Germantown. One is from Georgia, which tells you small businesses from anywhere will bid in your backyard. And a BPA isn't a paycheck: it's a license to receive orders. The win is where the work starts. All of this is public on SAM.gov; search the solicitation number.",
  eyebrow="How it ended", title="Who won")

slide("light", '''
  <div class="cols2">
    <div class="card accent r"><p class="card-k">Can sink you</p>''' + bullets([
        "Breaking a format or page-limit rule",
        "Missing a \"shall\"",
        "Treating the attachments as FYI",
        "Missing the due time or time zone"]) + '''</div>
    <div class="card r"><p class="card-k">Costs you points</p>''' + bullets([
        "Reading it once instead of three times",
        "Writing to what you do, not to Section M",
        "Skipping the Q&amp;A window",
        "Writing before building the matrix"]) + '''</div>
  </div>''',
  "The mistakes I see most. Number one killer: formatting non-compliance. Page limits and font rules are hard limits, and there's no appeal. Read it at least three times: once to understand it, once to build the matrix, once to check your proposal against it. Use the Q&amp;A period: if something is ambiguous, ask. Answers go to every offeror, so you're not giving away your strategy, and if you guess wrong, that's on you. And the one small businesses miss: the due time and time zone. 2:00 p.m. Eastern means 2:00 p.m. Eastern, not end of day.",
  eyebrow="Part 6 &middot; Watch for these", title="Traps that catch small businesses")

slide("light", '''
  <div class="tiles">
    <div class="r"><span>1</span><b>A &rarr; L &rarr; M &rarr; C &rarr; B</b>Not front to back</div>
    <div class="r"><span>2</span><b>L is the recipe</b>Follow it exactly</div>
    <div class="r"><span>3</span><b>M is how you win</b>One win theme per factor</div>
    <div class="r"><span>4</span><b>Every "shall" counts</b>Each one gets a row</div>
    <div class="r"><span>5</span><b>Matrix first</b>Then outline, then write</div>
    <div class="r"><span>6</span><b>Ask during Q&amp;A</b>Guessing wrong is on you</div>
  </div>''',
  "Bring it together. Reading an RFP is a skill: the first is overwhelming, the second is hard, by the fourth you know where to look. The reading order is the most practical thing today. The compliance matrix is the bridge between reading the RFP and writing the proposal. Monday is our last session: Basics of Proposal Writing, where we turn the matrix into content that scores.",
  eyebrow="Today", title="What to remember")

slide("light", f'''
  <div class="cols2">
    <div class="card r"><p class="card-k">Monday, Oct 5 &middot; 10:00 a.m. &middot; Session 4</p>
      <h3 class="next-h">Basics of proposal writing</h3>''' + bullets([
        "Writing to the evaluation criteria",
        "Structuring each section",
        "Standing out in a stack of 20",
        "Bring your compliance matrix"]) + f'''</div>
    <div class="submit-card r">
      <p class="eyebrow light">Worksheet &middot; Section C</p>
      <h3>Write your one step, then submit.</h3>
      <p>Your inbox gets: this deck with notes, the compliance matrix template, the practice solicitation link, and acquisition.gov.</p>
      <div class="mini-qr">{QR_FORM}</div>
    </div>
  </div>''',
  "Monday is Session 4, Basics of Proposal Writing: we take the compliance matrix and turn it into content that scores. Homework: pull two or three shall statements from today's PWS into your matrix. Now Section C of the worksheet, the one step you'll take this month, then the last page and Submit. That's what sends you the deck and the links.",
  eyebrow="What's next", title="Submit your worksheet")

slide("dark title close", f'''
  <img class="logo r" alt="America's SBDC Maryland" src="data:image/png;base64,{LOGO}">
  <div class="title-grid">
    <div>
      <h1 class="r">Questions?</h1>
      <div class="band r"></div>
      <p class="byline r">Your Name &middot; Maryland SBDC<br>you@yourorg.org</p>
      <p class="byline small r">No-cost, one-on-one consulting. Register as an SBDC client: {SIGNUP_LABEL}</p>
    </div>
    <div class="qr-card r">{QR_SIGNUP}<span>Register for 1:1 advising</span></div>
  </div>
  <p class="sba r">Funded in part through a Cooperative Agreement with the U.S. Small Business Administration. All opinions, conclusions, and/or recommendations expressed herein are those of the author(s) and do not necessarily reflect the views of the SBA. Reasonable accommodations for persons with disabilities will be made if requested at least two weeks in advance.</p>''',
  "Open it up. Let the conversation go where it needs to go. Remind them to submit the worksheet if they haven't.", label="Questions")

engine.render(pathlib.Path.cwd() / "How-to-Read-an-RFP-2026-10-02.html",
              title="How to Read a Federal RFP",
              footer="Session 3 &middot; How to Read a Federal RFP")
