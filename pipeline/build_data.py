import json
import random
import re
import sys
from pathlib import Path

from datasets import load_dataset

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
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
SHARDS = 4


def detok(text):
    text = text.strip().replace("`` ", '"').replace(" ''", '"').replace("``", '"').replace("''", '"')
    text = re.sub(r" ([,.;:!?)\]%])", r"\1", text)
    text = re.sub(r"([(\[$]) ", r"\1", text)
    text = re.sub(r" (n't|'s|'re|'ve|'ll|'d|'m)\b", r"\1", text)
    return re.sub(r"\s+", " ", text)


def rows(dataset, *splits):
    return [(detok(r["text"]), [CATEGORIES[i] for i in r["labels"]]) for s in splits for r in dataset[s]]


def write_jsonl(path, records):
    path.write_text("".join(json.dumps(r) + "\n" for r in records))


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def export(dataset):
    unfair = sorted({text: labels for text, labels in rows(dataset, "train", "validation") if labels}.items())
    items = [{"id": i, "text": text, "labels": labels} for i, (text, labels) in enumerate(unfair)]
    for k in range(SHARDS):
        write_jsonl(DATA / f"unfair_{k}.jsonl", items[k::SHARDS])
    print(f"exported {len(items)} unfair clauses in {SHARDS} shards")


def assemble(dataset):
    unfair = [r for k in range(SHARDS) for r in read_jsonl(DATA / f"unfair_{k}.jsonl")]
    plains = {r["id"]: r["plain"].strip() for k in range(SHARDS) for r in read_jsonl(DATA / f"plain_{k}.jsonl")}
    explained = {r["text"]: plains[r["id"]] for r in unfair if plains.get(r["id"])}

    train, dropped = [], 0
    for text, labels in rows(dataset, "train", "validation"):
        if labels and text not in explained:
            dropped += 1
            continue
        answer = json.dumps({"flags": labels, "plain": explained.get(text, "") if labels else ""})
        train.append({"messages": [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": text},
            {"role": "assistant", "content": answer},
        ]})
    random.Random(0).shuffle(train)
    write_jsonl(DATA / "train.jsonl", train)
    write_jsonl(DATA / "test.jsonl", [{"text": text, "flags": labels} for text, labels in rows(dataset, "test")])
    print(f"train {len(train)} rows, {dropped} unfair rows dropped without a plain sentence")


if __name__ == "__main__":
    DATA.mkdir(exist_ok=True)
    {"export": export, "assemble": assemble}[sys.argv[1]](load_dataset("coastalcph/lex_glue", "unfair_tos"))
