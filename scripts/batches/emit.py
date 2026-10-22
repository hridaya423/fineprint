import json, pathlib
OUT = pathlib.Path("/Users/hridyaagrawal/honey/fineprint/data/sub_offer.jsonl")
KEYS = ["trial", "then", "auto_renews", "first_charge", "cancel", "refund", "watch_out"]
def add(rows):
    with OUT.open("a", encoding="utf-8") as f:
        for r in rows:
            assert len(r) == 8, r[0][:40]
            f.write(json.dumps({"text": r[0].strip(), "offer": dict(zip(KEYS, r[1:]))}, ensure_ascii=False) + "\n")
