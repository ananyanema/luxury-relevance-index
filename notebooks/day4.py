import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)

brands = pd.read_csv("data/raw/trends_global.csv", index_col="date", parse_dates=True)
cat = pd.read_csv("data/raw/trends_category.csv", index_col="date", parse_dates=True)

# Chart 1: the three brands on one scale
brands.plot(figsize=(10, 5), title="Search interest: brands (Google Trends, 0-100)")
plt.ylabel("Relative interest")
plt.tight_layout()
plt.savefig("charts/brands.png", dpi=150)

# Chart 2: each luxury category term in its own panel
cat.plot(subplots=True, figsize=(10, 8), title="Search interest: luxury categories")
plt.tight_layout()
plt.savefig("charts/categories.png", dpi=150)

plt.show()