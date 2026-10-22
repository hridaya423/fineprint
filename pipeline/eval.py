import json
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT = (ROOT / "prompt.txt").read_text().strip()
CATEGORIES = [
    "limitation_of_liability",
    "unilateral_termination",
    "unilateral_change",
    "content_removal",
    "contract_by_using",
    "choice_of_law",
    "jurisdiction",
    "arbitration",
    "shares_for_ads",
    "shares_with_providers",
    "keeps_data",
    "can_opt_out",
]
RED = {"arbitration", "shares_for_ads"}


def ask(url, text):
    body = {"messages": [{"role": "system", "content": PROMPT}, {"role": "user", "content": text}], "temperature": 0, "max_tokens": 96}
    request = urllib.request.Request(f"{url}/v1/chat/completions", json.dumps(body).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.loads(response.read())["choices"][0]["message"]["content"]


def parse(reply):
    try:
        flags = json.loads(reply[reply.index("{"):reply.rindex("}") + 1])["flags"]
        return {f for f in flags if f in CATEGORIES}, True
    except (ValueError, KeyError, TypeError):
        return set(), False


def f1(tp, fp, fn):
    return 2 * tp / (2 * tp + fp + fn) if tp else 0.0


def score(examples):
    counts = {c: [0, 0, 0] for c in CATEGORIES}
    flagged, red, valid = [0, 0, 0], [0, 0, 0], 0
    for e in examples:
        predicted, ok = parse(e["reply"])
        gold = set(e["gold"])
        valid += ok
        for c in CATEGORIES:
            counts[c][0] += c in predicted and c in gold
            counts[c][1] += c in predicted and c not in gold
            counts[c][2] += c not in predicted and c in gold
        for tally, p, g in ((flagged, predicted, gold), (red, predicted & RED, gold & RED)):
            tally[0] += bool(p) and bool(g)
            tally[1] += bool(p) and not g
            tally[2] += not p and bool(g)
    present = [c for c in CATEGORIES if counts[c][0] + counts[c][2]]
    totals = [sum(v[i] for v in counts.values()) for i in range(3)]
    return {
        "rows": len(examples),
        "json_valid": round(valid / len(examples), 4),
        "micro_f1": round(f1(*totals), 4),
        "macro_f1": round(sum(f1(*counts[c]) for c in present) / len(present), 4),
        "flag_detection_f1": round(f1(*flagged), 4),
        "red_flag_f1": round(f1(*red), 4),
        "unflagged_clauses_wrongly_flagged": flagged[1],
        "per_category_f1": {c: round(f1(*counts[c]), 3) for c in present},
    }


def main(url, name, limit=None):
    rows = [json.loads(line) for line in (ROOT / "data/test.jsonl").read_text().splitlines()][:limit]
    started = time.time()
    with ThreadPoolExecutor(4) as pool:
        replies = list(pool.map(lambda r: ask(url, r["text"]), rows))

    examples = [{"text": r["text"], "gold": r["flags"], "source": r.get("source", "tos"), "reply": reply} for r, reply in zip(rows, replies)]
    result = {"server": url, "rows": len(rows), "seconds": round(time.time() - started, 1), **score(examples)}
    for source in sorted({e["source"] for e in examples}):
        result[source] = score([e for e in examples if e["source"] == source])
    out = ROOT / "eval" / name
    out.mkdir(parents=True, exist_ok=True)
    (out / "metrics.json").write_text(json.dumps(result, indent=2))
    (out / "replies.jsonl").write_text("".join(json.dumps(e) + "\n" for e in examples))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else None)
