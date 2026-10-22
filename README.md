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

The base model flags nearly every clause, so its output is useless. Fineprint flags only the traps.

## Real companies

| Service | Grade | What Fineprint found |
|---|---|---|
| Spotify Premium | D | The fee recurs "as amended from time to time" until you cancel; the trial turns paid automatically; no refunds |
| New York Times | C | "To end your account, you must call Customer Care or use their chat", during limited hours; forced arbitration |
| Netflix | C | "Payments are non-refundable"; they can change your plan and the price |

## Speed

M4 Pro, llama.cpp, Q4_K_M, flash attention, 32 parallel requests. The Spotify Premium terms (170 clauses) take about 14 seconds. The first version took 56 seconds for a page of similar size.

- The model is trained on a 12-word system prompt, so no long instructions are needed for each clause.
- Generation stops as soon as the model returns an empty list of flags, so harmless clauses cost about 5 output tokens.
- The cards stream in as each clause is read.

## Features

- Side panel with streaming cards: each card has a plain-English sentence and the quoted clause. Clicking a card highlights the clause on the page.
- A to E grade, by the number of distinct red flags.
- Clauses of the same kind are grouped into one card, which expands to show all the evidence.
- A document map of the page that shows where the flags are.
- Base versus fine-tuned switch with a side-by-side comparison.
- Sign-up forms (opt-in): a grade badge next to "I agree to the Terms" links, checked automatically.
- "What changed?": compares two versions of a document and shows only the new flags.
- Works offline. Nothing leaves the device.

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
4. Open `chrome://extensions`, turn on Developer mode, click "Load unpacked", and pick `chrome/`. A packaged copy is on the [v1.0 release](https://github.com/hridaya423/fineprint/releases/tag/v1.0).
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

## Future scope

- **Phones:** the 700 MB model fits on a phone (llama.cpp on Android, MLX on iOS). A share-sheet action and an overlay above checkout screens would grade terms inside apps, where most subscriptions are sold.
- **More document types:** employment contracts (non-compete clauses, IP assignment, notice periods), rental leases (deposits, fees, automatic renewal), loan and credit card agreements, gym and phone contracts, insurance policies. Each one needs a labelled dataset and the same Halo fine-tune.
- **Checkout summary:** one card above the "Start free trial" button: "7 days free → then £11.99/month · renews automatically · cancel in Settings". The data for this is already built (`sub_offer`).
- **Trial reminders:** a calendar file made on the device, set for two days before the trial charges.
- **Change alerts:** when a service updates its terms, show only what got worse.
- **Other languages:** CLAUDETTE already has German, Italian and Polish labels.
