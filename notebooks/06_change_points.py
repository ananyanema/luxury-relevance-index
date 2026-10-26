import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ruptures as rpt

os.makedirs("charts", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

trends = pd.read_csv("data/raw/trends_global.csv", index_col="date", parse_dates=True).iloc[:-1]
cat = pd.read_csv("data/raw/trends_category.csv", index_col="date", parse_dates=True).iloc[:-1]
wiki = pd.read_csv("data/raw/wikipedia_views.csv", index_col="date", parse_dates=True)

series = {}
for col in trends.columns:
    series[f"Trends: {col}"] = trends[col]
for col in cat.columns:
    series[f"Trends: {col}"] = cat[col]
for col in ["Hermès", "Gucci", "Louis Vuitton", "Quiet luxury", "Coffee", "Bicycle"]:
    series[f"Wikipedia: {col}"] = wiki[col]


def change_points(s, mult):
    """Months where a new level begins. Higher mult = stricter (fewer points)."""
    s = s.astype(float).dropna()
    x = np.log1p(s.values)                     # log scale: big spikes dominate less
    sigma = np.std(np.diff(x)) / np.sqrt(2)    # noise level from month-to-month changes
    pen = mult * np.log(len(x)) * sigma ** 2
    ends = rpt.Pelt(model="l2", min_size=4, jump=1).fit(x).predict(pen=pen)[:-1]
    return [s.index[i].strftime("%Y-%m") for i in ends]


rows = []
for name, s in series.items():
    rows.append({
        "series": name,
        "moderate (6x)": ", ".join(change_points(s, 6)),
        "strict (12x)": ", ".join(change_points(s, 12)),
    })
result = pd.DataFrame(rows)
pd.set_option("display.width", 250)
pd.set_option("display.max_colwidth", None)
print(result.to_string(index=False))
result.to_csv("data/processed/change_points.csv", index=False)

show = ["Trends: Gucci", "Trends: quiet luxury", "Wikipedia: Gucci", "Wikipedia: Quiet luxury"]
fig, axes = plt.subplots(2, 2, figsize=(12, 7))
for ax, name in zip(axes.ravel(), show):
    s = series[name].dropna()
    ax.plot(s.index, s.values, linewidth=1)
    for d in change_points(series[name], 6):
        ax.axvline(pd.to_datetime(d), color="red", linestyle="--", linewidth=0.8)
    ax.set_title(name)
fig.text(0.01, 0.01,
         "Dashed lines: detected change points (moderate setting). "
         "Data: Google Trends; Wikimedia Pageviews API (CC0)", fontsize=8)
plt.tight_layout()
plt.savefig("charts/change_points.png", dpi=150)
plt.show()