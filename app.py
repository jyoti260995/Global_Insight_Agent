import streamlit as st
import json
import re

st.set_page_config(page_title="GlobalInsight", page_icon="🌍", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
*,*::before,*::after{box-sizing:border-box;}
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],.main,.stMainBlockContainer,.block-container,[data-testid="stVerticalBlock"],[data-testid="stVerticalBlockBorderWrapper"],.element-container,.stMarkdown{background:transparent!important;font-family:'DM Sans',sans-serif!important;}
[data-testid="stAppViewContainer"]{background:radial-gradient(ellipse 90% 45% at 50% -5%,rgba(56,189,248,.10) 0%,transparent 55%),radial-gradient(ellipse 55% 35% at 85% 85%,rgba(99,102,241,.07) 0%,transparent 50%),#070b13!important;min-height:100vh;color:#e2e8f0!important;}
[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"]{display:none!important;}
section[data-testid="stSidebar"]{display:none!important;}
.block-container{max-width:700px!important;padding:0 1.5rem 5rem!important;}
.gi-hero{text-align:center;padding:4rem 0 2rem;}
.gi-globe{font-size:3.8rem;display:block;margin-bottom:.9rem;animation:floatGlobe 4s ease-in-out infinite;filter:drop-shadow(0 0 28px rgba(56,189,248,.55));}
@keyframes floatGlobe{0%,100%{transform:translateY(0);}50%{transform:translateY(-10px);}}
.gi-title{font-family:'Syne',sans-serif;font-size:2.9rem;font-weight:800;letter-spacing:-.03em;background:linear-gradient(135deg,#f1f5ff 25%,#38bdf8 65%,#818cf8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;margin-bottom:.55rem;}
.gi-sub{color:#475569;font-size:.95rem;}
[data-testid="stTextInput"] input{background:#0f172a!important;border:1px solid rgba(56,189,248,.25)!important;border-radius:11px!important;color:#f1f5ff!important;font-family:'DM Sans',sans-serif!important;font-size:1.05rem!important;padding:.8rem 1rem!important;caret-color:#38bdf8!important;}
[data-testid="stTextInput"] input:focus{border-color:rgba(56,189,248,.55)!important;box-shadow:0 0 0 3px rgba(56,189,248,.1)!important;outline:none!important;}
[data-testid="stTextInput"] input::placeholder{color:#334155!important;}
[data-testid="stTextInput"] label{display:none!important;}
[data-testid="stButton"]>button{width:100%!important;background:linear-gradient(130deg,#0ea5e9 0%,#6366f1 100%)!important;color:#fff!important;border:none!important;border-radius:11px!important;font-family:'Syne',sans-serif!important;font-size:.88rem!important;font-weight:700!important;letter-spacing:.1em!important;text-transform:uppercase!important;padding:.8rem!important;margin-top:.6rem!important;box-shadow:0 4px 22px rgba(14,165,233,.28)!important;transition:opacity .2s,transform .15s!important;}
[data-testid="stButton"]>button:hover{opacity:.88!important;transform:translateY(-1px)!important;}
.gi-pills{display:flex;flex-wrap:wrap;gap:.45rem;justify-content:center;margin:1.4rem 0 0;}
.gi-pill{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:999px;padding:.3rem .85rem;font-size:.78rem;color:#475569;}

/* result card */
.gi-result{background:#0d1526;border:1px solid rgba(99,102,241,.25);border-radius:18px;margin-top:1.6rem;overflow:hidden;box-shadow:0 12px 50px rgba(0,0,0,.6);animation:fadeUp .38s ease-out both;}
@keyframes fadeUp{from{opacity:0;transform:translateY(14px);}to{opacity:1;transform:translateY(0);}}
.gi-result-header{background:#111827;padding:1.3rem 2rem;border-bottom:1px solid rgba(255,255,255,.07);display:flex;align-items:center;gap:.7rem;}
.gi-result-city{font-family:'Syne',sans-serif;font-size:1.55rem;font-weight:700;color:#f1f5ff;}
.gi-result-body{background:#0d1526;padding:1.6rem 2rem;}
.gi-weather{background:rgba(56,189,248,.08);border:1px solid rgba(56,189,248,.18);border-radius:13px;padding:1.1rem 1.3rem;margin-bottom:1.6rem;}
.gi-sec-label{font-family:'Syne',sans-serif;font-size:.65rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#38bdf8;margin-bottom:.7rem;display:block;}
.gi-wgrid{display:grid;grid-template-columns:1fr 1fr;gap:.6rem 1.2rem;margin-top:.3rem;}
.gi-wrow{display:flex;flex-direction:column;gap:.1rem;}
.gi-wlabel{font-size:.7rem;color:#475569;text-transform:uppercase;letter-spacing:.08em;}
.gi-wval{font-size:1.05rem;color:#e2e8f0;font-weight:500;}
.gi-news-item{display:flex;gap:.9rem;align-items:flex-start;padding:.9rem 0;border-bottom:1px solid rgba(255,255,255,.06);}
.gi-news-item:last-child{border-bottom:none;padding-bottom:0;}
.gi-num{font-family:'Syne',sans-serif;font-size:.65rem;font-weight:800;background:rgba(99,102,241,.18);color:#818cf8;border-radius:7px;padding:.22rem .45rem;min-width:30px;text-align:center;margin-top:3px;flex-shrink:0;}
.gi-news-title{font-size:.94rem;color:#cbd5e1;line-height:1.5;}
.gi-news-link{display:inline-block;margin-top:.25rem;font-size:.75rem;color:#38bdf8;text-decoration:none;}
.gi-news-link:hover{text-decoration:underline;}
</style>
""", unsafe_allow_html=True)


def call_agent(location: str) -> dict:
    from agent import agent
    query = (
        f"For {location} provide current weather and top 5 news. "
        "Reply with ONLY a raw JSON object (no markdown, no code fences, no explanation). "
        "Schema: "
        '{"weather":{"temperature":"...","conditions":"...","humidity":"...","wind":"..."},'
        '"news":[{"headline":"...","url":"..."}]}'
    )
    resp = agent.invoke({"messages": [{"role": "user", "content": query}]})
    raw  = resp["messages"][-1].content
    # strip markdown fences if present
    raw  = re.sub(r"```[a-z]*", "", raw).replace("```", "").strip()
    # extract first JSON object
    m = re.search(r'\{.*\}', raw, re.DOTALL)
    if not m:
        raise ValueError(f"No JSON in response: {raw[:300]}")
    return json.loads(m.group())


def render_card(location: str, data: dict):
    w    = data.get("weather", {})
    news = data.get("news", [])[:5]

    # ── weather grid rows ──────────────────────────────────────────────────
    fields = [
        ("🌡", "TEMPERATURE", w.get("temperature", "—")),
        ("☁️", "CONDITIONS",  w.get("conditions",  "—")),
        ("💧", "HUMIDITY",    w.get("humidity",    "—")),
        ("💨", "WIND",        w.get("wind",        "—")),
    ]
    wgrid = "".join(
        f'<div class="gi-wrow">'
        f'<span class="gi-wlabel">{ico} {lbl}</span>'
        f'<span class="gi-wval">{val}</span>'
        f'</div>'
        for ico, lbl, val in fields
    )

    # ── news rows ──────────────────────────────────────────────────────────
    news_rows = ""
    for i, item in enumerate(news, 1):
        h   = item.get("headline", "")
        url = item.get("url", "")
        lnk = f'<a class="gi-news-link" href="{url}" target="_blank">↗ Read more</a>' if url else ""
        news_rows += (
            f'<div class="gi-news-item">'
            f'<span class="gi-num">{i:02d}</span>'
            f'<div><div class="gi-news-title">{h}</div>{lnk}</div>'
            f'</div>'
        )

    # ── single html string — render in ONE call ────────────────────────────
    html = (
        f'<div class="gi-result">'
        f'<div class="gi-result-header">'
        f'<span style="font-size:1.5rem">📍</span>'
        f'<span class="gi-result-city">{location.title()}</span>'
        f'</div>'
        f'<div class="gi-result-body">'
        f'<div class="gi-weather">'
        f'<span class="gi-sec-label">🌡&nbsp;CURRENT WEATHER</span>'
        f'<div class="gi-wgrid">{wgrid}</div>'
        f'</div>'
        f'<span class="gi-sec-label">📰&nbsp;LATEST HEADLINES</span>'
        f'{news_rows}'
        f'</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


# ── UI ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="gi-hero">
  <span class="gi-globe">🌍</span>
  <div class="gi-title">GlobalInsight</div>
  <div class="gi-sub">Real-time weather &amp; news · Anywhere on Earth</div>
</div>""", unsafe_allow_html=True)

location = st.text_input("loc",
    placeholder="e.g. Tokyo, Cape Town, Buenos Aires, Delhi…",
    label_visibility="collapsed")
go = st.button("🔍  Get Insights")

st.markdown("""
<div class="gi-pills">
  <span class="gi-pill">🗼 Tokyo</span><span class="gi-pill">🗽 New York</span>
  <span class="gi-pill">🏯 Delhi</span><span class="gi-pill">🌉 London</span>
  <span class="gi-pill">🎭 Paris</span><span class="gi-pill">🦁 Nairobi</span>
  <span class="gi-pill">🏖 Sydney</span><span class="gi-pill">🌴 Dubai</span>
</div>""", unsafe_allow_html=True)

if go:
    if not location.strip():
        st.warning("⚠️  Please type a location first.")
    else:
        with st.spinner(f"Scanning the globe for {location.title()}…"):
            try:
                data = call_agent(location.strip())
                render_card(location.strip(), data)
            except json.JSONDecodeError as e:
                st.error(f"JSON parse error: {e}")
            except Exception as e:
                st.error(f"Something went wrong: {e}")