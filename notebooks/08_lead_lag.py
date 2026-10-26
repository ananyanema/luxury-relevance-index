import warnings
import io
import contextlib
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

warnings.filterwarnings("ignore")

trends = pd.read_csv("data/raw/trends_global.csv", index_col="date", parse_dates=True).iloc[:-1]
cat = pd.read_csv("data/raw/trends_category.csv", index_col="date", parse_dates=True).iloc[:-1]
wiki = pd.read_csv("data/raw/wikipedia_views.csv", index_col="date", parse_dates=True)

MAXLAG = 3


def growth(s):
    """Monthly log change: makes the series steady."""
    return np.log1p(s.astype(float)).diff()


PAIRS = [
    ("Hermes", wiki["Hermès"], trends["Hermes"]),
    ("Gucci", wiki["Gucci"], trends["Gucci"]),
    ("Louis Vuitton", wiki["Louis Vuitton"], trends["Louis Vuitton"]),
    ("Quiet luxury", wiki["Quiet luxury"], cat["quiet luxury"]),
    ("CONTROL: Coffee vs Hermes", wiki["Coffee"], trends["Hermes"]),
    ("CONTROL: Coffee vs Gucci", wiki["Coffee"], trends["Gucci"]),
    ("CONTROL: Bicycle vs Louis Vuitton", wiki["Bicycle"], trends["Louis Vuitton"]),
]

def granger_min_p(y, x):
    """Smallest p-value over lags 1..MAXLAG for 'x helps predict y'."""
    with contextlib.redirect_stdout(io.StringIO()):
        res = grangercausalitytests(pd.concat([y, x], axis=1), maxlag=MAXLAG)
    return min(res[lag][0]["ssr_ftest"][1] for lag in range(1, MAXLAG + 1))



alpha = 0.05 / (len(PAIRS) * 2 * MAXLAG)   # Bonferroni threshold
rows = []
for name, w, t in PAIRS:
    df = pd.concat([growth(w).rename("wiki"), growth(t).rename("trends")], axis=1).dropna()
    # k > 0: Wikipedia this month is paired with Trends k months LATER (Wikipedia leads)
    cc = {k: df["wiki"].corr(df["trends"].shift(-k)) for k in range(-MAXLAG, MAXLAG + 1)}
    best = max(cc, key=lambda k: abs(cc[k]))
    p_wt = granger_min_p(df["trends"], df["wiki"])   # Wikipedia -> Trends
    p_tw = granger_min_p(df["wiki"], df["trends"])   # Trends -> Wikipedia
    rows.append({
        "pair": name,
        "months": len(df),
        "corr at lag 0": round(cc[0], 2),
        "best lag": best,
        "corr at best lag": round(cc[best], 2),
        "p: wiki leads": round(p_wt, 4),
        "p: trends leads": round(p_tw, 4),
        "survives correction": (p_wt < alpha) or (p_tw < alpha),
    })

out = pd.DataFrame(rows)
pd.set_option("display.width", 250)
print(out.to_string(index=False))
print()
print(f"Correction threshold: p < {alpha:.4f}")
print("Best lag > 0 means Wikipedia moves first; best lag < 0 means Google Trends moves first.")
out.to_csv("data/processed/lead_lag.csv", index=False)