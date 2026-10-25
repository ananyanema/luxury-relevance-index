import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)
df = pd.read_csv("data/raw/wikipedia_views.csv", index_col="date", parse_dates=True)
cols = ["Hermès", "Gucci", "Louis Vuitton", "Coffee", "Bicycle"]

base = df.loc["2019", cols].mean()
indexed = df[cols] / base * 100
print("Yearly average, indexed (2019 = 100):")
print(indexed.groupby(indexed.index.year).mean().round(0))

smooth = indexed.rolling(12, min_periods=6).mean()
ax = smooth.plot(figsize=(10, 5),
                 title="Wikipedia views, indexed (2019 average = 100), 12-month average")
ax.axhline(100, color="grey", linewidth=0.8)
ax.set_ylabel("Index")
plt.figtext(0.01, 0.01, "Data source: Wikimedia Pageviews API (CC0)", fontsize=8)
plt.tight_layout()
plt.savefig("charts/wikipedia_indexed.png", dpi=150)
plt.show()