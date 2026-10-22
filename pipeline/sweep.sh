#!/usr/bin/env bash
cd /workspace
run() {
  name=$1; shift
  out=/data/fineprint/checkpoints/$name
  rm -rf $out
  halo launch sft /data/fineprint/pipeline/sft.yaml --output_dir=$out "$@" > /data/fineprint/logs/$name.log 2>&1
  ckpt=$(ls -d $out/checkpoint-* | sort -V | tail -1)
  python /data/fineprint/pipeline/val_gpu.py $ckpt $name >> /data/fineprint/logs/$name.log 2>&1
}
mkdir -p /data/fineprint/logs
run v5 --learning_rate=5e-5
