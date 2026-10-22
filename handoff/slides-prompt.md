# Prompt: build the Fineprint pitch deck

Build a pitch deck for **Fineprint**, our entry in the White Circle track ("Build the most useful on-device AI") at a 3-hour hackathon. The demo slot is about 5 minutes, so make the deck 7 to 8 slides. It must leave room for a live demo. Use large type, one idea per slide, and real numbers. Do not use stock AI imagery.

## What the judges score (White Circle sheet)

- **Creativity and originality:** how inventive the application is.
- **Real-world usefulness:** does it solve a recurring problem people actually have?
- **Effectiveness of fine-tuning:** does the specialized model perform its task better than the base model?
- **Local experience:** is it practical, responsive and usable on a consumer device?

The sheet also asks each team to present: the problem, the dataset (what existing data we found and how we adapted it), the training (how we used Halo), the result (a working demo on a local device), and the benefit (why it beats a conventional solution or the base model). It says: "A tiny model that reliably saves someone five minutes every day is more interesting than a tiny model that occasionally produces an impressive answer." It closes with: "The best project won't necessarily have the smartest model. It will have the cleverest use for a small one."

## The product

Fineprint reads Terms of Service and privacy policies **on your own device** and tells you, in plain English, what you are agreeing to. It ships as a Chrome extension (a side panel on any terms page) and as an iPhone app that runs the model on the phone. Nothing leaves the device, and the demo runs with Wi-Fi off.

It separates clauses into three tiers, so it does not cry wolf:
- **Watch out (red):** you give up your right to sue (arbitration and class-action waivers), and they share or sell your data for advertising.
- **Standard (grey, collapsed):** account termination, term changes, liability limits, content removal, governing law, court location, "agree by using", sharing with service providers, data retention.
- **Your controls (green):** opt-outs and settings you can use.

Each card shows a plain-English sentence and the exact quoted clause. The grade (A, C or E) depends only on red flags.

## The problem

- Nobody reads terms. McDonald and Cranor (2008) estimated that reading every privacy policy you encounter would take about 76 working days per year.
- Cloud AI summarizers mean sending every page you sign up on to a third party. A local model keeps your browsing private and costs nothing per page.

## Dataset (found, adapted, combined)

- **UNFAIR-ToS** (LexGLUE, from the CLAUDETTE project): 9,414 sentences from 50 real online Terms of Service, labelled by legal experts with 8 potentially-unfair categories.
- **OPP-115** (via LegalBench): privacy-policy segments labelled by experts for third-party sharing, data retention and user choice. 1,721 positive segments plus negatives.
- **Adaptation:** we detokenized the text, mapped everything to one JSON schema, and split third-party sharing into "for ads or sale" and "service providers". We had Claude Sonnet 5.5 write one plain-English sentence for each flagged clause. The category labels remain the experts' labels.
- **Training set:** 10,018 examples. **Held-out test set:** 1,607 ToS clauses and 552 privacy segments, never trained on.

## Training (Halo)

- **Base model:** Liquid AI LFM2.5-1.2B-Instruct.
- **Method:** full supervised fine-tune with White Circle Halo 1.1.0 on one H200. v1 took **163 seconds** of training.
- **Iteration loop:** build data, train on the H200, export to GGUF (Q8_0 1.2 GB for laptops, Q4_K_M 697 MB for phones), then score the exported file on a laptop. One loop takes minutes, so we shipped several versions during the event.

## Results (held-out UNFAIR-ToS test set, 1,607 clauses, scored on the quantized model as shipped)

| Metric | Base LFM2.5-1.2B | Fineprint v1 |
|---|---|---|
| Micro-F1 across categories | 0.056 | **0.778** |
| Unfair-clause detection F1 | 0.216 | **0.823** |
| Harmless clauses wrongly flagged (of 1,435) | 970 | **21** |
| Valid JSON output | 100% | 100% |

Headline: the base model flags two out of three harmless clauses (970 of 1,435). After fine-tuning, it flags 21. Strongest categories: choice of law (F1 0.96) and jurisdiction (0.94).

On the real Spotify Terms of Use (277 clauses), Fineprint v1 found both arbitration clauses, with quotes and plain-English explanations, for example: "Disputes must go to individual arbitration, not court or class actions."

**Placeholders to fill before the pitch:** v2 numbers (privacy categories and red-flag F1), the final speed per document on the laptop and on the phone, and a cloud-model reference if we run one.

## Suggested slide outline

1. **Title:** "Fineprint: the fine print, read for you, on your device." One screenshot of the side panel.
2. **Problem:** 76 working days per year; nobody reads terms; cloud summarizers see everything you sign up for.
3. **What it does:** the three tiers, and one card with a plain sentence and a quote.
4. **Data:** two expert-labelled public datasets, adapted into one schema, with teacher-written explanations.
5. **Training:** Halo on an H200, 163 seconds per run, the iteration loop as a diagram.
6. **Results:** the base-against-fine-tuned table; make "970 → 21" the biggest number on the slide.
7. **Live demo:** Wi-Fi off. The Chrome side panel on a real ToS, then the base/fine-tuned switch, then the phone in airplane mode.
8. **Next:** cancellation and auto-renewal terms, "What changed?" for updated terms, paper contracts by camera, more languages.

## Tone

Direct and concrete. Prefer numbers to adjectives. Present the privacy point as a fact, not a slogan: the model runs on the device, so the text of the pages you agree to never leaves it.
