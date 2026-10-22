from emit import add
add([
("""Start your 7-day free trial of Lumio+. Then $14.99/month. Cancel anytime in Settings. By tapping Start free trial you agree to the Terms. Your subscription renews automatically each month until you cancel. You will be charged after your trial ends. Taxes may apply. No refunds for partial months. Available on up to 4 screens at once.""",
 "7 days free", "$14.99/month", True, "after your trial ends", "anytime in Settings", "no refunds for partial months", ""),
("""Pick your plan: Individual £4.99/month, or Family £9.99/month (up to 6 accounts) — selected. Try Family free for 30 days. Renews monthly at £9.99 after the trial. Cancel online before your trial ends and you won't be charged. Offer for new users only. VAT included in all prices. Listen offline on any device.""",
 "30 days free", "£9.99/month", True, "after the trial", "online before your trial ends", None, ""),
("""The Harbor Ledger Digital: $1 for your first 3 months, then $18/month. Introductory price applies to new subscribers only. Your subscription will renew automatically at the full price. Cancel anytime by calling 1-800-555-0142 during business hours. Taxes not included. No refunds on unused portions of any billing period. Unlimited articles, daily newsletter, and the crossword archive.""",
 "$1 for your first 3 months", "$18/month", True, None, "by calling 1-800-555-0142 during business hours", "no refunds on unused portions of any billing period", "After the $1 intro, the price jumps to $18/month, and you can only cancel by phone."),
("""Pulse TV is free to try for 14 days. No card needed. When the 14 days end you can choose to subscribe for €8.99/month, or your access simply stops. Nothing renews automatically and we will never charge you without your say-so. Watch live channels and on-demand shows on your phone, tablet or TV. Prices include VAT.""",
 "14 days free", "€8.99/month", False, None, None, None, ""),
("""BINGEBOX ANNUAL — $59.99 BILLED YEARLY ($4.99/mo equivalent). Start with 3 days free. Subscription auto-renews every year for $59.99 unless cancelled at least 24 hours before the end of the current period. Manage or cancel in your Apple ID account settings. Payment charged to your account at confirmation of purchase after trial.""",
 "3 days free", "$59.99/year", True, "after trial", "at least 24 hours before the end of the current period in Apple ID account settings", None, "The yearly $59.99 charge hits automatically; you must cancel 24 hours before the period ends."),
("""Cinephile Club — monthly €12, no ads, new films every Friday. Your first month is free. After that we charge €12 on the same day each month. You can cancel whenever you like from your profile page and keep access until the end of the paid month. Refunds are not given for months already started.""",
 "first month free", "€12/month", True, "after the first month", "whenever you like from your profile page", "not given for months already started", ""),
("""Welcome to SoundHaven. Choose a plan.
Student — $5.99/month (verification required)
Premium — $11.99/month  ← Best value
Start Premium today and get 2 months for $0. Then $11.99/month, billed monthly. Cancel anytime. Taxes calculated at checkout. Your card will be charged $11.99 when the 2 free months end.""",
 "2 months for $0", "$11.99/month", True, "when the 2 free months end", "anytime", None, ""),
("""Stream the full season of Dark Meridian and 4,000 other titles with Arcwave. First week is on us. Then just £7.99 a month. We'll bill you every month until you tell us to stop. To stop, email cancel@arcwave.example or use the Cancel button in your account. No contract, no cancellation fee.""",
 "first week free", "£7.99/month", True, None, "email cancel@arcwave.example or use the Cancel button in your account", None, ""),
("""Unlock Premium on Vellum Radio. $0.99 for your first month, then $10.99/month. By subscribing you authorize recurring charges to your payment method. The $0.99 is charged today. You may cancel at any time, but payments already made are non-refundable. Offer ends 30 November. Some tracks may be unavailable in your region.""",
 "$0.99 for your first month", "$10.99/month", True, "today", "at any time", "payments already made are non-refundable", "The $10.99 monthly price begins after one month and every payment is non-refundable."),
("""PodCastle Plus: ad-free shows and early episodes. Annual plan $39/year or monthly $4.99. Annual selected. 7-day free trial, then $39 billed once a year. We will email you 7 days before your renewal. Cancel in the app under Profile > Subscription. Prices exclude sales tax.""",
 "7 days free", "$39/year", True, None, "in the app under Profile > Subscription", None, ""),
("""FilmNest Premium. Try 30 days for €0, then €13.99 per month. Credit card required. Auto-renews monthly. We do not send reminders before charging, so set your own reminder if you plan to cancel. Cancel by phone only: +49 30 5550 1122, Mon–Fri 9–17h. Digital content, no refunds once streaming has started.""",
 "30 days for €0", "€13.99/month", True, None, "by phone only: +49 30 5550 1122, Mon–Fri 9–17h", "no refunds once streaming has started", "You get no reminder before the first charge, and cancelling is possible only by phone on weekdays."),
("""Join Kestrel Audio Books — your first audiobook is free with a 30-day trial. After the trial, membership is $14.95 a month and includes one credit. Unused credits roll over for up to 3 months. Cancel anytime online. You'll be billed $14.95 on day 31 unless you cancel before then. Taxes may apply.""",
 "30 days free", "$14.95/month", True, "on day 31", "anytime online", None, ""),
("""Never miss a game. SportsLoop Live is $24.99 per month with no commitment. Annual option: pay $199 once and save. Currently showing: Annual plan. Your card is charged $199 today and again each year on the anniversary. Cancel before renewal in My Account. Blackout restrictions apply to local games. No refunds.""",
 None, "$199/year", True, "today", "before renewal in My Account", "no refunds", "You pay $199 upfront and again each year automatically; there are no refunds after you subscribe."),
("""Gold members get early access to every Cobalt Studios release. Try Gold FREE for 14 days. After that, £5.50 per month. You can cancel at any time in the Account tab; your Gold features then end when the month you paid for is over. We charge on the first of each month. Prices include VAT.""",
 "14 days free", "£5.50/month", True, "on the first of each month", "at any time in the Account tab", None, ""),
("""LIVE NOW: Opera at Home. Subscribe and get 3 months for just £1 per month. Then £9.99 per month. Min. term 3 months. Cancel by writing to Opera at Home, PO Box 77, Leeds LS1 4ZZ. Offer for new customers. Subscription continues until cancelled in writing.""",
 "3 months at £1/month", "£9.99/month", True, None, "by writing to Opera at Home, PO Box 77, Leeds LS1 4ZZ", None, "You can only cancel by post, and the price rises nearly tenfold to £9.99 after three months."),
("""Radio Fjord Premium: 60 days free. Then 79 kr/month. Both plans include no ads. You will be charged 79 kr every 30 days from day 61 until you cancel. Cancel in the Fjord app, Settings, Subscription. Cancelling stops future charges; we do not refund the current period.""",
 "60 days free", "79 kr/month", True, "from day 61", "in the Fjord app, Settings, Subscription", "do not refund the current period", ""),
("""Mirador+ — Annual (selected): $71.88/yr, that's $5.99/mo.  Monthly: $9.99/mo.
Free for 7 days, then $71.88 will be charged to your account. Plan automatically renews for the same price and duration. Cancel at least a day before renewal. We will not notify you.""",
 "7 days free", "$71.88/year", True, "after 7 days", "at least a day before renewal", None, "You get no notice before the $71.88 annual charge, so cancel before the trial ends."),
("""Docuverse: watch award-winning documentaries. Start your free month. Then $6.99/mo. Cancel anytime, no questions asked. Not satisfied? Full refund within 14 days of any charge. Renews monthly. Your first payment of $6.99 is taken 30 days after you sign up.""",
 "free month", "$6.99/month", True, "30 days after you sign up", "anytime", "full refund within 14 days of any charge", ""),
("""Unlimited streaming. One flat price. $9 a month, billed monthly, for as long as you stay. No trial offered on this plan. Your first $9 is charged immediately when you press Subscribe. Cancel online anytime and you won't be billed again. We don't give refunds or credits for partial months.""",
 None, "$9/month", True, "immediately", "online anytime", "no refunds or credits for partial months", ""),
("""Kids Corner by Tinyland — safe videos and games. Try 7 days free, then $7.99/month. Parent account required. Subscription renews automatically. IMPORTANT: if you signed up through the Google Play Store, cancel there; cancelling in the app will not stop billing. Taxes may apply.""",
 "7 days free", "$7.99/month", True, None, "through the Google Play Store if you signed up there", None, "Cancelling inside the app won't stop billing if you subscribed through the Play Store."),
("""Weekly crossword club! $1.99 per week, billed weekly. First 3 days free. Auto-renewing weekly subscription — cancel anytime in your device settings. Weekly billing means about $8.60 a month. Payment will be charged to your iTunes account after the trial unless auto-renew is turned off.""",
 "3 days free", "$1.99/week", True, "after the trial", "anytime in your device settings", None, "At $1.99 weekly you pay about $8.60 a month, which the headline price hides."),
("""Join the Meridian Jazz Archive. Annual membership £48. No free trial. Pay today and enjoy 12 months of streaming. Membership does not renew automatically; we will email you a reminder one month before it ends. Thirty-day money-back guarantee, no questions asked.""",
 None, "£48/year", False, "today", None, "thirty-day money-back guarantee", ""),
("""Yearly or monthly? Choose.
[ ] Monthly €10.99
[x] Yearly €79.99 (save 39%)
Try it free for 5 days. We'll charge €79.99 when your trial ends and each year after. Renewal is automatic. Cancel through the account page. Offers cannot be combined with other discounts. VAT included.""",
 "5 days free", "€79.99/year", True, "when your trial ends", "through the account page", None, ""),
("""Welcome back! Your Streamly Premium offer: 3 months at $0.99/month. After 3 months your plan switches to $15.99/month. This is a special winback offer. Renews each month. To avoid being charged the full price, cancel before the 3 months end. Cancel anytime in Account > Plan.""",
 "3 months at $0.99/month", "$15.99/month", True, None, "anytime in Account > Plan", None, "After three months the price jumps from $0.99 to $15.99 per month automatically."),
("""Gigabeat Live Music Pass. £0 today. 14-day free trial, then £11.99/month. We'll send a reminder email 3 days before your trial ends. Cancel in two clicks from your dashboard. Monthly renewal. Pro-rata refunds available if you cancel mid-month. Terms apply.""",
 "14 days free", "£11.99/month", True, None, "in two clicks from your dashboard", "pro-rata refunds available if you cancel mid-month", ""),
("""SUBSCRIBE TO THE DAILY PRISM
Digital access: $4 every 4 weeks for the first year
Then $12 every 4 weeks
Your subscription renews automatically. Cancel through your account or by contacting customer care. Cancellations take effect at the end of the current billing period. Taxes added at checkout.""",
 "$4 every 4 weeks for the first year", "$12 every 4 weeks", True, None, "through your account or by contacting customer care", None, "The price triples to $12 every 4 weeks after the first year."),
("""Support independent journalism. Become a Tideline member for $7/month or $70/year. Members get ad-free reading and a weekly letter. Your membership renews automatically; you can cancel from your account at any time. All memberships are non-refundable. Annual selected. Charged $70 today.""",
 None, "$70/year", True, "today", "from your account at any time", "all memberships are non-refundable", ""),
("""Moonlit Stories: bedtime tales for kids.
— 7-day trial —
$6.99 monthly or $49.99 yearly (best deal)
Subscription auto-renews at the end of each period at the then-current price. The price may change, and we will notify you by email. Cancel any time before renewal.""",
 "7 days", "$49.99/year", True, None, "any time before renewal", None, "Renewal happens at the then-current price, which can change from $49.99."),
("""PlayStack Cloud Gaming — 1 month free for new players. Auto-bill of $17.99/month starts after your free month. We take payment on the same date each month. Hardware not included. Cancel anytime from the Billing page and play until the end of the paid period. All sales final.""",
 "1 month free", "$17.99/month", True, "after your free month", "anytime from the Billing page", "all sales final", ""),
("""BECOME A MEMBER of the Linden Review
Print + Digital: £3 a month for 6 months, then £16 a month. 
Delivery of the Saturday paper included. Subscription continues until cancelled. To cancel or pause, call 0800 123 456 (free) or visit any Linden shop. Refunds for undelivered issues only.""",
 "£3 a month for 6 months", "£16/month", True, None, "call 0800 123 456 or visit any Linden shop", "refunds for undelivered issues only", "The price rises from £3 to £16 a month after six months."),
("""Start listening free with Hum. 30 days of Hum Premium at no cost. Then $10.99/month. Your card is only charged after 30 days. Cancel in Settings > Account before day 30 to avoid paying. Family plan available from $16.99/month. Terms apply.""",
 "30 days free", "$10.99/month", None, "after 30 days", "in Settings > Account before day 30", None, ""),
("""Atlas Maps Pro. $29.99 per year after your 14-day free trial. Auto-renews each year. We charge your card on the renewal date and send a receipt. Cancel anytime in the app menu under Subscription. If you forget to cancel and are charged, contact us within 7 days for a full refund.""",
 "14 days free", "$29.99/year", True, "after your 14-day free trial", "anytime in the app menu under Subscription", "full refund if you contact us within 7 days of being charged", ""),
("""TVBox Plus gives you every channel. Pay $0 for the first 30 days. Then your subscription renews at $64.99 a month for a 12-month agreement. An early termination fee of $15 per remaining month applies if you cancel before 12 months. Equipment fee $10/month extra. Taxes apply.""",
 "$0 for the first 30 days", "$64.99/month", True, None, None, None, "You're locked into 12 months; cancelling early costs $15 per remaining month plus a $10 monthly equipment fee."),
("""Story Hour — unlimited audio stories. Monthly £6.99. Yearly £59.99. Yearly selected. Free trial of 7 days. Payment of £59.99 will be taken when the trial ends. Subscription renews yearly. Switch off auto-renew in Settings at least 24 hours before the end of the period.""",
 "7 days free", "£59.99/year", True, "when the trial ends", "switch off auto-renew in Settings at least 24 hours before the end of the period", None, ""),
("""Retro Reels, classic cinema. No contracts. $5.99/month. First 7 days are free — we mean it. We charge on day 8. Cancel with one tap. Free trial cannot be used again if you cancel and re-join. Don't forget: after cancellation your watchlist is deleted after 30 days.""",
 "7 days free", "$5.99/month", None, "on day 8", "with one tap", None, ""),
("""cookies: we use cookies to personalise ads. [Accept] [Reject] [Settings]
-----
GO PREMIUM
7 DAYS FREE, THEN $12.99 / MONTH
Auto renews monthly. You will be charged $12.99 on the 8th day. Cancel anytime in profile settings. See Terms of Service and Privacy Policy. © 2026 StreamDen Inc.""",
 "7 days free", "$12.99/month", True, "on the 8th day", "anytime in profile settings", None, ""),
("""WEEKEND PASS
€2.99 for 48 hours of unlimited streaming. This is a one-time purchase. It does not renew and you will not be charged again. Access ends automatically after 48 hours. All sales are final. Purchase is non-refundable once the stream is started.""",
 None, "€2.99 one-time", False, None, None, "non-refundable once the stream is started", ""),
("""Pay-per-view: Title Fight Night. $54.99 one time. Watch live or replay for 7 days. No subscription. No recurring fees. Taxes added at checkout. If the event is cancelled, you get a full refund automatically. Otherwise, all sales are final.""",
 None, "$54.99 one-time", False, None, None, "full refund if the event is cancelled, otherwise all sales are final", ""),
("""Own it forever. Buy the Director's Cut of Silt & Salt for £14.99. One payment. No subscription, no renewal. Download and keep. Refunds only if the file is faulty and you tell us within 14 days. Digital download; your statutory rights as a consumer are not affected.""",
 None, "£14.99 one-time", False, None, None, "only if the file is faulty and you tell us within 14 days", ""),
("""Buy the Complete Album: "Low Tide Radio" — $9.99. Instant MP3 + FLAC download. One-time payment, nothing recurring. Charged today. Tax added. Digital goods are not returnable. Contact support if your download fails.""",
 None, "$9.99 one-time", False, "today", None, "digital goods are not returnable", ""),
("""Subscribe for TheoryBeat Pro — 14 day free trial! Cancel anytime. $9.99/mo thereafter.""" + " " + """Subscription renews automatically unless auto-renew is turned off at least 24 hours before the end of the current period. Your account will be charged for renewal within 24 hours prior to the end of the current period.""",
 "14 days", "$9.99/month", True, "within 24 hours prior to the end of the current period", "anytime", None, ""),
("""Nordlicht Streaming: first 2 months at €1.99 per month, then €9.99 per month. 12-month minimum term applies. Payment each month by direct debit. After the minimum term the contract continues month to month and can be cancelled with 30 days' notice in writing. Prices include VAT.""",
 "2 months at €1.99/month", "€9.99/month", True, None, "with 30 days' notice in writing after the 12-month minimum term", None, "A 12-month minimum term applies, so you can't cancel in the first year."),
("""Meet Orbit News+ — all the headlines, none of the paywalls. Free for a week. After that, $3.50 per week. Yes, per week. Subscription is billed every Monday and continues until you cancel in the app. Cancellation is effective at the end of the billing week. No refunds.""",
 "free for a week", "$3.50/week", True, "every Monday", "in the app", "no refunds", "You're billed $3.50 every week, roughly $15 a month, with no refunds."),
("""Mixtape Premium Duo: two accounts, one bill. Start your 1-month trial for £0.00. After the trial, £14.99/month. Renews until you cancel. Cancel via Settings > Billing or by chat. We'll refund your latest charge if you cancel within 48 hours of a renewal.""",
 "1 month for £0.00", "£14.99/month", True, None, "via Settings > Billing or by chat", "refund of your latest charge if you cancel within 48 hours of a renewal", ""),
("""AnimeVault — 7 days FREE then $11.99 billed monthly. Charged in USD. Renewal charges may include currency conversion fees from your bank. Cancel any time from the website only (not available in the app). Access continues until the end of the billing period.""",
 "7 days free", "$11.99/month", True, None, "any time from the website only", None, "Cancelling works only on the website, not in the app."),
("""Join Lantern Premium. Get 90 days free when you sign up with code WELCOME90. After 90 days you'll pay $8.99/month unless you cancel. Code valid for new accounts. Card required. Cancel from Account Settings. Promo cannot be combined with student pricing.""",
 "90 days free with code WELCOME90", "$8.99/month", True, "after 90 days", "from Account Settings", None, ""),
])
