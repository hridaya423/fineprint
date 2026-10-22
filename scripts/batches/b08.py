from emit import add
add([
("""Join Atlas Rewards Premium. Introductory price £0.99 a month for 6 months, then £7.99 a month. Includes free delivery, cashback and members-only prices. Membership renews monthly. We may change the price with 30 days' notice. Cancel anytime in My Atlas.""",
 "£0.99 a month for 6 months", "£7.99/month", True, None, "anytime in My Atlas", None, "The price rises to £7.99 a month after six months and may change with 30 days' notice."),
("""Streamer's Choice Annual. Billed $49.99 today for the first year. Saves 58% on monthly. Renews at the regular price of $119.88 each year. No free trial. Cancel auto-renew in your account settings. 7-day refund window after each charge.""",
 None, "$119.88/year", True, "today", "auto-renew in your account settings", "7-day refund window after each charge", "The first-year price of $49.99 more than doubles to $119.88 at renewal."),
("""Pocket Doctor symptom checker. Try free for 3 days, then $13.99 per month. By tapping Subscribe, your payment method will be charged at the end of the trial. Manage or cancel via Settings > Subscriptions at least 24 hours before renewal. Not medical advice.""",
 "3 days free", "$13.99/month", True, "at the end of the trial", "via Settings > Subscriptions at least 24 hours before renewal", None, ""),
("""Buy Tickets – Harbour Boat Tour. Adult £22, child £12. Pay now and receive e-tickets by email. One-time payment. Free cancellation up to 24 hours before departure for a full refund. After that, no refunds. Weather cancellations are fully refunded.""",
 None, "£22 one-time", False, "now", None, "free cancellation up to 24 hours before departure; weather cancellations fully refunded", ""),
("""cookies on this website | I agree

Lotus Spa Membership
2 massages a month, £75 per month. 12 months minimum. 
Free first massage!
Membership renews monthly after 12 months. 
To cancel after the minimum term, 30 days' written notice at reception.
Unused massages expire.""",
 "free first massage", "£75/month", True, None, "30 days' written notice at reception after the minimum term", None, "A 12-month minimum applies and unused massages expire each month."),
("""Start learning Korean with SeoulSounds. 7 days free. Then $11.99 monthly. Includes unlimited lessons and a speaking coach. We charge your card after your free week. Renewal is automatic. Email support@seoulsounds.example to cancel; allow 2 business days.""",
 "7 days free", "$11.99/month", True, "after your free week", "email support@seoulsounds.example; allow 2 business days", None, ""),
("""BUY NOW, PAY LATER — New phone, Orbit X. 24 monthly payments of £31.25. No interest. £750 total. This is a purchase, not a subscription. Early repayment allowed without fee. Credit subject to status. Late payments may affect your credit file.""",
 None, "£31.25/month for 24 months", False, None, None, None, ""),
("""Taskly Business: the 14-day trial is on us. After 14 days you'll be charged $10 per user per month, minimum 5 users ($50/month). Plan auto-renews monthly. You can cancel anytime; removing users takes effect next billing cycle.""",
 "14 days free", "$10/user/month (minimum 5 users)", True, "after 14 days", "anytime", None, ""),
("""Free trial: MaxStream Sports. Watch every game for 7 days at $0. Then $29.99/mo. You must provide a credit card. We'll automatically charge you on day 8. There is a $15 fee if you cancel by phone; online cancellation is free.""",
 "7 days at $0", "$29.99/month", True, "on day 8", "online is free; $15 fee by phone", None, "Cancelling by phone costs $15; only online cancellation is free."),
("""Stationery subscription: Dear Diary Box. Receive 3 notebooks and a pen for €15 per month. Free postage in the EU. First box 20% off (€12). Billing on the 12th each month. Cancel by emailing care@deardiary.example before the 8th.""",
 "first box 20% off (€12)", "€15/month", True, "on the 12th each month", "emailing care@deardiary.example before the 8th", None, ""),
("""Upgrade now: Unlimited Cloud Notes. Annual plan £24.99. Your trial lasts 7 days. £24.99 will be charged to your account when your trial ends. Renews yearly. You can switch off renewal in your account and keep using until the period ends.""",
 "7 days", "£24.99/year", True, "when your trial ends", "switch off renewal in your account", None, ""),
("""GET HEALTHY WITH PURE JUICE! 
• 7 juices a week
• $59.99 per week
• Free first week for new customers
• Auto-ships weekly
• To skip or cancel, log in before Sunday 6pm
• No refunds, no returns on perishable items""",
 "free first week", "$59.99/week", True, None, "log in before Sunday 6pm", "no refunds, no returns on perishable items", "You're charged $59.99 each week unless you skip before Sunday 6pm, with no refunds on perishable items."),
("""Subscribe to Coastline Radio+: 1 month free then €2.99/month. Great value. Direct debit or card. Cancel with a single click in your account. A notification email is sent 7 days before the free month ends so you're never surprised.""",
 "1 month free", "€2.99/month", True, None, "with a single click in your account", None, ""),
("""Designer handbag rental. Wear a new bag every month, $89/month. First month $29. Rental renews monthly. Return bags within 5 days of the end of each period or pay the retail price. Cancel any time with 10 days' notice via email.""",
 "first month $29", "$89/month", True, None, "any time with 10 days' notice via email", None, "Not returning a bag within 5 days of period end means paying the full retail price."),
("""Digital Photo Frames Pro. Pay $9.99 once for lifetime use of the app on up to 5 frames. No subscription, no ads. Support included for 1 year. Refund within 30 days via your app store.""",
 None, "$9.99 one-time", False, None, None, "within 30 days via your app store", ""),
("""Winter Pass! Unlimited skiing at Pinecrest. Early-bird £399 — pay today. Pass is valid for the 2026/27 season only. Pass does not auto-renew. Passes are non-transferable. Refunds only if the resort closes for more than 30 days.""",
 None, "£399 one-time", False, "today", None, "only if the resort closes for more than 30 days", ""),
("""Journal+ for iPad. Free for a week then $39.99 for the year. Payment will be charged to iTunes account at confirmation of purchase after trial. Account will be charged for renewal within 24 hours prior to the end of the current period. Auto-renew may be turned off in Account Settings.""",
 "free for a week", "$39.99/year", True, "after trial", "turn off auto-renew in Account Settings", None, ""),
("""Welcome to BrainBoost Games. You've picked Annual Deal: $24.99 for 12 months. Free for 3 days. The deal is automatically replaced by the regular price of $79.99/yr at renewal. Cancel renewal any time. Trial available once per Apple ID.""",
 "3 days free", "$79.99/year", True, None, "cancel renewal any time", None, "The $24.99 deal renews at $79.99 per year, over three times higher."),
("""Learn anywhere. Open University Online: pay by the month at £48 per month for 12 months. Total £576. Monthly instalments by Direct Debit starting 7 days after enrolment. Course withdrawal within 14 days for a full refund; later, withdrawal fees apply.""",
 None, "£48/month for 12 months", False, "7 days after enrolment", None, "full refund within 14 days; later withdrawal fees apply", ""),
("""CLICK TO START YOUR FREE TRIAL OF SHIELDLINE IDENTITY PROTECTION. Free for 30 days. After the trial $17.99 per month will be billed. Renewal is automatic. To cancel, call 1-800-555-0138. It can take 3–5 days to process. Payments made before cancellation are non-refundable.""",
 "30 days free", "$17.99/month", True, "after the trial", "call 1-800-555-0138", "payments made before cancellation are non-refundable", "Cancelling takes 3–5 days to process, so you may still be billed $17.99."),
("""Yummy Snacks Around the World Box. £14.99 a month. Subscribe today and get your first box for just £4.99. Cancel any time. We'll bill £14.99 monthly from your second box. Delivery to the UK, free. Allergens listed on each box.""",
 "first box £4.99", "£14.99/month", True, "from your second box", "any time", None, ""),
("""Hey there! Hustle Planner Premium, the planner app. Want more? $6.99/mo with 7-day free trial. You'll be charged on the 8th day. Renews monthly. Cancel in your Apple settings. Group plans for 5 people at $19.99/mo.""",
 "7 days free", "$6.99/month", True, "on the 8th day", "in your Apple settings", None, ""),
("""Studio One Pilates. 5 classes for £25 (new clients), valid for 1 month. Then rolling membership at £79/month unless you tell us otherwise. To avoid membership, tell reception at your last class. Membership needs 30 days' notice to end.""",
 "5 classes for £25", "£79/month", True, None, "tell reception; 30 days' notice to end", None, "You're moved onto a £79 monthly membership unless you tell reception at your last class."),
("""Wise Owl Reading Club for kids. 1 free month then $8.95 monthly. Gift option: prepay 12 months for $99. Prepaid gifts do not renew. Regular subscriptions renew monthly and can be paused. Cancel any time via email: hoot@wiseowl.example.""",
 "1 free month", "$8.95/month", True, None, "any time via email: hoot@wiseowl.example", None, ""),
("""To keep the music playing, choose Plan.
LITE: €4.99/month, shuffle only
PLUS: €9.99/month ✓
Get 3 months of Plus for €0 as a new member! Then €9.99 per month. VAT included. Automatically renewing. You can cancel your plan on our website or app at any time.""",
 "3 months for €0", "€9.99/month", True, None, "on our website or app at any time", None, ""),
("""Home Shield energy plan. Fixed rate 24p/kWh for 12 months. £60 exit fee per fuel if you leave early. Plan switches to our standard variable tariff (currently 31p/kWh) automatically after 12 months. Standing charge 55p/day. 14-day cooling-off period.""",
 None, "24p/kWh for 12 months, then 31p/kWh", True, None, None, "14-day cooling-off period", "After 12 months you automatically move to the 31p/kWh variable tariff, and leaving early costs £60 per fuel."),
("""Fitness band cloud subscription. First 6 months free with your purchase. Then $9.99 per month to keep sleep and workout history online. Subscription will start automatically. Cancel anytime; your device continues to work in basic mode.""",
 "first 6 months free", "$9.99/month", True, "after 6 months", "anytime", None, ""),
("""**COOKIE NOTICE** OK
**PREMIUM OFFER**
Pay nothing today. 14 day free trial of PocketPress Premium. Then €7/month. Renews every month. Cancel before day 14 via the app. No hidden fees.
Terms apply.""",
 "14 days free", "€7/month", True, None, "before day 14 via the app", None, ""),
("""Gather round: The Board Game Box. A new game every month for £29. Pay for the first game today and the next on the 1st of every month. Skip a month any time. Cancel with a message to support at least 3 days before the 1st. Games can be returned unopened for credit within 14 days.""",
 None, "£29/month", True, "today", "with a message to support at least 3 days before the 1st", "unopened games returned for credit within 14 days", ""),
("""Newsletter Premium: Behind the Algorithm. $12/month or $100/year. 7-day free trial for annual plans. You will be charged $100 after 7 days. Auto-renewal on. To cancel, click 'Manage subscription' in any email we send you.""",
 "7 days free", "$100/year", True, "after 7 days", "click Manage subscription in any email", None, ""),
("""Hearing Aid Care Plan. £19.50 a month covers batteries, cleaning and repairs. First 2 months free. Starts on collection of your device. Payments by Direct Debit. 12-month minimum term. Cancel after the minimum term with 28 days' written notice.""",
 "first 2 months free", "£19.50/month", True, None, "after the minimum term with 28 days' written notice", None, ""),
("""Welcome to Wavelength: surf forecasts. Annual membership $59. One payment. Valid for 12 months from today. We'll offer you the chance to renew but it will not happen automatically. No refunds after 7 days.""",
 None, "$59/year", False, "today", None, "no refunds after 7 days", ""),
("""Cinema Sunday Club. Trial: £1 for 30 days. After 30 days you'll pay £9.99 per month. Auto-renews. Cancel anytime. Stream thousands of classic films. Not available outside the UK. Taxes incl.""",
 "£1 for 30 days", "£9.99/month", True, "after 30 days", "anytime", None, ""),
("""UltraClean Dishwasher Tablets – auto-delivery. Subscribe and save: €12.99 per box every 8 weeks. Save 10% vs one-off. Next shipment is charged when it dispatches. Edit or cancel anytime in your account; we recommend at least 48 hours prior. Returns accepted unopened within 30 days.""",
 None, "€12.99 every 8 weeks", True, "when it dispatches", "anytime in your account", "returns accepted unopened within 30 days", ""),
("""Sleep Sounds Pro unlocks 1,000 tracks. 1 week trial, then $39.99 each year. You will see a pending charge of $39.99 on day 8. Auto-renew yearly. Cancel in iPhone Settings. If you forget, we cannot refund. Apple handles all billing.""",
 "1 week", "$39.99/year", True, "on day 8", "in iPhone Settings", "we cannot refund; Apple handles all billing", ""),
("""SOLO TRAVELLER'S PASS: 60 DAYS OF UNLIMITED TRAIN TRAVEL ACROSS EUROPE. €349 ONE-OFF PAYMENT. ALL TAXES INCLUDED. NO AUTOMATIC RENEWAL. REFUNDS AVAILABLE FOR UNUSED PASSES WITHIN 3 MONTHS OF PURCHASE, MINUS A €15 HANDLING FEE.""",
 None, "€349 one-time", False, None, None, "available for unused passes within 3 months of purchase, minus a €15 handling fee", ""),
("""Unlimited Coding Practice. 1-year plan, $8/mo billed $96 upfront. Start with a 10-day free trial; $96 charged on day 11. Subscription auto-renews at the standard price, which is currently $144 a year. Cancel under Settings > Plans.""",
 "10 days free", "$96/year", True, "on day 11", "under Settings > Plans", None, "Renewal moves to the standard price, currently $144 a year."),
("""Premium Perks for Parents. Join The Village for $5.95 a month. 3-month trial at $0. Charges start after month 3. Includes discounts, advice, community. We'll email when the trial is ending. Cancel with 2 clicks.""",
 "3 months at $0", "$5.95/month", True, "after month 3", "with 2 clicks", None, ""),
("""Cookie Policy Accept | Reject | Manage

SPORTS NEWS UNLIMITED
LAUNCH OFFER – £0.50 for 8 weeks
STANDARD PRICE £8.00 A MONTH after 8 weeks
CONTINUOUS PAYMENT, CANCEL ANYTIME BY CALLING 0345 555 0123
Offer not available to existing subscribers""",
 "£0.50 for 8 weeks", "£8.00/month", True, None, "by calling 0345 555 0123", None, ""),
("""Welcome to Ironclad Shoes shoe-of-the-month club. Your first pair is $19.95 shipped. Each month after, you'll get a new pair for $79.95 unless you skip by the 5th. Shoes cannot be returned if worn outdoors. Cancel any time through your online account.""",
 "first pair $19.95 shipped", "$79.95/month", True, None, "any time through your online account", "shoes cannot be returned if worn outdoors", "A $79.95 pair ships every month unless you skip by the 5th."),
("""Join now for ad-free podcasts. SoundBox Plus costs $4.99 a month with a one-week trial. Your trial ends on the 29th. After that your card will be charged automatically. Cancel anytime, and you can still listen until the end of your paid period.""",
 "one-week trial", "$4.99/month", True, "after the trial ends on the 29th", "anytime", None, ""),
("""Photography Masterclass: 12 modules, lifetime access. £0 today, then 3 monthly payments of £49 (£147 total). Not a subscription. Payments stop after the third. 30-day money-back guarantee on first payment.""",
 None, "3 monthly payments of £49", False, None, None, "30-day money-back guarantee on first payment", ""),
("""Moonshine App premium. 3 DAYS FREE — then $12.99/week. Unlimited access. Billed weekly. Cancel anytime in Settings > Subscriptions. Prices in USD. Trial applies to new users only. Automatic renewal unless cancelled at least 24 hours before the end of the period.""",
 "3 days free", "$12.99/week", True, "after 3 days", "anytime in Settings > Subscriptions, at least 24 hours before the end of the period", None, "At $12.99 weekly, the plan costs about $675 a year."),
("""Premium Tidal Pools Aquarium Membership. Individual £39/yr, Family £89/yr (selected). Your card is charged £89 now. Renews automatically each year; we'll email you 28 days ahead. Cancel anytime by phone: 01234 555 012. Membership fees are non-refundable.""",
 None, "£89/year", True, "now", "anytime by phone: 01234 555 012", "membership fees are non-refundable", ""),
("""Win back your time. Zenith Calendar Pro. 30 days free, then $4.50 a month. Billing starts on the 31st day. Annual option saves 20%. Cancel at any time from the web dashboard. No refunds for months already billed.""",
 "30 days free", "$4.50/month", True, "on the 31st day", "at any time from the web dashboard", "no refunds for months already billed", ""),
])
