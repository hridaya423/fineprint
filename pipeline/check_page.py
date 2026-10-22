import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT = (ROOT / "prompt.txt").read_text().strip()
RED = {"arbitration", "shares_for_ads", "trial_converts_to_paid", "hard_to_cancel", "no_refund", "price_can_increase", "early_termination_fee"}
GOOD = {"can_opt_out"}


class Text(HTMLParser):
    skip = {"script", "style", "nav", "header", "footer", "noscript", "svg"}

    def __init__(self):
        super().__init__()
        self.depth, self.parts = 0, []

    def handle_starttag(self, tag, attrs):
        self.depth += tag in self.skip
        if tag in {"p", "li", "div", "br", "h1", "h2", "h3", "h4", "section", "tr"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        self.depth -= tag in self.skip and self.depth > 0

    def handle_data(self, data):
        if not self.depth:
            self.parts.append(data)


def page_text(source):
    if Path(source).exists():
        raw = Path(source).read_text(errors="ignore")
    else:
        request = urllib.request.Request(source, headers={"User-Agent": "Mozilla/5.0"})
        raw = urllib.request.urlopen(request, timeout=30).read().decode(errors="ignore")
    if "<" not in raw[:2000]:
        return raw
    parser = Text()
    parser.feed(raw)
    return "".join(parser.parts)


def clauses(text):
    out = []
    for block in re.split(r"\n\s*\n|\n", text):
        for sentence in re.split(r"(?<=[.;!?])\s+(?=[A-Z(\"])", " ".join(block.split())):
            if len(sentence) >= 40:
                out.append(sentence)
    return out[:400]


def ask(url, clause):
    body = {"messages": [{"role": "system", "content": PROMPT}, {"role": "user", "content": clause.lower()}], "temperature": 0, "max_tokens": 96}
    request = urllib.request.Request(f"{url}/v1/chat/completions", json.dumps(body).encode(), {"Content-Type": "application/json"})
    reply = json.loads(urllib.request.urlopen(request, timeout=120).read())["choices"][0]["message"]["content"]
    try:
        return json.loads(reply[reply.index("{"):reply.rindex("}") + 1])
    except ValueError:
        return {"flags": [], "plain": ""}


def main(source, url="http://127.0.0.1:8081", workers=8):
    found = clauses(page_text(source))
    started = time.time()
    with ThreadPoolExecutor(workers) as pool:
        answers = list(pool.map(lambda c: ask(url, c), found))
    seconds = time.time() - started

    flagged = [(c, a) for c, a in zip(found, answers) if a.get("flags")]
    red = [(c, a) for c, a in flagged if RED & set(a["flags"])]
    good = [(c, a) for c, a in flagged if GOOD & set(a["flags"])]
    grade = "ACE"[min(len({f for _, a in red for f in a["flags"] if f in RED}), 2)]
    print(f"{source}\n{len(found)} clauses in {seconds:.1f}s ({len(found) / seconds:.1f}/s). Grade {grade}. "
          f"{len(red)} red, {len(flagged) - len(red) - len(good)} standard, {len(good)} good.\n")
    for title, items in (("WATCH OUT", red), ("YOUR CONTROLS", good)):
        for clause, answer in items:
            print(f"[{title}] {answer.get('plain')}\n    flags: {answer['flags']}\n    quote: {clause[:220]}\n")


if __name__ == "__main__":
    main(*sys.argv[1:2], *sys.argv[2:3], *[int(a) for a in sys.argv[3:4]])
