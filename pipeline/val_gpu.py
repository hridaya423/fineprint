import json
import sys
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, str(Path(__file__).parent))
from eval import PROMPT, ROOT, score


def main(model_path, name):
    rows = [json.loads(line) for line in (ROOT / "data/val.jsonl").read_text().splitlines()]
    tokenizer = AutoTokenizer.from_pretrained(model_path, padding_side="left")
    model = AutoModelForCausalLM.from_pretrained(model_path, dtype=torch.bfloat16, device_map="cuda").eval()
    replies = []
    for start in range(0, len(rows), 128):
        chats = [[{"role": "system", "content": PROMPT}, {"role": "user", "content": r["text"]}] for r in rows[start:start + 128]]
        batch = tokenizer.apply_chat_template(chats, add_generation_prompt=True, return_tensors="pt", padding=True, return_dict=True).to("cuda")
        with torch.no_grad():
            out = model.generate(**batch, max_new_tokens=96, do_sample=False)
        replies += tokenizer.batch_decode(out[:, batch["input_ids"].shape[1]:], skip_special_tokens=True)
    result = score([{"gold": r["flags"], "reply": reply} for r, reply in zip(rows, replies)])
    (ROOT / f"val-{name}.json").write_text(json.dumps(result, indent=2))
    print(name, json.dumps({k: result[k] for k in ("micro_f1", "red_flag_f1", "flag_detection_f1", "unflagged_clauses_wrongly_flagged")}))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
