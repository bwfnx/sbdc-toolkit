# Session 2 class file (copied from the sbdc-workshops session1_example.py). Build:  py build.py  (run from this folder)
import pathlib, sys
sys.path.insert(0, str(pathlib.Path.home() / ".claude" / "skills" / "sbdc-workshops" / "scripts" / "deck"))
import engine
engine.setup("[YOUR-FORM-URL]")
from engine import *

# ============================ SLIDES ============================

slide("dark title", f'''
  <img class="logo r" alt="America's SBDC Maryland" src="data:image/png;base64,{LOGO}">
  <div class="title-grid">
    <div>
      <p class="eyebrow light r">Winning That Government Contracting Award &middot; Session 2 of 4</p>
      <h1 class="r">Team Roles and Responsibilities</h1>
      <div class="band r"></div>
      <p class="byline r">Your Name &middot; Maryland Small Business Development Center<br>Wednesday, September 30, 2026</p>
    </div>
    <div class="qr-card r">{QR_FORM}<span>Scan now: your worksheet</span></div>
  </div>''',
  "Welcome back. Monday we covered the full business development lifecycle: the 36-month pipeline, the six phases, Go/No-Go. Today we zoom in on something that trips up almost every small business I work with: who actually does the work on a proposal? I'll walk through every role on a full-scale capture and proposal team. In a large company that's 15 to 20 people. For most of you it's 2 or 3, or just you. That's fine. What matters is that the functions get covered, not that you have a separate person for each. As we go, ask yourself: which of these am I already doing, and which am I skipping? Before we start: scan the code on screen. That's today's worksheet.", label="Title")

slide("light scan", f'''
  <div class="scan-grid">
    <div>
      <ol class="steps">
        <li class="r"><b>Point your phone camera at the code.</b> Or click the link in the Zoom chat.</li>
        <li class="r"><b>Fill in page 1 now.</b> Name, email, business, where you are today.</li>
        <li class="r"><b>Keep the tab open.</b> We come back to it three times today.</li>
      </ol>
      <p class="url ink r">{FORM_LABEL}</p>
      <p class="fine r">When you submit at the end, the slides, the compliance matrix template and every link from today land in your inbox.</p>
    </div>
    <div class="qr-card big r">{QR_FORM}</div>
  </div>''',
  "Give them 90 seconds. This is a new worksheet, not Monday's, so even Monday's people scan again. Say: fill in your name and email now and keep the tab open. Host: please paste the link in the Zoom chat.",
  eyebrow="Before we start", title="Scan your worksheet")

slide("light", '''
  <ol class="agenda">
    <li class="r"><span>01</span>The full proposal team at a glance</li>
    <li class="r"><span>02</span>The six functional areas</li>
    <li class="r"><span>03</span>What each role does (and doesn't)</li>
    <li class="r"><span>04</span>Color reviews: built-in quality control</li>
    <li class="r"><span>05</span>Scaling it for a small business</li>
    <li class="r"><span>06</span>Where small businesses drop the ball</li>
  </ol>''',
  "Here's the roadmap. Six functional areas: Business Development, Capture and Proposal Management, Proposal Development, Solution Development, Contracts and Pricing, and Color Review Teams. For each one: what it looks like in a big company, then how you translate it to your size. These functions don't go away because you're small. You still need someone pricing. You still need someone reviewing before it goes out. The question is whether you do it on purpose or hope it works out.",
  eyebrow="Today", title="What we're covering")

slide("light", '''
  <div class="tiles">
    <div class="r"><span>1</span><b>Business development</b>Business developer &middot; lead executive</div>
    <div class="r"><span>2</span><b>Capture &amp; proposal mgmt</b>Capture manager &middot; proposal manager &middot; coordinator &middot; volume leads</div>
    <div class="r"><span>3</span><b>Proposal development</b>Writer &middot; editor &middot; graphic artist &middot; desktop publishing</div>
    <div class="r"><span>4</span><b>Solution development</b>Solution architect &middot; program manager</div>
    <div class="r"><span>5</span><b>Contracts &amp; pricing</b>Contracts manager &middot; subcontracts manager &middot; cost strategist</div>
    <div class="r"><span>6</span><b>Color review teams</b>Review team lead &middot; reviewers</div>
  </div>''',
  "Here's the full picture: what a large company's proposal team looks like. Eighteen roles across six areas. When I show this to small business owners I get one of two reactions: I can't afford all these people, or I'm doing all of this by myself. Both are valid. These are functions, not job titles. You don't need 18 people. You need all six areas covered. One-person shop: you wear all 18 hats. Team of three: you split them. The point is knowing what the hats are so you don't leave one on the shelf.",
  eyebrow="The master view", title="Six areas, eighteen hats")

section("Area 1", "Business development",
  "Let's start with Business Development. This is where everything begins, and it connects straight back to Monday.")

slide("light", '''
  <div class="cols2">
    <div class="roles r">
      <div><b>Business developer</b><span>finds opportunities, builds relationships, qualifies leads</span></div>
      <div><b>Lead executive</b><span>opens doors, sets strategic direction</span></div>
      <p class="fine">In a small business, both are usually you. That continuity is an advantage.</p>
    </div>''' + bullets([
    "Monitor SAM.gov, GovWin, agency forecasts",
    "Build relationships with COs and program managers",
    "Attend industry days and pre-solicitation conferences",
    "Qualify opportunities through the pipeline",
    "Make the first Go/No-Go recommendation"]) + '</div>',
  "If you were here Monday this should look familiar. BD is the front end of the lifecycle: finding opportunities, building relationships, qualifying leads. In a large company the BD person is at every industry day and knows every contracting officer by name. For most of you, the business developer is you. That's an advantage: the decision-maker is the same person building the relationship. In a big company BD hands off and knowledge gets lost. In your shop you found it, you know the customer, and you'll lead the proposal. The lead executive is about direction: which markets, which agencies, which partners. Are you being intentional, or chasing whatever shows up on SAM.gov?",
  eyebrow="Area 1 &middot; Business development", title="Find it, qualify it")

section("Area 2", "Capture & proposal management",
  "This is where it gets real: going from we found an opportunity to we're going to win this thing.")

slide("light", '''
  <div class="cols2 wide-right">''' + bullets([
    "Writes the capture strategy and win themes",
    "Manages customer engagement through the pursuit",
    "Coordinates the competitive analysis",
    "Drives Go/No-Go with data",
    "Hands the knowledge to the proposal team when the RFP drops"]) + '''
    <div class="callout r"><p>Write it down.</p><span>Usually the owner. Make it intentional.</span></div>
  </div>''',
  "The capture manager owns the win strategy. Period. Arguably the most important role on the chart, and the one small businesses almost never fill on purpose. They own the strategy from the moment an opportunity is found until the proposal goes out: why will the customer pick us, what's our win theme, who are we up against. In a small business it's usually the owner, doing it in their head instead of on paper. That's the problem. Write it down, even one page. When the RFP drops and you have 30 days, you don't have time to find your win themes. You should already know them. The capture management template from Monday is the tool that makes this manageable.",
  eyebrow="Area 2 &middot; Capture &amp; proposal management", title="Capture manager: owns the win")

slide("light", '''
  <div class="cols2 wide-left">''' + bullets([
    "Builds the proposal schedule; tracks deadlines",
    "Builds the compliance matrix (Section L &rarr; Section M)",
    "Assigns sections to writers and volume leads",
    "Runs the daily stand-ups",
    "Runs the color reviews",
    "Owns final production and submission"]) + '''
    <div class="keyouts r"><p class="card-k">Primary tool</p><div class="ko">Compliance matrix</div><p class="fine">Maps every requirement in Section L to every evaluation criterion in Section M. Template in your inbox today; we use it in Session 3.</p></div>
  </div>''',
  "The proposal manager makes sure the train runs on time. The capture manager says here's our strategy. The proposal manager says great, here's how we turn that into a compliant, compelling document in 30 days. It's a project management role: Section 3 is due Friday, Pink Team is Tuesday. The compliance matrix is their primary tool. If you don't have one, you're guessing at compliance. You get the template in today's follow-up email, and we dig into it Friday in Session 3.",
  eyebrow="Area 2 &middot; Capture &amp; proposal management", title="Proposal manager: owns the process")

slide("light", '''
  <div class="split r">
    <div class="half cap"><p>Capture hat</p><h3>Strategy</h3><span>Why will they pick us?</span></div>
    <div class="divider"><span>YOU</span></div>
    <div class="half prop"><p>Proposal hat</p><h3>Execution</h3><span>Compliant, on time, on page count</span></div>
  </div>
  <p class="statement center r">Same person is fine. Know which hat you're wearing.</p>''',
  "In a small business the capture manager and proposal manager are often the same person. That's fine, as long as you know you're wearing two hats. Capture hat: strategy and win themes. Proposal hat: schedules, compliance, production. Different mindsets. Mixing them is how you end up rewriting strategy three days before the deadline.",
  eyebrow="Area 2 &middot; Capture &amp; proposal management", title="Two hats, one head")

slide("light", '''
  <div class="cols2">
    <div class="card r"><p class="card-k">Proposal coordinator</p>''' + bullets([
        "Manages the shared drive and tools",
        "Tracks document versions",
        "Printing, binding, shipping if hard copy",
        "Verifies clearances"]) + '''</div>
    <div class="card r"><p class="card-k">Volume leads</p>''' + bullets([
        "One lead per major volume",
        "Technical &middot; Management &middot; Past Performance &middot; Cost",
        "Owns that volume's compliance and quality"]) + '''</div>
  </div>''',
  "Support roles, and where large companies start to look different from you. A big-company coordinator is full time: war room, every version, the logistics of a several-hundred-page submission. For you the function still matters. I've seen small businesses lose on technicalities: the wrong version of a document, a missing attachment. That's a coordinator failure even if nobody had the title. Volume leads matter more as proposals grow. Separate technical, management, past performance and cost volumes? Someone owns each one, even if it's you with four colored tabs in your binder.",
  eyebrow="Area 2 &middot; Capture &amp; proposal management", title="Coordinator &amp; volume leads")

section("Area 3", "Proposal development",
  "Now the people who actually write, design and produce the document.")

slide("light", '''
  <div class="four r">
    <div><b>Writer</b><span>Drafts sections from the win themes and the compliance requirements</span></div>
    <div><b>Editor</b><span>Consistency, grammar, readability, page limits</span></div>
    <div><b>Graphic artist</b><span>Original process diagrams, org charts, schedules. Not clip art.</span></div>
    <div><b>Desktop publishing</b><span>Layout, fonts, margins, headers, page numbers: final production</span></div>
  </div>
  <p class="takeaway r">Proposal writing is a skill. A good writer can move you from a 70 to a 90.</p>''',
  "This is the team that builds the document, and the biggest gap I see. Most owners are technical experts, not writers. Proposal writing is not email writing. A proposal writer turns your win themes into language that maps to the evaluation criteria: action-result statements, benefits to the government, not features of your company. No shame if that's not you; it's one of the best places to spend money. Graphics are the other underinvestment. Evaluators read dozens of proposals; one good graphic can do more than three pages of text. And DTP: the RFP tells you font, margins, page limits. Violate them and you can get thrown out.",
  eyebrow="Area 3 &middot; Proposal development", title="The people who build the document")

checkpoint("Section A", "Which hats are you wearing?",
  "Tap Next to Section A. Tick every role you cover yourself today, then name the one you're skipping and who could cover it.",
  "Two minutes. Ask for one or two people to share the hat they're skipping, in the Zoom chat or out loud. React to one: is that a gap you could fill with a contractor, a teaming partner or a mentor?")

section("Area 4", "Solution development",
  "This is where your technical expertise lives: how you'll actually do the work.")

slide("light", '''
  <div class="cols2">
    <div class="roles r">
      <div><b>Solution architect</b><span>designs the technical approach and methodology</span></div>
      <div><b>Program manager</b><span>plans execution, staffing and management</span></div>
      <p class="fine">Often the owner. You have the substance; the hard part is making an evaluator who never met you score it high. Pair with a writer.</p>
    </div>''' + bullets([
    "Technical approach and methodology",
    "Work breakdown structure (WBS)",
    "Staffing plan and org chart",
    "Risks and mitigations",
    "Transition plan from the incumbent",
    "Quality control and performance measures"]) + '</div>',
  "The solution architect answers: how are we going to do this work? For most small businesses that's the owner or lead technical person, and that's your strongest position. You've done this for 15 or 20 years. The challenge isn't having the solution; it's articulating it so an evaluator who has never met you scores it highly. That's why the solution architect and the writer need to work closely: you bring the substance, they translate it. The program manager is about execution: staffing, timelines, risk, quality. The government wants to know you've thought through how you'll manage it, not only that you can do it.",
  eyebrow="Area 4 &middot; Solution development", title="How we'll do the work")

section("Area 5", "Contracts & pricing",
  "Now the money side. This is where a lot of proposals either win or die.")

slide("light", '''
  <div class="cols2 wide-left">
    <div class="roles r">
      <div><b>Contracts manager</b><span>terms, conditions, FAR / DFARS compliance</span></div>
      <div><b>Subcontracts manager</b><span>teaming agreements, flow-downs</span></div>
      <div><b>Cost strategist</b><span>price-to-win, builds the cost volume</span></div>
      <p class="fine">Cost volume = direct labor + indirect rates + ODCs + fee. Contract type (FFP, T&amp;M, cost-plus) changes all of it.</p>
    </div>
    <div class="callout r"><p>Get help here.</p><span>Government pricing is not commercial pricing.</span></div>
  </div>''',
  "The area that terrifies most small businesses, for good reason. Government pricing is not commercial pricing: FAR Part 31, DCAA compliance, cost accounting standards, indirect rates. The contracts manager reads the terms most people skip and flags what you can't do. Often outsourced to an attorney or contracts consultant; fine, but someone reads them. The subcontracts manager matters if you're teaming, and most of you should be early on. The cost strategist builds your price. Lowest price isn't always how you win: on best value a stronger proposal at a higher price can win. My advice: get help. If you don't have a DCAA-compliant accounting system, don't know your indirect rates, or have never built a cost volume, find an accountant who specializes in government contracts. Not the place to wing it.",
  eyebrow="Area 5 &middot; Contracts &amp; pricing", title="Where proposals win or die")

section("Area 6", "Color review teams",
  "Last area, and the one that separates good proposals from great ones.")

slide("light", '''
  <div class="colorflow r">
    <div class="cf write">Write</div><i></i>
    <div class="cf pink">Pink team<small>~30&ndash;40% done. Right strategy? Right direction?</small></div><i></i>
    <div class="cf write">Revise</div><i></i>
    <div class="cf red">Red team<small>~80&ndash;90% done. Score it like the government.</small></div><i></i>
    <div class="cf write">Revise</div><i></i>
    <div class="cf gold">Gold team<small>Final. Ready to submit?</small></div><i></i>
    <div class="cf submit">Submit</div>
  </div>
  <p class="statement center r">Small business version: 2 or 3 trusted outside readers.</p>''',
  "Color reviews are your quality control: catch problems before the government does. Almost no small business does them, so if you do, you have an immediate edge. Pink Team at 30 to 40 percent: strategy, approach, compliance direction. Early enough to change course. Red Team at 80 to 90 percent: reviewers score the full draft against Section M, using the government's language: strengths, weaknesses, deficiencies. Your dress rehearsal. Gold Team: executive check, is this our best, ready to go. You won't have a 10-person review team, but find two or three people you trust: a former contracting officer, a teaming partner, a fellow SBDC client. Even one outside reader catches what you miss after three weeks staring at it.",
  eyebrow="Area 6 &middot; Color review teams", title="Pink, red, gold")

slide("light", '''
  <table class="compare r">
    <thead><tr><th>Function</th><th>Who does it in a small business</th></tr></thead>
    <tbody>
      <tr><td>BD &amp; capture</td><td>You, the owner</td></tr>
      <tr><td>Proposal manager</td><td>You, or your most organized person</td></tr>
      <tr><td>Writer</td><td>You, or a hired proposal writer</td></tr>
      <tr><td>Solution architect</td><td>You, the technical expert</td></tr>
      <tr><td>Pricing</td><td>You, or a govcon accountant</td></tr>
      <tr><td>Color reviews</td><td>2 or 3 trusted outside reviewers</td></tr>
    </tbody>
  </table>''',
  "Let's get real about your version. You're doing most of these yourself. That's not a weakness, it's reality, and the upside is continuity: you know the customer, the strategy, the technical approach, and you make every decision. In a large company, knowledge gets lost in the handoffs. But notice three rows say or someone else. That's next.",
  eyebrow="Scaling it", title="Your version of the team")

slide("light", '''
  <div class="tiles">
    <div class="r"><span>1</span><b>Proposal writing</b>If writing isn't your strength. It moves your technical score.</div>
    <div class="r"><span>2</span><b>Cost volume</b>If you're new to government accounting. Non-compliant pricing sinks a great proposal.</div>
    <div class="r"><span>3</span><b>Color reviews</b>You can't objectively review your own work. Buy them dinner.</div>
  </div>
  <p class="takeaway r">Everything else you can do yourself, on purpose.</p>''',
  "Three places I consistently see outside help pay off. One, proposal writing: translating technical knowledge into language that scores is a different skill. Two, the cost volume: specialized and unforgiving. A non-DCAA-compliant cost volume doesn't care how good your technical approach is. Three, color reviews: you've been too close to it for too long. Find people who've been on the government side, who've evaluated proposals. Buy them dinner. It's worth it.",
  eyebrow="Scaling it", title="Three things worth outsourcing")

checkpoint("Section B", "Who reads it before you submit?",
  "Section B: pick who reads your next proposal, name one person you could ask to review it, and the one function you'd get help with first.",
  "Two to three minutes. Then ask: how many picked Nobody yet? That's the conversation. Push them to write a real name for the reviewer, not a role. Tie back: start building the reviewer network now, before the RFP drops.")

slide("light", '''
  <div class="cols2">
    <div class="card accent r"><p class="card-k">Can sink you</p>''' + bullets([
        "No compliance matrix: guessing at what's required",
        "Cost volume as an afterthought",
        "No version control: the final has mismatches"]) + '''</div>
    <div class="card r"><p class="card-k">Costs you points</p>''' + bullets([
        "No capture strategy: writing starts when the RFP drops",
        "Owner does everything: burns out, ships a B-",
        "No review cycle: nobody reads it first"]) + '''</div>
  </div>''',
  "I've reviewed hundreds of small business proposals. These patterns show up over and over. Most common: no capture strategy. The RFP drops, the owner panics and starts writing. No win themes, no competitive analysis. That's how you get technically adequate and forgettable. Second: no compliance matrix. More in Session 3, but if nothing maps every requirement to where you answered it, you're gambling. Third: burnout. The owner does BD, capture, writing, pricing, graphics and reviews, and ships 70 percent of what it could be. And version control: I've seen Section 2 reference a staffing approach revised in Section 4 with nobody updating it, or a page limit blown by one last paragraph. A coordinator checklist prevents that.",
  eyebrow="Watch for these", title="Where small businesses drop the ball")

slide("light", '''
  <div class="tiles">
    <div class="r"><span>1</span><b>Functions, not titles</b>Every function gets covered, whatever your size</div>
    <div class="r"><span>2</span><b>Write the capture plan</b>The most critical and most skipped role</div>
    <div class="r"><span>3</span><b>Know your hat</b>Strategy and execution are different mindsets</div>
    <div class="r"><span>4</span><b>Buy help wisely</b>Writing and pricing pay for themselves</div>
    <div class="r"><span>5</span><b>Review before you submit</b>Color reviews are free quality control</div>
    <div class="r"><span>6</span><b>Build your reviewers now</b>Before the RFP drops, not after</div>
  </div>''',
  "Where I want to leave you. These are functions: one person or twenty, every function happens, on purpose or by accident. If you take one thing, it's that the capture manager function matters: a written capture strategy with win themes before the RFP drops. Know where to get help: writers, government accountants, reviewers. And start your reviewer network now. Don't wait until a proposal is due in three weeks. Ask people now, and offer to return the favor.",
  eyebrow="Today", title="What to remember")

slide("light", f'''
  <div class="cols2">
    <div class="card r"><p class="card-k">Friday, Oct 2 &middot; 10:00 a.m. &middot; Session 3</p>
      <h3 class="next-h">How to read an RFP</h3>''' + bullets([
        "What every section of a solicitation means",
        "Sections L and M, side by side",
        "Building your compliance matrix",
        "What the government is really asking for"]) + f'''</div>
    <div class="submit-card r">
      <p class="eyebrow light">Worksheet &middot; Section C</p>
      <h3>Write your one step, then submit.</h3>
      <p>Your inbox gets: this deck with notes, the compliance matrix template, and every link from today.</p>
      <div class="mini-qr">{QR_FORM}</div>
    </div>
  </div>''',
  "Friday is Session 3, How to Read an RFP. We take Sessions 1 and 2 and apply them to a real solicitation: what the sections mean, how to build the compliance matrix, what the government is really asking for. Bring the compliance matrix template from today's email. Now: Section C, write the one step you'll take this month, then the last page and Submit. That's what sends you the deck and the template.",
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

engine.render(pathlib.Path.cwd() / "Team-Roles-and-Responsibilities-2026-09-30.html",
              title="Team Roles and Responsibilities",
              footer="Session 2 &middot; Team Roles and Responsibilities")
