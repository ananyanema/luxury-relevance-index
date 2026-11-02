"""Recomputes the key numbers shown in the dashboard from your own data files and compares them
with the values recorded in FINDINGS.md. Prints OK or CHECK for each line. Nothing is changed."""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW, PROC = ROOT / "data" / "raw", ROOT / "data" / "processed"
rows = []


def check(name, expected, tol, fn):
    try:
        actual = float(fn())
        ok = abs(actual - expected) <= tol
        rows.append((name, expected, round(actual, 2), "OK" if ok else "CHECK"))
    except FileNotFoundError as e:
        rows.append((name, expected, "file missing", f"MISSING {Path(e.filename).name}"))
    except Exception as e:
        rows.append((name, expected, "error", f"CHECK ({type(e).__name__})"))


def rd(path, **kw):
    return pd.read_csv(path, **kw)


def cat():
    return rd(RAW / "trends_category.csv", index_col="date", parse_dates=True).iloc[:-1]


def brands():
    return rd(RAW / "trends_global.csv", index_col="date", parse_dates=True).iloc[:-1]


def wiki():
    return rd(RAW / "wikipedia_views.csv", index_col="date", parse_dates=True)


def pc_share(df):
    z = ((df - df.mean()) / df.std()).values
    s = np.linalg.svd(z, compute_uv=False)
    return (s ** 2) / (s ** 2).sum()


# 1. Search terms, 2025 on against 2019 to 2024 (change in points)
for term, exp in [("quiet luxury", 17.2), ("luxury resale", 12.7), ("luxury watches", 40.5), ("luxury handbags", 9.7)]:
    check(f"Change in points, {term}", exp, 0.15,
          lambda t=term: cat().loc["2025":, t].mean() - cat().loc["2019":"2024", t].mean())
check("Quiet luxury average 2019-24", 2.6, 0.1, lambda: cat().loc["2019":"2024", "quiet luxury"].mean())
check("Quiet luxury average 2025 on", 19.8, 0.1, lambda: cat().loc["2025":, "quiet luxury"].mean())

# 2. Wikipedia 2026, index 2019 = 100
def wiki_idx(col):
    w = wiki()
    y = w[col].groupby(w.index.year).mean()
    return y.loc[2026] / y.loc[2019] * 100
for col, exp in [("Hermès", 92), ("Gucci", 48), ("Louis Vuitton", 50), ("Coffee", 50), ("Bicycle", 29)]:
    check(f"Wikipedia 2026 index, {col}", exp, 1.5, lambda c=col: wiki_idx(c))
check("Quiet luxury Wikipedia views 2024 (monthly average)", 3690, 60, lambda: wiki()["Quiet luxury"].loc["2024"].mean())

# 3. Seasonally adjusted Google Trends trend (2019 = 100)
def trend_year(col, year):
    t = rd(PROC / "trends_trend_component.csv", index_col=0, parse_dates=True)
    return t[col].groupby(t.index.year).mean().loc[year]
check("Trend, Gucci 2025", 60, 1.5, lambda: trend_year("Gucci", 2025))
check("Trend, Hermes 2026", 121, 1.5, lambda: trend_year("Hermes", 2026))
check("Trend, Louis Vuitton 2026", 93, 1.5, lambda: trend_year("Louis Vuitton", 2026))

# 4. Correlations and principal components
check("Segments: first component share", 0.93, 0.01, lambda: pc_share(cat())[0])
check("Brands: first component share", 0.71, 0.01, lambda: pc_share(brands())[0])
check("Watches and handbags, monthly changes", 0.73, 0.02, lambda: cat().diff().dropna().corr().loc["luxury watches", "luxury handbags"])
check("Gucci and Louis Vuitton, monthly changes", 0.85, 0.02, lambda: brands().diff().dropna().corr().loc["Gucci", "Louis Vuitton"])
check("Hermes and Gucci, monthly changes", 0.46, 0.02, lambda: brands().diff().dropna().corr().loc["Hermes", "Gucci"])
check("Hermes and Louis Vuitton, monthly changes", 0.43, 0.02, lambda: brands().diff().dropna().corr().loc["Hermes", "Louis Vuitton"])

# 5. Relevance index
def idx_df():
    return rd(PROC / "relevance_index_tidy.csv", parse_dates=["month"])
for b, exp_r, exp_w in [("Hermes", 0.62, 219), ("Gucci", 0.04, 124), ("Louis Vuitton", -0.84, 124)]:
    check(f"Index: correlation of the two components, {b}", exp_r, 0.03,
          lambda b=b: idx_df().query("brand == @b")[["trends", "wiki_rel"]].corr().iloc[0, 1])
    check(f"Index: Wikipedia component 2026, {b}", exp_w, 2.5,
          lambda b=b: idx_df().query("brand == @b").set_index("month").loc["2026", "wiki_rel"].mean())

# 6. Change points: 2025-08 in the stricter setting for the four search terms
def n_aug():
    cp = rd(PROC / "change_points.csv")
    sub = cp[cp["series"].isin([f"Trends: {t}" for t in ["quiet luxury", "luxury resale", "luxury watches", "luxury handbags"]])]
    return sum("2025-08" in str(v) for v in sub[cp.columns[2]])
check("Search terms with a 2025-08 break (stricter setting)", 4, 0, n_aug)

# 7. Forecast backtest: series where exponential smoothing beat the best simple method
for h, exp in [(1, 6), (3, 5), (6, 2)]:
    check(f"Backtest: series beating best simple method, {h} month(s) ahead (of 10)", exp, 0,
          lambda h=h: (rd(PROC / "forecast_backtest.csv").query("h == @h")["ets / best simple"] < 1).sum())

# 8. Lead-lag correlations
def ll(wcol, tcol, lag, source="brands"):
    t = (brands() if source == "brands" else cat())
    w = wiki()
    g = lambda s: np.log1p(s.astype(float)).diff()
    df = pd.concat([g(w[wcol]).rename("w"), g(t[tcol]).rename("t")], axis=1).dropna()
    return df["w"].corr(df["t"].shift(-lag))
check("Lead-lag, Gucci at lag 0", 0.40, 0.02, lambda: ll("Gucci", "Gucci", 0))
check("Lead-lag, Hermes at lag 0", 0.28, 0.02, lambda: ll("Hermès", "Hermes", 0))
check("Lead-lag, Coffee vs Hermes at lag +2", 0.27, 0.02, lambda: ll("Coffee", "Hermes", 2))

width = max(len(r[0]) for r in rows)
print(f"{'Check'.ljust(width)}  {'Recorded':>9}  {'Recomputed':>11}  Result")
for name, exp, act, res in rows:
    print(f"{name.ljust(width)}  {str(exp):>9}  {str(act):>11}  {res}")
ok = sum(r[3] == "OK" for r in rows)
print(f"\n{ok} of {len(rows)} checks match. Anything marked CHECK or MISSING needs a look.")
