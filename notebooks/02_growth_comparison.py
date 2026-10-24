import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("data/processed", exist_ok=True)
os.makedirs("charts", exist_ok=True)

brands = pd.read_csv("data/raw/trends_global.csv", index_col="date", parse_dates=True)
cat = pd.read_csv("data/raw/trends_category.csv", index_col="date", parse_dates=True)

# The newest month is incomplete, so drop it
brands = brands.iloc[:-1]
cat = cat.iloc[:-1]


def yearly(df):
    return df.groupby(df.index.year).mean().round(1)


def growth(df):
    before = df.loc["2019":"2024"].mean()
    after = df.loc["2025":].mean()
    out = pd.DataFrame({"avg_2019_2024": before, "avg_2025_on": after})
    out["change_points"] = out["avg_2025_on"] - out["avg_2019_2024"]
    out["change_pct"] = out["change_points"] / out["avg_2019_2024"] * 100
    return out.round(1)


print("BRANDS: yearly average")
print(yearly(brands))
print()
print("BRANDS: 2019-2024 vs 2025 onward")
print(growth(brands))
print()
print("CATEGORIES: yearly average")
print(yearly(cat))
print()
print("CATEGORIES: 2019-2024 vs 2025 onward")
print(growth(cat))

# Save the tables
yearly(brands).to_csv("data/processed/brands_yearly.csv")
yearly(cat).to_csv("data/processed/categories_yearly.csv")
growth(brands).to_csv("data/processed/brands_growth.csv")
growth(cat).to_csv("data/processed/categories_growth.csv")

# Chart: yearly average for the three brands
yearly(brands).plot(kind="bar", figsize=(10, 5),
                    title="Brand search interest: yearly average (Google Trends)")
plt.ylabel("Relative interest")
plt.tight_layout()
plt.savefig("charts/brands_yearly.png", dpi=150)
plt.show()