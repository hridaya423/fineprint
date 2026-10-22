from emit import add
add([
("""Start your Moonrise Fitness journey. 7-day pass: free. Membership: $10/month for the first 3 months, $30/month after. 12-month agreement, auto-renews monthly after. Annual fee $39. Cancellation requires a signed form, available at the front desk only, and 30 days' notice.""",
 "7-day pass: free", "$30/month", True, None, "signed form at the front desk only with 30 days' notice", None, "After three months the fee triples to $30, plus a $39 annual fee, and cancelling needs a signed in-person form."),
("""PicklePlay League App Premium - Free for the first 14 days. Afterwards: €3.99/mo. Pay for 12 months at once and save 25%. Cancel any time online. Remember to cancel before the trial ends if you don't want to continue; renewal is automatic. VAT included.""",
 "14 days free", "€3.99/month", True, "after the 14 days", "any time online", None, ""),
("""Crush Calories Pro unlocks everything. Choose: Weekly $6.99 / Monthly $14.99 / Yearly $59.99 (selected). Start your free 3-day trial. Subscription automatically renews. After the trial, your Google account is charged $59.99. Cancel in Google Play: Menu > Subscriptions.""",
 "3 days free", "$59.99/year", True, "after the trial", "in Google Play: Menu > Subscriptions", None, ""),
("""Pay-What-You-Want Zine Pack. Name your price from £3. This is a one-time download, no account, no subscription. If you pay £10 or more you also get the print edition shipped free in the UK. Digital downloads are not refundable.""",
 None, "from £3 one-time", False, None, None, "digital downloads are not refundable", ""),
("""Upgrade to Sprout Pro. Get 2 months free when you pay annually. $120 per year billed today ($10 per month, 2 months free applied). Renews every year at $120. To cancel, contact support@sprout.example at least 7 days before the renewal date. Refunds within 7 days of any charge.""",
 "2 months free", "$120/year", True, "today", "contact support@sprout.example at least 7 days before the renewal date", "refunds within 7 days of any charge", ""),
("""Cookies on this site: we use them for ads. | Agree | More options |

ENJOY UNLIMITED TV — 1ST MONTH £0 — THEN £11.99/MO
Cancel online before your free month ends to avoid being charged.
Auto-renews. No refund for the final month.
Terms · Privacy · Help""",
 "1st month £0", "£11.99/month", True, "after the free month", "online before your free month ends", "no refund for the final month", ""),
("""BARK & BOW Dog Training Online. Join now: $1 for 14 days. After 14 days, you're charged $47 per month until you cancel. Please note that cancellation requests must be made at least 3 business days before billing. We cannot refund charges after they are processed.""",
 "14 days for $1", "$47/month", True, "after 14 days", "at least 3 business days before billing", "cannot refund charges after they are processed", "The $1 trial turns into $47 a month and processed charges can't be refunded."),
("""Daily Horoscope Plus. Premium readings, $8.99 each month. Includes a 3-day trial for $0. Your subscription will begin automatically after the trial and will renew each month. Cancel online by visiting Manage Plan. Questions? Contact us via the form.""",
 "3 days for $0", "$8.99/month", True, "after the trial", "online by visiting Manage Plan", None, ""),
("""Wine Fridge Rental Offer: 6 months FREE rental, then £15 a month. Rental continues until you return the fridge. Return fee £30 if not collected within 14 days. If you keep the fridge more than 24 months you own it. Refundable £50 deposit.""",
 "6 months free rental", "£15/month", True, None, "return the fridge", "£50 deposit refundable", "Returning the fridge incurs a £30 fee if it isn't collected within 14 days."),
("""Try our Pro features free for 10 days. Pricing after trial: $12/month. We will not auto-charge you. At the end of the trial your account reverts to Free unless you choose to upgrade. No card needed.""",
 "10 days free", "$12/month", False, None, None, None, ""),
("""Upgrade to Carbon Browser Sync. $2/month, billed every 12 months ($24). First month free. You'll be charged $24 at the end of the free month. Renews yearly at $24. 100% refund guaranteed for 30 days.""",
 "first month free", "$24/year", True, "at the end of the free month", None, "100% refund guaranteed for 30 days", ""),
("""Get the Compass membership card: £10 joining fee, then £5.95 a month. Includes breakdown cover. Direct Debit. Minimum 12 months; leaving early costs £30. After 12 months it rolls monthly. Cancel by phone on 0800 555 0172. Joining fee paid today.""",
 None, "£5.95/month", True, "today", "by phone on 0800 555 0172", None, "Leaving before 12 months costs £30, on top of the £10 joining fee."),
("""Weekly crossword + puzzles in your inbox. Join Wordsmith Club: 4 weeks for €1, then €2.99 every 4 weeks. Auto-renews. Cancel anytime via the unsubscribe page. You are billed on the day you sign up and every 4 weeks thereafter. Refunds on request within 7 days.""",
 "4 weeks for €1", "€2.99 every 4 weeks", True, "on the day you sign up", "anytime via the unsubscribe page", "refunds on request within 7 days", ""),
("""Kinder Math. Unlock the full program. Free trial: 7 days. Monthly $9.99. Yearly $79.99. When you start the trial you'll be asked to confirm with Face ID. Your account will be charged when the trial ends. Cancel by switching off auto-renew in your iPhone settings.""",
 "7 days free", "$9.99/month", True, "when the trial ends", "switching off auto-renew in your iPhone settings", None, ""),
("""Everything Sale! Buy the 'Photoshoot Presets' pack for $29 — one-time. Instant download of 120 presets. Not a subscription. No future charges. If you have issues we'll help; otherwise, no refunds on digital products.""",
 None, "$29 one-time", False, None, None, "no refunds on digital products", ""),
("""Sign-up bonus! Join the Vine Rewards wine club and receive 3 bottles for £19.99 including delivery. Then we'll send 6 bottles every month at £71.94 — you can pause or cancel by emailing orders@vinerewards.example before the 10th each month. Orders cannot be returned once opened.""",
 "3 bottles for £19.99", "£71.94/month", True, None, "by emailing orders@vinerewards.example before the 10th each month", "orders cannot be returned once opened", "After the £19.99 starter, £71.94 is charged monthly unless you email before the 10th."),
("""Premium Weather Radar. Remove ads and unlock hourly maps. $2.99 per month with a 7-day free trial, or $19.99 per year. Your subscription renews unless cancelled 24 hours before the renewal date. You can manage subscriptions from your account settings after purchase.""",
 "7 days free", "$2.99/month", True, None, "24 hours before the renewal date", None, ""),
("""Parcel Peak delivery membership. £3.99 a month for free next-day delivery. Try 2 months free, then £3.99 billed monthly. Membership auto-renews. Cancel in your account. Hint: remember to turn off auto-renew BEFORE the end of month two or you will be charged.""",
 "2 months free", "£3.99/month", True, "after month two", "in your account, before the end of month two", None, ""),
("""Gather — community platform. The Creator plan is $49 per month. Start with 14 days free. Your card will be billed $49 on day 15 and monthly after. Plan has a 3-month minimum. Cancel after minimum with a 7-day notice. Payments processed by Stripe.""",
 "14 days free", "$49/month", True, "on day 15", "after the 3-month minimum with 7 days' notice", None, "A 3-month minimum applies, so you can't cancel before three paid months have passed."),
("""Rise & Shine Candles... Monthly Subscription $12. Charged on the 1st. No trial. Cancel anytime. A first-order discount code was applied: WELCOME5 saves $5 on your first box ($7 charged today).""",
 "$5 off the first box with code WELCOME5", "$12/month", True, "today", "anytime", None, ""),
("""Annual Tax Software 2026 — Deluxe. $59.99, one payment. File up to 5 returns. State filings $39.99 each. Free e-file for federal. No recurring subscription. Full refund if you don't file, within 60 days of purchase.""",
 None, "$59.99 one-time", False, None, None, "full refund if you don't file, within 60 days of purchase", ""),
("""MOVIE NIGHT CLUB
START YOUR 14-DAY FREE TRIAL
AFTER TRIAL: $12.99 / MONTH
CANCEL ANYTIME
 
(by continuing, you authorize recurring payments and agree to our Terms; trial converts automatically; taxes may apply; offer valid once per household)""",
 "14 days free", "$12.99/month", True, "after the trial", "anytime", None, ""),
("""Gold Standard Cars membership. Join for $19 a month; first 3 months free. Includes oil changes and tire rotations. 24-month agreement; auto-renews for 12 months at the end unless cancelled in writing 30 days prior. Early cancellation fee $199.""",
 "first 3 months free", "$19/month", True, None, "in writing 30 days prior to the end of the term", None, "A 24-month agreement auto-renews, with a $199 fee if you cancel early."),
("""Sky Reader — digital newspapers from 1,000 titles. Your first 90 days cost only $1, then it's $19.99 a month. By pressing Subscribe you agree to automatic billing. Cancel online at any time. 14-day cooling-off right where applicable.""",
 "first 90 days for $1", "$19.99/month", True, None, "online at any time", "14-day cooling-off right where applicable", ""),
("""Choose your Nimbus Storage plan.
200 GB — £2.49/mo
2 TB — £7.99/mo  [Most popular — selected]
Free for 1 month, then £7.99 per month. VAT incl. Renews monthly. You can switch plans or cancel anytime. We refund the last payment if you cancel within 3 days.""",
 "free for 1 month", "£7.99/month", True, None, "anytime", "refund the last payment if you cancel within 3 days", ""),
("""One-Day Event Ticket – Tech Summit 2026. €149, VAT included. Single payment. Tickets are transferable but not refundable. If the event is postponed your ticket remains valid. No subscription or membership.""",
 None, "€149 one-time", False, None, None, "not refundable", ""),
("""Spark Ink Pens Club – Send me a new pen every month for $14! First pen free, just pay $3.95 shipping. Cancel anytime online or via our toll-free line. Your first $14 charge will be processed 14 days after your free pen ships. Pens can be returned in 30 days.""",
 "first pen free (pay $3.95 shipping)", "$14/month", True, "14 days after your free pen ships", "anytime online or via our toll-free line", "pens can be returned in 30 days", ""),
("""AUTO-RENEWAL NOTICE. Your Evergreen Antivirus subscription will renew on 14 March for $99.99 for another year. Not what you expected? Turn off auto-renewal at My Account. Refunds are not available after 30 days of purchase.""",
 None, "$99.99/year", True, None, "turn off auto-renewal at My Account", "not available after 30 days of purchase", ""),
("""Shortcuts to Success — audio lessons. Trial: 7 days for $0.00. Then $79.00 per quarter billed every three months. Cancel anytime. Don't see a way to cancel in the app? Email us. Pricing in USD and varies slightly by country.""",
 "7 days for $0.00", "$79.00/quarter", True, "after the trial", "anytime; email if the app has no cancel option", None, ""),
("""Welcome! Join the Wellness Collective for €29 per month. Month one is free. Contracts are rolling and can be ended with 14 days' notice by email to joinus@wellness.example. We bill by SEPA direct debit on the 1st. Pay by card? €2 surcharge applies.""",
 "month one free", "€29/month", True, "on the 1st", "with 14 days' notice by email to joinus@wellness.example", None, ""),
("""Phone Shield insurance, $13 a month. Deductible $99 screen, $149 other. Billed monthly. Renews automatically. Cancel at any time. Waiting period 30 days. No refunds on monthly charges, but you can cancel to avoid next month's. Claims limited to 2 per year.""",
 None, "$13/month", True, None, "at any time", "no refunds on monthly charges", ""),
("""Studio Ghibl... er, Studio Gable Animation Pass, 30 days of unlimited movies for $4.99. Auto-renews at $12.99 per month after your first 30 days. Cancel before renewal. We can't offer refunds on renewed periods. Prices subject to change.""",
 "30 days for $4.99", "$12.99/month", True, "after your first 30 days", "before renewal", "can't offer refunds on renewed periods", "After 30 days at $4.99 the price jumps to $12.99 per month, with no refund on renewals."),
("""Sprouts Organic Delivery. Veggie box £18, delivered weekly. First box £9. Skip weeks online. We bill the Sunday before delivery. Cancel at least 3 days before your next delivery. Contact us if anything is wrong and we'll credit your account.""",
 "first box £9", "£18/week", True, "the Sunday before delivery", "at least 3 days before your next delivery", "credit your account if anything is wrong", ""),
("""Choose your plan to continue
 ○ Pro Monthly — $19.99
 ● Pro Annual — $99.99 (billed once a year)
Includes 7-day trial. If you cancel during the trial you won't be charged.
After the trial the annual price is charged automatically and the plan renews yearly.
Prices are exclusive of tax.""",
 "7 days", "$99.99/year", True, "after the trial", "during the trial", None, ""),
("""BECOME A MEMBER! $1.00 FIRST MONTH, THEN $49.99/MO.

* Membership agreement: you agree to a minimum term of 12 months.
* Auto-renews monthly after the minimum term.
* Cancel by certified letter only.
* No refunds.

Join today and receive a free T-shirt!""",
 "$1.00 first month", "$49.99/month", True, None, "by certified letter only", "no refunds", "You commit to a 12-month minimum at $49.99 a month, and only a certified letter cancels."),
("""Storybox: personalised children's books. One book $24.99, one-time. Printed in the UK and delivered in 5–7 days. Free p&p. Personalised items cannot be returned unless faulty. Prefer a membership? Get a book each month for £19.99 — see the club page.""",
 None, "$24.99 one-time", False, None, None, "personalised items cannot be returned unless faulty", ""),
("""Free month of Ember Music. Cancel any time. After your free month: £10.99 monthly, or £109.90 annually. All new subscribers need to enter a valid payment method. We will charge it automatically after the free month. Not available with a student discount.""",
 "free month", "£10.99/month", True, "after the free month", "any time", None, ""),
("""Learn Guitar Online. Instant access: $39 one-time lifetime access to the Beginner course. Optional upgrade to the Pro Membership at $19/month: first month free, auto-renews, cancel anytime. Unticked by default; tick the box to add Pro. You're adding the Beginner course only.""",
 None, "$39 one-time", False, None, None, None, ""),
("""Zoom Fit Online Classes. Free for the first 30 days then $12.99/mo. Billing cycle starts after the trial and repeats every month. Cancel your subscription before the trial ends to stop billing. You'll receive a confirmation email. Prices may change.""",
 "free for the first 30 days", "$12.99/month", True, "after the trial", "before the trial ends", None, ""),
("""LUXE WATCH CLUB. EVERY MONTH A NEW LUXURY WATCH BOX FOR $29.90. YOU'LL BE CHARGED $29.90 TODAY. SUBSCRIPTION RENEWS EVERY 30 DAYS. TO CANCEL YOU MUST CALL 1-866-555-0154 BETWEEN 10AM AND 4PM EST. ALL SALES FINAL.""",
 None, "$29.90 every 30 days", True, "today", "you must call 1-866-555-0154 between 10am and 4pm EST", "all sales final", "Cancelling requires a phone call between 10am and 4pm EST, and all sales are final."),
("""Auto Detail Club – a monthly car wash for £19.99. Cancel any time, but note: price is per vehicle. First wash on us. Subscription is taken by Direct Debit on the 28th. We can refund the next wash if you cancel 24 hours before. Not valid on commercial vehicles.""",
 "first wash free", "£19.99/month", True, "on the 28th", "any time, 24 hours before the next wash for a refund", "refund the next wash if you cancel 24 hours before", ""),
("""Paperless Pro document scanner app. Free download. Premium: $4.99 per month after your 3-day free trial. Alternatively, a one-time lifetime purchase is available for $79.99. Premium subscription renews monthly and bills your account. Cancel at least a day prior to renewal.""",
 "3 days free", "$4.99/month", True, None, "at least a day prior to renewal", None, ""),
("""Teacher's Toolkit. Download 500 lesson plans. £29 for a single-user license, one-time. No subscription, no expiry. You may use the materials in your own classroom. Refunds within 14 days only if you haven't downloaded the files.""",
 None, "£29 one-time", False, None, None, "within 14 days only if you haven't downloaded the files", ""),
("""Join Birdsong Premium — your first 3 months are on us. Then pay €2.50 per month. Renews monthly. Free months can be used once per account. If you cancel in your first 3 months, you lose the offer and you cannot re-claim it.""",
 "first 3 months free", "€2.50/month", True, None, None, None, ""),
("""Welcome to the Neon Network. Upgrade for $0 today. Your 2-week trial of Neon Plus starts now. Afterwards a subscription of $22.99/mo begins. Neon will send a reminder 48 hours before the end of the trial. Cancel in app, or at neon.example/cancel.""",
 "2 weeks free", "$22.99/month", True, "after the trial", "in app, or at neon.example/cancel", None, ""),
("""Cookie preferences ✓ necessary ✓ marketing [Save]

Subscribe to Dispatch Daily
Intro offer: 52 weeks for £52 (that's £1 per week!)
Then £4 a week
By subscribing you accept automatic renewal. 
To cancel call 0333 555 0105. 
Terms & Conditions apply.""",
 "52 weeks for £52", "£4/week", True, None, "call 0333 555 0105", None, "The intro £1 a week quadruples to £4 a week after the first year."),
])
