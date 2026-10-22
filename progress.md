# Fineprint progress

Fineprint: a local model (LFM2.5-1.2B, fine-tuned with White Circle Halo) reads Terms of Service clauses and returns the unfair categories plus one plain-English sentence. White Circle track. v1 scope is ToS only, one training run, then iterate.

## Contract

- System prompt: `prompt.txt`. The clients send it verbatim.
- Input: one clause, lower-cased, whitespace collapsed. The UNFAIR-ToS text is lower-case.
- Output: `{"flags": [...], "plain": "..."}`. The clients own severity, grade, quote and fallback text.
- Client handoffs: `handoff/chrome-extension.md`, `handoff/mobile-app.md` (they run on the other machine).

## Data

- Source: `coastalcph/lex_glue` config `unfair_tos`. Train 5,532, validation 2,275, test 1,607 clauses, 8 categories, about 9 fair to 1 unfair.
- `pipeline/build_data.py export` writes 849 unique unfair train+validation clauses to `data/unfair_{0..3}.jsonl`.
- Sonnet 5.5 subagents write `data/plain_{0..3}.jsonl` (one plain sentence per unfair clause). The labels stay the expert labels.
- `pipeline/build_data.py assemble` writes `data/train.jsonl` (Halo chat records) and `data/test.jsonl`.
- Run with `uv run --no-project --with datasets python -I pipeline/build_data.py <export|assemble>`.

## Train (H200) and evaluate (Mac)

1. Add the host to `~/.ssh/config` as `h200`, with `IdentityFile ~/.ssh/h200_hackathon_ed25519`.
2. `pipeline/h200.sh push` (copies the repo to `/data/fineprint`; Halo is preinstalled in `/workspace`).
3. `pipeline/h200.sh train` (config `pipeline/sft.yaml`: full fine-tune, 3 epochs, lr 2e-5). Override per run, for example `pipeline/h200.sh train --learning_rate=1e-5`.
4. `pipeline/h200.sh pull` copies the final checkpoint to `models/fineprint-hf/`.
5. `pipeline/export_gguf.sh models/fineprint-hf fineprint` writes Q8_0 and Q4_K_M GGUF files to `models/`.
6. Serve it: `llama-server -m models/fineprint-Q8_0.gguf --port 8081 -np 4 -c 16384`. The base model runs on port 8080.
7. Score the shipped GGUF: `python3 -I pipeline/eval.py http://127.0.0.1:8081 ft-v1`. The base score is `eval/base-q8/metrics.json`.

## Status

- Done: data export, Halo config, eval script, H200 runbook, export script, client handoffs, base model on `127.0.0.1:8080`.
- Base model check (3 clauses): valid JSON, but it flags harmless clauses ("update your profile picture" was flagged as termination and change). About 140 tok/s on an M4 Pro.
- Done: `data/train.jsonl` (7,807 rows, all 849 unfair clauses explained) and `data/test.jsonl` (1,607 rows).
- Running: GGUF export test on the base model.
- Not verified: the Halo config has not run yet. The dense LFM2.5 config is adapted from Halo's LFM2.5-8B-A1B MoE example. Check the field names against the image's `examples/` if the launch fails.
- Next: run the first H200 training and the eval as soon as access arrives.
