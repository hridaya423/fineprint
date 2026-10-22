import json, sys, re
K = ["trial","then","auto_renews","first_charge","cancel","refund","watch_out"]
seen=set(); n=0; trial=0; onetime=0; bad=[]
for i,l in enumerate(open("data/sub_offer.jsonl",encoding="utf-8"),1):
    d=json.loads(l); n+=1
    t=d["text"]; o=d["offer"]
    if set(o)!=set(K): bad.append((i,"keys"))
    if t in seen: bad.append((i,"dup"))
    seen.add(t)
    w=len(t.split())
    if not 30<=w<=150: bad.append((i,f"words {w}"))
    if len(o["watch_out"].split())>20: bad.append((i,"watch>20"))
    if o["watch_out"] and not re.search(r"\byou", o["watch_out"], re.I): bad.append((i,"watch not 2nd person"))
    if o["trial"]: trial+=1
    if "one-time" in str(o["then"]) or o["auto_renews"] is False and o["trial"] is None: onetime+=1
    if re.search(r"\.\.\. |no wait|er,|no, in English|-ish", t): bad.append((i,"glitch text"))
print(n,"lines; trial:",trial,"; onetime-ish:",onetime); print(bad)
