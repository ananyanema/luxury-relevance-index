import io
import time

import pandas as pd
import requests

URL = "https://api.gdeltproject.org/api/v2/doc/doc"
HEADERS = {
    "User-Agent": "LuxuryRelevanceIndex/0.1 "
                  "(https://github.com/ananyanema/luxury-relevance-index)"
}
QUERY = '"quiet luxury" sourcelang:english'

for mode in ["TimelineVol", "TimelineTone"]:
    params = {
        "query": QUERY,
        "mode": mode,
        "format": "csv",
        "startdatetime": "20190101000000",
        "enddatetime": "20260930000000",
    }
    resp = requests.get(URL, params=params, headers=HEADERS, timeout=60)
    print(f"--- {mode}: HTTP {resp.status_code}")
    print(resp.text[:300])
    if resp.status_code == 429:
        raise SystemExit("Throttled by GDELT. Stop and try again another day.")
    if resp.status_code == 200 and resp.text.strip():
        try:
            df = pd.read_csv(io.StringIO(resp.text))
            print(df.head(3))
            print(df.tail(3))
            print("Rows:", len(df))
        except Exception as e:
            print("Could not read as a table:", e)
    time.sleep(6)