<img src="assets/icon.svg" width="64" height="64" alt="">

# Fineprint

Fineprint reads terms of service, privacy policies and subscription terms on your own laptop and tells you, in plain English, what you agree to. It flags the clauses that cost you money or rights — free trials that turn paid, no refunds, price rises, hard-to-cancel plans, forced arbitration, data sold for ads — quotes each one, and grades the document from A to E. Nothing leaves the device.

The model is Liquid AI LFM2.5-1.2B-Instruct, fully fine-tuned with White Circle Halo on one H200. It ships as a 700 MB Q4_K_M GGUF and runs in `llama-server`.

## Results

Scored on held-out test clauses (the CLAUDETTE / UNFAIR-ToS test split plus held-out privacy segments).

| Model | Micro F1 | Red-flag F1 | Harmless clauses wrongly flagged |
|---|---|---|---|
| Base LFM2.5-1.2B | 0.056 | — | 970 of 1,435 |
| Fineprint v1 | 0.778 | — | 21 |
| Fineprint v2 | 0.737 | 0.824 | 34 |
| Fineprint v5 (shipped, validation set) | 0.789 | 0.841 | — |

On an M4 Pro, the Spotify Premium terms (170 clauses) take about 14 seconds. Cards stream in as each clause is read.

## Data

- `coastalcph/lex_glue` `unfair_tos`: 9,414 expert-labelled ToS clauses.
- `joelniklaus/online_terms_of_service`: 3,546 more English CLAUDETTE clauses (test-set companies excluded).
- `nguha/legalbench` OPP-115 tasks: privacy sharing, retention and opt-out segments.
- Subscription terms: 503 clauses from 20 real services (held out by service for testing) and 1,200 synthetic clauses.
- Plain-English explanations and the ads-versus-providers split were written by Claude Sonnet 5.5 as a teacher. The flags are the expert labels.

18 categories. Red ("Watch out"): `trial_converts_to_paid`, `hard_to_cancel`, `early_termination_fee`, `no_refund`, `price_can_increase`, `arbitration`, `shares_for_ads`.

## Layout

| Folder | What it is |
|---|---|
| [`chrome/`](chrome/) | Chrome extension (Manifest V3, plain JavaScript, no build step). Side panel, streaming cards, A–E grade, base versus fine-tuned comparison, grades on sign-up forms. |
| [`pipeline/`](pipeline/) | Data build, Halo SFT config, GGUF export, evaluation and the real-page checker. |
| `pages/` | Real terms pages used for testing. |

## Run it

1. Install llama.cpp (`brew install llama.cpp`).
2. Fine-tuned model on port 8081:
   `llama-server -m fineprint-v5-Q4_K_M.gguf --port 8081 -np 32 -c 32768 -b 4096 -ub 2048 -fa on`
3. Base model on port 8080, for the comparison:
   `llama-server -hf LiquidAI/LFM2.5-1.2B-Instruct-GGUF:Q8_0 --port 8080 -np 8 -c 16384 -fa on`
4. Open `chrome://extensions`, turn on Developer mode, click "Load unpacked", and pick `chrome/`.
5. Open a terms page, click the Fineprint icon, pick Fine-tuned, and click "Check this page".

Offline demo pages: `python3 -m http.server 8765 --bind 127.0.0.1 -d chrome/fixtures`, then open `http://127.0.0.1:8765/spotify_premium.html`, `nyt.html` or `netflix.html`.

## Train it

```
uv run --no-project --with datasets python -I pipeline/build_data.py assemble
pipeline/h200.sh push
pipeline/h200.sh train --learning_rate=5e-5
pipeline/h200.sh pull
pipeline/export_gguf.sh models/fineprint-hf fineprint
python3 -I pipeline/eval.py http://127.0.0.1:8081 ft
```
