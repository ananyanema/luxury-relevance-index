import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL

os.makedirs("charts", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

trends = pd.read_csv("data/raw/trends_global.csv", index_col="date", parse_dates=True)
trends = trends.iloc[:-1]   # drop the incomplete latest month
wiki = pd.read_csv("data/raw/wikipedia_views.csv", index_col="date", parse_dates=True)
wiki = wiki[["Hermès", "Gucci", "Louis Vuitton", "Coffee", "Bicycle"]]


def decompose(df):
    trend, strength = {}, {}
    for col in df.columns:
        s = df[col].astype(float).dropna()
        res = STL(s, period=12, robust=True).fit()
        trend[col] = res.trend
        # seasonal strength: 0 = none, 1 = very strong
        strength[col] = round(max(0.0, 1 - res.resid.var() / (res.seasonal + res.resid).var()), 2)
    return pd.DataFrame(trend), pd.Series(strength)


def to_index(trend):
    return trend / trend.loc["2019"].mean() * 100


t_trend, t_strength = decompose(trends)
w_trend, w_strength = decompose(wiki)

print("Seasonal strength, Google Trends (0 = none, 1 = very strong):")
print(t_strength)
print()
print("Seasonal strength, Wikipedia:")
print(w_strength)

t_idx, w_idx = to_index(t_trend), to_index(w_trend)
print()
print("Google Trends: yearly average of the trend component (2019 = 100):")
print(t_idx.groupby(t_idx.index.year).mean().round(0))
print()
print("Wikipedia: yearly average of the trend component (2019 = 100):")
print(w_idx.groupby(w_idx.index.year).mean().round(0))

t_idx.to_csv("data/processed/trends_trend_component.csv")
w_idx.to_csv("data/processed/wikipedia_trend_component.csv")

fig, axes = plt.subplots(2, 1, figsize=(10, 9))
t_idx.plot(ax=axes[0], title="Google Trends: trend component (2019 average = 100)")
w_idx.plot(ax=axes[1], title="Wikipedia views: trend component (2019 average = 100)")
for ax in axes:
    ax.axhline(100, color="grey", linewidth=0.8)
    ax.set_ylabel("Index")
plt.figtext(0.01, 0.01, "Data sources: Google Trends; Wikimedia Pageviews API (CC0)", fontsize=8)
plt.tight_layout()
plt.savefig("charts/trend_components.png", dpi=150)
plt.show()