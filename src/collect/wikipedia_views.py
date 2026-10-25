import time
from urllib.parse import quote

import pandas as pd
import requests

ARTICLES = ["Hermès", "Gucci", "Louis Vuitton", "Quiet luxury", "Coffee", "Bicycle"]
START, END = "2019010100", "2026093000"   # complete months only
HEADERS = {
    "User-Agent": "LuxuryRelevanceIndex/0.1 "
                  "(https://github.com/ananyanema/luxury-relevance-index) python-requests"
}
BASE = ("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
        "en.wikipedia.org/all-access/user")

series = {}
for title in ARTICLES:
    slug = quote(title.replace(" ", "_"), safe="")
    url = f"{BASE}/{slug}/monthly/{START}/{END}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    if resp.status_code != 200:
        print(f"Problem with {title}: {resp.status_code} {resp.text[:200]}")
        continue
    items = resp.json()["items"]
    s = pd.Series(
        {pd.to_datetime(i["timestamp"][:8], format="%Y%m%d"): i["views"] for i in items},
        name=title,
    )
    series[title] = s
    print(f"{title}: {len(s)} months, total views {s.sum():,}")
    time.sleep(1)   # one request at a time, as Wikimedia asks

if not series:
    raise SystemExit("No data collected. See the messages above.")

df = pd.DataFrame(series)
df.index.name = "date"
print(df.head())
print(df.tail())
df.to_csv("data/raw/wikipedia_views.csv")
print("Saved to data/raw/wikipedia_views.csv")