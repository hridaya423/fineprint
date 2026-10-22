from emit import add
add([
("""cookie settings | accept all cookies

GET QUILLPAD UNLIMITED
$0.00 due today
Free for 7 days; $8.33/mo billed annually at $99.99 after.
Cancel before Nov 29 to avoid being charged.
Subscription renews yearly. Questions? help@quillpad.example""",
 "free for 7 days", "$99.99/year", True, "after the 7 days", "before Nov 29", None, ""),
("""Unlock the full Atlas of Birds. $3.99 per month after a 3-day free trial. Subscription auto-renews monthly. You can manage it in the Play Store. Photos by members. Content updated weekly. Tap 'Try for free' to begin. By continuing you accept the Terms of Use and Privacy Policy.""",
 "3 days free", "$3.99/month", True, None, "in the Play Store", None, ""),
("""Hearth Candles Club. A new scent every month, £16 including postage. Your first candle is half price: £8. Billed on the 5th of each month. Skip, pause or cancel online anytime before the 3rd. Candles cannot be returned for hygiene reasons.""",
 "first candle half price: £8", "£16/month", True, "on the 5th of each month", "online anytime before the 3rd", "candles cannot be returned", ""),
("""Welcome to Northern Lights TV.
Basic — €6.99/mo
Standard — €11.99/mo (you chose this)
Premium — €16.99/mo
Your first 30 days are free. Then we charge €11.99 monthly. No tie-in, cancel whenever. Remember: we can't refund the month in progress.""",
 "first 30 days free", "€11.99/month", True, None, "whenever", "can't refund the month in progress", ""),
("""Cheap flights alert service. FlyWatch Premium: $1 trial for 5 days. After the 5 days, $24.99 per month. We may change pricing. Cancellation takes effect at the end of your billing cycle. Email support@flywatch.example to cancel. Refunds are at our discretion.""",
 "5 days for $1", "$24.99/month", True, "after the 5 days", "email support@flywatch.example", "refunds are at our discretion", "The $1 trial leads to $24.99 per month, and cancelling needs an email to support."),
("""Annual Library Plus card, £30. Borrow unlimited e-books and audiobooks. One payment per year. We will email you before your card expires, but it does not renew unless you choose to renew it. Free for under-18s. Non-refundable.""",
 None, "£30/year", False, None, None, "non-refundable", ""),
("""You're almost in. Your Rumble Pass: 1 month free, then $13/month. No commitment. Easy cancel. Payment info required to start. We will charge your card $13 on the 31st day. Prefer to pay yearly? $130/year is available in settings.""",
 "1 month free", "$13/month", True, "on the 31st day", "easy cancel", None, ""),
("""SnapChef — recipe app. Subscribe for $4.99 a week with a 3-day free trial. Charged weekly until you cancel. To cancel go to Settings > Apple ID > Subscriptions > SnapChef > Cancel. Failure to cancel at least 24 hours before the next period will result in a charge.""",
 "3 days free", "$4.99/week", True, None, "Settings > Apple ID > Subscriptions > SnapChef > Cancel, at least 24 hours before the next period", None, ""),
("""LOCAL PAPER PREMIUM, £1 FOR THE FIRST 12 WEEKS. THEN £9.99 EVERY 4 WEEKS. DIRECT DEBIT. SUBSCRIPTION CONTINUES UNLESS CANCELLED. TO CANCEL EMAIL SUBSCRIPTIONS@LOCALPAPER.EXAMPLE QUOTING YOUR REFERENCE. 
Pay no more than the price shown. Rates may change with 30 days notice.""",
 "£1 for the first 12 weeks", "£9.99 every 4 weeks", True, None, "email subscriptions@localpaper.example quoting your reference", None, ""),
("""Smart Fridge Insurance. Pay £0 now. Your 30 days of cover are free. After that, £3.49 a month by Direct Debit. We'll write to you before the free period ends. Cancel any time with no fee; any premium paid for unused cover is refunded.""",
 "30 days of cover free", "£3.49/month", True, None, "any time with no fee", "premium paid for unused cover is refunded", ""),
("""Stock Signals Pro. 14 days for $0. Then $59/month. Auto-renews monthly. Billing is in USD. You authorize us to charge your card on file. Annual plan: $499 (save $209). Cancel by emailing cancel@stocksignals.example from your registered address. No refunds, no pro-ration.""",
 "14 days for $0", "$59/month", True, None, "by emailing cancel@stocksignals.example from your registered address", "no refunds, no pro-ration", ""),
("""Little Linguists – kids language app.

Family Plan – $9.99/month
- Cancel any time
- 7-day free trial
Payment will be charged to your account at confirmation of purchase unless free trial is active. Subscription renews automatically unless cancelled 24 hours before the end of the period.""",
 "7 days free", "$9.99/month", True, None, "any time, 24 hours before the end of the period", None, ""),
("""Sofa Subscribe: rent furniture by the month. Starting at £39/month for the Lounge Set. 12-month minimum, then continues monthly. Delivery £49 one-off, paid today. Return the set to end the agreement; collection fee £35. Damage charges may apply. Credit check required.""",
 None, "£39/month", True, "today", None, None, "A 12-month minimum, a £49 delivery fee and a £35 collection fee all apply on top of the monthly rent."),
("""NEWSLETTER+ from The Marginalia. $5 a month or $50 a year. Founding members get a free tote. Your membership renews on the same date until you cancel. Cancel any time through the link in your receipt email. We keep all payments but you'll retain access through the end of the period.""",
 None, "$5/month", True, None, "any time through the link in your receipt email", "we keep all payments", ""),
("""Your Mobile Deal: Samsong Galaxia 12, £0 upfront, £42 per month for 36 months. Total £1,512. Includes 100GB data. Pay-monthly device plan, not a subscription. Early settlement available. Leaving early means paying the remaining balance. Credit subject to status.""",
 None, "£42/month", False, None, None, None, "You owe all 36 payments totalling £1,512, and leaving early means paying the remaining balance."),
("""Get the Dataviz Pro plugin. $79 one-time, lifetime license, 3 devices. Free updates for 12 months. No subscription. 14-day money-back guarantee. Pay by card or invoice. All prices exclude VAT where applicable.""",
 None, "$79 one-time", False, None, None, "14-day money-back guarantee", ""),
("""Track your sleep with Dozee. Premium trial: free for 7 days, then $39.99 per year. The subscription renews automatically every 12 months at $39.99. Don't want to be charged? Cancel at least 24 hours before the trial ends in the Apple subscriptions screen.""",
 "7 days free", "$39.99/year", True, None, "at least 24 hours before the trial ends in the Apple subscriptions screen", None, ""),
("""Choose the plan that's right for your team. Solo: $9/mo. Team (highlighted): $29/mo for 5 seats, $5 each additional. Enterprise: contact us. Team plan includes a 14-day free trial and then bills monthly. No credit card needed to start. Cancel from workspace settings.""",
 "14 days free", "$29/month for 5 seats", None, None, "from workspace settings", None, ""),
("""FUEL REWARDS CARD – $4.99 per month. Save 10c a gallon. Membership begins today, with the first fee charged at signup. Auto-renews monthly and cancellation requests must be made in writing to the address on your agreement. No refunds of monthly fees.""",
 None, "$4.99/month", True, "at signup", "in writing to the address on your agreement", "no refunds of monthly fees", "You must cancel in writing by post, and monthly fees are never refunded."),
("""Pickle Ball Pros: Online coaching. Sign up now for a free 21-day trial. After the trial, you'll be charged €15 per month. Cancel anytime during or after the trial by logging in and clicking 'End membership'. Billing is monthly and VAT is added at checkout.""",
 "21 days free", "€15/month", True, "after the trial", "anytime by logging in and clicking End membership", None, ""),
("""Wine Wednesday Club. 2 bottles per month of curated wine, £29.99. No trial. First order £29.99 charged today, then monthly on the same date. 14-day cancellation right on first order. After that, cancel at least 7 days before the next order.""",
 None, "£29.99/month", True, "today", "at least 7 days before the next order", "14-day cancellation right on first order", ""),
("""By clicking Start My Free Trial, you agree to the Terms. Start free for 30 days, then it's $99/year. We store your card but won't charge it during the trial. Your subscription will renew every year on the anniversary of the first charge. You can cancel at any time from Account > Billing. No questions asked refund within 30 days of any annual charge.""",
 "30 days free", "$99/year", True, None, "at any time from Account > Billing", "no questions asked refund within 30 days of any annual charge", ""),
("""SONGBIRD HD AUDIO
Pay as you go: 500 credits for $9.99. Credits never expire. No monthly fees. No subscription. Each song download uses 1 credit. Credits are non-refundable once purchased. Taxes added at checkout.""",
 None, "$9.99 one-time", False, None, None, "credits are non-refundable once purchased", ""),
("""Mom's Meal Prep Delivered! Week 1 FREE — yes, free! Weekly plans from $64.99 afterwards. You'll be charged for week 2 unless you cancel before 6pm Thursday. Plan renews every week automatically. Cancellation window closes every Thursday at 6pm. No refunds for missed deadlines.""",
 "week 1 free", "$64.99/week", True, "for week 2", "before 6pm Thursday", "no refunds for missed deadlines", "Miss the Thursday 6pm deadline and $64.99 is charged with no refund."),
("""Premium Puzzles Daily. Subscribe for £2.50 per month. The first month is free. Direct debit starts after your free month. Cancel by clicking the link in any of our emails. Payments already made cannot be refunded. 3 puzzle books included each year.""",
 "first month free", "£2.50/month", True, "after your free month", "by clicking the link in any of our emails", "payments already made cannot be refunded", ""),
("""Protect your devices with ShieldSafe. 1 year, 5 devices for $19.99 first year. Auto-renews at $89.99 per year. You will be notified 30 days before renewal. To avoid renewal, turn off auto-renew in your account. 60-day money-back guarantee on all purchases and renewals.""",
 "$19.99 for the first year", "$89.99/year", True, None, "turn off auto-renew in your account", "60-day money-back guarantee on all purchases and renewals", "The first-year $19.99 price becomes $89.99 per year at automatic renewal."),
("""Open the Door to Unlimited Learning. Courseway Plus: first 7 days free, then $39 a month. Subscription renews automatically. We'll send a reminder email 3 days before your trial ends. Cancel with one click: Profile > Subscription > Cancel. Certificates included.""",
 "first 7 days free", "$39/month", True, None, "with one click: Profile > Subscription > Cancel", None, ""),
("""Local Gym Day Pass: $12. Single use, valid for one visit today only. No membership required. No recurring charge. Non-refundable. Bring ID.""",
 None, "$12 one-time", False, None, None, "non-refundable", ""),
("""Vox Translator Pro  (best value!)
Annual: $119.99  —  ✔ selected
Monthly: $14.99
Includes 3-day free trial. Then $119.99 will be charged to your store account. Auto-renews annually. Cancel any time.
Restore purchases | Terms | Privacy""",
 "3 days free", "$119.99/year", True, "after the 3-day trial", "any time", None, ""),
("""Subscribe to receive Saffron & Salt Magazine, 6 issues a year. £24 for the first year. After that £42 a year by continuous payment authority. We'll write to you 21 days before. To cancel call 0330 555 0144 (local rate). Refund for unmailed issues only.""",
 "£24 for the first year", "£42/year", True, None, "call 0330 555 0144", "refund for unmailed issues only", ""),
("""Free trial! Tap to start your 7 day free trial of Hike Pass. No payment now. After 7 days, $64.99/yr. Cancel any time to avoid being charged. Payments are processed by Apple.""",
 "7 days free", "$64.99/year", None, "after 7 days", "any time", None, ""),
("""Join Coastline Sailing Club. Annual membership £280 or £26 per month on a 12-month plan (£312 total). Monthly option selected. A £50 joining fee is due today. Plan renews each year. Cancel with 60 days' written notice. Joining fee is not refunded.""",
 None, "£26/month", True, "today", "with 60 days' written notice", "joining fee is not refunded", "Monthly payment totals £312 against £280 yearly, plus a non-refundable £50 joining fee today."),
("""Anti-virus Citadel 2026. 3 devices, 1 year. $0 for 30 days. After the trial you pay $49.99 for the year. Auto-renews at $119.99 per year. Cancel in your account under Billing & Renewals. Customer support available 24/7. You are charged on day 31.""",
 "30 days free", "$49.99/year", True, "on day 31", "in your account under Billing & Renewals", None, "Automatic renewal later jumps from $49.99 to $119.99 per year."),
("""Be part of Studio Eight: indie film streaming. Join for $5.99/month, get your first 2 weeks free, cancel online whenever. We use your card for billing; the first payment of $5.99 is taken on day 15. Subscribers can download 5 films at a time. All prices are inclusive of GST.""",
 "first 2 weeks free", "$5.99/month", True, "on day 15", "online whenever", None, ""),
("""Welcome to Lumina Learning
Premium Annual   $144 /year   [Start 7-Day Free Trial]
Premium Monthly  $18 /month   [Start 7-Day Free Trial]
Free trial converts to paid subscription at the end of the 7 days. 
Cancel anytime. Refunds up to 48 hours after charge.""",
 "7 days free", None, True, "at the end of the 7 days", "anytime", "refunds up to 48 hours after charge", ""),
("""BOOK A CALL?? No. Just grab Coach-in-a-Box: 12 video lessons, one-time $297. Lifetime access, downloadable PDF workbooks. No upsells inside. 30-day 'no-quibble' refund: email us and we'll send it back. Secure checkout.""",
 None, "$297 one-time", False, None, None, "30-day no-quibble refund by email", ""),
("""Your free week of Rally Tennis Live starts now. After that $7.99 weekly or $99.99 yearly — the yearly plan is selected for you. Auto-renewal is on by default. To cancel, open Subscriptions on your phone. Not all matches are available in your region.""",
 "free week", "$99.99/year", True, "after the free week", "open Subscriptions on your phone", None, ""),
("""Home Cleaning Club: a professional clean every two weeks, $119 per visit. First visit $59. Payment taken after each visit. Reschedule or cancel up to 24 hours before; otherwise a $40 late-cancellation fee applies. No long-term contract.""",
 "first visit $59", "$119/visit every two weeks", True, "after each visit", "up to 24 hours before a visit", None, "Cancelling within 24 hours of a visit costs a $40 fee."),
("""Beyond Bytes Bootcamp. Pay $0 now; pay $15,000 only after you get a job paying over $60,000. Income share agreement: 12% of your gross salary for 36 months. Applicable fees, repayment cap $22,000. Not a loan. Missed payments can be sent to collections.""",
 None, "12% of gross salary for 36 months", None, None, None, None, "You repay 12% of your salary for 36 months, up to a $22,000 cap."),
("""Ready to read more? Trial: 4 weeks for $0.99. Digital Standard $8.50 every 4 weeks after. You agree to be billed automatically, and the price may change with 30 days' notice. Cancel online via My Account or by calling 0345 555 0102. Taxes may apply.""",
 "4 weeks for $0.99", "$8.50 every 4 weeks", True, None, "online via My Account or by calling 0345 555 0102", None, ""),
("""We value your privacy ▸ Manage cookies ▸ Accept

Try CineBox Free 
30 days, no obligation
£8.99/month after trial
If you do not cancel during your trial, your payment method will be charged £8.99 per month automatically.
Cancel in Settings > Membership.""",
 "30 days free", "£8.99/month", True, "after the trial", "in Settings > Membership", None, ""),
("""Handyman Home Plan. Covers boiler, plumbing and electrics. £12.50 a month, 12-month minimum. Waiting period of 30 days before first claim. Renews automatically at a price we set at renewal. Cancel within 14 days for a full refund; after that, a £25 admin fee applies.""",
 None, "£12.50/month", True, None, None, "full refund within 14 days; after that a £25 admin fee applies", "The renewal price is set by the company later and a £25 admin fee applies after 14 days."),
("""SIGN UP FOR GLOW BOX BEAUTY
$13/month
Free shipping. Skip anytime. Your card is charged on the 1st of every month, including the month you sign up if you sign up before the 20th. Cancel by Skype chat only. Limited quantity: items may be substituted. Final sale.""",
 None, "$13/month", True, "on the 1st of every month", "by Skype chat only", "final sale", ""),
("""JazzFM Premium. Annual plan: pay £36 today for 12 months. Ad-free listening, offline mode. This is not a rolling subscription: your plan ends on its expiry date and we'll invite you to renew. No auto-charge. Money back within 14 days if unused.""",
 None, "£36/year", False, "today", None, "money back within 14 days if unused", ""),
("""Learning Tree Preschool App — Try 3 days free, then pay $89.99 for the year. Auto-renews. Sorry, we cannot offer refunds. Turn off auto-renewal from your account settings before the trial ends.""",
 "3 days free", "$89.99/year", True, "after the 3-day trial", "from your account settings before the trial ends", "cannot offer refunds", ""),
("""Hello! You've been invited to Shimmer Live Shopping VIP. First 30 days $0, then $9.99 each month. Billing is automatic. You'll be charged on the 31st day. Cancel inside the app by tapping Profile, Membership, End. VIP members get free shipping on orders over $25.""",
 "30 days free", "$9.99/month", True, "on the 31st day", "inside the app by tapping Profile, Membership, End", None, ""),
("""Beacon Fiber Business. 12 months at £29 per month, then £49 per month. 24-month term. Static IP included. Terms: ending the contract early requires paying 100% of the remaining fees. Auto-renews into a rolling 30-day contract after the initial term.""",
 "12 months at £29 per month", "£49/month", True, None, None, None, "Ending the 24-month contract early requires paying 100% of the remaining fees."),
("""Sign in to read this article. Subscribe to The Compass: $0 for 1 month, then $15 per month. Cancel anytime. Subscription continues automatically. Gift subscriptions available. Already a subscriber? Log in.""",
 "$0 for 1 month", "$15/month", True, None, "anytime", None, ""),
("""Streamline Accounting for freelancers. Free for 30 days, no card required. Then $16 per month, or $160 per year. Your subscription won't start automatically — we'll ask you to confirm after the trial. Export your data anytime, even after cancelling.""",
 "30 days free", "$16/month", False, None, None, None, ""),
("""Cat Café Box. £22 monthly. Treats, toys and a surprise. Join this week and get free catnip. Your first box is charged at checkout, then every 30 days. Cancel online anytime. If the box doesn't arrive, we'll resend or refund it.""",
 None, "£22/month", True, "at checkout", "online anytime", "resend or refund if the box doesn't arrive", ""),
("""Final step! Confirm your Orbit VPN plan. 1 year: $4.50/mo, billed $54 now. Auto-renews at $12/mo. 7 days free for new users — you'll see $0 today and your first charge of $54 after 7 days. Cancel before day 8 in your account. All sales after 30 days are final.""",
 "7 days free", "$54/year", True, "after 7 days", "before day 8 in your account", "all sales after 30 days are final", "Renewal later jumps to $12 a month, and the $54 charge comes after 7 days."),
])
