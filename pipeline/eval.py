import json
import sys
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

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
]


def parse(reply):
    try:
        flags = json.loads(reply[reply.index("{"):reply.rindex("}") + 1])["flags"]
        return {f for f in flags if f in CATEGORIES}, True
    except (ValueError, KeyError, TypeError):
        return set(), False


def f1(tp, fp, fn):
    return 2 * tp / (2 * tp + fp + fn) if tp else 0.0


def main(model_path, name, limit=None):
    rows = [json.loads(line) for line in (ROOT / "data/test.jsonl").read_text().splitlines()][:limit]
    tokenizer = AutoTokenizer.from_pretrained(model_path, padding_side="left")
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map="cuda").eval()

    replies = []
    for start in range(0, len(rows), 64):
        chats = [[{"role": "system", "content": PROMPT}, {"role": "user", "content": r["text"]}] for r in rows[start:start + 64]]
        batch = tokenizer.apply_chat_template(chats, add_generation_prompt=True, return_tensors="pt", padding=True, return_dict=True).to("cuda")
        with torch.no_grad():
            out = model.generate(**batch, max_new_tokens=96, do_sample=False)
        replies += tokenizer.batch_decode(out[:, batch["input_ids"].shape[1]:], skip_special_tokens=True)

    counts = {c: [0, 0, 0] for c in CATEGORIES}
    flagged = [0, 0, 0]
    valid, examples = 0, []
    for row, reply in zip(rows, replies):
        predicted, ok = parse(reply)
        gold = set(row["flags"])
        valid += ok
        for c in CATEGORIES:
            counts[c][0] += c in predicted and c in gold
            counts[c][1] += c in predicted and c not in gold
            counts[c][2] += c not in predicted and c in gold
        flagged[0] += bool(predicted) and bool(gold)
        flagged[1] += bool(predicted) and not gold
        flagged[2] += not predicted and bool(gold)
        examples.append({"text": row["text"], "gold": sorted(gold), "reply": reply})

    totals = [sum(v[i] for v in counts.values()) for i in range(3)]
    result = {
        "model": model_path,
        "rows": len(rows),
        "json_valid": valid / len(rows),
        "micro_f1": f1(*totals),
        "macro_f1": sum(f1(*v) for v in counts.values()) / len(CATEGORIES),
        "unfair_detection_f1": f1(*flagged),
        "per_category_f1": {c: round(f1(*v), 3) for c, v in counts.items()},
    }
    out = ROOT / "eval" / name
    out.mkdir(parents=True, exist_ok=True)
    (out / "metrics.json").write_text(json.dumps(result, indent=2))
    (out / "replies.jsonl").write_text("".join(json.dumps(e) + "\n" for e in examples))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else None)
