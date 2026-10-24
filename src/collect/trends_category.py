from pytrends.request import TrendReq

terms = ["quiet luxury", "luxury resale", "luxury watches", "luxury handbags"]

pytrends = TrendReq(hl="en-US", tz=0)
pytrends.build_payload(terms, timeframe="2019-01-01 2026-10-23")

df = pytrends.interest_over_time()
df = df.drop(columns="isPartial")

print(df.head())
print(df.describe())

df.to_csv("data/raw/trends_category.csv")
print("Saved to data/raw/trends_category.csv")