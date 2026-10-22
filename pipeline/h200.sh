#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

HOST=${HOST:-h200}
REMOTE=/data/fineprint

case "$1" in
  push) rsync -rltz --exclude .git --exclude models --exclude checkpoints ./ "$HOST:$REMOTE/" ;;
  train) ssh "$HOST" "cd /workspace && HF_HOME=/data/hf halo launch sft $REMOTE/pipeline/sft.yaml ${*:2} 2>&1 | tee $REMOTE/train.log" ;;
  pull)
    CKPT=$(ssh "$HOST" "ls -d $REMOTE/checkpoints/fineprint-1.2b/checkpoint-* | sort -V | tail -1")
    rsync -rltz --delete --exclude 'optimizer.pt' --exclude 'rng_state*' "$HOST:$CKPT/" models/fineprint-hf/
    uv run --no-project --with huggingface_hub hf download LiquidAI/LFM2.5-1.2B-Instruct tokenizer_config.json special_tokens_map.json --local-dir models/fineprint-hf
    ;;
  *) echo "usage: pipeline/h200.sh push|train [--key=value ...]|pull" >&2; exit 1 ;;
esac
