import os
import sqlite3
import pandas as pd

os.makedirs("data/processed", exist_ok=True)
DB = "data/processed/luxury.db"
if os.path.exists(DB):
    os.remove(DB)

trends = pd.read_csv("data/raw/trends_global.csv", index_col="date", parse_dates=True).iloc[:-1]
cat = pd.read_csv("data/raw/trends_category.csv", index_col="date", parse_dates=True).iloc[:-1]
wiki = pd.read_csv("data/raw/wikipedia_views.csv", index_col="date", parse_dates=True)

SPEC = [
    (trends, "Trends", "brands",
     {"Hermes": "brand", "Gucci": "brand", "Louis Vuitton": "brand"}),
    (cat, "Trends", "categories",
     {"quiet luxury": "theme", "luxury resale": "segment",
      "luxury watches": "segment", "luxury handbags": "segment"}),
    (wiki, "Wikipedia", "wikipedia",
     {"Hermès": "brand", "Gucci": "brand", "Louis Vuitton": "brand",
      "Quiet luxury": "theme", "Coffee": "control", "Bicycle": "control"}),
]

con = sqlite3.connect(DB)
con.executescript("""
CREATE TABLE series (series_id INTEGER PRIMARY KEY, source TEXT, label TEXT, role TEXT, pull TEXT);
CREATE TABLE observations (series_id INTEGER, month TEXT, value REAL, PRIMARY KEY (series_id, month));
CREATE TABLE change_points (series_id INTEGER, setting TEXT, month TEXT);
""")

ids, sid = {}, 0
for df, source, pull, roles in SPEC:
    for col, role in roles.items():
        sid += 1
        ids[(source, col)] = sid
        con.execute("INSERT INTO series VALUES (?,?,?,?,?)", (sid, source, col, role, pull))
        s = df[col].dropna()
        con.executemany(
            "INSERT INTO observations VALUES (?,?,?)",
            [(sid, d.strftime("%Y-%m-%d"), float(v)) for d, v in s.items()],
        )

cp = pd.read_csv("data/processed/change_points.csv")
for _, row in cp.iterrows():
    source, label = row["series"].split(": ", 1)
    sid = ids[(source, label)]
    for setting, col in (("moderate", cp.columns[1]), ("strict", cp.columns[2])):
        if pd.notna(row[col]) and str(row[col]).strip():
            for m in str(row[col]).split(", "):
                con.execute("INSERT INTO change_points VALUES (?,?,?)",
                            (sid, setting, m.strip() + "-01"))

con.commit()
for t in ("series", "observations", "change_points"):
    print(t, con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0], "rows")
con.close()