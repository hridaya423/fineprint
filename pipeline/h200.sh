#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

HOST=${HOST:-h200}
REMOTE=/workspace/fineprint
IMAGE=public.ecr.aws/whitecircle/halo:hopper
RUN="docker run --gpus all --rm --ipc=host -v $REMOTE:$REMOTE -v \$HOME/.cache/huggingface:/root/.cache/huggingface -w $REMOTE $IMAGE"

case "$1" in
  setup) ssh "$HOST" "mkdir -p $REMOTE && docker pull $IMAGE" ;;
  push) rsync -az --exclude .git --exclude models --exclude checkpoints ./ "$HOST:$REMOTE/" ;;
  train) ssh "$HOST" "$RUN halo launch sft pipeline/sft.yaml ${*:2}" ;;
  eval) ssh "$HOST" "$RUN python pipeline/eval.py $2 $3" ;;
  pull)
    rsync -az "$HOST:$REMOTE/eval/" eval/
    rsync -az --exclude 'checkpoint-*' "$HOST:$REMOTE/checkpoints/fineprint-1.2b/" models/fineprint-hf/
    ;;
  *) echo "usage: pipeline/h200.sh setup|push|train|eval <model> <name>|pull" >&2; exit 1 ;;
esac
