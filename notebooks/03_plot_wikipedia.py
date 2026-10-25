import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)
df = pd.read_csv("data/raw/wikipedia_views.csv", index_col="date", parse_dates=True)

print("First month with data for each article:")
print(df.apply(lambda s: s.first_valid_index()))
print()
print("Yearly average of monthly views:")
print(df.groupby(df.index.year).mean().round(0))

fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
df[["Hermès", "Gucci", "Louis Vuitton"]].plot(
    ax=axes[0], title="Wikipedia monthly views: brands (human readers)")
df[["Quiet luxury"]].plot(
    ax=axes[1], title="Wikipedia monthly views: Quiet luxury (own scale)")
axes[0].set_ylabel("Views per month")
axes[1].set_ylabel("Views per month")
fig.text(0.01, 0.01, "Data source: Wikimedia Pageviews API (CC0)", fontsize=8)
plt.tight_layout()
plt.savefig("charts/wikipedia_views.png", dpi=150)
plt.show()