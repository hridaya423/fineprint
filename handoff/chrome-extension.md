# Handoff: Fineprint Chrome extension

You build the Chrome extension for **Fineprint** at a 3-hour hackathon (White Circle track: "Build the most useful on-device AI"). Another person trains the model at the same time. Ship a small, working version first, then iterate. 100% of a simple idea beats 40% of a large one.

## The product

Fineprint reads Terms of Service on your own machine and tells you, in plain English, what you agree to. A fine-tuned 1.2B model (Liquid AI LFM2.5-1.2B, trained with White Circle Halo on the UNFAIR-ToS dataset, expert-labelled) runs locally. No text leaves the device. The demo runs with Wi-Fi off.

Judging criteria: creativity, real-world usefulness, fine-tuning effectiveness (base model compared with the fine-tuned model), and local experience (fast, practical on a consumer device).

## The model interface (fixed contract, do not change)

The model runs in `llama-server` (llama.cpp), which exposes an OpenAI-compatible API.

Start the base model now for development (Homebrew: `brew install llama.cpp`):

```bash
llama-server -hf LiquidAI/LFM2.5-1.2B-Instruct-GGUF:Q8_0 --port 8080 -np 4 -c 16384
```

Later the fine-tuned model arrives as a `.gguf` file. Run it on port 8081 with the same flags (`-m fineprint-Q8_0.gguf --port 8081`). The API is identical, so the only change is the port.

**One request per clause:**

```
POST http://127.0.0.1:{port}/v1/chat/completions
{
  "messages": [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": normalize(clause)}
  ],
  "temperature": 0,
  "max_tokens": 96
}
```

- `normalize(clause)` = `clause.toLowerCase().replace(/\s+/g, " ").trim()`. The training data is lower-case, so this step is required.
- Do **not** send `response_format`. The demo compares how well the base and the fine-tuned model produce valid JSON by themselves.

`SYSTEM_PROMPT`, verbatim (one line, no trailing newline):

```
You read one clause from a Terms of Service. Reply with JSON only: {"flags": [...], "plain": "..."}. "flags" lists every category that applies, chosen from: limitation_of_liability, unilateral_termination, unilateral_change, content_removal, contract_by_using, choice_of_law, jurisdiction, arbitration. "plain" is one short sentence that tells the user what they agree to. If the clause is harmless, reply {"flags": [], "plain": ""}.
```

**Reply parsing:** read `choices[0].message.content`. Take the text from the first `{` to the last `}` and run `JSON.parse`. Keep only flags that are in the category list. If parsing fails, count the clause as "invalid output" and show no flag. The base model will often fail, and the UI must not crash when it does.

**Categories, severity and fallback text** (the client owns these; the model never decides severity):

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

**Clause splitting:** split the text on blank lines, then split each block into sentences with `Intl.Segmenter("en", {granularity: "sentence"})`. Drop pieces shorter than 40 characters. Cap the count at 400. Send at most 4 requests at the same time (the server runs with `-np 4`).

## Scope v1 (build this first, then stop and test)

1. Manifest V3. Permissions: `activeTab`, `scripting`, `sidePanel`, `storage`. Host permission: `http://127.0.0.1/*`. Make the model calls from the service worker; with the host permission, CORS does not apply.
2. A toolbar click opens the side panel with a "Check this page" button. If the user has selected text, check only the selection. If not, check `main`, `article` or `document.body` `innerText`.
3. The side panel shows a progress bar ("clause 37 of 210"), then:
   - the grade (A to E), large;
   - one card per flagged clause, high severity first: label, plain sentence, and the quoted clause (the original text with original casing, not the lower-case version);
   - clicking a card scrolls to the clause on the page and highlights it.
4. A model switch in the side panel: **Base (8080)** or **Fine-tuned (8081)**, saved in `chrome.storage`. Show the count of "invalid output" clauses. This switch is the before/after demo for the judges.
5. A short message if the server is down: "Start the local model: llama-server …".

Test on real pages: a long ToS (for example, the Tinder, Spotify or Uber terms). Save 2 or 3 of these pages as local HTML files for the offline demo.

## After v1 works (in order, stop when time runs out)

1. Auto-detect: on pages with an "I agree" or "Terms" checkbox or link, show a small badge with the grade next to it.
2. "What changed?": paste an old and a new version, and show only the new flags.
3. Cache results per URL in `chrome.storage.local`.

## Rules

- No backend, no analytics, no remote calls apart from `127.0.0.1`. The privacy claim depends on this.
- Plain JavaScript and HTML, no build step, unless a build step saves real time.
- Create the project under `~/honey/fineprint-chrome` (or the equivalent on that machine), with `git init`. Keep a `progress.md` that says what works, what does not, and how to load the extension (`chrome://extensions` → Load unpacked).
- Verify visually: load the extension, run it on a real ToS page, and look at screenshots of the side panel. Tests alone are not enough.

## Suggested skills

- `design-engineering` (primary, for the side panel UI), `emil-design-eng` for the card and progress interaction details.
- `ponytail` and `code-deslop` for every coding step.
- `computer-use` or `anthropic-skills:chrome-browser` to load and screenshot the extension.
- `verification-before-completion` before you say v1 is done.
