#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

SRC=${1:-models/fineprint-hf}
NAME=${2:-fineprint}
LLAMA=/tmp/llama.cpp
mkdir -p models

[ -d $LLAMA ] || git clone --depth 1 https://github.com/ggml-org/llama.cpp $LLAMA
uv run --no-project --python 3.12 --with-requirements $LLAMA/requirements/requirements-convert_hf_to_gguf.txt \
  python $LLAMA/convert_hf_to_gguf.py "$SRC" --outtype bf16 --outfile "models/$NAME-BF16.gguf"
llama-quantize "models/$NAME-BF16.gguf" "models/$NAME-Q8_0.gguf" Q8_0
llama-quantize "models/$NAME-BF16.gguf" "models/$NAME-Q4_K_M.gguf" Q4_K_M
ls -lh models/$NAME-*.gguf
