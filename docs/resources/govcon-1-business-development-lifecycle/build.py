# Builds the Session 1 deck (single self-contained HTML) in the Maryland SBDC design system.
# Re-run after changing FORM_URL:  py build.py
import base64, html, io, pathlib
import qrcode, qrcode.image.svg

HERE = pathlib.Path(__file__).parent
OUT = HERE / "Business-Development-Lifecycle-2026-09-28.html"

# ponytail: long link on purpose (no short link made); on Zoom the label points people to the chat.
FORM_URL = "[YOUR-FORM-URL]"
FORM_LABEL = "Link is in the Zoom chat"
SIGNUP_URL = "https://mdsbdc.ecenterdirect.com/signup"
SIGNUP_LABEL = "mdsbdc.ecenterdirect.com/signup"

LOGO = base64.b64encode((HERE / "logo-reverse-900.png").read_bytes()).decode()
VIEWPORT_BASE = (pathlib.Path(__file__).parent / "viewport-base.css").read_text()


def qr(url):
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage, box_size=10, border=2)
    buf = io.BytesIO(); img.save(buf)
    svg = buf.getvalue().decode()
    return svg[svg.index("<svg"):]


QR_FORM, QR_SIGNUP = qr(FORM_URL), qr(SIGNUP_URL)
SLIDES = []


def slide(kind, body, notes, eyebrow="", title="", label=""):
    head = ""
    if eyebrow:
        head += f'<p class="eyebrow r">{eyebrow}</p>'
    if title:
        head += f'<h2 class="r">{title}</h2><div class="rule r"></div>'
    SLIDES.append((kind, head + body, notes, html.unescape(label or title or eyebrow)))


def section(num, title, notes):
    slide("dark section", f'''
      <div class="sec-num r">{num}</div>
      <h1 class="r">{title}</h1>
      <div class="band r"></div>''', notes, title="")
    SLIDES[-1] = (*SLIDES[-1][:3], title)


def checkpoint(qs, title, blurb, notes):
    slide("dark checkpoint", f'''
      <div class="cp-grid">
        <div>
          <p class="eyebrow light r">Worksheet checkpoint &middot; {qs}</p>
          <h1 class="r">{title}</h1>
          <p class="lead r">{blurb}</p>
          <p class="url r">{FORM_LABEL}</p>
        </div>
        <div class="qr-card r">{QR_FORM}<span>Lost the tab? Scan again.</span></div>
      </div>''', notes)
    SLIDES[-1] = (*SLIDES[-1][:3], f"Checkpoint {qs}")


def bullets(items, cls=""):
    return f'<ul class="list {cls}">' + "".join(f'<li class="r">{i}</li>' for i in items) + "</ul>"


# ============================ SLIDES ============================

slide("dark title", f'''
  <img class="logo r" alt="America's SBDC Maryland" src="data:image/png;base64,{LOGO}">
  <div class="title-grid">
    <div>
      <p class="eyebrow light r">Winning That Government Contracting Award &middot; Session 1 of 4</p>
      <h1 class="r">Business Development Lifecycle</h1>
      <div class="band r"></div>
      <p class="byline r">Your Name &middot; Maryland Small Business Development Center<br>Monday, September 28, 2026</p>
    </div>
    <div class="qr-card r">{QR_FORM}<span>Scan now: your worksheet</span></div>
  </div>''',
  "Welcome everyone. I'm Your Name with the Maryland SBDC. Over the next four sessions we walk through what it actually takes to win a government contract, from finding the opportunity to submitting a winning proposal. Today is the big picture: the full business development lifecycle. This is not theory. Everything today comes from working with hundreds of small businesses going after government work. Some of it you'll know. Some of it might change how you think about this whole process. Before we start: scan the code on screen. That's your worksheet for today.", label="Title")

slide("light scan", f'''
  <div class="scan-grid">
    <div>
      <ol class="steps">
        <li class="r"><b>Point your phone camera at the code.</b> Or click the link in the Zoom chat.</li>
        <li class="r"><b>Fill in page 1 now.</b> Name, email, business, where you are today.</li>
        <li class="r"><b>Keep the tab open.</b> We come back to it three times today.</li>
      </ol>
      <p class="url ink r">{FORM_LABEL}</p>
      <p class="fine r">When you submit at the end, the capture template and every link from today land in your inbox.</p>
    </div>
    <div class="qr-card big r">{QR_FORM}</div>
  </div>''',
  "Give them 90 seconds. Say: fill in your name and email now and keep that tab open. If you close it you start over, and no email means no follow-up and no capture template. Host: please paste the link in the Zoom chat.",
  eyebrow="Before we start", title="Scan your worksheet")

slide("light", '''
  <ol class="agenda">
    <li class="r"><span>01</span>Where to find government opportunities</li>
    <li class="r"><span>02</span>How the government actually buys</li>
    <li class="r"><span>03</span>Revenue strategies: where you fit right now</li>
    <li class="r"><span>04</span>The 36-month capture pipeline</li>
    <li class="r"><span>05</span>The six phases of business development</li>
    <li class="r"><span>06</span>Go/No-Go: knowing when to walk away</li>
  </ol>''',
  "Here's the roadmap. This is usually more information than most people can handle in one sitting. That's fine. It all lands in your inbox after you submit the worksheet. I'd honestly recommend throwing it into NotebookLM or ChatGPT and asking it questions. That's what most of my clients do.",
  eyebrow="Today", title="What we're covering")

section("Part 1", "Finding opportunities",
  "Let's start at the beginning. Before capture strategy or proposal writing, you need to know where to actually look.")

slide("light", '''
  <div class="tiers">
    <div class="tier t1 r"><b>Federal</b><span>SAM.gov &middot; the single federal marketplace</span><em>$$$</em></div>
    <div class="tier t2 r"><b>State</b><span>eMaryland Marketplace Advantage (eMMA)</span><em>$30k+</em></div>
    <div class="tier t3 r"><b>County &amp; City</b><span>Howard, Montgomery, Prince George's, Baltimore Co., Baltimore City, Annapolis</span><em>$15k+</em></div>
  </div>
  <div class="also r"><b>Also look at:</b> subcontractor &amp; expiring-contract lists &middot; master contract award lists &middot; procurement forecasts &middot; networking, industry days, social media</div>''',
  "SAM.gov is where most people start, and that's fine. But I listed eight places and SAM.gov is one of them. Government contracting doesn't mean federal contracting. Maryland buys through eMMA. Your county buys. Your city buys. The thresholds are lower: $15k local, $30k state. If you're just starting out, look there first. Federal is where the big money is, and the big competition. Also flag procurement forecasts: agencies publish what they plan to buy next fiscal year. Most small businesses don't know these exist. Links come in the follow-up email.",
  eyebrow="Part 1 &middot; Finding opportunities", title="Where to look")

slide("light", '''
  <div class="cols2">
    <div class="card r"><p class="card-k">How they buy</p>
      <dl class="buy">
        <dt>Federal</dt><dd>Existing contract vehicles (IDIQs, GSA Schedule, SeaPort-e, OASIS+, OTAs), open solicitations on SAM.gov, DSBS for set-asides, forecasts</dd>
        <dt>State</dt><dd>eMMA for $30k+</dd>
        <dt>County / City</dt><dd>Procurement portals for $15k+</dd>
      </dl>
    </div>
    <div class="card accent r"><p class="card-k">Below ~$15k</p>
      <p class="big-line">Purchase cards.</p>
      <p>A government credit card. No formal solicitation required. If you sell something an agency needs for under ~$15k, a contracting officer can just buy it.</p>
    </div>
  </div>''',
  "The government doesn't buy like a normal customer. At the federal level most money flows through existing contract vehicles: IDIQs, GSA Schedules, OASIS+. Those are basically pre-approved lists of vendors. If you're not on one, you're either competing on an open solicitation through SAM.gov or, where a lot of my clients start, subcontracting under someone who is. Below about $15k, agencies can use purchase cards. No formal solicitation. That's worth knowing.",
  eyebrow="Part 1 &middot; Finding opportunities", title="How the government actually buys")

slide("light", '''
  <table class="compare r">
    <thead><tr><th></th><th>Government</th><th>B2B</th></tr></thead>
    <tbody>
      <tr><td>Where</td><td>Portals &amp; contract vehicles</td><td>Supplier portals, direct outreach</td></tr>
      <tr><td>Process</td><td>Formal: RFPs, RFQs, set-asides</td><td>RFPs, RFQs, traditional sales</td></tr>
      <tr><td>Timeline</td><td>Months to years</td><td>Weeks to months</td></tr>
      <tr><td>Rules</td><td>Compliance on top of everything</td><td>Fewer rules</td></tr>
      <tr><td>Relationships</td><td>Matter, within the rules</td><td>Often drive the deal</td></tr>
    </tbody>
  </table>
  <p class="takeaway r">The capture discipline works for both. Government adds compliance on top.</p>''',
  "Quick sidebar for those coming from the private sector. B2B is simpler: fewer rules, shorter timelines, more room for relationships. Some of you will do both, and the skills overlap more than you'd think. The capture discipline we're about to cover works for B2B too.",
  eyebrow="Quick comparison", title="Government vs. B2B")

section("Part 2", "Revenue strategies: where do you fit?",
  "You know where to look. Now: where do you actually fit in this ecosystem right now? That determines your strategy.")

slide("light", '''
  <div class="stairs">
    <div class="step s1 r"><p class="step-n">Strategy 1</p><h3>Sub under small</h3><p>Start here. Find a small-business prime with the contract, past performance and certifications, and offer your skills as a sub.</p></div>
    <div class="step s2 r"><p class="step-n">Strategy 2</p><h3>Prime with agencies</h3><p>When you have: federal experience, 3+ years of revenue, clearances if needed, strategic partnerships.</p></div>
    <div class="step s3 r"><p class="step-n">Strategy 3 &middot; parallel track</p><h3>Sub under large</h3><p>Large primes need small subs to hit small-business goals (often 23%+). Steady, but a smaller piece of a bigger pie.</p></div>
  </div>
  <p class="takeaway r">Know which strategy you're running <u>right now</u>.</p>''',
  "One of the most important slides in the whole series. A lot of clients want to prime on federal contracts right away. Unless you have past performance and revenue history, that's not where you start. Strategy 1 is where most begin: find a small business that has contracts and past performance and ideally doesn't have your certifications. That's your unicorn partner. Strategy 2 is where you're headed. Strategy 3 is the Lockheed play: large primes have small-business subcontracting goals and need small businesses to team with. Don't run Strategy 2 when you're still in Strategy 1 mode.",
  eyebrow="Part 2 &middot; Revenue strategies", title="Three revenue strategies")

slide("light", '''
  <div class="cols2 wide-left">
    <div>
      <p class="statement r">Early on, certifications are about <em>subcontracting</em>, not priming.</p>
      <div class="chips r"><span>8(a)</span><span>MBE</span><span>EDWOSB</span><span>SDVOSB</span><span>HUBZone</span></div>
    </div>
    <div class="card r">''' + bullets([
        "They make you the partner a prime needs",
        "SDVOSB and some others rarely see large prime awards (mostly VA)",
        "Maryland MBE matters most on state contracts",
        "The SBDC helps with certifications, free",
        "Tedious, not hard"]) + '''</div>
  </div>''',
  "Correct the misconception: certifications are not a golden ticket. What they do is make you attractive as a subcontractor. That unicorn partner is looking for certifications they don't have. Yes, there are 8(a), HUBZone, SDVOSB set-asides. But early on the value is in teaming. Maryland MBE is specifically valuable for state procurements because state contracts carry MBE participation goals. We help with all of this for free.",
  eyebrow="Part 2 &middot; Revenue strategies", title="Certifications = teaming leverage")

checkpoint("Section A", "Where do you fit?",
  "Tap Next to Section A. Which strategy are you running right now, and which one agency or buyer would you focus on first?",
  "Give them two minutes. Ask for one or two volunteers to say their answer out loud or drop it in the Zoom chat. React to one: is that strategy honest for where they are today?")

section("Part 3", "The 36-month capture pipeline",
  "This is the part that changes how you think about government contracting. Here's the real timeline.")

slide("light", '''
  <div class="timeline r">
    <div class="tl-bar">
      <div class="tl-seg a"><b>Positioning &amp; research</b><span>Months 1&ndash;12</span></div>
      <div class="tl-seg b"><b>Capture &amp; teaming</b><span>Months 12&ndash;24</span></div>
      <div class="tl-seg c"><b>Pre-proposal &amp; proposal</b><span>Months 24&ndash;36</span></div>
    </div>
    <div class="tl-rfp"><span>RFP released<br><small>~month 28&ndash;30</small></span></div>
    <div class="tl-award">Award</div>
  </div>
  <p class="statement center r">You will lose if you wait until the RFP is released.</p>''',
  "Let that sink in. Three years. Most clients think they'll find an RFP this week, write the proposal next month and win by the end of the quarter. That's not how this works. Winners start two to three years before the solicitation drops: building relationships, positioning, shaping requirements. By the time the RFP hits the street, the winner is usually already decided in practice. Can you win something you just found? It happens. But the odds are dramatically better when you've been working the pipeline.",
  eyebrow="Part 3 &middot; The pipeline", title="The real timeline: 36 months")

slide("light", '''
  <div class="cols2">
    <div class="stat r"><p class="stat-n">150+</p><p class="stat-l">hours to write your first federal proposal</p></div>
    <div>
      <div class="curve r">
        <div><b>Proposal #1</b><span style="width:100%"></span><em>150+ hrs</em></div>
        <div><b>Proposal #2</b><span style="width:50%"></span><em>about half</em></div>
        <div><b>Proposal #3</b><span style="width:25%"></span><em>about a quarter</em></div>
      </div>
      ''' + bullets(["Processes and templates make every cycle faster",
                     "One agency or customer speeds it up even more",
                     "3 weeks on a proposal you miss the deadline for = lost opportunity"]) + '''
    </div>
  </div>''',
  "The good news: the first one is brutal, 150 hours minimum. But once you've done one you have templates, boilerplate, a reusable compliance matrix, past performance narratives. The second takes half the time, the third a quarter. Pick a lane: don't chase DOD, HHS and the State of Maryland at once. And I've had clients spend three weeks on a proposal and miss the deadline. That's opportunity cost. Go/No-Go later today helps with that.",
  eyebrow="Part 3 &middot; The pipeline", title="The first proposal is the hardest")

slide("light", '''
  <div class="cols2">
    <div class="capstmt r">
      <p class="card-k">Capability statement &middot; one page</p>
      <div class="cs"><div class="cs-h">Company &middot; contact</div><div class="cs-r"><span>Core competencies</span><span>Differentiators</span></div><div class="cs-r"><span>Past performance</span><span>NAICS &middot; certs &middot; UEI/CAGE</span></div></div>
      <p class="fine">Have several versions, one per buyer or NAICS. <b>Pro tip:</b> image-search &ldquo;Capability Statement [your NAICS]&rdquo; for real examples.</p>
    </div>
    <div class="card r"><p class="card-k">Buyers will Google you</p>''' + bullets([
        "No website = you don't exist",
        "No social media = you don't exist",
        "Neglected social media = red flag",
        "It doesn't have to be fancy. It has to exist and look professional."], "checks") + '''</div>
  </div>''',
  "Two things that trip people up. Your cap statement is your one-page resume for government buyers: NAICS codes, certifications, past performance, differentiators, contact info. One page. Beltway firms keep 30 to 60 versions ready to email. The trick: Google image search Capability Statement plus your NAICS code, and study the layouts. Don't copy, study. And yes, government buyers Google you. A 2005 website or a LinkedIn untouched for a year is a problem.",
  eyebrow="Part 3 &middot; The pipeline", title="Your marketing collateral")

section("Part 4", "The six phases of business development",
  "Now the meat of it. Six phases. This is the framework large companies use, and I'll show you how to scale it down.")

slide("light", '''
  <div class="phases">
    <div class="ph pre r"><span>1</span>Long-term positioning</div>
    <div class="ph pre r"><span>2</span>Opportunity assessment</div>
    <div class="ph pre r"><span>3</span>Capture team development</div>
    <div class="ph post r"><span>4</span>Pre-proposal preparation</div>
    <div class="ph post r"><span>5</span>Proposal development</div>
    <div class="ph post r"><span>6</span>Post-submittal activities</div>
  </div>
  <div class="ph-legend r"><span class="pre">Capture &middot; before the RFP</span><span class="post">Proposal &middot; after the RFP</span></div>''',
  "Six phases. Large companies have entire departments for each. You probably don't, and that's okay. What matters is you understand each phase well enough to do a reasonable version at your scale. Don't memorize this. It's in the follow-up.",
  eyebrow="Part 4 &middot; Six phases", title="The business development lifecycle")

slide("light phase", '<div class="phase-tag r">1</div>' + bullets([
    "Identify your strategic markets: where do you want to play?",
    "Assess market direction and upcoming opportunities",
    "Benchmark your capabilities: where are your gaps?",
    "Build strategic alliances: teaming partners, mentors, primes",
    "Set criteria to prioritize (you can't chase everything)",
    "Start marketing: industry days, relationships, get known"], "checks"),
  "The phase most small businesses skip entirely, and arguably the most important. For you this looks like: pick your NAICS codes, pick 2 or 3 agencies, attend their industry days, find the small business liaison officer, start building relationships. Look at who's winning in your space and figure out how you complement them. As soon as I know your constraints, I can move forward. Same here. Pick a lane.",
  eyebrow="Phase 1 &middot; Capture", title="Long-term positioning")

slide("light phase", '''<div class="phase-tag r">2</div>
  <div class="cols2 wide-left">''' + bullets([
    "Gather preliminary customer intelligence",
    "Attend industry briefings and pre-solicitation conferences",
    "Understand basic requirements; identify probable competitors",
    "Early analysis: is this a fit? can you compete?",
    "<b>Make the Bid/No-Bid decision</b>",
    "If Go: assign a capture manager (even if it's you)"]) + '''
    <div class="funnel r"><div>Every opportunity</div><div>Bid / No-Bid filter</div><div>Qualified</div></div>
  </div>''',
  "Phase 2 is where you find a specific opportunity and decide whether to pursue it. Intelligence gathering: who's the incumbent, how long have they held it, estimated value, set-aside, do you have the certs and past performance. Clients who skip this and write the day the RFP drops are how you waste 150 hours.",
  eyebrow="Phase 2 &middot; Capture", title="Opportunity assessment")

slide("light phase", '''<div class="phase-tag r">3</div>
  <div class="cols2">
    <div class="roles r">
      <div><b>Capture manager</b><span>owns the strategy and the win</span></div>
      <div><b>Proposal manager</b><span>owns the document and process</span></div>
      <div><b>Solution architect / SME</b><span>owns the technical approach</span></div>
      <div><b>Pricing strategist</b><span>owns the numbers</span></div>
      <div><b>Business development</b><span>owns the relationship</span></div>
      <p class="fine">In a small business, one person may fill 2 or 3 of these.</p>
    </div>''' + bullets([
    "Establish customer contacts",
    "Gather and analyze program intelligence",
    "Write the capture strategy and plan",
    "Set the bid and proposal budget",
    "Start teaming and subcontractor relationships",
    "Define your winning price"]) + '</div>',
  "In a large company this is 15 to 20 people. For most of you it's 2 or 3, or just you. What matters is the functions get covered. The capture strategy answers: why will the customer pick us? It has to be specific. Not we're the best, but three past performance examples on this exact work, 15% below the incumbent's likely price, a local team that starts day one. This is also when you find the unicorn partner.",
  eyebrow="Phase 3 &middot; Capture", title="Capture team development")

slide("light phase", '''<div class="phase-tag post r">4</div>
  <div class="cols2">''' + bullets([
    "Proposal strategy, tasks, budget and schedule",
    "Work breakdown structure (WBS)",
    "Teaming and subcontractor statements of work",
    "Outline from Sections L and M of the RFP",
    "Reuse what you can from past proposals",
    "Draft the Executive Summary; hold a kickoff"]) + '''
    <div class="keyouts r"><p class="card-k">Key outputs</p><div class="ko">Compliance matrix</div><div class="ko">Storyboards</div><p class="fine">Map Section L (instructions) and Section M (evaluation) before you write a word. Template in Session 3.</p></div>
  </div>''',
  "Now you shift from should we do this to how will we do this. Biggest mistake: people start writing immediately. Don't. Outline first. Map Section L, the preparation instructions, and Section M, the evaluation criteria. Build the compliance matrix. Then write. A storyboard is a one-page visual outline per section: heading, key message, theme, main graphic, supporting points. At minimum, do one for the Executive Summary and the technical approach.",
  eyebrow="Phase 4 &middot; Proposal", title="Pre-proposal preparation")

slide("light phase", '''<div class="phase-tag post r">5</div>
  <div class="colorflow r">
    <div class="cf write">Write</div><i></i>
    <div class="cf pink">Pink team<small>Is the story there?</small></div><i></i>
    <div class="cf write">Revise</div><i></i>
    <div class="cf red">Red team<small>Compliant? Persuasive? Priced right?</small></div><i></i>
    <div class="cf write">Revise</div><i></i>
    <div class="cf gold">Gold team<small>Legal, cost, management sign-off</small></div><i></i>
    <div class="cf submit">Submit</div>
  </div>
  <p class="statement center r">Never submit a proposal that only its writers have read.</p>''',
  "This is where the work happens. Pink team is your first-draft review: does this tell a winning story? Red team is the hard one: bring in someone who hasn't been writing, ideally someone who has evaluated proposals, and let them tear it apart. Gold team is final legal, cost and management sign-off. Small business can combine pink and red. But get at least one external review. Fresh eyes catch what you can't see. More in Session 2 on Wednesday.",
  eyebrow="Phase 5 &middot; Proposal", title="Proposal development")

slide("light phase", '''<div class="phase-tag post r">6</div>
  <div class="cols2 wide-right">''' + bullets([
    "Keep all proposal documentation organized",
    "Answer clarification requests",
    "Orals, demos, discussions",
    "Revalidate pricing if asked",
    "Negotiate if selected",
    "Run lessons learned"]) + '''
    <div class="callout r"><p>Always request a debrief.</p><span>Win or lose.</span></div>
  </div>''',
  "Proposal's in. Don't disband the team: the government may come back with questions or ask for orals. And always ask for a debrief. If you win, it tells you what they liked. If you lose, it tells you exactly why. Clients who take debriefs seriously improve their win rate dramatically. Lessons learned is how 150 hours becomes a fraction of that.",
  eyebrow="Phase 6 &middot; Proposal", title="Post-submittal activities")

section("Part 5", "Go/No-Go: the decision that saves you",
  "One of the most important skills in government contracting: knowing when to walk away.")

slide("light", '''
  <div class="four r">
    <div><b>Customer</b><span>Do you know them? Have you engaged? Do you understand their pain?</span></div>
    <div><b>Competition</b><span>Who else is bidding? Who's the incumbent, and are they happy with them?</span></div>
    <div><b>Capabilities</b><span>Can you do the work? Do you have past performance on this type of contract?</span></div>
    <div><b>Cost</b><span>Can you win on price? Do you understand the pricing structure?</span></div>
  </div>
  <p class="takeaway r">Weak on two or more? Red flag.</p>''',
  "The Four C's: Customer, Competition, Capabilities, Cost. Weak on two or more is a red flag. The one people skip most is Competition. If the incumbent has done the work for 10 years and the customer's happy, your pWin is low unless you bring something genuinely different. The one people overestimate is Capabilities. Similar work is not the same as federal past performance on the same type of contract. Be honest.",
  eyebrow="Part 5 &middot; Go/No-Go", title="Probability of win: the Four C's")

checkpoint("Section B", "Score one opportunity",
  "Section B: name one opportunity you're watching and rate it 1 to 5 on Customer, Competition, Capabilities and Cost. Then make the call: Go or No-Go.",
  "Three minutes. Then ask: who scored themselves below 3 on two or more? That's the conversation. Anyone without an opportunity yet: score the buyer you named in Section A.")

slide("light", '''
  <div class="gng">
    <div class="no r"><h3>No-Go if you</h3>''' + bullets([
        "Lack expertise in the work",
        "Have a business or ethical conflict",
        "Would stretch resources too thin",
        "Don't believe it's real or attainable",
        "Don't have time for an <em>excellent</em> proposal"]) + '''</div>
    <div class="go r"><h3>Go if you</h3>''' + bullets([
        "Have expertise in the work",
        "Have resources to perform",
        "Have time for an excellent proposal",
        "Can submit a letter of intent if required"]) + '''</div>
  </div>
  <p class="takeaway r">Weigh probability of win, cost to propose, and estimated profit.</p>''',
  "Be selective. It feels counterintuitive when you're breaking in, but chasing everything is how you burn out and win nothing. The best contractors might look at 50 and bid 5. No-Go is as important as Go. If you don't have time for an excellent proposal, not a good one, that's a No-Go. Protect the work you have while pursuing new work.",
  eyebrow="Part 5 &middot; Go/No-Go", title="Be selective")

slide("light", '''
  <div class="split r">
    <div class="half cap"><p>Phases 1&ndash;3</p><h3>Capture</h3><span>Everything before the RFP</span></div>
    <div class="divider"><span>RFP</span></div>
    <div class="half prop"><p>Phases 4&ndash;6</p><h3>Proposal</h3><span>Everything after</span></div>
  </div>
  <p class="statement center r">Most small businesses only do proposal. Consistent winners do both.</p>''',
  "Credit where it's due: the six phases are adapted from the Shipley process, the industry standard. If you want to go deeper, Shipley's materials are excellent. The key takeaway ties back to the 36-month pipeline. Capture is everything before the RFP drops. Proposal is everything after. Stop being reactive. Start being proactive.",
  eyebrow="Industry standard &middot; Shipley", title="Capture before, proposal after")

slide("light", '''
  <div class="tiles">
    <div class="r"><span>1</span><b>Look beyond SAM.gov</b>State, county and city have lower barriers</div>
    <div class="r"><span>2</span><b>Know your strategy</b>Subbing, priming, or both. Be honest.</div>
    <div class="r"><span>3</span><b>Think in 36 months</b>Winners start years before the RFP</div>
    <div class="r"><span>4</span><b>Build templates now</b>The first proposal is the hardest</div>
    <div class="r"><span>5</span><b>Be selective</b>Not every opportunity is yours</div>
    <div class="r"><span>6</span><b>Always debrief</b>Win or lose</div>
  </div>''',
  "Six things. If you remember nothing else: think in 36-month cycles, know your revenue strategy, and be selective.",
  eyebrow="Today", title="What to remember")

slide("light", f'''
  <div class="cols2">
    <div class="card r"><p class="card-k">Wednesday, Sept 30 &middot; 10:00 a.m. &middot; Session 2</p>
      <h3 class="next-h">Team roles &amp; responsibilities</h3>''' + bullets([
        "Who does what on a proposal team",
        "Scaling roles when you're one to three people",
        "Running color team reviews",
        "When to bring in outside help"]) + f'''</div>
    <div class="submit-card r">
      <p class="eyebrow light">Worksheet &middot; Section C</p>
      <h3>Write your one step, then submit.</h3>
      <p>Your inbox gets: this deck with notes, the capture management template, and links to SAM.gov, eMMA, county portals and forecasts.</p>
      <div class="mini-qr">{QR_FORM}</div>
    </div>
  </div>''',
  "Wednesday: team roles. If you're thinking I don't have a team, that's fine, we cover one- to three-person operations. Now: Section C, write the one capture step you'll take this month, tick what you want, then the last page and Submit. That's what triggers the follow-up with the deck, the capture template and all the links. Throw it into NotebookLM and ask it questions.",
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


# ============================ RENDER ============================

CSS = r"""
/* === THEME: Maryland SBDC design system tokens (colors.css / typography.css / spacing.css) === */
:root{
  --sbdc-red:#d11142; --sbdc-blue:#002d62; --sbdc-gray:#adafb2;
  --red-50:#fceef2; --red-100:#f8d3dd; --red-200:#f0a3b7; --red-600:#b00d38; --red-700:#8c0a2c;
  --blue-50:#e8eef5; --blue-100:#c6d4e6; --blue-200:#8ea9cc; --blue-300:#4f7aad; --blue-400:#1f5290;
  --blue-600:#002752; --blue-700:#001e40; --blue-800:#00162e; --blue-900:#000d1c;
  --n-50:#f7f8f9; --n-100:#eef0f2; --n-200:#e2e4e7; --n-300:#cdd0d4; --n-500:#8b8e92; --n-600:#6a6d71; --n-800:#313438;
  --success:#1f7a4d; --gold:#c9821a;
  --font-display:'Archivo','Helvetica Neue',Arial,sans-serif;
  --font-body:Arial,'Helvetica Neue',Helvetica,sans-serif;
  --ease:cubic-bezier(0.22,0.61,0.36,1);
  --stage-bg:#000d1c; --slide-bg:#ffffff;
}
*{margin:0;padding:0;box-sizing:border-box}
"""

CSS += VIEWPORT_BASE

CSS += r"""
/* === SLIDE FRAME: 120px side margins, blue footer band with page number === */
.slide{font-family:var(--font-body);color:var(--n-800)}
.frame{position:absolute;inset:88px 120px 150px 120px}
.foot{position:absolute;left:0;right:0;bottom:0;height:72px;background:var(--sbdc-blue);display:flex;align-items:center;justify-content:space-between;padding:0 120px;color:#fff;font:700 20px/1 var(--font-display);letter-spacing:.12em;text-transform:uppercase}
.foot .pg{color:var(--blue-200);font-variant-numeric:tabular-nums}
.foot .band-mini{background:var(--sbdc-red);padding:8px 14px}
.dark .foot{display:none}

/* === TYPE: heavy Archivo display, red eyebrow + 4px accent rule (SectionHeader motif) === */
.eyebrow{font:700 24px/1.2 var(--font-display);letter-spacing:.12em;text-transform:uppercase;color:var(--sbdc-red);margin-bottom:18px}
.eyebrow.light{color:var(--red-200)}
h2{font:900 76px/1.05 var(--font-display);letter-spacing:-.02em;color:var(--sbdc-blue)}
.rule{width:96px;height:6px;background:var(--sbdc-red);margin:26px 0 48px}
h3{font:800 40px/1.15 var(--font-display);color:var(--sbdc-blue);letter-spacing:-.01em}
.list{list-style:none;display:flex;flex-direction:column;gap:22px;font-size:34px;line-height:1.35}
.list li{padding-left:40px;position:relative}
.list li::before{content:"";position:absolute;left:0;top:.5em;width:16px;height:16px;background:var(--sbdc-red)}
.list.checks li::before{width:22px;height:12px;background:none;border:solid var(--success);border-width:0 0 5px 5px;transform:rotate(-45deg);top:.3em}
.takeaway{position:absolute;bottom:0;left:0;font:800 38px/1.2 var(--font-display);color:var(--sbdc-blue);border-left:8px solid var(--sbdc-red);padding:6px 0 6px 28px}
.statement{font:800 52px/1.2 var(--font-display);color:var(--sbdc-blue);letter-spacing:-.01em}
.statement em{font-style:normal;color:var(--sbdc-red)}
.statement.center{position:absolute;bottom:0;left:0;right:0;text-align:center;font-size:46px}
.fine{font-size:24px;line-height:1.45;color:var(--n-600);margin-top:22px}
.card{background:#fff;border:1px solid var(--n-200);border-top:6px solid var(--sbdc-blue);border-radius:10px;padding:40px 44px;box-shadow:0 4px 12px rgba(0,45,98,.10),0 2px 4px rgba(0,45,98,.06)}
.card.accent{border-top-color:var(--sbdc-red);background:var(--red-50)}
.card-k{font:700 22px/1.2 var(--font-display);letter-spacing:.12em;text-transform:uppercase;color:var(--n-600);margin-bottom:22px}
.cols2{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start}
.cols2.wide-left{grid-template-columns:1.25fr 1fr}
.cols2.wide-right{grid-template-columns:1fr 1.1fr;align-items:center}

/* === DARK SLIDES: title, sections, checkpoints, close — navy ground, red MARYLAND band === */
.dark{--slide-bg:var(--blue-800);background:radial-gradient(ellipse at 85% 10%,rgba(31,82,144,.55),transparent 55%),linear-gradient(160deg,var(--sbdc-blue),var(--blue-800) 70%);color:#fff}
.dark h1{font:900 124px/1.0 var(--font-display);letter-spacing:-.025em;color:#fff}
.band{width:360px;height:22px;background:var(--sbdc-red);margin:40px 0}
.logo{position:absolute;top:80px;left:120px;width:300px}
.title .frame{inset:0}
.title-grid{position:absolute;left:120px;right:120px;bottom:120px;display:grid;grid-template-columns:1fr 340px;gap:80px;align-items:end}
.byline{font:600 34px/1.45 var(--font-display);color:var(--blue-100)}
.byline.small{font:500 24px/1.4 var(--font-body);color:var(--blue-200);margin-top:22px}
.qr-card{background:#fff;border-radius:10px;padding:22px;display:flex;flex-direction:column;align-items:center;gap:12px;box-shadow:0 12px 28px rgba(0,0,0,.35)}
.qr-card svg{width:100%;height:auto;display:block}
.qr-card svg path{fill:var(--blue-800)}
.qr-card span{font:800 20px/1.2 var(--font-display);color:var(--sbdc-blue);text-align:center;letter-spacing:.02em}
.close .title-grid{bottom:210px}
.sba{position:absolute;left:120px;right:120px;bottom:56px;font-size:17px;line-height:1.45;color:var(--blue-200)}
.section .frame{display:flex;flex-direction:column;justify-content:center;inset:0 120px}
.sec-num{font:700 30px/1 var(--font-display);letter-spacing:.2em;text-transform:uppercase;color:var(--red-200);margin-bottom:30px}
.section h1{max-width:1500px}
.checkpoint .frame{inset:0 120px;display:flex;align-items:center}
.cp-grid{display:grid;grid-template-columns:1fr 420px;gap:110px;align-items:center;width:100%}
.checkpoint h1{font-size:104px}
.lead{font:500 36px/1.45 var(--font-body);color:var(--blue-100);margin-top:36px;max-width:1100px}
.url{font:800 34px/1 var(--font-display);color:#fff;margin-top:44px;letter-spacing:.01em}
.url.ink{color:var(--sbdc-blue)}

/* === SCAN SLIDE === */
.scan-grid{display:grid;grid-template-columns:1fr 520px;gap:110px;align-items:start}
.steps{list-style:none;counter-reset:s;display:flex;flex-direction:column;gap:30px}
.steps li{counter-increment:s;font-size:36px;line-height:1.35;padding-left:86px;position:relative}
.steps li::before{content:counter(s);position:absolute;left:0;top:-4px;width:58px;height:58px;background:var(--sbdc-red);color:#fff;font:900 32px/58px var(--font-display);text-align:center}
.steps b{color:var(--sbdc-blue)}
.qr-card.big{border:2px solid var(--n-200);box-shadow:0 12px 28px rgba(0,45,98,.14);margin-top:-80px}

/* === AGENDA === */
.agenda{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:28px 80px}
.agenda li{font:700 40px/1.2 var(--font-display);color:var(--sbdc-blue);display:flex;gap:28px;align-items:baseline;border-bottom:1px solid var(--n-200);padding-bottom:24px}
.agenda span{font-size:28px;color:var(--sbdc-red);letter-spacing:.08em}

/* === TIERS (where to look) === */
.tiers{display:flex;flex-direction:column;align-items:center;gap:14px}
.tier{display:grid;grid-template-columns:380px 1fr 150px;gap:30px;align-items:center;padding:30px 44px;color:#fff;font-size:28px;line-height:1.3}
.tier b{font:900 44px/1 var(--font-display)}
.tier em{font:800 30px/1 var(--font-display);font-style:normal;text-align:right;color:var(--red-100)}
.t1{width:72%;background:var(--sbdc-blue)} .t2{width:86%;background:var(--blue-400)} .t3{width:100%;background:var(--blue-300)}
.t1 em{font-size:26px}
.also{margin-top:40px;font-size:28px;line-height:1.45;background:var(--n-50);border-left:6px solid var(--sbdc-red);padding:22px 30px}
.also b{color:var(--sbdc-blue)}
.buy{display:grid;grid-template-columns:230px 1fr;gap:22px 24px;font-size:28px;line-height:1.4}
.buy dt{font:800 30px/1.3 var(--font-display);color:var(--sbdc-blue)}
.big-line{font:900 64px/1.05 var(--font-display);color:var(--sbdc-red);margin-bottom:22px}
.card.accent p:not(.card-k):not(.big-line){font-size:30px;line-height:1.45}

/* === COMPARE TABLE === */
.compare{width:100%;border-collapse:collapse;font-size:32px}
.compare th{font:800 34px/1 var(--font-display);color:#fff;background:var(--sbdc-blue);text-align:left;padding:24px 30px}
.compare th:first-child{background:none}
.compare td{padding:22px 30px;border-bottom:1px solid var(--n-200)}
.compare td:first-child{font:800 30px/1 var(--font-display);color:var(--sbdc-blue);width:300px}

/* === STRATEGY STAIRS === */
.stairs{display:grid;grid-template-columns:1fr 1fr 1fr;gap:32px;align-items:end;height:520px}
.step{padding:36px 36px 40px;color:#fff;display:flex;flex-direction:column;gap:16px}
.step h3{color:#fff;font-size:44px}
.step p{font-size:26px;line-height:1.4}
.step-n{font:700 20px/1 var(--font-display)!important;letter-spacing:.14em;text-transform:uppercase;opacity:.8}
.s1{height:62%;background:var(--sbdc-red)} .s2{height:100%;background:var(--sbdc-blue)} .s3{height:78%;background:var(--blue-300);border:4px dashed var(--blue-100)}
.chips{display:flex;flex-wrap:wrap;gap:16px;margin-top:48px}
.chips span{font:900 34px/1 var(--font-display);color:var(--sbdc-blue);border:3px solid var(--sbdc-blue);padding:16px 24px;border-radius:3px}

/* === 36-MONTH TIMELINE === */
.timeline{position:relative;height:330px;margin-top:10px}
.tl-bar{display:grid;grid-template-columns:1fr 1fr 1fr;height:150px;margin-right:150px}
.tl-seg{padding:26px 30px;color:#fff;display:flex;flex-direction:column;justify-content:space-between}
.tl-seg b{font:800 34px/1.1 var(--font-display)} .tl-seg span{font-size:24px;opacity:.85}
.tl-seg.a{background:var(--blue-300)} .tl-seg.b{background:var(--blue-400)} .tl-seg.c{background:var(--sbdc-blue)}
.tl-rfp{position:absolute;top:150px;height:40px;left:calc((100% - 150px) * 0.8);border-left:6px solid var(--sbdc-red)}
.tl-rfp span{position:absolute;top:40px;left:-6px;background:var(--sbdc-red);color:#fff;font:900 30px/1.1 var(--font-display);padding:16px 22px;white-space:nowrap}
.tl-rfp small{font:500 20px/1 var(--font-body)}
.tl-award{position:absolute;right:0;top:0;width:150px;height:150px;background:var(--success);color:#fff;font:900 32px/150px var(--font-display);text-align:center}

/* === STAT + CURVE === */
.stat-n{font:900 300px/0.9 var(--font-display);color:var(--sbdc-red);letter-spacing:-.04em}
.stat-l{font:800 44px/1.2 var(--font-display);color:var(--sbdc-blue);margin-top:24px;max-width:680px}
.curve{display:flex;flex-direction:column;gap:16px;margin-bottom:44px}
.curve div{display:grid;grid-template-columns:220px 1fr 200px;align-items:center;gap:20px;font-size:26px}
.curve b{font:800 26px/1 var(--font-display);color:var(--sbdc-blue)}
.curve span{height:34px;background:var(--sbdc-blue);display:block}
.curve em{font-style:normal;color:var(--n-600)}

/* === CAPABILITY STATEMENT MOCK === */
.cs{border:2px solid var(--sbdc-blue);border-radius:6px;overflow:hidden}
.cs-h{background:var(--sbdc-blue);color:#fff;font:800 28px/1 var(--font-display);padding:22px 26px}
.cs-r{display:grid;grid-template-columns:1fr 1fr}
.cs-r span{padding:30px 26px;font:700 26px/1.2 var(--font-display);color:var(--sbdc-blue);border-top:1px solid var(--n-200)}
.cs-r span:first-child{border-right:1px solid var(--n-200)}

/* === SIX PHASES === */
.phases{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-top:40px}
.ph{height:300px;padding:34px 28px;color:#fff;font:800 32px/1.15 var(--font-display);display:flex;flex-direction:column;gap:22px;clip-path:polygon(0 0,88% 0,100% 50%,88% 100%,0 100%,12% 50%)}
.ph:first-child{clip-path:polygon(0 0,88% 0,100% 50%,88% 100%,0 100%)}
.ph{padding-left:48px;padding-right:44px}
.ph span{font-size:64px;font-weight:900;opacity:.9}
.ph.pre{background:var(--sbdc-blue)} .ph.post{background:var(--sbdc-red)}
.ph-legend{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:34px}
.ph-legend span{font:800 30px/1 var(--font-display);padding-top:22px;border-top:8px solid}
.ph-legend .pre{color:var(--sbdc-blue);border-color:var(--sbdc-blue)} .ph-legend .post{color:var(--sbdc-red);border-color:var(--sbdc-red)}
.phase-tag{position:absolute;right:0;top:-40px;font:900 260px/1 var(--font-display);color:var(--blue-50);z-index:-1}
.phase-tag.post{color:var(--red-50)}
.funnel{display:flex;flex-direction:column;align-items:center;gap:10px;margin-top:10px}
.funnel div{color:#fff;font:800 30px/1 var(--font-display);padding:34px 0;text-align:center}
.funnel div:nth-child(1){width:100%;background:var(--blue-300)} .funnel div:nth-child(2){width:78%;background:var(--sbdc-red)} .funnel div:nth-child(3){width:52%;background:var(--sbdc-blue)}
.roles{display:flex;flex-direction:column;gap:12px}
.roles div{display:grid;grid-template-columns:340px 1fr;align-items:center;padding:18px 24px;background:var(--blue-50);border-left:6px solid var(--sbdc-blue);font-size:25px}
.roles b{font:800 27px/1.2 var(--font-display);color:var(--sbdc-blue)}
.keyouts .ko{font:900 46px/1 var(--font-display);color:#fff;background:var(--sbdc-red);padding:30px 34px;margin-bottom:14px}

/* === COLOR TEAM FLOW === */
.colorflow{display:flex;align-items:stretch;gap:0;margin-top:40px}
.colorflow i{width:34px;flex:0 0 34px;background:linear-gradient(90deg,transparent 45%,var(--n-300) 45% 55%,transparent 55%) center/100% 6px no-repeat;display:block}
.cf{flex:1;min-height:250px;padding:28px 22px;font:900 34px/1.1 var(--font-display);display:flex;flex-direction:column;gap:14px;justify-content:center;text-align:center}
.cf small{font:500 21px/1.35 var(--font-body)}
.cf.write{background:var(--n-100);color:var(--sbdc-blue);flex:.7}
.cf.pink{background:var(--red-200);color:var(--red-700)} .cf.red{background:var(--sbdc-red);color:#fff} .cf.gold{background:var(--gold);color:#fff}
.cf.submit{background:var(--sbdc-blue);color:#fff;flex:.8}

.callout{background:var(--sbdc-red);color:#fff;padding:70px 60px}
.callout p{font:900 80px/1.02 var(--font-display);letter-spacing:-.02em}
.callout span{display:block;font:800 44px/1 var(--font-display);margin-top:24px;color:var(--red-100)}

/* === FOUR C's, GO/NO-GO, SPLIT, TILES === */
.four{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.four div{border:2px solid var(--n-200);border-top:8px solid var(--sbdc-blue);padding:34px 40px;display:flex;flex-direction:column;gap:14px}
.four b{font:900 50px/1 var(--font-display);color:var(--sbdc-blue)}
.four b::first-letter{color:var(--sbdc-red)}
.four span{font-size:29px;line-height:1.4}
.gng{display:grid;grid-template-columns:1fr 1fr;gap:44px}
.gng>div{padding:40px 46px}
.gng h3{margin-bottom:28px;font-size:46px}
.gng .list{font-size:30px;gap:18px}
.no{background:var(--red-50);border-top:8px solid var(--sbdc-red)} .no h3{color:var(--red-700)}
.go{background:#e9f4ee;border-top:8px solid var(--success)} .go h3{color:var(--success)}
.go .list li::before{background:var(--success)}
.split{display:grid;grid-template-columns:1fr 120px 1fr;height:470px}
.half{padding:60px;color:#fff;display:flex;flex-direction:column;justify-content:flex-end;gap:14px}
.half p{font:700 24px/1 var(--font-display);letter-spacing:.14em;text-transform:uppercase;opacity:.8}
.half h3{color:#fff;font-size:104px;font-weight:900;letter-spacing:-.02em}
.half span{font-size:32px}
.cap{background:var(--sbdc-blue)} .prop{background:var(--sbdc-red)}
.divider{position:relative;background:linear-gradient(90deg,var(--sbdc-blue) 50%,var(--sbdc-red) 50%)}
.divider span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:#fff;color:var(--sbdc-blue);font:900 34px/1 var(--font-display);padding:26px 18px;border:4px solid var(--sbdc-blue)}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.tiles div{border:1px solid var(--n-200);border-top:6px solid var(--sbdc-red);padding:34px 36px 38px;font-size:26px;line-height:1.4;color:var(--n-600);min-height:250px;box-shadow:0 1px 3px rgba(0,45,98,.08)}
.tiles span{font:900 60px/1 var(--font-display);color:var(--blue-100);display:block;margin-bottom:10px}
.tiles b{display:block;font:800 36px/1.15 var(--font-display);color:var(--sbdc-blue);margin-bottom:10px}
.next-h{font-size:52px;margin-bottom:34px}
.submit-card{background:var(--sbdc-blue);color:#fff;padding:44px 48px;position:relative;min-height:540px}
.submit-card h3{color:#fff;font-size:50px;max-width:560px}
.submit-card p:not(.eyebrow){font-size:28px;line-height:1.45;color:var(--blue-100);margin-top:22px;max-width:430px}
.mini-qr{position:absolute;right:40px;bottom:40px;width:200px;background:#fff;padding:12px;border-radius:6px}
.mini-qr svg{width:100%;height:auto;display:block} .mini-qr svg path{fill:var(--blue-800)}

/* === MOTION: quick fade + rise, 60ms stagger (design system: 120–320ms, no bounce) === */
.r{opacity:0;transform:translateY(18px);transition:opacity 320ms var(--ease),transform 320ms var(--ease)}
.slide.visible .r{opacity:1;transform:none}
.slide.visible .r:nth-child(2){transition-delay:60ms} .slide.visible .r:nth-child(3){transition-delay:120ms}
.slide.visible .r:nth-child(4){transition-delay:180ms} .slide.visible .r:nth-child(5){transition-delay:240ms}
.slide.visible .r:nth-child(6){transition-delay:300ms} .slide.visible .r:nth-child(7){transition-delay:360ms}
@media print{.r{opacity:1!important;transform:none!important}}

/* === PROGRESSIVE REVEAL: .f elements wait for the next click; .on shows them (JS assigns both) === */
.slide .f:not(.on){opacity:0!important;transform:translateY(14px)!important}
.slide.visible .f.on{transition-delay:0s!important}
@media print{.slide .f:not(.on),.slide .f.on{opacity:1!important;transform:none!important}}
@page{size:1920px 1080px;margin:0}
@media print{.progress,.hint{display:none!important}}

/* === PRESENTATION CHROME (outside the stage) === */
.progress{position:fixed;left:0;top:0;height:4px;background:var(--sbdc-red);z-index:1000;transition:width 200ms var(--ease)}
.hint{position:fixed;right:16px;bottom:12px;font:600 13px/1 var(--font-display);color:rgba(255,255,255,.35);z-index:1000;letter-spacing:.04em}
"""

JS = r"""
/* === SLIDE CONTROLLER: arrows/space/PageUp/PageDown/Home/End, click, swipe, wheel.
       F = fullscreen. P = presenter window with notes, timer, next slide (share only the deck window in Zoom). === */
class Deck{
  constructor(){
    this.slides=[...document.querySelectorAll('.slide')];
    this.stage=document.getElementById('deckStage');
    this.bar=document.getElementById('progress');
    this.i=Math.min(parseInt(location.hash.slice(1)||'1',10)-1||0,this.slides.length-1);
    this.t0=null; this.pw=null; this.k=0;
    // Progressive reveal: every leaf matching STEPS on a light slide becomes one click. Dark slides and the scan slide show at once.
    const STEPS='.list>li,.tier,.also,.step,.four>div,.tiles>div,.ph,.ph-legend,.roles>div,.funnel>div,.colorflow>.cf,.gng>div,.half,.tl-seg,.tl-rfp,.tl-award,.takeaway,.statement,.stat,.curve>div,.agenda>li,.compare tbody tr,.ko,.callout,.chips,.cols2>*,.capstmt,.submit-card';
    this.frags=this.slides.map(s=>{
      if(s.classList.contains('dark')||s.classList.contains('scan'))return [];
      const c=[...s.querySelector('.frame').querySelectorAll(STEPS)];
      const leaves=c.filter(el=>!c.some(o=>o!==el&&el.contains(o)));
      leaves.forEach(el=>el.classList.add('f'));
      return leaves;
    });
    const fit=()=>{const f=Math.min(innerWidth/1920,innerHeight/1080);
      this.stage.style.transform=`translate(${(innerWidth-1920*f)/2}px,${(innerHeight-1080*f)/2}px) scale(${f})`;};
    fit(); addEventListener('resize',fit);
    addEventListener('keydown',e=>this.key(e));
    let x0=null; addEventListener('touchstart',e=>x0=e.touches[0].clientX,{passive:true});
    addEventListener('touchend',e=>{if(x0===null)return;const dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)(dx<0?this.next():this.prev());x0=null;});
    let lock=0; addEventListener('wheel',e=>{const n=Date.now();if(n-lock<600||Math.abs(e.deltaY)<20)return;lock=n;e.deltaY>0?this.next():this.prev();},{passive:true});
    this.show();
  }
  key(e){
    const k=e.key;
    if(['ArrowRight','ArrowDown',' ','PageDown','Enter'].includes(k)){e.preventDefault();this.next();}
    else if(['ArrowLeft','ArrowUp','PageUp','Backspace'].includes(k)){e.preventDefault();this.prev();}
    else if(k==='Home')this.go(0); else if(k==='End')this.go(this.slides.length-1);
    else if(k==='f'||k==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}
    else if(k==='p'||k==='P')this.presenter();
  }
  next(){const fr=this.frags[this.i];if(this.k<fr.length){fr[this.k++].classList.add('on');this.renderPresenter();}else if(this.i<this.slides.length-1)this.go(this.i+1);}
  prev(){if(this.i>0)this.go(this.i-1,true);}  // going back lands on the fully built slide
  go(n,full=false){this.i=Math.max(0,Math.min(n,this.slides.length-1));const fr=this.frags[this.i];this.k=full?fr.length:0;fr.forEach((el,j)=>el.classList.toggle('on',j<this.k));this.show();}
  show(){
    this.slides.forEach((s,j)=>{s.classList.toggle('active',j===this.i);s.classList.toggle('visible',j===this.i);});
    this.bar.style.width=((this.i+1)/this.slides.length*100)+'%';
    history.replaceState(null,'','#'+(this.i+1));
    this.renderPresenter();
  }
  presenter(){
    if(this.pw&&!this.pw.closed){this.pw.focus();return;}
    this.pw=open('','sbdc-presenter','width=960,height=720');
    if(!this.pw)return;
    this.t0=this.t0||Date.now();
    const d=this.pw.document;
    d.title='Presenter notes';
    d.body.style.cssText='margin:0;font:22px/1.5 Arial,sans-serif;background:#00162e;color:#fff;padding:28px 34px';
    d.body.innerHTML='<div id="h" style="font:700 16px Archivo,Arial;letter-spacing:.1em;text-transform:uppercase;color:#8ea9cc;display:flex;justify-content:space-between"><span id="n"></span><span id="t"></span></div><h2 id="ti" style="font:800 34px/1.15 Arial;margin:14px 0 18px"></h2><div id="no" style="font-size:26px;line-height:1.55"></div><p id="nx" style="margin-top:28px;color:#8ea9cc;font-size:18px"></p><p style="color:#4f7aad;font-size:14px;margin-top:24px">Arrow keys work here too.</p>';
    d.addEventListener('keydown',e=>this.key(e));
    setInterval(()=>{if(this.pw.closed)return;const s=Math.floor((Date.now()-this.t0)/1000);this.pw.document.getElementById('t').textContent=Math.floor(s/60)+':'+String(s%60).padStart(2,'0')+' elapsed';},1000);
    this.renderPresenter();
  }
  renderPresenter(){
    if(!this.pw||this.pw.closed)return;
    const d=this.pw.document,s=this.slides[this.i],nx=this.slides[this.i+1];
    const fr=this.frags[this.i];d.getElementById('n').textContent='Slide '+(this.i+1)+' of '+this.slides.length+(fr.length?' · step '+this.k+' of '+fr.length:'');
    d.getElementById('ti').textContent=s.dataset.title;
    d.getElementById('no').textContent=s.querySelector('.notes').textContent;
    d.getElementById('nx').textContent=nx?'Next: '+nx.dataset.title:'Last slide';
  }
}
new Deck();
"""

parts = []
n = len(SLIDES)
for i, (kind, body, notes, title) in enumerate(SLIDES, 1):
    foot = f'<div class="foot"><span class="band-mini">Maryland SBDC</span><span>Session 1 &middot; Business Development Lifecycle</span><span class="pg">{i:02d} / {n:02d}</span></div>'
    parts.append(
        f'<section class="slide {kind}" data-title="{html.escape(title)}" aria-label="Slide {i}: {html.escape(title)}">\n'
        f'  <div class="frame">{body}</div>{foot}\n'
        f'  <aside class="notes" hidden>{html.escape(notes)}</aside>\n'
        f'  <!-- NOTES: {html.escape(notes)} -->\n</section>')

doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Business Development Lifecycle</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="progress" id="progress"></div>
<div class="deck-viewport">
<main class="deck-stage" id="deckStage">
{chr(10).join(parts)}
</main>
</div>
<div class="hint">&larr; &rarr; move &middot; F fullscreen &middot; P notes</div>
<script>{JS}</script>
</body>
</html>"""

OUT.write_text(doc, encoding="utf-8")
print(f"{OUT.name}: {n} slides, {len(doc)//1024} KB, form -> {FORM_URL}")
