#!/usr/bin/env python3
"""Build the Maryland SBDC success story authorization email.

Usage:
    python3 build_authorization_email.py story.json OUT_DIR
    python3 build_authorization_email.py --self-test

story.json fields (strings unless noted):
    client_full_name, client_email, business_name,
    story_title, story_paragraphs (list of strings),
    draft_date (YYYY-MM-DD),
    counselor_name, counselor_title, counselor_email,
    client_first_name (optional; defaults to the first word of client_full_name),
    quote (optional object: text, name, role)

Writes OUT_DIR/authorization-email.html and OUT_DIR/authorization-email.txt,
then prints a JSON summary (to, subject, logo path) for creating the draft.

Never put the counselor's Neoserra postbox address in story.json: it goes in
the draft's Bcc only, and must never appear anywhere the client can see.
Standard library only, so it runs in Claude and in ChatGPT.
"""
import datetime
import html
import json
import os
import re
import sys
from urllib.parse import quote as urlquote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEMPLATE = os.path.join(ROOT, "assets", "authorization-email.html")
QUOTE_TEMPLATE = os.path.join(ROOT, "assets", "authorization-quote-block.html")
RELEASE = os.path.join(ROOT, "references", "publicity-release.md")
LOGO = os.path.join(ROOT, "assets", "sbdc-maryland-logo.png")

REQUIRED = ["client_full_name", "client_email", "business_name", "story_title",
            "story_paragraphs", "draft_date", "counselor_name",
            "counselor_title", "counselor_email"]
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
# The Gmail connector rewrites any web address (even plain "site.org") into a
# google.com/url redirect, so the email must contain none. Emails are allowed.
WEB_RE = re.compile(r"https?://|www\.|\b[a-z0-9-]+\.(?:com|org|net|edu|gov|io|us|biz|info|co)\b", re.I)
DOLLAR_RE = re.compile(r"\$\s?\d|\b\d[\d,.]*\s?(?:dollars|USD)\b", re.I)
STORY_PARA = '<p style="margin:0 0 16px 0;">{}</p>'
RELEASE_PARA = '<p style="margin:0 0 12px 0;">{}</p>'


class BuildError(ValueError):
    pass


def clean(value, field):
    if not isinstance(value, str) or not value.strip():
        raise BuildError(f"{field} is missing or empty")
    # one line, no control characters (stops header/subject injection)
    return re.sub(r"[\x00-\x1f\x7f]+", " ", value).strip()


def release_paragraphs(client_full_name):
    text = open(RELEASE, encoding="utf-8").read()
    body = text.split("<!-- RELEASE START -->")[1].split("<!-- RELEASE END -->")[0]
    return [p.strip().replace("{client_full_name}", client_full_name)
            for p in body.strip().split("\n\n")]


def long_date(iso):
    try:
        d = datetime.date.fromisoformat(iso)
    except ValueError:
        raise BuildError("draft_date must be YYYY-MM-DD")
    return f"{d:%B} {d.day}, {d.year}", f"{d:%b} {d.day}, {d.year}"


def mailto(to, subject, body):
    return "mailto:{}?subject={}&amp;body={}".format(
        to, urlquote(subject, safe=""), urlquote(body, safe=""))


def build(data):
    f = {k: clean(data.get(k), k) for k in REQUIRED if k != "story_paragraphs"}
    paras = data.get("story_paragraphs")
    if not isinstance(paras, list) or not paras:
        raise BuildError("story_paragraphs must be a non-empty list")
    paras = [clean(p, "story_paragraphs") for p in paras]
    for k in ("client_email", "counselor_email"):
        if not EMAIL_RE.match(f[k]):
            raise BuildError(f"{k} is not a valid email address: {f[k]}")
    first = clean(data.get("client_first_name") or f["client_full_name"].split()[0], "client_first_name")
    q = data.get("quote") or None
    if q:
        q = {k: clean(q.get(k), "quote." + k) for k in ("text", "name", "role")}

    # Checks on everything the client will read
    visible = [first, f["client_full_name"], f["business_name"], f["story_title"],
               f["counselor_name"], f["counselor_title"], *paras]
    if q:
        visible += list(q.values())
    for v in visible:
        if WEB_RE.search(v):
            raise BuildError(f"remove the web address from: {v!r} (Gmail rewrites links)")
        if DOLLAR_RE.search(v):
            raise BuildError(f"remove the dollar amount from: {v!r} (no exact financials in stories)")

    date_long, date_short = long_date(f["draft_date"])
    tag = f'{f["business_name"]} success story (draft dated {date_short})'
    approve = mailto(f["counselor_email"], f"APPROVED - {tag}",
                     f"I approve my Maryland SBDC success story (draft dated {date_long}) as written "
                     "and agree to the Publicity Release.\r\n\r\nFull name (serves as my signature): "
                     "\r\nBusiness name: \r\nDate: ")
    changes = mailto(f["counselor_email"], f"CHANGES - {tag}",
                     "I'd like these changes before my story is published:\r\n\r\n")

    e = html.escape
    release = release_paragraphs(f["client_full_name"])
    quote_html = ""
    if q:
        quote_html = (open(QUOTE_TEMPLATE, encoding="utf-8").read()
                      .replace("{{QUOTE_TEXT}}", e(q["text"]))
                      .replace("{{QUOTE_NAME}}", e(q["name"]))
                      .replace("{{QUOTE_ROLE}}", e(q["role"])))
    values = {
        "APPROVE_MAILTO": approve, "CHANGES_MAILTO": changes, "LOGO_CID": "att0",
        "CLIENT_FIRST_NAME": e(first), "CLIENT_FULL_NAME": e(f["client_full_name"]),
        "BUSINESS_NAME": e(f["business_name"]), "STORY_TITLE": e(f["story_title"]),
        "DRAFT_DATE_LONG": e(date_long),
        "STORY_PARAGRAPHS": "\n".join(STORY_PARA.format(e(p)) for p in paras),
        "QUOTE_BLOCK": quote_html,
        "RELEASE_PARAGRAPHS": "\n".join(RELEASE_PARA.format(e(p)) for p in release),
        "COUNSELOR_NAME": e(f["counselor_name"]), "COUNSELOR_TITLE": e(f["counselor_title"]),
        "COUNSELOR_EMAIL": e(f["counselor_email"]),
    }
    template = open(TEMPLATE, encoding="utf-8").read()
    missing = set(re.findall(r"\{\{(\w+)\}\}", template)) - set(values)
    if missing:
        raise BuildError(f"template has unknown placeholders: {sorted(missing)}")
    # one pass over the template only, so text a person typed is never expanded
    out = re.sub(r"\{\{(\w+)\}\}", lambda m: values[m.group(1)], template)
    if WEB_RE.search(re.sub(r"[\w.+-]+@[\w.-]+", "", out)):
        raise BuildError("template contains a web address")

    quote_txt = f'\n"{q["text"]}" - {q["name"]}, {q["role"]}\n' if q else ""
    text = (
        f"Congratulations, {first}. {f['business_name']} has been selected for a Maryland SBDC "
        "Client Success Story, the highest recognition we give a client.\n\n"
        "Before we share your story, we need your approval. Reply with \"APPROVED,\" your full name "
        "(serves as your signature), and the date. Or reply with the changes you'd like.\n\n"
        f"YOUR STORY (draft dated {date_long})\n{f['story_title']}\n\n" + "\n\n".join(paras) + "\n"
        + quote_txt + "\nPUBLICITY RELEASE\n" + "\n\n".join(release)
        + "\n\nApproving your story with your full name and the date means you agree to this "
        "Publicity Release.\n\n"
        f"{f['counselor_name']}\n{f['counselor_title']}\nMaryland Small Business Development Center\n"
        f"{f['counselor_email']}\n\nFunded in part through a Cooperative Agreement with the U.S. Small "
        "Business Administration. All opinions, conclusions, and/or recommendations expressed herein "
        "are those of the author(s) and do not necessarily reflect the views of the SBA.\n")
    summary = {
        "to": f["client_email"],
        "subject": f"Congratulations! Your Maryland SBDC Client Success Story - {f['business_name']}",
        "approval_subject_starts_with": f"APPROVED - {tag}",
        "changes_subject_starts_with": f"CHANGES - {tag}",
        "logo": LOGO,  # attach inline; the template points at cid att0
    }
    return out, text, summary


SAMPLE = {
    "client_full_name": "Jordan Rivera", "client_email": "jordan@example.com",
    "business_name": "Rivera Bakeshop",
    "story_title": "From Farmers Market Stall to Second Storefront",
    "story_paragraphs": [
        "Jordan Rivera started Rivera Bakeshop selling conchas and sourdough at the Columbia farmers market.",
        "Rivera Bakeshop received an SBA loan and opened a second location this fall."],
    "quote": {"text": "I came in with a recipe box and a dream.", "name": "Jordan Rivera",
              "role": "Owner, Rivera Bakeshop"},
    "draft_date": "2026-11-19", "counselor_name": "Brandon Mason",
    "counselor_title": "Senior Business and Technology Consultant",
    "counselor_email": "bwmason@umd.edu",
}


def self_test():
    out, text, s = build(SAMPLE)
    assert "Congratulations, Jordan." in out and "I, Jordan Rivera, hereby" in out
    assert "APPROVED%20-%20Rivera%20Bakeshop%20success%20story%20%28draft%20dated%20Nov%2019%2C%202026%29" in out
    assert "bgcolor=\"#d11142\"" in out and "background:" not in out
    assert "pb.neoserra.com" not in out and "http" not in out
    assert s["to"] == "jordan@example.com"
    # story text is escaped, not injected as HTML
    evil = dict(SAMPLE, story_paragraphs=['<img src=x onerror="alert(1)"> {{CLIENT_EMAIL}}'])
    built = build(evil)[0]
    assert "&lt;img src=x" in built and "<img src=x" not in built
    # no quote -> no quote block
    assert "Georgia" in out and "Georgia" not in build(dict(SAMPLE, quote=None))[0]
    for bad, why in [({"story_paragraphs": ["We got a $10,000 loan."]}, "dollar"),
                     ({"story_paragraphs": ["Visit rivera.com today."]}, "web address"),
                     ({"client_email": "not-an-email"}, "valid email"),
                     ({"client_email": "a@b.com\r\nBcc: x@y.com"}, "valid email"),
                     ({"draft_date": "Nov 19"}, "YYYY-MM-DD")]:
        try:
            build(dict(SAMPLE, **bad))
        except BuildError as err:
            assert why in str(err), (why, err)
        else:
            raise AssertionError(f"accepted bad input: {bad}")
    print("self-test passed")


def main(argv):
    if argv[1:] == ["--self-test"]:
        return self_test()
    if len(argv) != 3:
        sys.exit(__doc__)
    data = json.load(open(argv[1], encoding="utf-8"))
    try:
        out, text, summary = build(data)
    except BuildError as err:
        sys.exit(f"Cannot build the email: {err}")
    os.makedirs(argv[2], exist_ok=True)
    open(os.path.join(argv[2], "authorization-email.html"), "w", encoding="utf-8").write(out)
    open(os.path.join(argv[2], "authorization-email.txt"), "w", encoding="utf-8").write(text)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main(sys.argv)
