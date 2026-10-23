import pandas as pd

df = pd.read_csv("data/raw/practice.csv")

# 1. Average interest per brand
print(df.groupby("brand")["interest"].mean())

# 2. Only Hermes rows
hermes = df[df["brand"] == "Hermes"]
print(hermes)

# 3. Change from first month to last month, per brand
change = df.groupby("brand")["interest"].agg(["first", "last"])
change["difference"] = change["last"] - change["first"]
print(change)