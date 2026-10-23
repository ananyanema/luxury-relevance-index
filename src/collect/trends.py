from pytrends.request import TrendReq

brands = ["Hermes", "Gucci", "Louis Vuitton"]

pytrends = TrendReq(hl="en-US", tz=0)
pytrends.build_payload(brands, timeframe="2019-01-01 2026-10-23")

df = pytrends.interest_over_time()
df = df.drop(columns="isPartial")

print(df.head())
print(df.shape)

df.to_csv("data/raw/trends_global.csv")
print("Saved to data/raw/trends_global.csv")