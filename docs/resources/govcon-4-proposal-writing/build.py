# Session 4 class file (copied from the sbdc-workshops session1_example.py). Build:  py build.py  (run from this folder)
import pathlib, sys
sys.path.insert(0, str(pathlib.Path.home() / ".claude" / "skills" / "sbdc-workshops" / "scripts" / "deck"))
import engine
engine.setup("[YOUR-FORM-URL]")
from engine import *

# Running example: the Session 3 practice RFQ (USACE Baltimore W912DR26QA051, janitorial, Total SB, LPTA).
# Sentences marked "example" are illustrative, written for class; they are not from any real proposal.

# ============================ SLIDES ============================

slide("dark title", f'''
  <img class="logo r" alt="America's SBDC Maryland" src="data:image/png;base64,{LOGO}">
  <div class="title-grid">
    <div>
      <p class="eyebrow light r">Winning That Government Contracting Award &middot; Session 4 of 4</p>
      <h1 class="r">Basics of Proposal Writing</h1>
      <div class="band r"></div>
      <p class="byline r">Your Name &middot; Maryland Small Business Development Center<br>Monday, October 5, 2026</p>
    </div>
    <div class="qr-card r">{QR_FORM}<span>Scan now: your worksheet</span></div>
  </div>''',
  "Welcome to our last session. We've covered the lifecycle, the team, and how to read an RFP. Today we write. This is where small businesses either stand out or blend into the pile. I'll give you a framework for proposals that are compliant, correct and compelling, and the specific techniques that make evaluators pay attention. We'll keep using Friday's Army Corps janitorial RFQ, so the whole series ends on one story. Scan the code: that's today's worksheet. Fill in page 1, keep the tab open, and don't hit Submit until the last slide.", label="Title")

slide("light scan", f'''
  <div class="scan-grid">
    <div>
      <ol class="steps">
        <li class="r"><b>Point your phone camera at the code.</b> Or click the link in the Zoom chat.</li>
        <li class="r"><b>Fill in page 1 now.</b> Name, email, business, where you are today.</li>
        <li class="r"><b>Keep the tab open.</b> Today you write two real sentences in it.</li>
      </ol>
      <p class="url ink r">{FORM_LABEL}</p>
      <p class="fine r">Don't hit Submit until the last slide. When you do, the slides and a proposal-writing checklist land in your inbox.</p>
    </div>
    <div class="qr-card big r">{QR_FORM}</div>
  </div>''',
  "Ninety seconds. New worksheet, so everyone scans again. Today's worksheet is where you'll actually write: one feature-benefit sentence and one win theme for your own business. Repeat: don't hit Submit until the last slide.",
  eyebrow="Before we start", title="Scan your worksheet")

slide("light", '''
  <ol class="agenda">
    <li class="r"><span>01</span>The blank page problem</li>
    <li class="r"><span>02</span>Compliant, correct, compelling</li>
    <li class="r"><span>03</span>Features and benefits</li>
    <li class="r"><span>04</span>Themes, discriminators, ghosting</li>
    <li class="r"><span>05</span>Customer focus and the evaluator's job</li>
    <li class="r"><span>06</span>Writing mechanics and graphics</li>
  </ol>''',
  "The roadmap. First the practical problem: you're assigned a section and staring at a blank page. Then the framework: compliance, features and benefits, themes, customer focus, clean writing. We finish with graphics, because a good graphic can do more than a page of text. Everything connects back to Friday's compliance matrix. The matrix tells you what to write. Today is how to write it well.",
  eyebrow="Today", title="What we're covering")

section("Part 1", "The blank page problem",
  "You've been assigned a section. Now what?")

slide("light", '''
  <div class="four r">
    <div><b>Last proposal</b><span>Written for a different customer and different criteria. Evaluators can tell.</span></div>
    <div><b>Marketing copy</b><span>"World-class solutions provider" scores zero points.</span></div>
    <div><b>Technical manual</b><span>Everything you know, none of it tied to how they score.</span></div>
    <div><b>The compliance matrix</b><span>Start here: the requirement, where it goes, how it's scored.</span></div>
  </div>
  <p class="takeaway r">Start from the matrix row, not a blank page.</p>''',
  "Three instincts, all wrong as a starting point. Pulling from your last proposal: it was written for a different customer, RFP and criteria, and if you don't tailor it, evaluators notice. Marketing copy is worse: it's written to sound impressive, proposal copy is written to score. The technical manual is the subject-matter expert's trap: ten pages of methodology that never connects to the evaluation criteria. So start with the compliance matrix. Pull up your row: what's the requirement, where does Section L say it goes, what does Section M score? Now you know what to write and how it's graded.",
  eyebrow="Part 1 &middot; Where to start", title="Three wrong starts, one right one")

section("Part 2", "Compliant, correct, compelling",
  "Every winning proposal clears three bars, in this order.")

slide("light", '''
  <div class="stairs">
    <div class="step s1 r"><p class="step-n">Bar 1</p><h3>Compliant</h3><p>You followed every instruction and answered every requirement. Miss it and you can be eliminated before anyone reads your best work.</p></div>
    <div class="step s2 r"><p class="step-n">Bar 2</p><h3>Correct</h3><p>Your solution works, your staffing makes sense, your numbers add up. This gets you to "Acceptable."</p></div>
    <div class="step s3 r"><p class="step-n">Bar 3</p><h3>Compelling</h3><p>Clear themes, quantified benefits, customer focus. This is what moves you from "Acceptable" to "Outstanding."</p></div>
  </div>
  <p class="takeaway r">On an LPTA buy like Friday's, bars 1 and 2 are the whole game.</p>''',
  "Think of it as stairs. Compliance is the base: wrong font, blown page limit, missed requirement, and nothing else matters. Correct is the next step: the solution works and the numbers add up; that's Acceptable. Compelling is what wins on a best-value buy: the evaluator thinks, these people get our problem. One nuance from Friday: our janitorial RFQ was LPTA. Technical was pass or fail, so there was no extra credit for compelling; being clearly, completely acceptable and then priced right was the whole game. On best-value buys, compelling is where you win. Most small businesses reach compliant and correct. The gap is compelling, and that's the rest of today.",
  eyebrow="Part 2 &middot; Three bars", title="Compliant &rarr; correct &rarr; compelling")

section("Part 3", "Features and benefits",
  "The foundation of compelling writing is the difference between a feature and a benefit.")

slide("light", '''
  <table class="compare r">
    <thead><tr><th>Feature: what you have</th><th>Benefit: what the customer gets</th></tr></thead>
    <tbody>
      <tr><td>A supervisor assigned to every region</td><td>One accountable contact, so deficiencies get fixed the same day</td></tr>
      <tr><td>Backup porters on call</td><td>Callouts never leave an office uncleaned</td></tr>
      <tr><td>Monthly QC inspections with written records</td><td>The contracting officer's representative sees problems before recruiters do</td></tr>
    </tbody>
  </table>
  <p class="statement center r">After every sentence, ask: so what?</p>''',
  "The most important writing technique today. A feature is something about your company or approach: a supervisor, backup staff, an inspection program. A benefit is what it does for the customer. The test: after every sentence you write, ask so what? Our team has 15 years of janitorial experience. So what? The feature alone scores nothing; the benefit scores, because it connects your capability to their problem. Most small-business proposals I review are all features: we have this certification, we use this tool. Every competitor has those. The winners connect them to outcomes the customer cares about. These rows are examples written for the practice RFQ.",
  eyebrow="Part 3 &middot; Features and benefits", title="The \"so what?\" test")

slide("light", '''
  <div class="roles r">
    <div><b>Weak: feature only</b><span>"Our company has provided janitorial services for 10 years."</span></div>
    <div><b>Better: + benefit</b><span>"Our 10 years of janitorial experience lets us close deficiencies within 24 hours, so offices stay ready for applicants."</span></div>
    <div><b>Best: + proof + customer</b><span>"Across 3 comparable federal contracts, our supervisors closed 98% of deficiencies within 24 hours, keeping USACE's 29 Maryland recruiting offices ready for every applicant visit."</span></div>
  </div>
  <p class="fine r">Example written for class. Formula: feature &rarr; quantified benefit &rarr; proof &rarr; the customer by name.</p>''',
  "Watch the progression. Weak: a fact about your company. Better: adds the benefit, what it means for them. Best does four things: the feature, a quantified benefit, proof from past performance, and the customer by name with their mission. Feature, quantified benefit, proof, customer impact. Use that formula for every key claim and you're ahead of most of the competition. These numbers are illustrative; yours have to be real and checkable.",
  eyebrow="Part 3 &middot; Features and benefits", title="Weak, better, best")

checkpoint("Section A", "Write one \"so what\" sentence",
  "Section A of the worksheet: one feature of your business, its benefit to a government customer, and the proof. Then combine them into one sentence.",
  "Three minutes, full pause, even if you're behind. Ask two people to read their sentence aloud and apply the so-what test live: is there a number? Is the customer in it? Push for a number every time. Remind: don't hit Submit yet.")

section("Part 4", "Themes, discriminators, ghosting",
  "Now the strategic messaging tools.")

slide("light", '''
  <div class="cols2 wide-left">''' + bullets([
    "The conclusion you want the evaluator to reach",
    "A quantified feature plus a customer benefit",
    "The customer first, in the RFP's own words",
    "Two or three sentences, 40 words max",
    "3 or 4 per proposal, woven through every section"]) + '''
    <div class="callout r"><p>3 or 4. Not 10.</p><span>Evaluators read 15 or 20 proposals. They remember three things.</span></div>
  </div>''',
  "Win themes are what you want the evaluator saying in the evaluation room: this company has what? That's your theme. Themes aren't repeated word for word. Their essence runs through the technical approach, the staffing plan, past performance, each from a different angle. Keep it to three or four. And this connects back to Monday of last week: your capture strategy should have defined your themes before the RFP dropped. You're executing a strategy, not inventing one at the deadline.",
  eyebrow="Part 4 &middot; Win themes", title="What you want them to remember")

slide("light", '''
  <div class="roles r">
    <div><b>Good: compliant</b><span>"Our quality control program meets all PWS requirements."</span></div>
    <div><b>Better: quantified</b><span>"Our quality control program inspects every site monthly and closes deficiencies within 24 hours."</span></div>
    <div><b>Best: customer first</b><span>"Keeping USACE's recruiting offices applicant-ready every day, our quality control program inspects every site monthly and closes deficiencies within 24 hours."</span></div>
  </div>
  <p class="fine r">Example written for class.</p>''',
  "How a theme evolves. Good is a compliance statement: we meet the requirements. So does everyone else. Better quantifies: monthly inspections, 24-hour closure. Best leads with the customer's goal, applicant-ready offices, then delivers the specifics. Compliance, then quantified advantage, then customer framing. That's the path from Acceptable to Outstanding.",
  eyebrow="Part 4 &middot; Win themes", title="Good, better, best themes")

slide("light", '''
  <div class="cols2">
    <div class="card r"><p class="card-k">Counts</p>''' + bullets([
        "Near-identical past performance",
        "Key people the customer already trusts",
        "Local presence when competitors are remote",
        "A certification competitors lack",
        "A method with documented results"]) + '''</div>
    <div class="card accent r"><p class="card-k">Doesn't count</p>''' + bullets([
        "\"We have the best people\"",
        "\"We're committed to quality\"",
        "Technology claims with no specifics",
        "Anything every bidder could say"]) + '''</div>
  </div>''',
  "A discriminator is truly yours, something the customer cares about, and verifiable. Different isn't enough; it has to address a customer concern. You need to know who you're competing against: Friday we saw a Georgia firm win Maryland sites. If you're local and they're 600 miles away, response time is a discriminator. Back it up. We have the best people is not a discriminator. Our supervisor has run three federal janitorial contracts in these same counties is.",
  eyebrow="Part 4 &middot; Discriminators", title="What makes you different")

slide("light", '''
  <div class="split r">
    <div class="half cap"><p>What you know</p><h3>They're remote</h3><span>A likely rival's supervisor is hours away</span></div>
    <div class="divider"><span>SO</span></div>
    <div class="half prop"><p>What you write</p><h3>We're local</h3><span>"Our supervisors live within 30 minutes of every Maryland site."</span></div>
  </div>
  <p class="takeaway r">Never name them. Never knock them.</p>''',
  "Ghosting: you position your strength exactly where you believe a competitor is weak, without naming them. You don't say Company X is far away; you say our supervisors live within 30 minutes of every site. The evaluator connects the dots. The line: ghosting is positioning, not disparaging. Never name names, never say anything negative about another company. It only works if you did the competitive research in capture.",
  eyebrow="Part 4 &middot; Ghosting", title="Ghosting, done right")

section("Part 5", "Customer focus",
  "None of this works unless the focus stays on the customer.")

slide("light", '''
  <div class="cols2">
    <div class="stat r"><p class="stat-n">2:1</p><p class="stat-l">the customer's name to yours</p></div>
    <div class="roles r">
      <div><b>About you</b><span>"Acme Cleaning has 15 years of experience maintaining federal offices."</span></div>
      <div><b>About them</b><span>"USACE's recruiting offices will benefit from 15 years of maintaining comparable federal offices."</span></div>
      <p class="fine">Count both names in your draft. If yours wins, flip it.</p>
    </div>
  </div>''',
  "A quick test for any section you write: count your company's name and the customer's name. It should be about two to one for the customer. If it's the other way, you wrote a brochure. The evaluator doesn't care about your history in the abstract; they care how you solve their problem. Same information, different focus: the first sentence is about you, the second is about them.",
  eyebrow="Part 5 &middot; Customer focus", title="The 2:1 rule")

slide("light", '''
  <div class="cols2">
    <div class="card r"><p class="card-k">Do</p>''' + bullets([
        "Answer every requirement, in the RFP's order",
        "Use their words: if they say \"plan,\" say plan",
        "Clear headings that match the requirement",
        "Tie it back: \"In response to PWS 1.2 ...\""]) + '''</div>
    <div class="card accent r"><p class="card-k">Don't</p>''' + bullets([
        "Rewrite requirements in your own words",
        "Reorganize their structure",
        "Leave leaps in logic",
        "Bury your best point mid-paragraph"]) + '''</div>
  </div>''',
  "The evaluator has a stack of proposals, a scorecard and a deadline. Make the answer obvious. Use the RFP's language: if they say Quality Control Program, don't call it your quality approach. They're scanning for their words. Respond in their order; their scorecard goes one through ten. And explain every step. They won't fill gaps for you; they'll mark a weakness.",
  eyebrow="Part 5 &middot; The evaluator's job", title="Make their job easy")

checkpoint("Section B", "Write one win theme",
  "Section B: one win theme for a government customer you want, 40 words or fewer, customer first. Then count: whose name shows up more, yours or theirs?",
  "Three minutes. Take two themes aloud. Coach live: does it open with the customer's goal? Is there a number? Is it under 40 words? Remind: don't hit Submit yet.")

section("Part 6", "Writing mechanics and graphics",
  "The mechanics, then graphics, which can give a small business a real edge.")

slide("light", '''
  <div class="cols2">''' + bullets([
    "Short, declarative sentences",
    "Lead each paragraph with the key point",
    "Numbers beat adjectives",
    "Back every claim with evidence",
    "Active voice: \"Our team will ...\"",
    "Paragraphs of 4 or 5 sentences"]) + '''
    <table class="compare r">
      <thead><tr><th>Cut</th><th>Replace with</th></tr></thead>
      <tbody>
        <tr><td>"World-class"</td><td>A number</td></tr>
        <tr><td>"We believe / strive"</td><td>"Our team will"</td></tr>
        <tr><td>"We understand"</td><td>Show it in the approach</td></tr>
      </tbody>
    </table>
  </div>''',
  "Mechanics. The evaluator is tired; short sentences are easier to score. Lead with the point: if they read only first sentences, they should still get your message. Quantify: significant experience means nothing; 12 years across 7 contracts means something. And cut the killers: world-class, state-of-the-art, we are pleased to, we believe, we will strive. Strive tells them you'll try. They want will. My rule: if a sentence would be true for any company bidding, delete it.",
  eyebrow="Part 6 &middot; Writing mechanics", title="Write so they can score it")

slide("light", '''
  <div class="tiles">
    <div class="r"><span>1</span><b>Process diagram</b>Your method, step by step</div>
    <div class="r"><span>2</span><b>Org chart</b>Real names, real reporting lines</div>
    <div class="r"><span>3</span><b>Schedule</b>Their milestones, your dates</div>
    <div class="r"><span>4</span><b>Comparison table</b>Claims backed by data</div>
    <div class="r"><span>5</span><b>Site map</b>For us: 125 offices by region</div>
    <div class="r"><span>6</span><b>Caption with a theme</b>Every figure says why it matters</div>
  </div>
  <p class="takeaway r">Original, not clip art. One good graphic can replace two pages.</p>''',
  "Graphics are underused by small businesses. After hours of dense text, a clear graphic lands. With a page limit, one graphic can replace two or three pages. For our janitorial RFQ, a map of 125 offices by pricing region with your supervisor coverage would say more than a page of prose. Make them original: real names on the org chart, the RFP's milestones on the schedule. Every figure gets a number and a caption that carries a theme. If you're not a designer, this is one of the places outside help pays off.",
  eyebrow="Part 6 &middot; Graphics", title="Graphics that score")

slide("light", '''
  <div class="cols2">
    <div class="card accent r"><p class="card-k">Loses</p>''' + bullets([
        "Missing a requirement",
        "All about you, not them",
        "Telling, not showing how",
        "Claims with no evidence"]) + '''</div>
    <div class="card r"><p class="card-k">Blends in</p>''' + bullets([
        "No differentiation",
        "Walls of text, no graphics",
        "Marketing language",
        "Themes invented at the deadline"]) + '''</div>
  </div>''',
  "The mistakes I see most. Missing a requirement: your compliance matrix prevents it. All about you: go back to 2:1. Telling, not showing: we will manage effectively. How? What tools, what escalation path? And no differentiation, which is what happens when you skip capture. Generic proposals don't win.",
  eyebrow="Watch for these", title="Common proposal mistakes")

slide("light", '''
  <div class="tiles">
    <div class="r"><span>1</span><b>Find and pursue</b>Session 1: the lifecycle and capture</div>
    <div class="r"><span>2</span><b>Build the team</b>Session 2: every function covered</div>
    <div class="r"><span>3</span><b>Read the RFP</b>Session 3: A &rarr; L &rarr; M &rarr; C &rarr; B</div>
    <div class="r"><span>4</span><b>Write to win</b>Session 4: feature, benefit, proof, customer</div>
  </div>
  <p class="takeaway r">Capture feeds themes. Themes feed the matrix. The matrix drives the writing.</p>''',
  "Over four sessions we went from finding opportunities to writing the proposal. Government contracting is a process, not luck: structured, repeatable, rewarding preparation, compliance and specificity. My ask: don't let this sit. Next time you see an opportunity on SAM.gov, even one you won't bid, practice: build the matrix, draft a theme, write one section with the formula. It's a muscle.",
  eyebrow="The series", title="How it all connects")

slide("light", f'''
  <div class="cols2">
    <div class="card r"><p class="card-k">Keep going</p>''' + bullets([
        "Your capture template (Session 1) and compliance matrix (Sessions 2 and 3)",
        "<i>Persuasive Business Proposals</i>, Tom Sant",
        "acquisition.gov for the FAR, SAM.gov for opportunities",
        "Free 1:1 advising: capture, matrix, proposal reviews"]) + f'''</div>
    <div class="submit-card r">
      <p class="eyebrow light">Worksheet &middot; Section C</p>
      <h3>Write your one step, then submit.</h3>
      <p>Your inbox gets: this deck with notes, a proposal-writing checklist, and every link from today.</p>
      <div class="mini-qr">{QR_FORM}</div>
    </div>
  </div>''',
  "Everything from the series is in your follow-up emails. If you want one book, Tom Sant's Persuasive Business Proposals is the best practical guide I know. The SBDC is free: capture strategy, the compliance matrix, proposal reviews, teaming. Email me and we'll get you on the calendar. Now Section C, your one step, then the last page and Submit. Thank you all. Go win something.",
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
  "Open it up. Remind them to submit the worksheet if they haven't.", label="Questions")

engine.render(pathlib.Path.cwd() / "Basics-of-Proposal-Writing-2026-10-05.html",
              title="Basics of Proposal Writing",
              footer="Session 4 &middot; Basics of Proposal Writing")
