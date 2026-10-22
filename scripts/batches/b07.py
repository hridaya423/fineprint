from emit import add
add([
("""Accept all cookies   Reject   Cookie settings



VELOCITY BIKE SHARE
ANNUAL PASS £99
- Unlimited 30-minute rides
- Auto-renews each year at £99
- Cancel before renewal in the app
7 days free for new riders.""",
 "7 days free", "£99/year", True, None, "before renewal in the app", None, ""),
("""Tap to unlock Pixel Pals+. $0.99 for 3 days, then $6.99 per week. Subscription auto-renews weekly until cancelled. You can cancel in your App Store settings. Delete the app doesn't cancel. Parents: make sure children cannot purchase without permission.""",
 "3 days for $0.99", "$6.99/week", True, None, "in your App Store settings", None, "After the $0.99 trial you pay $6.99 every week, and deleting the app doesn't cancel it."),
("""Hearthstone Home Warranty. First month for $1, then $59.99 a month. A $75 service fee applies per claim. 12-month agreement. After the first year it renews for 12 months unless cancelled with 30 days' written notice. Cancellation within 30 days: full refund.""",
 "first month for $1", "$59.99/month", True, None, "30 days' written notice", "full refund if cancelled within 30 days", ""),
("""Welcome to Pocketfolio Plus: investment tracker. Annual £48. You won't be charged during your 21-day trial. We'll send you a reminder 5 days before. Subscription renews each year at £48. Cancel in your profile.""",
 "21 days free", "£48/year", True, None, "in your profile", None, ""),
("""Whittle & Co. Woodworking Course. Pay once: $149. Includes every lesson, templates and community. Lifetime access. Not a subscription. 14-day returns, if you've watched less than 25% of the course.""",
 None, "$149 one-time", False, None, None, "14-day returns if you've watched less than 25% of the course", ""),
("""Seasonal Produce Box - Veg Plus. €17.90 per box, weekly or fortnightly delivery. First box €8.95. Billing via SEPA. Pause anytime in the account area. Cancel by email with a 5-day notice before the next delivery. Prices VAT included.""",
 "first box €8.95", "€17.90/box", True, None, "by email with a 5-day notice before the next delivery", None, ""),
("""Unlimited Reads. 1 month for $1.99. Auto-renews at $12.99 per month. By clicking Continue you agree to our Terms. Your card will be charged $1.99 right away. Cancel any time in Account > Subscription, or chat with Support.""",
 "1 month for $1.99", "$12.99/month", True, "right away", "any time in Account > Subscription, or chat with Support", None, ""),
("""**LOOK** — The Ultimate Fitness Tracker Subscription!!! 
Start 14-day TRIAL at just $4.95 
(then auto-enrolled in Elite Membership $47.95 per month)
Cancel by contacting Support. Subscription charges are non-refundable. Limit one trial per customer.""",
 "14 days for $4.95", "$47.95/month", True, "after the trial", "by contacting Support", "subscription charges are non-refundable", "The $4.95 trial auto-enrols you in a $47.95 monthly membership with no refunds."),
("""Gold Coast Surf School: 10-lesson pass AU... no, $250 one-time. Valid 6 months from first lesson. No refunds, but passes can be transferred to another person. Wetsuit hire $10 per lesson, extra.""",
 None, "$250 one-time", False, None, None, "no refunds", ""),
("""Rhythm Pro Drum Lessons. £1 for your first month. After that £30 a month, auto-renewing. Payments are taken via Direct Debit on the same day each month. You can cancel at any time up to 3 working days before payment is due.""",
 "£1 for your first month", "£30/month", True, "same day each month", "up to 3 working days before payment is due", None, ""),
("""Meet MyMenu AI. Plans: Weekly €4.99 / Annual €39.99 (selected) — includes 7-day free trial. When the trial ends, €39.99 will be charged automatically. You can cancel before then. After purchase manage your plan in the Play Store.""",
 "7 days free", "€39.99/year", True, "when the trial ends", "before then, in the Play Store", None, ""),
("""Your cart: Basecamp Wetsuit £189. Add a protection plan for £4.99/month? [x] Yes, add Wetsuit Care (£4.99/month, renews automatically, cancel anytime in your account). Protection plan charged today along with your order. Plan is non-refundable after 30 days.""",
 None, "£4.99/month", True, "today", "anytime in your account", "non-refundable after 30 days", "The protection plan is already ticked and renews monthly at £4.99 until you cancel."),
("""cookie banner: By continuing you agree. Close X
 
Welcome to FlightDeck Premium
Free for 30 days
Then $5.99/mo
We'll remind you before billing starts.
Cancel anytime in My Profile.""",
 "30 days free", "$5.99/month", None, None, "anytime in My Profile", None, ""),
("""Introducing the Trailblazer Credit Card Club. Join for $0. Annual fee $149, billed to your card monthly as $12.42. Fee increases to $169 after year one. No cancellation fee, but you must pay the remaining balance in full when you close the account.""",
 None, "$12.42/month", None, None, None, None, "The annual fee rises to $169 after year one, and closing requires paying the remaining balance in full."),
("""Writers' Retreat Newsletter. Pay what you can: £0 to £20 per month. Cancel any time. No contracts. Your payment helps pay for the writers. We never share your data. If you choose a paid tier, your card is charged on the 1st each month.""",
 None, "£0 to £20/month", True, "on the 1st each month", "any time", None, ""),
("""Smooth Move Moving Boxes. Rent 40 reusable moving boxes for 2 weeks: £79. One-time hire, no subscription. Late fee £5 per day after 14 days. Deposit £60 refunded within 7 days of box return. Delivery included in the price.""",
 None, "£79 one-time", False, None, None, "£60 deposit refunded within 7 days of box return", "Each day you keep the boxes beyond 14 days costs £5."),
("""Premium Podcast Network. First 14 days free. After that, $6.50/mo. Cancel any time. Included free with your car? Enter the code on your dashboard. Subscription auto-renews monthly unless cancelled. Your car's radio will stop playing premium shows when it ends.""",
 "14 days free", "$6.50/month", True, "after the 14 days", "any time", None, ""),
("""Sign up for WealthWise Newsletter. 30 days for $1. Then $199 per year automatically. This is an annual subscription billed once per year. To avoid being charged $199, cancel within 30 days by email. We do not remind you. Non-refundable.""",
 "30 days for $1", "$199/year", True, "after 30 days", "within 30 days by email", "non-refundable", "The $1 offer converts to a non-refundable $199 annual charge with no reminder."),
("""Welcome to Dream Home Magazine. Digital + Print bundle. £2.50 for 3 issues, then £14.99 every quarter. Direct Debit Guarantee applies. Subscription continues until cancelled; you can cancel by phoning 0344 555 0166. Unwanted issues cannot be returned.""",
 "3 issues for £2.50", "£14.99 every quarter", True, None, "by phoning 0344 555 0166", "unwanted issues cannot be returned", ""),
("""Kids' Yoga Online: join the club. $0 for the first 7 days. After this, billing is $9.99 each month. You can cancel before your trial ends by following the instructions in the confirmation email. We'll send it to the address you give.""",
 "7 days free", "$9.99/month", None, "after the trial", "by following the instructions in the confirmation email", None, ""),
("""BESTSELLER BUNDLE: 5 e-books + audiobook for $19.99. One-time purchase — yours to keep. No account required, no recurring fees. We'll email a download link right away. If a file doesn't open, we'll fix it or refund you.""",
 None, "$19.99 one-time", False, None, None, "fix it or refund if a file doesn't open", ""),
("""Ready for the Grid? Your free month of Racing Online starts today. After that £11.99 per month. Include live timing, onboard cameras. Cancel any time in your Account. Season ends in December; subscription does not pause during the winter break.""",
 "free month", "£11.99/month", True, "after the free month", "any time in your Account", None, "The subscription keeps billing during the winter break when there are no races."),
("""Join PureWater Delivery. 4 x 19L bottles delivered every 2 weeks at $39.80. First delivery free. Billed after delivery. Bottle deposit $12 per bottle, refundable on return. Cancel with 7 days' notice via phone: 1-877-555-0188.""",
 "first delivery free", "$39.80 every 2 weeks", True, "after delivery", "with 7 days' notice via phone: 1-877-555-0188", "bottle deposit $12 per bottle refundable on return", ""),
("""Unlimited Tutoring for Uni Students. Free 7-day trial then €29.90 billed every month. Annual option €249. To cancel, send a registered letter to the address in the terms. Online cancellation is not offered. Subscriptions renew tacitly.""",
 "7 days free", "€29.90/month", True, "after the trial", "send a registered letter to the address in the terms", None, "Online cancellation isn't offered; you must send a registered letter to stop billing."),
("""ACCEPT COOKIES? [YES] [NO]

TRY AMBERLY PRO
FREE 14 DAYS
THEN $7.99 / MONTH OR $59.99 / YEAR (SAVE 37%)
CANCEL ANYTIME. NO CONTRACT.
YOUR SUBSCRIPTION WILL AUTO-RENEW UNLESS CANCELLED 24H BEFORE PERIOD END.""",
 "14 days free", "$7.99/month", True, None, "24h before period end", None, ""),
("""Taste of Italy Pasta Club. Get 4 packs for £9.99 delivered each month. Pay £9.99 today. Free postage. Renews automatically monthly at the same price. Skip a month any time; cancel by logging into your account. 30-day money-back if you don't love it.""",
 None, "£9.99/month", True, "today", "by logging into your account", "30-day money-back", ""),
("""Moonbase Podcast Studio. $39/mo (billed annually at $468). Start your free 14-day trial. You'll be charged $468 on 5 Nov unless you cancel. Annual plans can't be cancelled mid-term for a refund. Contact sales to downgrade.""",
 "14 days free", "$468/year", True, "on 5 Nov", "contact sales to downgrade", "annual plans can't be cancelled mid-term for a refund", "A $468 annual charge lands on 5 Nov and can't be refunded mid-term."),
("""Jaunt Travel Insurance annual multi-trip policy. £69 a year. Renews automatically each year at a price calculated 21 days before. You can opt out of auto-renew at any time by phone: 0345 555 0199. 14 days to cancel for a full refund if no claim made.""",
 None, "£69/year", True, None, "opt out of auto-renew at any time by phone: 0345 555 0199", "full refund within 14 days if no claim made", "The renewal price is recalculated 21 days before renewal, so it may differ from £69."),
("""Join the FamilyFeast app. Meal plans for the week: 7-day free trial. After: $9.99/month. Bundle with the grocery add-on for $4.99/month extra (pre-selected). Both auto-renew. Remove the add-on before checkout if you don't want it. Cancel in profile.""",
 "7 days free", "$9.99/month", True, None, "in profile", None, "A $4.99 monthly grocery add-on is pre-selected and renews automatically unless you remove it."),
("""All-access pass to The Tennis Hub. 2 months free with annual plan. £5.99 per month billed annually £71.88. 1-year commitment. No cancellations during commitment. Renews yearly. Pay by card or PayPal.""",
 "2 months free", "£71.88/year", True, None, None, None, "The annual commitment can't be cancelled before the year ends."),
("""We use cookies for personalised content. Continue / Customise

Subscribe to Vroom Auto Magazine
First 3 issues: €1
Then €9.90 per month by direct debit
Min. term 12 months
Cancel by registered post.""",
 "first 3 issues: €1", "€9.90/month", True, None, "by registered post", None, "You commit to 12 months at €9.90 and must cancel by registered post."),
("""Dial In: VoIP for small business. Free for 30 days, then $19.99/month per line. Charged on day 31. Month-to-month, cancel any time. Taxes & regulatory fees extra (about 8%). Port your number free.""",
 "30 days free", "$19.99/month per line", True, "on day 31", "any time", None, ""),
("""Hot new release! Download Beat Machine Studio for $39.99. One license, lifetime updates for v3.x. Not a subscription. 14-day refund policy if you encounter technical issues we can't solve.""",
 None, "$39.99 one-time", False, None, None, "14-day refund if we can't solve technical issues", ""),
("""Get 3 months of Starlight Reads for £0. Then £4.99 a month. We'll take your first payment on 24 January. Payments continue monthly. To end your plan, sign in and choose 'Cancel membership'. Offer ends 31 October.""",
 "3 months for £0", "£4.99/month", True, "on 24 January", "sign in and choose Cancel membership", None, ""),
("""FRESH START DETOX TEA – 30 DAY SUPPLY $4.95 SHIPPING ONLY (FREE TRIAL)
After 14 days we will ship your next supply and charge $89.95. Continues every 30 days. Call 1-888-555-0143 to cancel. Returns must be authorised by phone. No refunds on opened items.""",
 "30 day supply, pay $4.95 shipping only", "$89.95 every 30 days", True, "after 14 days", "call 1-888-555-0143", "no refunds on opened items", "After 14 days $89.95 is charged and ships every 30 days until you phone to cancel."),
("""Vocal Booth: studio recording by the hour. £25/hour, pay as you go. Or become a member: £99/month for 6 hours. Monthly membership cancellable with 30 days' notice. Unused hours do not roll over. First hour free for new members.""",
 "first hour free", "£99/month", True, None, "with 30 days' notice", None, ""),
("""My Money Plus: boost your credit score. 7 days for free, then $24.95 a month. Subscription auto-renews monthly. To cancel, call us at 1-800-555-0129 or manage online. Credit monitoring only; not a guarantee of a better score.""",
 "7 days free", "$24.95/month", True, "after 7 days", "call 1-800-555-0129 or manage online", None, ""),
("""Wonder Workshop kids' craft box. Pay $19.95 now for your first box. Then $19.95 each month when your next box ships. You can skip or cancel anytime before the 10th. Returns accepted within 30 days for store credit.""",
 None, "$19.95/month", True, "now", "anytime before the 10th", "returns within 30 days for store credit", ""),
("""Premium Navigator GPS. Free trial for 30 days. $0 due today. Upon trial end, $29.99 per year. Auto-renew yearly. Our trial has no commitment: cancel before day 30. Subscription is charged via Google Play.""",
 "30 days free", "$29.99/year", True, "upon trial end", "before day 30", None, ""),
("""Subscribe to receive BakeLab recipes in your inbox. Free forever tier available. Supporter tier £3/month — 2 weeks free, then charged monthly. Your support is appreciated. Cancel in one click via the email footer. No questions.""",
 "2 weeks free", "£3/month", True, "after 2 weeks", "in one click via the email footer", None, ""),
("""LIFETIME DEAL ENDS TONIGHT! Get TaskPilot for a one-time payment of $199 (normally $15/mo). No renewals. No usage limits. Includes all future updates. 60-day money-back guarantee, no questions asked.""",
 None, "$199 one-time", False, None, None, "60-day money-back guarantee, no questions asked", ""),
("""Choose a plan to start streaming Cricket Live:
Match Pass £4.99 (one match)
Season Pass £39.99 — 12 months, then renews at £49.99
Select Season Pass. Renews annually unless cancelled in your account at least 7 days before renewal. Non-refundable.""",
 None, "£39.99/year", True, None, "in your account at least 7 days before renewal", "non-refundable", "The Season Pass renews at £49.99 instead of £39.99 unless you cancel 7 days ahead."),
("""Tune in to Classical Radio Premium. Try 30 days free with promo code CLASSIC30. Then £6.99 a month. Billing begins after 30 days. Pay with card or PayPal. Cancel any time via My Account; no refunds on current period. Code valid until 31 December.""",
 "30 days free with promo code CLASSIC30", "£6.99/month", True, "after 30 days", "any time via My Account", "no refunds on current period", ""),
("""Hospital Cash Plan. £0.99 for the first month. Then £9.99 a month, collected by Direct Debit. Cover starts after 90 days of payments. Premiums may increase each year. Cancel by calling 0800 555 0166. No refunds except in the first 14 days.""",
 "£0.99 for the first month", "£9.99/month", True, None, "by calling 0800 555 0166", "no refunds except in the first 14 days", "Cover only starts after 90 days of payments, and premiums may rise each year."),
("""Easy Invoicing for Small Biz. Plan: Starter, $0 for 30 days then $11/mo; Pro, $25/mo. Selected: Starter. At the end of 30 days you'll be billed $11 unless you downgrade to free or cancel. Cancel at any time in Billing.""",
 "$0 for 30 days", "$11/month", True, "at the end of 30 days", "at any time in Billing", None, ""),
("""Zumba With Maria Online. Start your 1-week trial for $0.99. After the trial, $19.99 a month. Subscription renews monthly automatically. To cancel, send a message to the instructor via the contact form. Allow 48 hours for cancellation to be processed.""",
 "1 week for $0.99", "$19.99/month", True, "after the trial", "send a message via the contact form; allow 48 hours to process", None, "Cancellation takes 48 hours to process, so a late request can still be billed."),
("""Sign up to Cloud Kitchen Weekly. Zero commitment. Dinner boxes from £32 per week. Pay for each week 4 days before delivery. Cancel at any time by 11:59pm on the cut-off day. Missed cut-off means you're charged. Free delivery over £30.""",
 None, "£32/week", True, "4 days before delivery", "at any time by 11:59pm on the cut-off day", None, ""),
("""Download your tickets. Concert: The Night Owls, 14 Dec. 2 tickets, £96.00 total. One-time purchase. Tickets cannot be exchanged or refunded unless the show is cancelled. Booking fee £7.50 included in total.""",
 None, "£96.00 one-time", False, None, None, "cannot be exchanged or refunded unless the show is cancelled", ""),
])
