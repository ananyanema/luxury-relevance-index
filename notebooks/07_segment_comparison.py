import numpy as np
import pandas as pd

cat = pd.read_csv("data/raw/trends_category.csv", index_col="date", parse_dates=True).iloc[:-1]
brands = pd.read_csv("data/raw/trends_global.csv", index_col="date", parse_dates=True).iloc[:-1]


def report(df, label):
    print(f"=== {label} ===")
    print("Correlation of levels:")
    print(df.corr().round(2))
    print()
    print("Correlation of month-to-month changes:")
    print(df.diff().dropna().corr().round(2))
    z = (df - df.mean()) / df.std()
    _, s, _ = np.linalg.svd(z.values, full_matrices=False)
    share = (s ** 2) / (s ** 2).sum()
    print()
    print("Share of variance explained by each component:", share.round(2))
    print()


report(cat, "Category terms (one Google Trends pull)")
report(brands, "Brand terms (one Google Trends pull)")