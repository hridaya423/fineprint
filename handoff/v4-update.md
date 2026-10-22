# Fineprint client update: v4 (subscriptions, speed)

This update replaces the system prompt, the category table and the request settings from earlier handoffs. Use it together with the v4 model files (`fineprint-v4-Q4_K_M.gguf`).

## 1. Clause requests (faster)

The v4 model uses a short system prompt. It cuts each request from about 210 tokens to about 80, which is about 3× faster.

```
POST http://127.0.0.1:{port}/v1/chat/completions
{
  "messages": [
    {"role": "system", "content": "Flag this Terms of Service or privacy policy clause as JSON."},
    {"role": "user", "content": normalize(clause)}
  ],
  "temperature": 0,
  "max_tokens": 80,
  "stop": ["[]"]
}
```

- `normalize(clause)` stays the same: lower case, whitespace collapsed, trimmed.
- `"stop": ["[]"]` ends a harmless clause right after `{"flags": []`. The reply then has no closing `}`, and the parser treats it as "no flags", as before. Flagged clauses are not affected.
- Send up to 32 requests at the same time.

## 2. Server settings (fastest measured on an M4 Pro)

```
llama-server -m fineprint-v4-Q4_K_M.gguf --port 8081 -np 32 -c 32768 -b 4096 -ub 2048 -fa on
```

Measured: about 19 clauses per second, so a 300-clause ToS takes about 16 seconds.

## 3. Show results fast

- Sort clauses before sending them. Send clauses first if they contain any of: renew, trial, cancel, refund, fee, price, arbitration, class action, terminate, liability, sell, advertis. Send the rest afterwards.
- Stream the cards as each reply arrives. Do not wait for the whole page. The first red card should appear within 1 to 2 seconds.

## 4. Category table (replaces earlier tables)

| flag | label | tier | fallback plain text |
|---|---|---|---|
| trial_converts_to_paid | Free trial turns paid | red | Your free trial becomes a paid plan unless you cancel in time. |
| hard_to_cancel | Hard to cancel | red | Cancelling takes more than a click. |
| early_termination_fee | Fee to leave early | red | You pay a fee if you cancel before the minimum term ends. |
| no_refund | No refunds | red | You do not get money back for unused time. |
| price_can_increase | Price can go up | red | They can raise the price. |
| arbitration | You cannot sue them | red | You give up your right to sue in court or join a class action. |
| shares_for_ads | Your data goes to advertisers | red | They share or sell your data for advertising. |
| auto_renews | Renews automatically | standard | It renews and charges you automatically until you cancel. |
| shares_with_providers | Shares data with partners | standard | They share your data with companies that work for them. |
| keeps_data | Keeps your data | standard | They keep your data for a period they choose. |
| limitation_of_liability | Liability limit | standard | They limit what they owe you if something goes wrong. |
| unilateral_termination | Can close your account | standard | They can end your account whenever they choose. |
| unilateral_change | Can change the terms | standard | They can change these terms without asking you. |
| content_removal | Can remove your content | standard | They can delete what you post. |
| jurisdiction | Court location | standard | Disputes go to a court they choose. |
| choice_of_law | Governing law | standard | A law they choose applies to disputes. |
| contract_by_using | Agree by using | standard | Using the service means you accept these terms. |
| can_opt_out | You can opt out | good | You can change this in your settings. |

Order the red cards so the subscription flags come first: they cost the user money.

Grade: let `r` = the number of distinct red flags. Grade A if `r = 0`, B if `r = 1`, C if `r = 2`, D if `r = 3`, E if `r ≥ 4`.

## 5. New: offer summary (checkout pages)

On a page with a "Start free trial", "Subscribe" or "Join" button, send the text near the button (about 30 to 150 words) once:

```
{
  "messages": [
    {"role": "system", "content": "Extract the subscription offer from this checkout text as JSON."},
    {"role": "user", "content": checkoutText}
  ],
  "temperature": 0,
  "max_tokens": 160
}
```

Do not lower-case this text. The reply is JSON with these keys (each one can be null): `trial`, `then`, `auto_renews`, `first_charge`, `cancel`, `refund`, `watch_out`.

Show it as one card at the top: "7 days free → then £11.99/month · renews automatically · cancel: anytime in Settings". Put `watch_out` underneath in red if it is not empty.

**Reminder button:** if `trial` is set, show "Remind me before I'm charged". It makes an `.ics` calendar file on the device, dated 2 days before the trial ends, with the title "Cancel {site} trial before you are charged {then}". No network is needed.
