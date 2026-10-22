from emit import add
add([
("""We value your privacy. By clicking Accept you agree to cookies. [Accept] [Settings]
==========
DRIVESAFE DASHCAM CLOUD
Free 30 days
$5.99/mo after
Auto-renew
Cancel from the app
==========
Powered by DriveSafe Inc. | Legal""",
 "30 days free", "$5.99/month", True, "after 30 days", "from the app", None, ""),
("""PICK YOUR PLAN
PRO MONTHLY  £12.99
PRO ANNUAL   £69.99 ← SELECTED
START FREE TRIAL — 7 DAYS
YOU WILL BE CHARGED £69.99 ON DAY 8. SUBSCRIPTION RENEWS ANNUALLY. CANCEL ANYTIME BEFORE RENEWAL TO AVOID BEING CHARGED. NO PARTIAL REFUNDS.""",
 "7 days", "£69.99/year", True, "on day 8", "anytime before renewal", "no partial refunds", ""),
("""One-time purchase: Complete Spanish Verb Trainer. €12.99. Lifetime access on all your devices. No subscription and no additional fees. Download immediately after payment. If you're not satisfied, request a refund within 14 days.""",
 None, "€12.99 one-time", False, None, None, "request a refund within 14 days", ""),
("""Join Revive Recovery Studio. Your first class is free; afterwards £12 per class or £89 per month for unlimited. Monthly membership has no contract, but the first month's payment is non-refundable. Direct debit on the 1st. Cancel with 14 days' notice by email.""",
 "first class free", "£89/month", True, "on the 1st", "with 14 days' notice by email", "first month's payment is non-refundable", ""),
("""Unlock premium themes for Pixel Launcher. $1.99 once. Not a subscription. Works on all your Android devices. Refundable within 2 hours of purchase through Google Play.""",
 None, "$1.99 one-time", False, None, None, "refundable within 2 hours of purchase through Google Play", ""),
("""Subscribe to Morning Brief Plus: 14 days free, then $6 monthly. No credit card needed to begin. At the end of 14 days we'll ask if you'd like to continue; we never bill without your consent. Cancel any time by email.""",
 "14 days free", "$6/month", False, None, "any time by email", None, ""),
("""Hot tub servicing plan: £29 per month. First month free. Includes two chemical top-ups and an annual inspection. The agreement lasts 24 months and renews yearly. Early cancellation: £150 fee. Cancel by writing to us 30 days before the term ends.""",
 "first month free", "£29/month", True, None, "by writing to us 30 days before the term ends", None, "Cancelling early costs a £150 fee, and the 24-month agreement then renews yearly."),
("""Welcome. Your Eco Cleaners box: laundry, dish and surface refills, delivered every 8 weeks. £18.50 per box. Bill taken 3 days before dispatch. Free to skip, delay or cancel before billing. Contact hello@ecocleaners.example. Refunds for damaged goods only.""",
 None, "£18.50 every 8 weeks", True, "3 days before dispatch", "before billing; contact hello@ecocleaners.example", "refunds for damaged goods only", ""),
("""Open now: ChampionTV. Watch 90+ sports channels. Sign up today for 30 days free, then $39.99/month. 2-year agreement required: early termination fee of $240. Includes DVR service for $10/month extra. Regional sports fee $11/month.""",
 "30 days free", "$39.99/month", True, None, None, None, "A 2-year agreement and $240 early termination fee apply, plus $10 DVR and $11 regional sports fees."),
("""Audiobook Haven. First book free with 30-day trial. Membership: £7.99 a month for one audiobook credit. At the end of your trial, we'll start charging £7.99 per month. Unused credits expire after 12 months. Cancel in My Account any time.""",
 "30 days free", "£7.99/month", True, "at the end of your trial", "in My Account any time", None, "Unused credits expire after 12 months."),
("""cookies: allow | deny

TEACH YOURSELF PIANO
Instant access, £19.99 once.
NOT a subscription.
Works offline. Free updates for 12 months.
14-day money back guarantee.""",
 None, "£19.99 one-time", False, None, None, "14-day money back guarantee", ""),
("""Moments Journal Premium. 7-day trial. Then US$59.99/year. You can cancel the trial at any point. Subscription will auto-renew annually. We email you 14 days before renewal so you can decide. Manage via account page.""",
 "7 days", "US$59.99/year", True, None, "at any point during the trial; manage via account page", None, ""),
("""Final price: $49.00 today. Includes 1 year of CoachBot access. After 12 months, access renews at $149 annually unless you cancel before expiry. Reminder emails are sent 7 days before renewal. All sales are final.""",
 None, "$149/year", True, "today", "before expiry", "all sales are final", "Renewal after year one is $149, three times today's $49.00 price."),
("""Spark Joy cleaning service. Weekly clean for $120. First visit half price. Cancel anytime with 48 hours' notice; otherwise you're charged for the visit. Payment is taken after the clean. Not satisfied? We'll re-clean for free within 24 hours.""",
 "first visit half price", "$120/week", True, "after the clean", "anytime with 48 hours' notice", "free re-clean within 24 hours", ""),
("""Everyday Wellness Pass. £0 today. 1 month free; after, £16.99 a month. Not available with other offers. Your membership will automatically continue. To end it, you must visit your local branch. Online and phone cancellations are not accepted.""",
 "1 month free", "£16.99/month", True, None, "visit your local branch", None, "Only an in-person branch visit can cancel; online and phone requests are refused."),
("""TryEats: your first 3 deliveries are $5 each. Then regular price of $14.99 per delivery. Membership $9.99/month required after the first 3 deliveries. Both auto-renew. Cancel anytime in app. Taxes and driver tips extra.""",
 "first 3 deliveries $5 each", "$14.99/delivery + $9.99/month membership", True, None, "anytime in app", None, ""),
("""Podcast: The Deep End — Premium. £3.99 a month. Join today to get the first week free. Ad-free episodes and bonus content. Payment is taken after the first week. Cancel any time on the website; access stays until the period ends.""",
 "first week free", "£3.99/month", True, "after the first week", "any time on the website", None, ""),
("""Smart Parking Permit. €120 per year. Pay once for 12 months. Does not renew automatically; we'll send a reminder. Permit holds one licence plate. No refunds if your plate changes mid-year; replacement permit €10.""",
 None, "€120/year", False, None, None, "no refunds if your plate changes mid-year", ""),
("""Streaming Giant+ Annual Pass: Pay $79.99/year. Now only $39.99 for the first year. Automatic renewal at $79.99. Tax not included. Try free for 7 days. Cancel any time in your account. Refunds not available, but you keep access until the term ends.""",
 "7 days free", "$79.99/year", True, None, "any time in your account", "refunds not available", ""),
("""Subscribe to receive your Fresh Flowers Weekly bouquet. 1st bouquet £9.99; £21.99 each week thereafter. Cancel by midnight on Mondays to avoid the following week's delivery. Delivery included. Flowers arrive in bud.""",
 "1st bouquet £9.99", "£21.99/week", True, None, "by midnight on Mondays", None, ""),
("""WE USE COOKIES [OK]

SIGN IN TO SAVE YOUR PROGRESS. 
UPGRADE TO CODEQUEST PRO 
$0.00 for 14 days 
then $29.99 per month, billed monthly 
auto-renews until you cancel, any time, from Settings""",
 "14 days at $0.00", "$29.99/month", True, "after 14 days", "any time, from Settings", None, ""),
("""Home Security Camera Plan. Record 30 days of video in the cloud. $3 per camera per month. First 2 months free. Your plan renews monthly. If you cancel, recordings are deleted after 7 days. Cancel in the app under Account.""",
 "first 2 months free", "$3/camera/month", True, "after 2 months", "in the app under Account", None, "Cancelling deletes your recordings after 7 days."),
("""Bakery Bundle — treats shipped monthly! £25 a month. Join now and get your first box free (you pay £4.95 postage). Next box £25 on 15th of next month. Cancel before the 10th. Nothing refundable once packed.""",
 "first box free (pay £4.95 postage)", "£25/month", True, "15th of next month", "before the 10th", "nothing refundable once packed", ""),
("""Get started with Orchid CRM — free for 21 days. Subscriptions start at €15 per user per month, billed annually (€180 per user). You'll be charged when your trial ends. To avoid charges cancel before day 21. Annual contracts are non-cancellable and non-refundable.""",
 "21 days free", "€180/user/year", True, "when your trial ends", "before day 21", "annual contracts are non-cancellable and non-refundable", "The €15 per user figure is billed as €180 yearly, and annual contracts can't be cancelled or refunded."),
("""A Year of Great Reads. Subscribe to Page One magazine: 12 issues for $29.95. One-time payment. Subscription ends automatically after 12 issues. We do not auto-renew. Refund for unmailed issues if you cancel.""",
 None, "$29.95 one-time", False, None, None, "refund for unmailed issues if you cancel", ""),
("""Be fluent in 3 months. SpeakEasy: try 3 days free, then $24.99 each month. Includes live tutor sessions. Subscription auto-renews. Cancel via the profile page. We can't cancel by chat. Prices differ by region.""",
 "3 days free", "$24.99/month", True, "after 3 days", "via the profile page", None, ""),
("""Gutenberg Press Book Club. Introductory offer: 4 books for £1. Then buy 3 more in the next 12 months at the regular price. Membership continues until cancelled: a Book of the Month at £12.99 is sent every month unless you decline it by the date on your statement.""",
 "4 books for £1", "£12.99/month", True, None, "decline each Book of the Month by the date on your statement", None, "A £12.99 book is sent every month unless you decline it by the date on your statement."),
("""My VPN Plus. €3.49 a month for 12 months, billed upfront €41.88. Renews at €7.99 per month. Free 14-day trial included. After 14 days €41.88 will be charged. 30-day money-back guarantee applies to the first purchase only.""",
 "14 days free", "€7.99/month", True, "after 14 days", None, "30-day money-back guarantee applies to the first purchase only", ""),
("""Welcome aboard! The Midnight Library Pass. $5 per month. Your first 30 days are free. Then $5 charged on the 31st day. Cancel any time. No contract. If you have a library card from a participating library, you can skip this and read free.""",
 "first 30 days free", "$5/month", True, "on the 31st day", "any time", None, ""),
("""Gym equipment financing. 0% APR for 12 months, then 29.9% APR on remaining balance. Treadmill T9, $1,899 total. Monthly payment $158.25 for 12 months. This is a purchase, not a membership. Late fee $35.""",
 None, "$158.25/month for 12 months", False, None, None, None, "After the 0% period, any remaining balance accrues 29.9% APR, and late payments cost $35."),
("""Sky High Drone Club. £14.99 a month includes insurance and flight planning. Try 14 days for free. We take payment automatically on day 15. Cancel by emailing pilots@skyhigh.example — we reply within 3 working days. Ts&Cs apply.""",
 "14 days free", "£14.99/month", True, "on day 15", "by emailing pilots@skyhigh.example", None, ""),
("""Parenting Hub Premium
Free 7 days → $9.99 monthly or $69.99 yearly
Pre-selected: yearly
Cancel anytime. Renewal is automatic. We'll send a reminder before your first yearly charge.
Terms | Privacy | Restore""",
 "7 days free", "$69.99/year", True, None, "anytime", None, ""),
("""Hola! Join the Madrid Gym Club. No fee to join. €39 a month. 12-month contract. After 12 months the contract renews automatically for another 12 months unless cancelled 30 days before. Payment is taken on the 5th. Cancel in writing at reception.""",
 None, "€39/month", True, "on the 5th", "in writing at reception, 30 days before the contract ends", None, "The 12-month contract renews automatically for another 12 months unless you cancel in writing 30 days before."),
("""Simple Savings App Premium: invest the change. Try 30 days free. After, $3/month or 0.25% of your balance, whichever is higher. Renews monthly. Cancel in Settings. Investing involves risk. Fees are deducted from your account balance.""",
 "30 days free", "$3/month or 0.25% of your balance, whichever is higher", True, None, "in Settings", None, "Fees are deducted from your balance and can exceed $3 as your savings grow."),
("""Birthday Box Club for your kids. £12.50 per box. Choose when. Pay as you order — no subscription. Free delivery over £30. Orders are non-refundable once personalised. Contact support if there's a problem with your box.""",
 None, "£12.50 per box", False, None, None, "orders are non-refundable once personalised", ""),
("""Rewatch Cinema Classics: 7 days free. After that, $9.99 a month. By continuing you start a monthly subscription that renews until you cancel. Cancel with a single tap on the Manage Plan screen. Taxes may apply. Subscription is tied to your Roku account.""",
 "7 days free", "$9.99/month", True, "after 7 days", "with a single tap on the Manage Plan screen", None, ""),
("""BECOME A FOUNDING MEMBER. £150 for lifetime membership of the Writers' Guild. One payment, no renewals. Includes monthly workshops and a members' directory. 28-day cooling-off period, full refund. Pay by card or bank transfer.""",
 None, "£150 one-time", False, None, None, "28-day cooling-off period, full refund", ""),
("""Run Club app unlocks custom plans. $0 for 3 days, then $8.99 per month. Auto-renew. Your first payment date will be shown in the Apple payment sheet. To cancel go to Settings > your name > Subscriptions. Free trial available once per user.""",
 "3 days at $0", "$8.99/month", True, None, "Settings > your name > Subscriptions", None, ""),
("""Meal Prep Monday. Subscribe to our weekly plan. Starter box $39. After 4 weeks, price changes to $59 per box. Auto-delivered every Monday. Skip up to 2 weeks in a row. Cancel by Wednesday 3pm to avoid next Monday's box. No refunds on delivered boxes.""",
 "starter box $39 for 4 weeks", "$59/week", True, None, "by Wednesday 3pm", "no refunds on delivered boxes", "The price rises from $39 to $59 per box after four weeks."),
("""Our Paper Online. Digital edition 7 days a week. Get 28 days free, then €9.99 per month. 3-month minimum from the end of the free period. Subscription then continues until cancelled. Contact subscriptions@ourpaper.example to cancel.""",
 "28 days free", "€9.99/month", True, None, "contact subscriptions@ourpaper.example", None, "A 3-month minimum starts once the free period ends."),
("""Weekend Hobbyist Woodcraft Kit: £34.99 includes plans, tools, materials. One kit, one payment. Not a subscription. Delivery 3–5 days. Returns accepted within 30 days if unused and in original packaging. Return postage paid by customer.""",
 None, "£34.99 one-time", False, None, None, "returns accepted within 30 days if unused, return postage paid by customer", ""),
("""Seamless Cloud Gaming — 2 weeks for $1, then $19.99 per month. Subscription renews monthly. 'Fair use' applies: 100 hours per month. After 100 hours, play continues at $0.30 per hour. Cancel anytime in your account.""",
 "2 weeks for $1", "$19.99/month", True, None, "anytime in your account", None, "Playing past 100 hours in a month costs an extra $0.30 per hour."),
("""cookies | OK

Bella Vista Italian Online Lessons
Pay £39 per month. Cancel any time before the next payment. 
Your first lesson is free! 
Payment taken from your card each month on the day you sign up.
Refund of unused lessons possible on request.""",
 "first lesson free", "£39/month", True, "on the day you sign up", "any time before the next payment", "refund of unused lessons possible on request", ""),
("""Dream Big Premium: the goal-setting app. Plans: Weekly $9.99 / Yearly $49.99. Try the yearly plan free for 3 days. At the end of your trial, $49.99 will be charged to your iTunes account. If you do not wish to continue, cancel at least 24 hours prior.""",
 "3 days free", "$49.99/year", True, "at the end of your trial", "at least 24 hours prior to the end of the trial", None, ""),
("""Fairway Golf Club membership. Joining fee £500, one time. Annual subscription £1,200, payable in 12 instalments of £100. Membership renews every April 1st. Resignation must be received in writing by 31 January. No refund of joining fee.""",
 None, "£1,200/year", True, "joining fee £500 at joining", "in writing by 31 January", "no refund of joining fee", "Resignation must be in writing by 31 January, or you're liable for the next year's £1,200."),
("""Classic Car Magazine Digital. First issue free, then £3.50 each month by Direct Debit. You'll receive an email before your first payment. Cancel anytime by calling 0330 555 0140. Back issues can be bought separately.""",
 "first issue free", "£3.50/month", True, None, "anytime by calling 0330 555 0140", None, ""),
("""Seven-day free pass to Cloud Orchestra streaming. Afterwards €12.50 a month, taken automatically from your bank account via SEPA. You can end your subscription on the last day of any month. Please allow 5 working days for processing. No refunds.""",
 "seven-day free pass", "€12.50/month", True, "after the free pass", "on the last day of any month; allow 5 working days for processing", "no refunds", ""),
("""START YOUR MEMBERSHIP: Pure Barre Studio. Intro offer $49 for 30 days of unlimited classes. After 30 days, continues at $189 per month. Your card will be charged automatically. Cancel with 30 days' written notice. Intro offer is new clients only.""",
 "30 days of unlimited classes for $49", "$189/month", True, "after 30 days", "with 30 days' written notice", None, "After the $49 intro month you pay $189 a month, and cancelling needs 30 days' written notice."),
("""Study Buddy+ for exam season. Lock in lifetime access for $59.99. No more payments. Includes all current and future subjects. Not a subscription. We offer a full refund if you're not satisfied in the first 30 days. Student ID not required.""",
 None, "$59.99 one-time", False, None, None, "full refund in the first 30 days", ""),
("""Paddle Pass — season pass for the canal marina. £90 for the year. Pay by direct debit in 3 instalments of £30. Pass renews automatically next April. Cancel by 1 March by post or email. No cash refunds; credit toward hire possible.""",
 None, "£90/year", True, None, "by 1 March by post or email", "no cash refunds; credit toward hire possible", ""),
("""Hello! Your free trial of ShopSmart Rewards has started. 30 days free. After the trial, you will pay $14.99 per year (not per month). Your card will be charged on 20 Nov. Renews yearly. Cancel in Account Settings before 20 Nov to avoid charges.""",
 "30 days free", "$14.99/year", True, "on 20 Nov", "in Account Settings before 20 Nov", None, ""),
("""Animal Rescue Monthly Giving. Give £10 a month and save lives. Your donation will be collected on the 1st by Direct Debit. This is not a purchase and no goods are provided. Change or cancel your gift at any time by calling 0300 555 0100 — no questions asked.""",
 None, "£10/month", True, "on the 1st", "at any time by calling 0300 555 0100", None, ""),
("""Photo Restore Pro. Use for 3 days free; $9.99 weekly afterwards. Subscription auto-renews each week. Your Apple ID will be charged after the trial. Cancel in Apple Subscriptions. We can't issue refunds for subscription fees.""",
 "3 days free", "$9.99/week", True, "after the trial", "in Apple Subscriptions", "can't issue refunds for subscription fees", "The weekly $9.99 fee adds up to over $500 a year, and subscription fees can't be refunded."),
("""Simple Plan: Easy Bookkeeping. Month 1 free. £14 per month from month 2, no contract. VAT extra. Add payroll for £5 per employee. Your subscription renews each month. Cancel from Settings. Export your records anytime.""",
 "month 1 free", "£14/month", True, "from month 2", "from Settings", None, ""),
("""Wellness Retreat Weekend. Book now with a £150 deposit. Remaining £450 due 30 days before. One-off booking, not a subscription. Cancel up to 60 days before arrival: deposit refunded minus £25. After that, deposit non-refundable.""",
 None, "£600 one-time", False, None, None, "deposit refunded minus £25 up to 60 days before arrival, non-refundable after that", ""),
("""Streaming kids' shows – Jelly Bean TV! 14 days free, then $5.99 per month. Auto-renew. To keep kids safe, a parent must create the account. Cancel anytime in Parent Zone. No charges after you cancel. Tap 'Start free trial' to begin.""",
 "14 days free", "$5.99/month", True, "after 14 days", "anytime in Parent Zone", None, ""),
("""Download Pro Tax Advisor Q&A. Annual plan $120. Free for 10 days. We'll send you a reminder 3 days before the trial ends. Auto-renewing yearly. Cancel by phone or app. Payments in USD. No refunds on annual plans after day 14.""",
 "10 days free", "$120/year", True, None, "by phone or app", "no refunds on annual plans after day 14", ""),
("""Surprise Me Candy Club. $15.99 a month for 3 bags of sweets. Your first month is free. Billing starts when your second box ships. Pause any time. Cancel online. Sweets can't be returned. Contains allergens.""",
 "first month free", "$15.99/month", True, "when your second box ships", "online", "sweets can't be returned", ""),
])
