import sqlite3
import pandas as pd

pd.set_option("display.width", 200)
con = sqlite3.connect("data/processed/luxury.db")


def run(title, sql):
    print(f"=== {title} ===")
    print(pd.read_sql_query(sql, con).to_string(index=False))
    print()


run("1. Wikipedia yearly average, indexed to the first year (CTE + window function)", """
WITH yearly AS (
  SELECT s.label, s.role, strftime('%Y', o.month) AS year, AVG(o.value) AS avg_value
  FROM observations o JOIN series s ON s.series_id = o.series_id
  WHERE s.source = 'Wikipedia'
  GROUP BY s.series_id, year
)
SELECT label, year,
       ROUND(100.0 * avg_value / FIRST_VALUE(avg_value) OVER (PARTITION BY label ORDER BY year)) AS idx
FROM yearly
WHERE role != 'theme'
ORDER BY label, year
""")

run("2. Biggest month-to-month jumps in Google Trends brand series (LAG)", """
WITH changes AS (
  SELECT s.label, o.month, o.value,
         o.value - LAG(o.value) OVER (PARTITION BY o.series_id ORDER BY o.month) AS change
  FROM observations o JOIN series s ON s.series_id = o.series_id
  WHERE s.source = 'Trends' AND s.role = 'brand'
)
SELECT label, month, value, change FROM changes
ORDER BY ABS(change) DESC LIMIT 8
""")

run("3. Months where several series break at once (strict setting)", """
SELECT c.month, COUNT(DISTINCT c.series_id) AS n_series,
       GROUP_CONCAT(s.source || ': ' || s.label, '; ') AS series_list
FROM change_points c JOIN series s ON s.series_id = c.series_id
WHERE c.setting = 'strict'
GROUP BY c.month
HAVING n_series >= 2
ORDER BY c.month
""")

run("4. Rolling 12-month average, Google Trends Gucci and Hermes, 2026", """
SELECT s.label, o.month, o.value,
       ROUND(AVG(o.value) OVER (PARTITION BY o.series_id ORDER BY o.month
                                ROWS BETWEEN 11 PRECEDING AND CURRENT ROW), 1) AS avg12
FROM observations o JOIN series s ON s.series_id = o.series_id
WHERE s.source = 'Trends' AND s.label IN ('Gucci', 'Hermes') AND o.month >= '2026-01-01'
ORDER BY s.label, o.month
""")
con.close()