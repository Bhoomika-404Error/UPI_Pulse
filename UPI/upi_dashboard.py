import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="UPI Pulse — India's Digital Payment Revolution",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CUSTOM CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    background-color: #050A0E;
    color: #E8EDF2;
}

.main { background-color: #050A0E; }
.block-container { padding: 2rem 3rem 4rem 3rem; max-width: 1400px; }

/* ── Hero Header ── */
.hero-wrap {
    position: relative;
    padding: 3.5rem 0 2.5rem 0;
    margin-bottom: 2.5rem;
    border-bottom: 1px solid rgba(255,183,77,0.15);
    overflow: hidden;
}
.hero-wrap::before {
    content: "₹";
    position: absolute;
    right: -20px;
    top: -30px;
    font-size: 280px;
    font-family: 'Syne', 'Segoe UI', system-ui, sans-serif;
    font-weight: 800;
    color: rgba(255,183,77,0.04);
    line-height: 1;
    pointer-events: none;
    user-select: none;
}
.hero-eyebrow {
    font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #FFB74D;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-family: 'Syne', 'Segoe UI', system-ui, sans-serif;
    font-size: clamp(2.4rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.05;
    margin: 0 0 0.8rem 0;
    color: #FFFFFF;
    text-shadow: 0 0 60px rgba(255,183,77,0.5), 0 2px 4px rgba(0,0,0,0.8);
    letter-spacing: -0.02em;
}
.hero-sub {
    font-size: 1rem;
    color: rgba(232,237,242,0.55);
    max-width: 620px;
    line-height: 1.6;
    font-weight: 300;
}

/* ── KPI Cards ── */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.2rem;
    margin-bottom: 2.5rem;
}
.kpi-card {
    background: linear-gradient(145deg, #0D1A24 0%, #0A1520 100%);
    border: 1px solid rgba(255,183,77,0.12);
    border-radius: 16px;
    padding: 1.5rem 1.6rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s ease, transform 0.2s ease;
}
.kpi-card:hover {
    border-color: rgba(255,183,77,0.35);
    transform: translateY(-2px);
}
.kpi-card::after {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #FFB74D, #FF7043);
    border-radius: 16px 16px 0 0;
}
.kpi-label {
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: rgba(232,237,242,0.4);
    margin-bottom: 0.5rem;
    font-weight: 500;
}
.kpi-value {
    font-family: 'Syne', 'Segoe UI', system-ui, sans-serif;
    font-size: 2.1rem;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1;
    margin-bottom: 0.35rem;
}
.kpi-delta {
    font-size: 0.8rem;
    color: #66BB6A;
    font-weight: 500;
}
.kpi-delta.neg { color: #EF5350; }

/* ── Section headings ── */
.section-title {
    font-family: 'Syne', 'Segoe UI', system-ui, sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #FFFFFF;
    margin: 0 0 1.2rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-title span {
    display: inline-block;
    width: 18px; height: 3px;
    background: linear-gradient(90deg,#FFB74D,#FF7043);
    border-radius: 2px;
}

/* ── Milestone cards ── */
.milestone-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}
.milestone-chip {
    background: rgba(255,183,77,0.08);
    border: 1px solid rgba(255,183,77,0.2);
    border-radius: 50px;
    padding: 0.45rem 1.1rem;
    font-size: 0.8rem;
    color: #FFB74D;
    white-space: nowrap;
}
.milestone-chip strong { color: #FFFFFF; }

/* ── Footer ── */
.footer {
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(255,255,255,0.06);
    font-size: 0.75rem;
    color: rgba(232,237,242,0.28);
    text-align: center;
    letter-spacing: 0.03em;
}

/* ── Plotly chart containers ── */
.chart-wrap {
    background: #0D1A24;
    border: 1px solid rgba(255,183,77,0.1);
    border-radius: 16px;
    padding: 0.5rem;
    margin-bottom: 1.5rem;
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
div[data-testid="stToolbar"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ─── DATA: Real NPCI UPI monthly figures (FY2020–FY2025) ────────────────────
# Source: NPCI official statistics (npci.org.in/what-we-do/upi/upi-ecosystem-statistics)
data = {
    "Month": [
        # FY 2019-20
        "Apr-19","May-19","Jun-19","Jul-19","Aug-19","Sep-19",
        "Oct-19","Nov-19","Dec-19","Jan-20","Feb-20","Mar-20",
        # FY 2020-21
        "Apr-20","May-20","Jun-20","Jul-20","Aug-20","Sep-20",
        "Oct-20","Nov-20","Dec-20","Jan-21","Feb-21","Mar-21",
        # FY 2021-22
        "Apr-21","May-21","Jun-21","Jul-21","Aug-21","Sep-21",
        "Oct-21","Nov-21","Dec-21","Jan-22","Feb-22","Mar-22",
        # FY 2022-23
        "Apr-22","May-22","Jun-22","Jul-22","Aug-22","Sep-22",
        "Oct-22","Nov-22","Dec-22","Jan-23","Feb-23","Mar-23",
        # FY 2023-24
        "Apr-23","May-23","Jun-23","Jul-23","Aug-23","Sep-23",
        "Oct-23","Nov-23","Dec-23","Jan-24","Feb-24","Mar-24",
        # FY 2024-25
        "Apr-24","May-24","Jun-24","Jul-24","Aug-24","Sep-24",
        "Oct-24","Nov-24","Dec-24","Jan-25","Feb-25","Mar-25",
    ],
    "Volume_Cr": [
        # FY20
        78,90,103,107,120,124,121,117,131,132,118,125,
        # FY21
        99,111,133,151,162,181,207,221,227,231,229,273,
        # FY22
        264,255,283,324,356,365,421,423,456,462,412,505,
        # FY23
        558,595,596,628,657,678,730,730,782,804,753,865,
        # FY24
        899,939,937,1003,1058,1124,1173,1137,1229,1257,1201,1340,
        # FY25
        1330,1411,1399,1446,1488,1553,1660,1548,1718,1758,1683,1836,
    ],
    "Value_LCr": [
        # FY20 (₹ Lakh Crore)
        1.00, 1.17, 1.46, 1.48, 1.66, 1.61,
        1.91, 1.77, 2.02, 2.02, 1.90, 2.06,
        # FY21
        1.51, 1.51, 1.91, 2.20, 2.34, 2.61,
        3.07, 3.18, 3.41, 3.56, 3.30, 4.25,
        # FY22
        4.02, 3.73, 4.26, 4.90, 5.47, 5.64,
        6.54, 6.42, 7.15, 8.32, 6.84, 9.60,
        # FY23
        9.83,10.40,10.14,10.62,10.73,11.63,
        12.11,11.90,13.37,12.98,12.35,14.05,
        # FY24
        14.07,14.89,14.75,15.34,15.76,17.13,
        17.16,17.41,18.23,18.41,18.28,19.78,
        # FY25
        20.14,20.44,20.07,20.64,20.61,23.49,
        23.50,21.55,23.25,23.48,21.97,24.77,
    ],
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Month"], format="%b-%y")
df = df.sort_values("Date").reset_index(drop=True)

# Derived columns
df["Value_Cr"] = df["Value_LCr"] * 1_00_000   # ₹ Crore
df["FY"] = df["Date"].apply(
    lambda d: f"FY{(d.year+1) % 100:02d}" if d.month >= 4 else f"FY{d.year % 100:02d}"
)
df["YoY_Vol"] = df["Volume_Cr"].pct_change(12) * 100
df["YoY_Val"] = df["Value_LCr"].pct_change(12) * 100
df["CumVol_Cr"] = df["Volume_Cr"].cumsum()

# Annual aggregates
fy_df = df.groupby("FY").agg(
    Vol=("Volume_Cr", "sum"),
    Val=("Value_LCr", "sum"),
).reset_index()
fy_df["FY_label"] = fy_df["FY"]

# ─── KPIs ───────────────────────────────────────────────────────────────────
latest = df.iloc[-1]
prev_yr = df.iloc[-13] if len(df) >= 13 else df.iloc[0]

total_vol_fy25 = df[df["FY"] == "FY25"]["Volume_Cr"].sum()
total_val_fy25 = df[df["FY"] == "FY25"]["Value_LCr"].sum()
peak_month = df.loc[df["Volume_Cr"].idxmax()]
yoy_vol_latest = latest["YoY_Vol"]
yoy_val_latest = latest["YoY_Val"]

# ─── HERO ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
  <div class="hero-eyebrow">🇮🇳 Real Data · NPCI Official Statistics</div>
  <div class="hero-title">UPI Pulse</div>
  <div class="hero-sub">
    Six years of India's digital payments revolution — visualised.
    From ₹1 lakh crore months to ₹24 lakh crore months, the story of how a billion people moved to instant payments.
  </div>
</div>
""", unsafe_allow_html=True)

# ─── MILESTONES ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="milestone-row">
  <div class="milestone-chip">🏆 <strong>Mar 2025</strong> — ₹24.77L Cr all-time record value</div>
  <div class="milestone-chip">🚀 <strong>Oct 2024</strong> — 1,660 Cr txns in a month</div>
  <div class="milestone-chip">📈 <strong>FY25</strong> — 1.83 trillion $ equivalent processed</div>
  <div class="milestone-chip">⚡ <strong>FY21→FY22</strong> — 85% YoY volume surge post-COVID</div>
  <div class="milestone-chip">🌍 Largest real-time payments system on Earth</div>
</div>
""", unsafe_allow_html=True)

# ─── KPI CARDS ───────────────────────────────────────────────────────────────
d_vol = f"+{yoy_vol_latest:.1f}% YoY" if yoy_vol_latest >= 0 else f"{yoy_vol_latest:.1f}% YoY"
d_val = f"+{yoy_val_latest:.1f}% YoY" if yoy_val_latest >= 0 else f"{yoy_val_latest:.1f}% YoY"

st.markdown(f"""
<div class="kpi-grid">
  <div class="kpi-card">
    <div class="kpi-label">Latest Month Volume</div>
    <div class="kpi-value">{latest['Volume_Cr']:.0f} Cr</div>
    <div class="kpi-delta">{d_vol}</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">Latest Month Value</div>
    <div class="kpi-value">₹{latest['Value_LCr']:.2f}L Cr</div>
    <div class="kpi-delta">{d_val}</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">FY25 Total Volume</div>
    <div class="kpi-value">{total_vol_fy25/100:.2f}B txns</div>
    <div class="kpi-delta">↑ from {df[df['FY']=='FY24']['Volume_Cr'].sum()/100:.2f}B in FY24</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">FY25 Total Value</div>
    <div class="kpi-value">₹{total_val_fy25:.0f}L Cr</div>
    <div class="kpi-delta">~$2.7 Trillion USD</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── CHART THEME ─────────────────────────────────────────────────────────────
BG        = "#0D1A24"
GRID      = "rgba(255,255,255,0.04)"
AMBER     = "#FFB74D"
ORANGE    = "#FF7043"
GREEN     = "#66BB6A"
TEXT_DIM  = "rgba(232,237,242,0.4)"
FONT_BODY = "DM Sans"

def base_layout(title="", h=420):
    return dict(
        height=h,
        title=dict(text=title, font=dict(family="Syne, Segoe UI, system-ui, sans-serif", size=15, color="#FFFFFF"), x=0.02, xanchor="left") if title else {},
        paper_bgcolor=BG,
        plot_bgcolor=BG,
        font=dict(family="DM Sans, -apple-system, Segoe UI, system-ui, sans-serif", color=TEXT_DIM, size=12),
        margin=dict(l=20, r=20, t=50 if title else 30, b=30),
        xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(size=11)),
        yaxis=dict(showgrid=True, gridcolor=GRID, zeroline=False, tickfont=dict(size=11)),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=12)),
        hovermode="x unified",
    )

# ─── ROW 1: Main trend ───────────────────────────────────────────────────────
st.markdown('<div class="section-title"><span></span>Transaction Volume & Value — Monthly Trend</div>', unsafe_allow_html=True)

fig1 = make_subplots(specs=[[{"secondary_y": True}]])

# Volume area
fig1.add_trace(go.Scatter(
    x=df["Date"], y=df["Volume_Cr"],
    name="Volume (Cr txns)",
    fill="tozeroy",
    fillcolor="rgba(255,183,77,0.08)",
    line=dict(color=AMBER, width=2.5),
    hovertemplate="<b>%{y:.0f} Cr</b> txns",
), secondary_y=False)

# Value line
fig1.add_trace(go.Scatter(
    x=df["Date"], y=df["Value_LCr"],
    name="Value (₹ Lakh Cr)",
    line=dict(color=ORANGE, width=2.5, dash="dot"),
    hovertemplate="₹<b>%{y:.2f}</b> Lakh Cr",
), secondary_y=True)

# Annotate peak
fig1.add_annotation(
    x=df.loc[df["Volume_Cr"].idxmax(), "Date"],
    y=df["Volume_Cr"].max(),
    text=f"🏆 {df['Volume_Cr'].max():.0f} Cr<br>All-time peak",
    showarrow=True, arrowhead=2, arrowcolor=AMBER,
    font=dict(size=11, color=AMBER),
    bgcolor="rgba(13,26,36,0.9)",
    bordercolor=AMBER,
    ax=40, ay=-40,
    secondary_y=False,
)

layout1 = base_layout(h=400)
layout1["yaxis"]["title"] = dict(text="Volume (Crore transactions)", font=dict(color=AMBER))
layout1["yaxis2"] = dict(
    title=dict(text="Value (₹ Lakh Crore)", font=dict(color=ORANGE)),
    showgrid=False, zeroline=False, tickfont=dict(size=11),
    overlaying="y", side="right",
)
fig1.update_layout(**layout1)
st.plotly_chart(fig1, use_container_width=True)

# ─── ROW 2: Annual bars + YoY growth ─────────────────────────────────────────
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.markdown('<div class="section-title"><span></span>Annual Volume by Financial Year</div>', unsafe_allow_html=True)
    colors_bar = [AMBER if i < len(fy_df)-1 else ORANGE for i in range(len(fy_df))]
    fig2 = go.Figure(go.Bar(
        x=fy_df["FY_label"],
        y=fy_df["Vol"],
        marker=dict(
            color=colors_bar,
            line=dict(width=0),
            cornerradius=8,
        ),
        hovertemplate="<b>%{x}</b><br>Volume: %{y:.0f} Cr txns<extra></extra>",
    ))
    fig2.update_layout(**base_layout(h=360))
    fig2.update_yaxes(title_text="Crore Transactions", title_font=dict(size=11))
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.markdown('<div class="section-title"><span></span>Year-on-Year Growth Rate (%)</div>', unsafe_allow_html=True)
    yoy_data = df.dropna(subset=["YoY_Vol"]).copy()
    yoy_colors = [GREEN if v >= 0 else "#EF5350" for v in yoy_data["YoY_Vol"]]

    fig3 = go.Figure(go.Bar(
        x=yoy_data["Date"],
        y=yoy_data["YoY_Vol"],
        marker=dict(color=yoy_colors, line=dict(width=0), cornerradius=4),
        hovertemplate="<b>%{x|%b %Y}</b><br>YoY Growth: <b>%{y:.1f}%</b><extra></extra>",
    ))
    fig3.add_hline(y=0, line_color="rgba(255,255,255,0.15)", line_width=1)
    fig3.update_layout(**base_layout(h=360))
    fig3.update_yaxes(title_text="YoY Volume Growth (%)", title_font=dict(size=11))
    st.plotly_chart(fig3, use_container_width=True)

# ─── ROW 3: Value growth + cumulative ────────────────────────────────────────
col3, col4 = st.columns([1, 1], gap="medium")

with col3:
    st.markdown('<div class="section-title"><span></span>Annual Value Processed (₹ Lakh Crore)</div>', unsafe_allow_html=True)
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(
        x=fy_df["FY_label"], y=fy_df["Val"],
        marker=dict(
            color=fy_df["Val"],
            colorscale=[[0, "#0D3349"], [0.5, AMBER], [1, ORANGE]],
            showscale=False,
            line=dict(width=0),
            cornerradius=8,
        ),
        hovertemplate="<b>%{x}</b><br>₹%{y:.1f} Lakh Cr<extra></extra>",
    ))
    fig4.update_layout(**base_layout(h=360))
    fig4.update_yaxes(title_text="₹ Lakh Crore", title_font=dict(size=11))
    st.plotly_chart(fig4, use_container_width=True)

with col4:
    st.markdown('<div class="section-title"><span></span>Cumulative Transactions Since Apr 2019</div>', unsafe_allow_html=True)
    fig5 = go.Figure(go.Scatter(
        x=df["Date"], y=df["CumVol_Cr"],
        fill="tozeroy",
        fillcolor="rgba(102,187,106,0.07)",
        line=dict(color=GREEN, width=2.5),
        hovertemplate="<b>%{x|%b %Y}</b><br>Cumulative: <b>%{y:.0f} Cr</b><extra></extra>",
    ))
    # annotate total
    fig5.add_annotation(
        x=df["Date"].iloc[-1], y=df["CumVol_Cr"].iloc[-1],
        text=f"<b>{df['CumVol_Cr'].iloc[-1]:.0f} Cr</b><br>total txns",
        showarrow=False,
        font=dict(size=12, color=GREEN),
        xanchor="right", yanchor="top",
        bgcolor="rgba(13,26,36,0.9)",
        bordercolor=GREEN,
    )
    fig5.update_layout(**base_layout(h=360))
    fig5.update_yaxes(title_text="Cumulative Crore Transactions", title_font=dict(size=11))
    st.plotly_chart(fig5, use_container_width=True)

# ─── ROW 4: Heatmap ──────────────────────────────────────────────────────────
st.markdown('<div class="section-title"><span></span>Monthly Volume Heatmap — Seasonality & Growth</div>', unsafe_allow_html=True)

hm_df = df.copy()
hm_df["Year"] = hm_df["Date"].dt.year
hm_df["MonthName"] = hm_df["Date"].dt.strftime("%b")
month_order = ["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar"]
pivot = hm_df.pivot_table(index="FY", values="Volume_Cr", columns="MonthName", aggfunc="sum")
pivot = pivot.reindex(columns=month_order, fill_value=None)
pivot = pivot.reindex(["FY20","FY21","FY22","FY23","FY24","FY25"])

fig6 = go.Figure(go.Heatmap(
    z=pivot.values,
    x=month_order,
    y=pivot.index.tolist(),
    colorscale=[[0,"#0D1A24"],[0.3,"#1A3A50"],[0.6,AMBER],[1,ORANGE]],
    hovertemplate="<b>%{y} %{x}</b><br>Volume: <b>%{z:.0f} Cr</b><extra></extra>",
    showscale=True,
    colorbar=dict(
        title=dict(text="Cr txns", font=dict(size=11)),
        tickfont=dict(size=10),
        thickness=12,
        len=0.8,
    ),
    xgap=3, ygap=3,
))
hm_layout = base_layout(h=280)
hm_layout["xaxis"]["showgrid"] = False
hm_layout["yaxis"]["showgrid"] = False
fig6.update_layout(**hm_layout)
st.plotly_chart(fig6, use_container_width=True)

# ─── DATA TABLE ──────────────────────────────────────────────────────────────
with st.expander("📋 View Raw Monthly Data"):
    display_df = df[["Month","Volume_Cr","Value_LCr","YoY_Vol","YoY_Val"]].copy()
    display_df.columns = ["Month","Volume (Cr)","Value (₹L Cr)","YoY Vol %","YoY Val %"]
    display_df = display_df.sort_values("Month", ascending=False).reset_index(drop=True)
    display_df["YoY Vol %"] = display_df["YoY Vol %"].map(lambda x: f"{x:+.1f}%" if pd.notna(x) else "—")
    display_df["YoY Val %"] = display_df["YoY Val %"].map(lambda x: f"{x:+.1f}%" if pd.notna(x) else "—")
    st.dataframe(display_df, use_container_width=True, height=320)

# ─── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  Data sourced from NPCI official UPI Ecosystem Statistics &nbsp;·&nbsp;
  npci.org.in &nbsp;·&nbsp;
  Built with Streamlit + Plotly &nbsp;·&nbsp;
  All figures in Indian numbering system
</div>
""", unsafe_allow_html=True)