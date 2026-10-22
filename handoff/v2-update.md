# Fineprint client update: v2 categories and severity

This update replaces two parts of the original handoff: the system prompt and the category table. Everything else stays the same.

## Why

Most of the original 8 categories (account closure, governing law, court location, "agree by using") are in almost every Terms of Service. If they drive the grade, every site gets a D or an E, and the grade means nothing. v2 shows only the clauses that genuinely hurt the user, and it adds privacy-policy risks.

## Step 1: do now (works with the current model)

Replace the severity table and the grade rule. Standard clauses no longer affect the grade.

| flag | label | tier | fallback plain text |
|---|---|---|---|
| arbitration | You cannot sue them | red | You give up your right to sue in court or join a class action. |
| shares_for_ads | Your data goes to advertisers | red | They share or sell your data for advertising. |
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

UI:
- **Red** cards go at the top, under the heading "Watch out".
- **Standard** clauses collapse into one line, for example "9 standard clauses". Expanding it shows their cards.
- **Good** cards go in a short "Your controls" section at the end.

Grade: let `r` = the number of distinct red flags in the document. Grade A if `r = 0`. Grade C if `r = 1`. Grade E if `r = 2`.

Unknown flags still get dropped. The four privacy flags (`shares_for_ads`, `shares_with_providers`, `keeps_data`, `can_opt_out`) appear only after the v2 model ships. The table already works with the current model.

## Step 2: when the v2 model ships

Replace `SYSTEM_PROMPT` with this text, verbatim (one line, no trailing newline):

```
You read one clause from a Terms of Service or a privacy policy. Reply with JSON only: {"flags": [...], "plain": "..."}. "flags" lists every category that applies, chosen from: limitation_of_liability, unilateral_termination, unilateral_change, content_removal, contract_by_using, choice_of_law, jurisdiction, arbitration, shares_for_ads, shares_with_providers, keeps_data, can_opt_out. "plain" is one short sentence that tells the user what they agree to. If the clause has none of these, reply {"flags": [], "plain": ""}.
```

Privacy-policy pages work the same way as ToS pages: split into clauses, lower-case, one request per clause. For the demo, test on a real privacy policy page as well as a ToS page.
