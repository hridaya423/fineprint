# Handoff: Fineprint mobile app (iOS, on-device)

You build the iPhone app for **Fineprint** at a 3-hour hackathon (White Circle track: "Build the most useful on-device AI"). Another person trains the model at the same time. Ship a small, working version first, then iterate. 100% of a simple idea beats 40% of a large one.

## The product

Fineprint reads Terms of Service and contracts on your own device and tells you, in plain English, what you agree to. A fine-tuned 1.2B model (Liquid AI LFM2.5-1.2B, trained with White Circle Halo on the UNFAIR-ToS dataset, expert-labelled) runs **on the phone**. No text leaves the device. The demo runs in airplane mode.

Judging criteria: creativity, real-world usefulness, fine-tuning effectiveness (base model compared with the fine-tuned model), and local experience (fast, practical on a consumer device).

## Stack decision (timebox it)

1. **Try first (20-minute timebox): Liquid AI's LEAP SDK**, Liquid's own on-device runtime for LFM models (iOS, Swift Package). The GGUF repo `LiquidAI/LFM2.5-1.2B-Instruct-GGUF` ships `leap/*.json` manifests, which suggests LEAP supports this model. Read the official LEAP docs first. Check one thing early: can LEAP load a **custom fine-tuned GGUF** from a local file? If it cannot, use the fallback.
2. **Fallback: llama.cpp on iOS**, either the official `llama.swiftui` example in the llama.cpp repo (SwiftUI, loads any GGUF), or Expo with `llama.rn` if React Native is faster for you.

Whichever path you use, **load the model from a file the user imports** (Files app or AirDrop into the app's Documents folder). Do not bundle it in the app. The fine-tuned GGUF arrives later; with file import it drops in without a rebuild. Start with the base model: `LFM2.5-1.2B-Instruct-Q4_K_M.gguf` from `LiquidAI/LFM2.5-1.2B-Instruct-GGUF` on Hugging Face (about 700 MB).

Run on a real iPhone if one is available, because the simulator is much slower. The simulator is acceptable for development.

## The model contract (fixed, do not change)

**One generation per clause**, with the model's chat template, greedy decoding (temperature 0), and at most 96 new tokens.

- System message: `SYSTEM_PROMPT` below, verbatim.
- User message: `clause.lowercased()` with all whitespace runs collapsed to one space and trimmed. The training data is lower-case, so this step is required.
- Do **not** use grammar or JSON-constrained decoding. The demo compares how well the base and the fine-tuned model produce valid JSON by themselves.

`SYSTEM_PROMPT`, verbatim (one line, no trailing newline):

```
You read one clause from a Terms of Service. Reply with JSON only: {"flags": [...], "plain": "..."}. "flags" lists every category that applies, chosen from: limitation_of_liability, unilateral_termination, unilateral_change, content_removal, contract_by_using, choice_of_law, jurisdiction, arbitration. "plain" is one short sentence that tells the user what they agree to. If the clause is harmless, reply {"flags": [], "plain": ""}.
```

**Reply parsing:** take the text from the first `{` to the last `}` and decode it as JSON. Keep only flags that are in the category list. If decoding fails, count the clause as "invalid output" and show no flag. The base model will often fail, and the UI must not crash when it does.

**Categories, severity and fallback text** (the app owns these; the model never decides severity):

| flag | label | severity | fallback plain text (use if `plain` is empty) |
|---|---|---|---|
| arbitration | Arbitration | high | You give up your right to sue in court. |
| limitation_of_liability | Liability limit | high | They limit what they owe you if something goes wrong. |
| unilateral_termination | Can close your account | high | They can end your account whenever they choose. |
| unilateral_change | Can change the terms | high | They can change these terms without asking you. |
| content_removal | Can remove your content | medium | They can delete what you post. |
| jurisdiction | Court location | medium | Disputes go to a court they choose. |
| choice_of_law | Governing law | medium | A law they choose applies to disputes. |
| contract_by_using | Agree by using | low | Using the service means you accept these terms. |

**Grade:** let `h` = number of distinct high flags and `m` = number of distinct medium flags in the document. Grade A if `h = 0` and `m = 0`. Grade B if `h = 0`. Grade C if `h = 1`. Grade D if `h = 2`. Grade E if `h ≥ 3`.

**Clause splitting:** split the text on blank lines, then split each block into sentences (`NLTokenizer(unit: .sentence)` in Swift, or `Intl.Segmenter` in JavaScript). Drop pieces shorter than 40 characters. Cap the count at 300. Run clauses one at a time and update the UI after each one.

## Scope v1 (build this first, then stop and test)

1. A single screen with a large text field: "Paste terms here", plus a "Check" button.
2. A progress line ("clause 37 of 210") with results that stream in as clauses finish.
3. The result view:
   - the grade (A to E), large;
   - one card per flagged clause, high severity first: label, plain sentence, and the quoted clause (original casing, not the lower-case version).
4. A settings sheet: import a `.gguf` file, and choose **Base** or **Fine-tuned** if two files are present. Show the count of "invalid output" clauses. This switch is the before/after demo for the judges.
5. Show tokens per second and total time, because "local experience" is a judging criterion.

Include 2 bundled sample ToS texts (for example, sections of the Tinder or Spotify terms) behind a "Try a sample" button, so the demo does not depend on pasting.

## After v1 works (in order, stop when time runs out)

1. **Camera scan:** photograph a paper contract (gym membership, lease) and run Apple Vision `VNRecognizeTextRequest` on the device, then check the text. This is the strongest mobile-only demo.
2. **Share sheet:** a Share Extension that accepts text from Safari ("Share → Fineprint").
3. History of checked documents, stored on the device.

## Rules

- No backend, no analytics, no network calls. The privacy claim depends on this. Test in airplane mode.
- Create the project under `~/honey/fineprint-mobile` (or the equivalent on that machine), with `git init`. Keep a `progress.md` that says what works, what does not, and how to build and run it.
- Verify visually: run the app, paste a real ToS, and look at screenshots of the result screen. Tests alone are not enough.

## Suggested skills

- `design-engineering` (primary, for the result screen), `emil-design-eng` for streaming-result motion details.
- `ponytail` and `code-deslop` for every coding step.
- `computer-use` to drive the simulator and take screenshots.
- `verification-before-completion` before you say v1 is done.
