from emit import add
add([
("""We and our partners use cookies and similar technologies to store and access personal data. Accept all | Reject all | Show purposes

-----
STORMCAST PRO
-----
Try free for 7 days
$3.99 per month after
Renews automatically. Cancel in the app before the trial ends or you will be charged.
Sign in | Restore | Terms""",
 "7 days free", "$3.99/month", True, "after the trial", "in the app before the trial ends", None, ""),
("""HOME CHEF MEAL KIT 

NEW CUSTOMER OFFER
60% OFF YOUR FIRST BOX
THEN 25% OFF YOUR NEXT 2 BOXES
THEN FULL PRICE $71.88 PER BOX

DELIVERY EVERY WEEK UNLESS SKIPPED. CANCEL OR SKIP BY 5PM FRIDAY. SHIPPING $8.99 PER BOX.""",
 "60% off your first box", "$71.88/box", True, None, "or skip by 5pm Friday", None, "Full price of $71.88 per box plus $8.99 shipping applies from the fourth weekly box."),
("""Looking for a way to learn music theory? Join Notation Station. No ads. Cancel anytime. 
 
Price: £6.50/month
Trial: 14 days
 
Billing: starts the day your trial ends. Renewal: automatic every month. Payment: card or PayPal. Refund: contact us within 7 days of any payment.""",
 "14 days", "£6.50/month", True, "the day your trial ends", "anytime", "contact us within 7 days of any payment", ""),
("""Buy SnapShot Cam 2 — $129. Includes 3 months of free cloud storage. After 3 months, storage is $3/month if you want to keep recordings. Camera works without it. Subscription starts automatically after 3 months unless you opt out in the app. One-time hardware cost, 30-day returns.""",
 "3 months free cloud storage", "$3/month", True, "after 3 months", "opt out in the app", "30-day returns on the camera", ""),
("""YOUR SPOT IS RESERVED
Complete checkout to start the 'Everyday Chef' program.
$0 today
Day 8: $197
Then $97 each month for 12 months
Total: $1,361
We will charge your card each month. No cancellations after day 14. Results vary.""",
 "7 days at $0", "$97/month", True, "day 8: $197", "no cancellations after day 14", None, "You owe $1,361 in total, and cancelling isn't allowed after day 14."),
("""Free book offer! Claim your free copy of "The Quiet Mind" — just cover $6.95 shipping. By claiming, you also start a 30-day trial of Mindful Monthly. After the trial, $29.95 will be charged monthly. Cancel by phone within 30 days to stop. Shipping fee non-refundable.""",
 "free book, pay $6.95 shipping; 30-day trial", "$29.95/month", True, "after the trial", "by phone within 30 days", "shipping fee non-refundable", "Claiming the free book starts a $29.95 monthly charge after 30 days unless you phone to cancel."),
("""Welcome to the Library of Sounds. Annual plan, £60. Pay today to unlock 20,000 sound effects. Auto-renew is OFF by default. At expiry you keep any sounds you've downloaded under licence. No refunds after download.""",
 None, "£60/year", False, "today", None, "no refunds after download", ""),
("""Unlimited Coffee Club — a cup a day at 300 cafés. €24.99 a month, first month free. Cancel with 14 days' notice. After the first month your card will be debited on the same date each month. One coffee per 24 hours; no refunds for unused days.""",
 "first month free", "€24.99/month", True, "after the first month", "with 14 days' notice", "no refunds for unused days", ""),
("""Final Step ▸ Choose how to pay for your plan
 Monthly: $12.99
 Annual: $79.99
 Lifetime: $249.99 (one-time)
Selected: Lifetime. You'll pay $249.99 now, once. No renewals, ever. Refund within 14 days. Taxes where applicable.""",
 None, "$249.99 one-time", False, "now", None, "refund within 14 days", ""),
("""Bluebell Baby Box. Everything for your newborn, delivered every month, £35. Sign up today and get your first box for £10. Billed the 1st of each month, from next month. Cancel before the 25th. Unwanted items can be exchanged within 14 days.""",
 "first box for £10", "£35/month", True, "the 1st of each month, from next month", "before the 25th", "unwanted items can be exchanged within 14 days", ""),
("""Get unlimited storage for your photos. PhotoVault: 5 TB. We offer a 30-day free trial. Then $19.99 a month; if you choose annual, you pay $239.88 up front. Plans renew automatically and prices may rise annually. Cancelling does not delete your photos for 60 days.""",
 "30 days free", "$19.99/month", True, None, None, None, "Prices may rise each year and plans renew automatically."),
("""Uni Textbook Rental. Rent for the semester: $39.99. Return by 15 January. Late fee: $1 a day, up to the book's price. If not returned within 30 days you are charged the full replacement value of $149. Rental is a one-time payment.""",
 None, "$39.99 one-time", False, None, None, None, "A late return costs $1 a day, and after 30 days you are charged the full $149 replacement value."),
("""RISE AND GRIND MOTIVATION APP
Start for FREE: 7 days
Weekly plan $7.99 (auto-renews)
Cancel anytime in iTunes
By tapping 'Start' you agree to the Terms & conditions
Prices may vary""",
 "7 days free", "$7.99/week", True, None, "anytime in iTunes", None, ""),
("""Welcome to Cloudy Backup. Special: 50% off for 3 months, then regular price $15/month. Plan renews monthly until cancelled. We will bill your card $7.50 today. Cancel anytime from your account. Annual billing available at checkout.""",
 "50% off for 3 months", "$15/month", True, "today", "anytime from your account", None, ""),
("""Charity membership: Friends of the Heron Marsh. Annual £35, Direct Debit £3 a month. Your membership continues until you tell us to stop. You can cancel at any time by calling 01234 555 087. Gift Aid declaration included if you are a UK taxpayer. Joining pack free.""",
 None, "£3/month", True, None, "at any time by calling 01234 555 087", None, ""),
("""Smart Lock Cloud Service. Free for 1 year with your lock. Then $29.99 per year. Renews automatically; we'll email 30 days before. Without it, remote unlock stops working but keypad still works. Cancel any time.""",
 "1 year free", "$29.99/year", True, None, "any time", None, ""),
("""cookie preferences - Accept - Reject

Mamba Mobile 
Free SIM. First month £0.
Then £10 a month for 12GB.
30 day rolling contract.
Cancel any time online.
Credit card needed to activate.
Price will increase by £2 in April.""",
 "first month £0", "£10/month", True, None, "any time online", None, "The price will rise by £2 in April."),
("""Annual Premium Membership for Truck Drivers: $119. Includes discount fuel and parking. Pay now and your membership is activated instantly. Auto-renews on the anniversary. Cancel renewal by phone. Fees are non-refundable.""",
 None, "$119/year", True, "now", "cancel renewal by phone", "fees are non-refundable", ""),
("""Tonight's Special: unlock WordFlow Plus for 99¢... 7 day trial, then $9.99 per month. Auto renews. Cancel any time under Account. We'll charge 99¢ now.""",
 "7 days for 99¢", "$9.99/month", True, "now", "any time under Account", None, ""),
("""Streaming Anime Hub: Standard plan £5.99/mo, includes 14 days free. Charges begin when the 14 days are over. A subscription runs until you cancel it. You'll be given 7 days' warning before the first charge. Cancel at any time in your profile.""",
 "14 days free", "£5.99/month", True, "when the 14 days are over", "at any time in your profile", None, ""),
("""YEARLY GARDEN CLUB CARD. 12 months of discounts for £15. Pay once; enjoy till 31 December next year. Renewal reminder sent, no automatic charge. Card is non-transferable. Non-refundable once activated.""",
 None, "£15 one-time", False, None, None, "non-refundable once activated", ""),
("""Don't miss out on the Wildlife Weekly app. Free for 3 months. After that, $2.49 every month. Subscription renews automatically. To cancel, tap Menu, then Settings, then Manage subscription. If you delete the app, you'll still be billed. Content in English and Spanish.""",
 "3 months free", "$2.49/month", True, "after 3 months", "tap Menu, then Settings, then Manage subscription", None, "Deleting the app does not stop the monthly $2.49 charge."),
("""Business Hosting Plan: £2.99 a month for 36 months if you pay for the full term today (£107.64). Renews at £11.99 a month when the term ends. Free domain for year one. Domain renews at £17.99 a year. 30-day money-back guarantee.""",
 None, "£11.99/month", True, "today", None, "30-day money-back guarantee", "The £2.99 price lasts only 36 months; renewal is £11.99 a month, plus £17.99 a year for the domain."),
("""Trade Journal Premium — Industry News Daily. Enter your card for a free 2-week trial. If you do not cancel within 14 days we'll start a $499 annual subscription. Renews each year. Contact customer care to cancel. All fees are payable in advance and non-refundable.""",
 "2 weeks free", "$499/year", True, "after 14 days", "contact customer care within 14 days", "all fees are payable in advance and non-refundable", "A non-refundable $499 annual fee starts after 14 days unless you cancel in that window."),
("""Join The Reading Nook for free. Upgrade to Gold for an extra £2.50 a month. 30-day free trial. We'll remind you with an email 3 days before we charge you. Gold perks: early access, no ads. Cancel any time online. No contract.""",
 "30 days free", "£2.50/month", True, None, "any time online", None, ""),
("""Gutter Guard Pros maintenance plan. Two cleanings per year, $19.99 per month. Contract 12 months, auto-renews yearly. Cancellation requires 60 days written notice via certified mail. Pay $0 today; first charge in 30 days.""",
 "$0 today", "$19.99/month", True, "in 30 days", "60 days written notice via certified mail", None, "Cancelling requires 60 days' written notice by certified mail, and the contract renews yearly."),
("""Moon Phase Calendar app - lifetime unlock: $14.99. No ads, no subscriptions. This unlocks all features on your devices for life. Purchase restores on new devices. Refund requests handled by Google Play.""",
 None, "$14.99 one-time", False, None, None, "handled by Google Play", ""),
("""FitFam Premium: unlimited workouts and meal plans.
► 7-DAY FREE TRIAL
► Then £9.99/month
► Cancel any time
You will be charged £9.99 each month starting day 8. Subscriptions auto-renew unless auto-renew is turned off at least 24 hours before the end of the current period.""",
 "7 days free", "£9.99/month", True, "day 8", "any time", None, ""),
("""Welcome back, Sam! Come back to Lumo Fitness for $1 for your first month. After that, $34.99 each month. Your membership restarts when you click below. Cancel anytime. Prior members only. We will not send a reminder about renewal.""",
 "$1 for your first month", "$34.99/month", True, None, "anytime", None, "No renewal reminder is sent, and the $1 month turns into $34.99 afterwards."),
("""Pick 3 meals a week for £24.99. Prefer 5? £39.99. Selected: 3 meals. Weekly charge. Free delivery on your first box. Pause or cancel until midnight Thursday before the next delivery. Boxes can't be returned, but we'll credit missing items.""",
 "free delivery on your first box", "£24.99/week", True, None, "until midnight Thursday before the next delivery", "boxes can't be returned, but missing items are credited", ""),
("""Scholar Plus. 14 days free. Then you'll be enrolled in the annual plan at $108/yr. 'Why annual?' Because we found students prefer it. Switch to monthly ($14.99) in Billing. Auto-renews. Cancel at least 3 days before renewal to avoid being charged.""",
 "14 days free", "$108/year", True, None, "at least 3 days before renewal", None, "You're enrolled in the $108 annual plan by default, not the $14.99 monthly one."),
("""SIGN-UP FOR OUR NEWSLETTER 'TREND WATCH'. FIRST ISSUE FREE. THEN $9 AN ISSUE. 4 ISSUES PER MONTH. PAY MONTHLY $36. CANCEL ANYTIME BY REPLYING STOP TO ANY EMAIL. YOU CAN ALSO CANCEL BY CALLING 1-800-555-0101.""",
 "first issue free", "$36/month", True, None, "anytime by replying STOP to any email, or by calling 1-800-555-0101", None, ""),
("""Gift subscriptions at The Stationery Society: 3 months £30, 6 months £55, 12 months £100. Gift recipients are not charged. One-off payment from you. Does not renew. Redeemable within 12 months. Refund possible before redemption, minus 10%.""",
 None, "£100 one-time", False, None, None, "refund possible before redemption, minus 10%", ""),
("""Welcome to Pulse Oximeter Companion app. Premium unlocks history and export. Monthly $2.99. Start with 5 days free. Your Google Play account will be charged $2.99 on day 6. Subscription renews monthly. Manage in the Google Play Store.""",
 "5 days free", "$2.99/month", True, "on day 6", "in the Google Play Store", None, ""),
("""LEARN TO TRADE. 7-DAY TRIAL FOR $7. After 7 days: $297 per month. 'Elite Circle' membership. Billed every 30 days. Cancellation: submit a ticket 5 business days before billing. Past payments are not refunded. Past performance is not indicative of future results.""",
 "7 days for $7", "$297/month", True, "after 7 days", "submit a ticket 5 business days before billing", "past payments are not refunded", "After the $7 trial, $297 is billed every 30 days unless you file a ticket five business days ahead."),
("""Pressed Juice Co. Subscribe and save 20%. 6 bottles delivered every week for $44.00 (usually $55.00). Pay when your order ships. Change, skip or cancel at any time until the order ships. No contract. Product is perishable and non-returnable.""",
 None, "$44.00/week", True, "when your order ships", "at any time until the order ships", "product is perishable and non-returnable", ""),
("""Join the Orchard Players theatre club. £8 a month gives you ticket discounts and priority booking. First 2 months free. After 2 months, £8 each month by standing order. Cancel by cancelling your standing order and emailing us.""",
 "first 2 months free", "£8/month", True, "after 2 months", "cancel your standing order and email us", None, ""),
("""Your PDF toolkit is waiting. Start 7-day trial, then $11.99 per month. Plans automatically renew monthly. IMPORTANT: Cancellations must be made before trial ends. We do not cancel on your behalf and cannot issue refunds after renewal.""",
 "7 days", "$11.99/month", True, "after the trial", "before the trial ends", "cannot issue refunds after renewal", ""),
("""Sunset Sounds ambient music. Choose a plan: Week $4.99 | Month $9.99 | Year $29.99. Year is pre-selected, with a 3-day free trial. Auto renewing. Billed $29.99 at the end of the trial. Cancel at least 24 hours before the trial ends.""",
 "3 days free", "$29.99/year", True, "at the end of the trial", "at least 24 hours before the trial ends", None, ""),
("""Pay As You Go Printing: 5p per page black & white, 15p colour. Top up your account from £5. Credit never expires. No subscription. Top-ups are non-refundable but unused credit can be transferred to another account.""",
 None, "5p per page", False, None, None, "top-ups are non-refundable", ""),
("""Netly Wi-Fi Boost. Start 1-month trial at $0. $9.99 a month after. Add to your existing Netly plan. Cancel any time from your Netly app. Your bill will show the charge as a service add-on. Billed with your monthly internet bill.""",
 "1 month at $0", "$9.99/month", True, "after the trial, with your monthly bill", "any time from your Netly app", None, ""),
("""Welcome to Hiker's Union — outdoor gear club. £5 joining fee today. Members save 20% on all gear. Annual membership auto-renews at £45 per year unless you cancel. Cancel by letter to Hiker's Union, 4 Ridge Rd. Joining fee is not refunded.""",
 None, "£45/year", True, "today", "by letter to Hiker's Union, 4 Ridge Rd", "joining fee is not refunded", ""),
("""Coach's Corner Soccer Training App. 7 days free then $5.99/mo. The Pro plan renews each month. Charges appear on your statement as CC-SOCCER. Cancel anytime in app settings or by writing to support. Billing disputes: contact us first, we reply within 24 hours.""",
 "7 days free", "$5.99/month", True, "after 7 days", "anytime in app settings or by writing to support", None, ""),
("""Be part of Solar Neighbors. Rooftop solar lease with $0 down. Pay $129/month for 20 years. Rate increases 2.9% every year. Early termination or transfer requires full payoff or buyout. Includes maintenance and monitoring.""",
 "$0 down", "$129/month", None, None, None, None, "Payments run for 20 years, rise 2.9% every year, and leaving early requires a full payoff or buyout."),
("""Play Together: family games night in a box. $29.99 per month. First box free with the code FAMILYFIRST (just pay $5.95 shipping). Billed from box two. Cancel online until the day before shipping. Games can be returned in 30 days.""",
 "first box free with code FAMILYFIRST (pay $5.95 shipping)", "$29.99/month", True, "from box two", "online until the day before shipping", "games can be returned in 30 days", ""),
("""Keep your yard spotless. Monthly lawn mowing plan from $65 per visit. Visits every 2 weeks March–October. Card billed after each visit. No contract; text STOP to cancel. Rain delays may postpone visits.""",
 None, "$65/visit every 2 weeks", True, "after each visit", "text STOP", None, ""),
("""I want to go Premium
Annual: €29.99
Monthly: €3.99
Best choice: Annual
Free for 7 days, then €29.99. Renews yearly. Cancel in Google Play. Payment is charged to your Google account after the 7 days end.""",
 "7 days free", "€29.99/year", True, "after the 7 days end", "in Google Play", None, ""),
("""Introducing Wandr Travel Club. Get 2 months free when you sign up. Members get 15% off hotels. After 2 months, £9.99 per month. Min. 6 months membership. Auto-renews monthly after. Cancel with 30 days' notice. You pay £9.99 on day 61.""",
 "2 months free", "£9.99/month", True, "on day 61", "with 30 days' notice", None, ""),
("""CROSSWORD HEAVEN
 
$1.99 FOR 7 DAYS 
THEN $14.99 EVERY 4 WEEKS
(That's $195 per year)
RENEWS AUTOMATICALLY. CANCEL ANYTIME IN SETTINGS.""",
 "7 days for $1.99", "$14.99 every 4 weeks", True, None, "anytime in Settings", None, "At $14.99 every 4 weeks you pay about $195 a year."),
("""Lone Wolf VPN extended offer: pay €71.76 today for 24 months (€2.99/mo). Renews for 12 months at €59.88 after the term. Cancel auto-renewal in Account > Billing. 30-day no-risk refund.""",
 None, "€59.88/year", True, "today", "auto-renewal in Account > Billing", "30-day no-risk refund", ""),
("""Spice Route cooking kits. Every month a new cuisine, $24. Sign up today & get your first kit at $9.99. Subscribers can skip any month. Your card is charged on the 15th. To cancel, use the link in your account by the 10th. No returns on food.""",
 "first kit $9.99", "$24/month", True, "on the 15th", "use the link in your account by the 10th", "no returns on food", ""),
("""Language Exchange Network. Pay $0.00 now, 3-day trial, then $99.99/yr. Cancel any time during the trial; no charge. Your yearly subscription will auto-renew. Group lessons billed separately at $15 each.""",
 "3 days at $0.00", "$99.99/year", True, "after the trial", "any time during the trial", None, ""),
("""Sports Almanac Online — £4.50 a month. 30 days free. To thank you for joining, here is a free e-book. Auto-renewing. We will charge you after 30 days. You may cancel at any time. Thank you for supporting independent sports journalism.""",
 "30 days free", "£4.50/month", True, "after 30 days", "at any time", None, ""),
])
