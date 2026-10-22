import hashlib
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
    "shares_for_ads",
    "shares_with_providers",
    "keeps_data",
    "can_opt_out",
]
SHARDS = 4
PRIVACY_TASKS = {
    "opp115_third_party_sharing_collection": "sharing",
    "opp115_data_retention": "keeps_data",
    "opp115_user_choice_control": "can_opt_out",
}


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


def privacy_segments():
    found = {}
    for task, flag in PRIVACY_TASKS.items():
        for r in load_dataset("nguha/legalbench", task)["test"]:
            text = re.sub(r"\s+", " ", r["text"]).strip().lower()
            found.setdefault(text, set())
            if r["answer"] == "Yes":
                found[text].add(flag)
    return sorted((text, sorted(flags)) for text, flags in found.items())


def export_privacy(dataset):
    positive = [(text, flags) for text, flags in privacy_segments() if flags]
    items = [{"id": i, "text": text, "known": flags} for i, (text, flags) in enumerate(positive)]
    for k in range(SHARDS):
        write_jsonl(DATA / f"privacy_{k}.jsonl", items[k::SHARDS])
    print(f"exported {len(items)} positive privacy segments in {SHARDS} shards")


def privacy_rows():
    labels = {r["id"]: r for k in range(SHARDS) for r in read_jsonl(DATA / f"privacy_labels_{k}.jsonl")}
    texts = {r["id"]: r["text"] for k in range(SHARDS) for r in read_jsonl(DATA / f"privacy_{k}.jsonl")}
    by_text = {texts[i]: r for i, r in labels.items()}
    out = []
    for text, known in privacy_segments():
        if not known:
            out.append((text, [], ""))
            continue
        label = by_text.get(text)
        if not label or not label.get("plain"):
            continue
        flags = [f for f in known if f != "sharing"]
        if "sharing" in known:
            flags.append("shares_for_ads" if label.get("sharing") == "ads" else "shares_with_providers")
        out.append((text, sorted(flags, key=CATEGORIES.index), label["plain"].strip()))
    return out


def is_test(text):
    return int(hashlib.md5(text.encode()).hexdigest(), 16) % 5 == 0


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
    test = [{"text": text, "flags": labels, "source": "tos"} for text, labels in rows(dataset, "test")]
    if (DATA / "privacy_labels_0.jsonl").exists():
        for text, flags, plain in privacy_rows():
            if is_test(text):
                test.append({"text": text, "flags": flags, "source": "privacy"})
            else:
                train.append({"messages": [
                    {"role": "system", "content": PROMPT},
                    {"role": "user", "content": text},
                    {"role": "assistant", "content": json.dumps({"flags": flags, "plain": plain})},
                ]})
    random.Random(0).shuffle(train)
    write_jsonl(DATA / "train.jsonl", train)
    write_jsonl(DATA / "test.jsonl", test)
    print(f"train {len(train)} rows, {dropped} unfair rows dropped without a plain sentence")


if __name__ == "__main__":
    DATA.mkdir(exist_ok=True)
    {"export": export, "export_privacy": export_privacy, "assemble": assemble}[sys.argv[1]](load_dataset("coastalcph/lex_glue", "unfair_tos"))
