import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).parent
df = pd.read_excel(ROOT / "data" / "marketing_campaign.xlsx")

spend_cols = [
    "MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts",
    "MntSweetProducts", "MntGoldProds",
]
previous_cols = ["AcceptedCmp1", "AcceptedCmp2", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5"]
df["totalSpending"] = df[spend_cols].sum(axis=1)
df["previousCount"] = df[previous_cols].sum(axis=1)
df["previousAccepted"] = (df["previousCount"] > 0).astype(int)
df["ageGroup"] = pd.cut(
    df["Age"],
    bins=[-float("inf"), 30, 40, 50, 60, 70, 100, float("inf")],
    labels=["18–30", "31–40", "41–50", "51–60", "61–70", "71+", "Invalid/Unknown"],
).astype(str)
df["incomeGroup"] = pd.cut(
    pd.to_numeric(df["Income"], errors="coerce"),
    bins=[-float("inf"), 30000, 50000, 70000, 100000, float("inf")],
    labels=["Below 30K", "30–50K", "50–70K", "70–100K", "100K+"],
    right=False,
).astype(str).replace("nan", "Missing")
df["spendingLevel"] = pd.qcut(
    df["totalSpending"], 4, labels=["Low", "Medium", "High", "Very High"]
).astype(str)
df["recencyGroup"] = pd.cut(
    df["Recency"],
    bins=[-1, 30, 60, 90, float("inf")],
    labels=["0–30 days", "31–60 days", "61–90 days", "91+ days"],
).astype(str)
df["tenureCohort"] = "Joined " + pd.to_datetime(
    df["Dt_Customer"], dayfirst=True
).dt.year.astype(str)

fields = [
    "ID", "Response", "previousCount", "previousAccepted", "totalSpending",
    "ageGroup", "incomeGroup", "spendingLevel", "NumWebPurchases",
    "NumStorePurchases", "NumCatalogPurchases", "recencyGroup", "tenureCohort",
    *spend_cols,
]
records = df[fields].to_dict(orient="records")
data_json = json.dumps(records, ensure_ascii=False, separators=(",", ":"))

spending_ranges = (
    df.groupby("spendingLevel", observed=True)["totalSpending"]
    .agg(["min", "max"])
    .astype(int)
    .to_dict("index")
)

html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Retail Promotion Response Optimization Dashboard</title>
<style>
:root{{--ink:#172b4d;--muted:#62748a;--bg:#f3f6fa;--card:#fff;--line:#dce5ef;--teal:#0b8f87;--purple:#6c63b5;--coral:#d35d6e;--blue:#2367a3;--amber:#d38b28}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);font-family:Inter,Segoe UI,Arial,sans-serif;color:var(--ink)}}.shell{{max-width:1480px;margin:auto;padding:24px}}.header{{margin-bottom:18px}}.header h1{{margin:0 0 6px;font-size:27px}}.header p{{margin:0;color:var(--muted)}}
.kpis{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:16px}}.kpi{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;border-left:7px solid var(--c)}}.kpi .label{{font-size:13px;color:var(--muted);font-weight:700}}.kpi .value{{font-size:29px;font-weight:800;margin:5px 0 2px}}.kpi .note{{font-size:12px;color:var(--muted)}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}.card{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px;min-height:350px}}.card.wide{{grid-column:span 2}}.card h2{{font-size:15px;margin:0}}.card .sub{{font-size:12px;color:var(--muted);margin:4px 0 14px}}.insight{{font-size:12px;color:var(--muted);margin-top:10px;line-height:1.4}}
.chart{{min-height:245px;display:flex;align-items:flex-end;gap:10px;padding:12px 8px 28px;border-bottom:1px solid var(--line);position:relative}}.group{{height:220px;flex:1;display:flex;align-items:flex-end;justify-content:center;gap:5px;position:relative;min-width:40px}}.bar{{width:min(32px,42%);min-height:1px;border-radius:5px 5px 0 0;position:relative;transition:.25s}}.bar.latest{{background:var(--teal)}}.bar.previous{{background:var(--purple)}}.bar.web{{background:var(--blue)}}.bar.store{{background:var(--teal)}}.bar.catalogue{{background:var(--purple)}}.bar.visits{{background:var(--amber)}}.bar span{{position:absolute;top:-19px;left:50%;transform:translateX(-50%);font-size:11px;font-weight:800;white-space:nowrap}}.xlabel{{position:absolute;top:226px;left:50%;transform:translateX(-50%);font-size:11px;color:var(--muted);white-space:nowrap;text-align:center}}.nlabel{{position:absolute;top:244px;left:50%;transform:translateX(-50%);font-size:10px;color:#8896a8;white-space:nowrap}}.legend{{display:flex;gap:18px;flex-wrap:wrap;font-size:11px;color:var(--muted);margin-top:12px}}.legend i{{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px}}
.control{{display:flex;align-items:center;gap:8px;margin:0 0 12px}}.control label{{font-size:12px;font-weight:800;color:var(--muted)}}.control select{{border:1px solid #cbd7e4;border-radius:7px;padding:8px;background:#fff;color:var(--ink)}}.analysis-layout{{display:grid;grid-template-columns:minmax(0,1fr) 220px;gap:14px}}.definitions{{background:#f7f9fc;border:1px solid var(--line);border-radius:9px;padding:12px;font-size:12px;color:var(--muted)}}.definitions h3{{font-size:12px;color:var(--ink);margin:0 0 8px}}.definitions ul{{margin:0;padding-left:18px}}.definitions li{{margin:7px 0}}
.actions{{display:grid;grid-template-columns:1.15fr 1fr;gap:14px;margin-top:14px}}.actionbox,.caveat{{border-radius:12px;padding:17px}}.actionbox{{background:#e6f5f3;border:1px solid #b9e0dc}}.caveat{{background:#fff7e8;border:1px solid #f2d7a6}}.actionbox h2,.caveat h2{{font-size:15px;margin:0 0 9px}}.actionbox ul,.caveat ul{{margin:0;padding-left:19px}}.actionbox li,.caveat li{{margin:7px 0;font-size:13px;line-height:1.35}}.footer{{font-size:11px;color:var(--muted);margin-top:14px}}
@media(max-width:900px){{.kpis{{grid-template-columns:repeat(2,1fr)}}.grid{{grid-template-columns:1fr}}.card.wide{{grid-column:span 1}}.actions,.analysis-layout{{grid-template-columns:1fr}}}}
</style></head><body><main class="shell">
<div class="header"><h1>Retail Promotion Response Optimization Dashboard</h1><p>Historical campaign response patterns to support customer prioritization for future promotions.</p></div>
<section class="kpis">
 <div class="kpi" style="--c:var(--teal)"><div class="label">Latest Responders</div><div class="value" id="responders">–</div><div class="note" id="responseRate"></div></div>
 <div class="kpi" style="--c:var(--coral)"><div class="label">Latest Non-Responders</div><div class="value" id="nonresponders">–</div><div class="note" id="nonRate"></div></div>
 <div class="kpi" style="--c:var(--purple)"><div class="label">Accepted Previous Campaign(s)</div><div class="value" id="previous">–</div><div class="note" id="previousRate"></div></div>
 <div class="kpi" style="--c:var(--blue)"><div class="label">Total Customers</div><div class="value" id="total">–</div><div class="note">Unique customer records</div></div>
</section>
<section class="grid">
 <div class="card wide"><h2>Latest response likelihood by previous campaign history</h2><p class="sub">Response rate after accepting 0–5 earlier campaigns</p><div id="history"></div></div>
 <div class="card wide"><h2>Campaign response by customer characteristic</h2><p class="sub">Compare latest response and previous acceptance using one characteristic at a time.</p>
   <div class="control"><label for="analysisParameter">View by</label><select id="analysisParameter"><option value="ageGroup">Age</option><option value="incomeGroup">Income</option><option value="spendingLevel">Spending</option></select></div>
   <div class="analysis-layout"><div id="combined"></div><aside class="definitions" id="definitions"></aside></div>
 </div>
 <div class="card wide"><h2>Preferred purchase channel</h2><p class="sub">Customers grouped by the channel in which they made the most purchases.</p>
   <div class="control"><label for="channelAge">Age group</label><select id="channelAge"><option value="All">All age groups</option><option>18–30</option><option>31–40</option><option>41–50</option><option>51–60</option><option>61–70</option><option>71+</option><option>Invalid/Unknown</option></select></div>
   <div id="channels"></div>
 </div>
 <div class="card"><h2>Product-category spending: responders vs non-responders</h2><p class="sub">Average customer spending in each product category.</p><div id="products"></div></div>
 <div class="card"><h2>Latest response rate by recency</h2><p class="sub">Latest response rate by days since the customer’s last purchase.</p><div id="recency"></div></div>
 <div class="card wide"><h2>Campaign response by customer tenure</h2><p class="sub">Latest response and previous-campaign acceptance by customer join-year cohort.</p><div id="tenure"></div></div>
</section>
<section class="actions"><div class="actionbox"><h2>Recommended actions</h2><ul><li>Retarget customers who accepted earlier campaigns first, because their latest response likelihood is substantially higher.</li><li>Time acquisition messages toward recently active customers; use a separate re-engagement offer for customers whose last purchase was longer ago.</li><li>Feature the product categories on which responders spend most, and tailor the product mix instead of sending one generic promotion.</li><li>Deliver the campaign through each customer’s preferred purchase channel—web, store or catalogue—rather than treating web visits as purchases.</li><li>Use tenure cohorts to separate loyalty offers for established customers from welcome or education-led offers for newer customers.</li><li>Test each priority segment against a control group before scaling; track response rate, incremental sales and campaign cost.</li></ul></div><div class="caveat"><h2>How to use these insights</h2><ul><li>Start with previous campaign history to identify likely responders.</li><li>Use recency to decide when to contact them.</li><li>Use product-category spending to decide what to promote.</li><li>Use preferred channel to decide where to deliver the offer.</li><li>Use tenure as a supporting loyalty signal, not a stand-alone prediction.</li><li>These are historical propensity insights—not guaranteed predictions or a validated machine-learning model.</li></ul></div></section>
<p class="footer">Source: cleaned marketing campaign dataset (2,240 customers). No global filters are applied. Previous campaign acceptance means accepting at least one of Campaigns 1–5.</p>
</main><script>
const DATA={data_json};
const orders={{ageGroup:["18–30","31–40","41–50","51–60","61–70","71+","Invalid/Unknown"],incomeGroup:["Below 30K","30–50K","50–70K","70–100K","100K+","Missing"],spendingLevel:["Low","Medium","High","Very High"],previousCount:[0,1,2,3,4,5],recencyGroup:["0–30 days","31–60 days","61–90 days","91+ days"],tenureCohort:["Joined 2012","Joined 2013","Joined 2014"]}};
const fmt=n=>n.toLocaleString("en-IN"),pct=n=>`${{(n*100).toFixed(1)}}%`;
function grouped(rows,key,order){{return order.map(value=>{{const a=rows.filter(r=>String(r[key])===String(value));return{{value,n:a.length,latest:a.length?a.reduce((s,r)=>s+r.Response,0)/a.length:0,previous:a.length?a.reduce((s,r)=>s+r.previousAccepted,0)/a.length:0}}}}).filter(x=>x.n)}}
function bars(id,groups){{const max=Math.max(.01,...groups.flatMap(g=>[g.latest,g.previous]));document.getElementById(id).innerHTML=`<div class="chart">${{groups.map(g=>`<div class="group"><div class="bar latest" style="height:${{190*g.latest/max}}px"><span>${{pct(g.latest)}}</span></div><div class="bar previous" style="height:${{190*g.previous/max}}px"><span>${{pct(g.previous)}}</span></div><div class="xlabel">${{g.value}}</div><div class="nlabel">n=${{fmt(g.n)}}</div></div>`).join("")}}</div><div class="legend"><span><i style="background:var(--teal)"></i>Latest response rate</span><span><i style="background:var(--purple)"></i>Accepted at least one previous campaign</span></div>`}}
function singleRateBars(id,groups,labeler=v=>v){{const max=Math.max(.01,...groups.map(g=>g.latest));document.getElementById(id).innerHTML=`<div class="chart">${{groups.map(g=>`<div class="group"><div class="bar latest" style="height:${{190*g.latest/max}}px;width:min(52px,62%)"><span>${{pct(g.latest)}}</span></div><div class="xlabel">${{labeler(g.value)}}</div><div class="nlabel">n=${{fmt(g.n)}}</div></div>`).join("")}}</div><div class="legend"><span><i style="background:var(--teal)"></i>Latest campaign response rate</span></div>`}}
const definitions={{
 ageGroup:`<h3>Age-group definitions</h3><ul><li>18–30</li><li>31–40</li><li>41–50</li><li>51–60</li><li>61–70</li><li>71+</li><li>Invalid/Unknown: age above 100</li></ul>`,
 incomeGroup:`<h3>Income-band definitions</h3><ul><li>Below 30K</li><li>30K–49,999</li><li>50K–69,999</li><li>70K–99,999</li><li>100K+</li><li>Missing: income recorded as Null</li></ul>`,
 spendingLevel:`<h3>Spending-group definitions</h3><ul><li>Low: {spending_ranges["Low"]["min"]}–{spending_ranges["Low"]["max"]}</li><li>Medium: {spending_ranges["Medium"]["min"]}–{spending_ranges["Medium"]["max"]}</li><li>High: {spending_ranges["High"]["min"]}–{spending_ranges["High"]["max"]}</li><li>Very High: {spending_ranges["Very High"]["min"]}–{spending_ranges["Very High"]["max"]}</li></ul><p>Total spending is the sum spent across all product categories.</p>`
}};
function renderCombined(){{const key=document.getElementById("analysisParameter").value;bars("combined",grouped(DATA,key,orders[key]));document.getElementById("definitions").innerHTML=definitions[key]}}
function renderChannels(){{const age=document.getElementById("channelAge").value,rows=age==="All"?DATA:DATA.filter(r=>r.ageGroup===age);const counts={{Web:0,Store:0,Catalogue:0,"Multiple channels":0}};rows.forEach(r=>{{const vals=[["Web",r.NumWebPurchases],["Store",r.NumStorePurchases],["Catalogue",r.NumCatalogPurchases]],m=Math.max(...vals.map(x=>x[1])),w=vals.filter(x=>x[1]===m);counts[w.length===1?w[0][0]:"Multiple channels"]++}});const items=[["Web","web"],["Store","store"],["Catalogue","catalogue"],["Multiple channels","visits"]].map(([label,cls])=>({{label,cls,value:counts[label]}})),max=Math.max(...items.map(x=>x.value));document.getElementById("channels").innerHTML=`<div class="chart">${{items.map(x=>`<div class="group"><div class="bar ${{x.cls}}" style="height:${{190*x.value/max}}px;width:min(58px,68%)"><span>${{fmt(x.value)}}</span></div><div class="xlabel">${{x.label}}</div></div>`).join("")}}</div><div class="legend">${{items.map(x=>`<span><i style="background:var(--${{x.cls==="web"?"blue":x.cls==="store"?"teal":x.cls==="catalogue"?"purple":"amber"}})"></i>${{x.label}}</span>`).join("")}}</div><div class="insight">Preferred channel is the channel with the highest purchase count for each customer. “Multiple channels” indicates a tie.</div>`}}
function productBars(){{const cats=[["Wine","MntWines"],["Fruits","MntFruits"],["Meat","MntMeatProducts"],["Fish","MntFishProducts"],["Sweets","MntSweetProducts"],["Gold","MntGoldProds"]],groups=cats.map(([value,key])=>{{const yes=DATA.filter(r=>r.Response===1),no=DATA.filter(r=>r.Response===0);return{{value,n:DATA.length,latest:yes.reduce((s,r)=>s+r[key],0)/yes.length,previous:no.reduce((s,r)=>s+r[key],0)/no.length}}}}),max=Math.max(...groups.flatMap(g=>[g.latest,g.previous]));document.getElementById("products").innerHTML=`<div class="chart">${{groups.map(g=>`<div class="group"><div class="bar latest" style="height:${{190*g.latest/max}}px"><span>${{g.latest.toFixed(0)}}</span></div><div class="bar previous" style="height:${{190*g.previous/max}}px"><span>${{g.previous.toFixed(0)}}</span></div><div class="xlabel">${{g.value}}</div></div>`).join("")}}</div><div class="legend"><span><i style="background:var(--teal)"></i>Latest responders</span><span><i style="background:var(--purple)"></i>Latest non-responders</span></div><div class="insight">Values are average spend per customer, so unequal group sizes do not distort the comparison.</div>`}}
function render(){{const responders=DATA.filter(x=>x.Response===1).length,prev=DATA.filter(x=>x.previousAccepted===1).length;document.getElementById("responders").textContent=fmt(responders);document.getElementById("nonresponders").textContent=fmt(DATA.length-responders);document.getElementById("previous").textContent=fmt(prev);document.getElementById("total").textContent=fmt(DATA.length);document.getElementById("responseRate").textContent=pct(responders/DATA.length)+" of all customers";document.getElementById("nonRate").textContent=pct((DATA.length-responders)/DATA.length)+" of all customers";document.getElementById("previousRate").textContent=pct(prev/DATA.length)+" accepted at least one";singleRateBars("history",grouped(DATA,"previousCount",orders.previousCount),v=>`${{v}} accepted`);renderCombined();renderChannels();productBars();singleRateBars("recency",grouped(DATA,"recencyGroup",orders.recencyGroup));bars("tenure",grouped(DATA,"tenureCohort",orders.tenureCohort))}}
document.getElementById("analysisParameter").addEventListener("change",renderCombined);document.getElementById("channelAge").addEventListener("change",renderChannels);render();
</script></body></html>"""

(ROOT / "dashboard" / "index.html").write_text(html, encoding="utf-8")
