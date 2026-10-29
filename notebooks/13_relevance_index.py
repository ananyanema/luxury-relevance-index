import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

t_trend = pd.read_csv("data/processed/trends_trend_component.csv", index_col=0, parse_dates=True)
w_trend = pd.read_csv("data/processed/wikipedia_trend_component.csv", index_col=0, parse_dates=True)
cat = pd.read_csv("data/raw/trends_category.csv", index_col="date", parse_dates=True).iloc[:-1]

BRANDS = {"Hermes": "Hermès", "Gucci": "Gucci", "Louis Vuitton": "Louis Vuitton"}


def rebase(s):
    return s / s.loc["2019"].mean() * 100


baseline = {
    "both": w_trend[["Coffee", "Bicycle"]].mean(axis=1),
    "coffee": w_trend["Coffee"],
    "bicycle": w_trend["Bicycle"],
}

frames = []
for t_name, w_name in BRANDS.items():
    wiki_rel = {k: rebase(w_trend[w_name] / b) for k, b in baseline.items()}
    df = pd.DataFrame({
        "trends": t_trend[t_name],
        "wiki_rel": wiki_rel["both"],
        "wiki_rel_coffee": wiki_rel["coffee"],
        "wiki_rel_bicycle": wiki_rel["bicycle"],
    }).dropna()
    df["midpoint"] = (df["trends"] + df["wiki_rel"]) / 2
    df["band_low"] = df[["trends", "wiki_rel"]].min(axis=1)
    df["band_high"] = df[["trends", "wiki_rel"]].max(axis=1)
    df.insert(0, "brand", t_name)
    df.index.name = "month"
    frames.append(df)

tidy = pd.concat(frames)
tidy.to_csv("data/processed/relevance_index_tidy.csv")

for name, df in tidy.groupby("brand"):
    print(f"=== {name}: yearly average (2019 = 100) ===")
    print(df[["trends", "wiki_rel", "midpoint"]].groupby(df.index.year).mean().round(0))
    print("Correlation of the two components:", round(df["trends"].corr(df["wiki_rel"]), 2))
    print()

print("Sensitivity: 2026 average of the Wikipedia component by choice of control")
print(tidy.groupby("brand")[["wiki_rel", "wiki_rel_coffee", "wiki_rel_bicycle"]]
      .apply(lambda g: g.loc["2026"].mean()).round(0))
print()

sm = cat.rolling(12, min_periods=6).mean()
z = (sm - sm.mean()) / sm.std()
composite = z.mean(axis=1).rename("category_composite")
composite.index.name = "month"
composite.to_csv("data/processed/category_composite.csv")
print("Category composite, yearly average (z-score, 12-month smoothed):")
print(composite.groupby(composite.index.year).mean().round(2))

fig, axes = plt.subplots(3, 1, figsize=(10, 11), sharex=True)
for ax, (name, df) in zip(axes, tidy.groupby("brand")):
    ax.fill_between(df.index, df["band_low"], df["band_high"], alpha=0.25)
    ax.plot(df.index, df["trends"], linewidth=1, label="Google Trends")
    ax.plot(df.index, df["wiki_rel"], linewidth=1, linestyle="--", label="Wikipedia vs controls")
    ax.plot(df.index, df["midpoint"], color="black", linewidth=1.5, label="Midpoint")
    ax.axhline(100, color="grey", linewidth=0.8)
    ax.set_title(f"{name} (2019 average = 100)")
    ax.legend(loc="upper left", fontsize=8)
plt.figtext(0.01, 0.01, "Data sources: Google Trends; Wikimedia Pageviews API (CC0). Experimental index.", fontsize=8)
plt.tight_layout()
plt.savefig("charts/relevance_index.png", dpi=150)
plt.show()