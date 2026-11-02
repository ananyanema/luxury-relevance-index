from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
INK, CALF, BRASS, GREY, OXBLOOD, GRID, TICK = "#1F1B17", "#8B5A36", "#B8995F", "#BDB29C", "#7A2430", "#E6DFD0", "#6B655B"
HEAT = [[0, OXBLOOD], [0.5, "#F6F1E6"], [1, "#8F7440"]]


@st.cache_data
def _read(path, **kw):
    return pd.read_csv(path, **kw)


def _style(fig, height=300, legend=True):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="system-ui, sans-serif", size=12, color=INK),
        margin=dict(l=0, r=0, t=8, b=0), height=height, showlegend=legend,
        legend=dict(orientation="h", y=-0.2, x=0), hovermode="x unified",
    )
    fig.update_xaxes(showgrid=False, linecolor=GREY, tickfont=dict(color=TICK))
    fig.update_yaxes(gridcolor=GRID, zeroline=False, tickfont=dict(color=TICK))
    return fig


def _vline(fig, x, text, color=OXBLOOD):
    fig.add_shape(type="line", x0=x, x1=x, xref="x", yref="paper", y0=0, y1=1,
                  line=dict(color=color, width=1, dash="dot"))
    fig.add_annotation(x=x, y=1, xref="x", yref="paper", text=text, showarrow=False,
                       yanchor="bottom", font=dict(size=10, color=color))


def _trends_brands():
    t = _read(RAW / "trends_global.csv", index_col="date", parse_dates=True).iloc[:-1]
    return t.rename(columns={"Hermes": "Hermès"})


def _trends_cat():
    return _read(RAW / "trends_category.csv", index_col="date", parse_dates=True).iloc[:-1]


# ---------- Question 1 ----------
def trend_chart():
    df = _read(PROC / "trends_trend_component.csv", index_col=0, parse_dates=True)
    styles = {"Hermes": (INK, "solid"), "Gucci": (CALF, "dash"), "Louis Vuitton": (BRASS, "dot")}
    fig = go.Figure()
    for col, (color, dash) in styles.items():
        fig.add_trace(go.Scatter(x=df.index, y=df[col], name=col.replace("Hermes", "Hermès"),
                                 line=dict(color=color, width=2, dash=dash)))
    fig.add_hline(y=100, line_width=1, line_color=GREY)
    return _style(fig)


def wiki_chart():
    w = _read(RAW / "wikipedia_views.csv", index_col="date", parse_dates=True)
    cols = ["Hermès", "Gucci", "Louis Vuitton", "Coffee", "Bicycle"]
    y = w[cols].groupby(w.index.year).mean()
    idx = y / y.loc[2019] * 100
    styles = {"Hermès": (INK, "solid", 2), "Gucci": (CALF, "dash", 2), "Louis Vuitton": (BRASS, "dot", 2),
              "Coffee": (GREY, "solid", 1.5), "Bicycle": (GREY, "dot", 1.5)}
    fig = go.Figure()
    for col, (color, dash, width) in styles.items():
        label = col + " (control)" if col in ("Coffee", "Bicycle") else col
        fig.add_trace(go.Scatter(x=idx.index, y=idx[col], name=label, line=dict(color=color, width=width, dash=dash)))
    fig.add_hline(y=100, line_width=1, line_color=GREY)
    fig.update_xaxes(dtick=1)
    return _style(fig)


def category_chart():
    c = _trends_cat()
    before, after = c.loc["2019":"2024"].mean(), c.loc["2025":].mean()
    names = [n.capitalize() for n in c.columns]
    fig = go.Figure([
        go.Bar(name="2019 to 2024", x=names, y=before.values, marker_color=GREY),
        go.Bar(name="2025 on", x=names, y=after.values, marker_color=BRASS),
    ])
    fig.update_layout(barmode="group")
    return _style(fig)


def break_chart():
    cp = _read(PROC / "change_points.csv")
    strict = cp.columns[2]
    xs, ys, colors = [], [], []
    for _, r in cp.iterrows():
        val = r[strict]
        if isinstance(val, str) and val.strip():
            for m in val.split(","):
                m = m.strip()
                xs.append(pd.to_datetime(m + "-01"))
                ys.append(r["series"])
                colors.append(OXBLOOD if m == "2025-08" else BRASS)
    fig = go.Figure(go.Scatter(
        x=xs, y=ys, mode="markers",
        marker=dict(color=colors, size=10, line=dict(width=1, color=INK)),
        hovertemplate="%{y}<br>%{x|%b %Y}<extra></extra>",
    ))
    _style(fig, height=390, legend=False)
    fig.update_yaxes(autorange="reversed", showgrid=True)
    fig.update_layout(hovermode="closest")
    return fig


# ---------- Question 2 ----------
def quiet_search_chart():
    c = _trends_cat()
    fig = go.Figure(go.Scatter(x=c.index, y=c["quiet luxury"], line=dict(color=INK, width=2), name="Quiet luxury searches"))
    _vline(fig, "2023-04-01", "April 2023")
    _vline(fig, "2025-08-01", "August 2025")
    return _style(fig, legend=False)


def quiet_wiki_chart():
    w = _read(RAW / "wikipedia_views.csv", index_col="date", parse_dates=True)
    s = w["Quiet luxury"].dropna()
    fig = go.Figure(go.Scatter(x=s.index, y=s.values, line=dict(color=CALF, width=2), fill="tozeroy",
                               fillcolor="rgba(184,153,95,0.18)", name="Monthly views"))
    return _style(fig, legend=False)


# ---------- Question 3 ----------
def survey_chart():
    labels = ["Name quality and craftsmanship as top reason (MG2)",
              "Link luxury with rarity or status (MG2, more than 75%)",
              "Walked away from an unjustified price (BCG)",
              "Newer brands reflect my identity, US (McKinsey)",
              "Established houses reflect my identity, US (McKinsey)"]
    values = [62, 75, 70, 68, 63]
    texts = ["62%", "more than 75%", "70%", "68%", "63%"]
    colors = [BRASS, BRASS, INK, CALF, CALF]
    fig = go.Figure(go.Bar(x=values, y=labels, orientation="h", marker_color=colors, text=texts,
                           textposition="outside", cliponaxis=False, hoverinfo="skip"))
    _style(fig, height=300, legend=False)
    fig.update_xaxes(range=[0, 100], showgrid=True, gridcolor=GRID)
    fig.update_yaxes(autorange="reversed", showgrid=False)
    fig.update_layout(margin=dict(l=0, r=60, t=8, b=0), hovermode="closest")
    return fig


def toptier_chart():
    fig = go.Figure(go.Bar(x=["Ten years earlier", "Latest"], y=[14, 24], marker_color=[GREY, BRASS],
                           text=["14%", "24%"], textposition="outside", hoverinfo="skip"))
    _style(fig, height=300, legend=False)
    fig.update_yaxes(range=[0, 32], title=None)
    fig.update_layout(hovermode="closest")
    return fig


# ---------- Question 4 ----------
def _heat(corr):
    z = corr.values
    labels = list(corr.columns)
    fig = go.Figure(go.Heatmap(z=z, x=labels, y=labels, zmin=-1, zmax=1, colorscale=HEAT,
                               text=np.round(z, 2), texttemplate="%{text}", showscale=False, hoverinfo="skip"))
    _style(fig, height=290, legend=False)
    fig.update_yaxes(autorange="reversed", showgrid=False)
    fig.update_xaxes(showgrid=False)
    fig.update_layout(hovermode="closest")
    return fig


def segment_heat():
    c = _trends_cat()
    d = c.diff().dropna().corr()
    d.columns = d.index = [n.capitalize() for n in d.columns]
    return _heat(d)


def brand_heat():
    return _heat(_trends_brands().diff().dropna().corr())


def _pc_share(df):
    z = ((df - df.mean()) / df.std()).values
    _, s, _ = np.linalg.svd(z, full_matrices=False)
    return (s ** 2) / (s ** 2).sum()


def pc_chart():
    cat, br = _pc_share(_trends_cat()), _pc_share(_trends_brands())
    labels = ["Component 1", "Component 2", "Component 3", "Component 4"]
    fig = go.Figure([
        go.Bar(name="Four search segments", x=labels, y=list(cat * 100), marker_color=BRASS),
        go.Bar(name="Three brands", x=labels, y=list(br * 100) + [None], marker_color=INK),
    ])
    fig.update_layout(barmode="group")
    fig.update_yaxes(range=[0, 100], title=None)
    return _style(fig)


# ---------- Question 5 ----------
def leadlag_chart():
    t, c = _trends_brands(), _trends_cat()
    w = _read(RAW / "wikipedia_views.csv", index_col="date", parse_dates=True)

    def g(s):
        return np.log1p(s.astype(float)).diff()

    pairs = [("Hermès", w["Hermès"], t["Hermès"]), ("Gucci", w["Gucci"], t["Gucci"]),
             ("Louis Vuitton", w["Louis Vuitton"], t["Louis Vuitton"]),
             ("Quiet luxury", w["Quiet luxury"], c["quiet luxury"]),
             ("Control: Coffee vs Hermès", w["Coffee"], t["Hermès"]),
             ("Control: Coffee vs Gucci", w["Coffee"], t["Gucci"]),
             ("Control: Bicycle vs Louis Vuitton", w["Bicycle"], t["Louis Vuitton"])]
    lags = list(range(-3, 4))
    z = []
    for _, a, b in pairs:
        df = pd.concat([g(a).rename("w"), g(b).rename("t")], axis=1).dropna()
        z.append([df["w"].corr(df["t"].shift(-k)) for k in lags])
    z = np.array(z, dtype=float)
    fig = go.Figure(go.Heatmap(z=z, x=[f"{k:+d}" for k in lags], y=[p[0] for p in pairs], zmin=-0.5, zmax=0.5,
                               colorscale=HEAT, text=np.round(z, 2), texttemplate="%{text}", showscale=False,
                               hoverinfo="skip"))
    _style(fig, height=340, legend=False)
    fig.update_yaxes(autorange="reversed", showgrid=False)
    fig.update_xaxes(showgrid=False, title="Lag in months (positive: Wikipedia moves first)")
    fig.update_layout(hovermode="closest", margin=dict(l=0, r=0, t=8, b=40))
    return fig


def backtest_chart():
    b = _read(PROC / "forecast_backtest.csv")
    p = b.pivot(index="series", columns="h", values="ets / best simple")
    fig = go.Figure()
    for h, color in zip([1, 3, 6], [BRASS, CALF, INK]):
        if h in p.columns:
            fig.add_trace(go.Bar(x=p.index, y=p[h], name=f"{h} month{'s' if h > 1 else ''} ahead", marker_color=color))
    fig.add_hline(y=1, line_dash="dot", line_color=OXBLOOD, line_width=1.5)
    fig.update_layout(barmode="group")
    fig.update_xaxes(tickangle=-30)
    fig.update_yaxes(title=None)
    return _style(fig, height=360)


# ---------- Question 6 ----------
def results_chart():
    labels = ["Kering revenue, 2025", "Gucci revenue, 2025", "Gucci recurring operating income, 2025",
              "LVMH revenue, 2025", "LVMH operating profit, 2025", "LVMH operating profit, first half 2026"]
    values = [-13, -22, -40, -1, -9, -4]
    colors = [CALF, CALF, CALF, INK, INK, INK]
    fig = go.Figure(go.Bar(x=values, y=labels, orientation="h", marker_color=colors,
                           text=[f"{v}%" for v in values], textposition="outside", cliponaxis=False, hoverinfo="skip"))
    _style(fig, height=300, legend=False)
    fig.update_xaxes(range=[-50, 5], showgrid=True, gridcolor=GRID)
    fig.update_yaxes(autorange="reversed", showgrid=False)
    fig.update_layout(margin=dict(l=0, r=40, t=8, b=0), hovermode="closest")
    return fig


# ---------- Relevance index page ----------
def band_chart(brand):
    df = _read(PROC / "relevance_index_tidy.csv", parse_dates=["month"])
    d = df[df["brand"] == brand].sort_values("month")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=d["month"], y=d["band_low"], line=dict(width=0), hoverinfo="skip", showlegend=False))
    fig.add_trace(go.Scatter(x=d["month"], y=d["band_high"], line=dict(width=0), fill="tonexty",
                             fillcolor="rgba(139,90,54,0.14)", hoverinfo="skip", name="Range between sources"))
    fig.add_trace(go.Scatter(x=d["month"], y=d["trends"], name="Google Trends", line=dict(color=INK, width=1.5)))
    fig.add_trace(go.Scatter(x=d["month"], y=d["wiki_rel"], name="Wikipedia vs controls",
                             line=dict(color=CALF, width=1.5, dash="dash")))
    fig.add_trace(go.Scatter(x=d["month"], y=d["midpoint"], name="Average of the two", line=dict(color=BRASS, width=3)))
    fig.add_hline(y=100, line_width=1, line_color=GREY)
    return _style(fig, height=380), d


def composite_chart():
    c = _read(PROC / "category_composite.csv", index_col=0, parse_dates=True)
    fig = go.Figure(go.Scatter(x=c.index, y=c.iloc[:, 0], line=dict(color=BRASS, width=2.5), name="Composite"))
    fig.add_hline(y=0, line_width=1, line_color=GREY)
    return _style(fig, height=280, legend=False)
