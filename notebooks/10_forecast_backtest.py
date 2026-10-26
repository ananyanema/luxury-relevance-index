import warnings
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

warnings.filterwarnings("ignore")

trends = pd.read_csv("data/raw/trends_global.csv", index_col="date", parse_dates=True).iloc[:-1]
cat = pd.read_csv("data/raw/trends_category.csv", index_col="date", parse_dates=True).iloc[:-1]
wiki = pd.read_csv("data/raw/wikipedia_views.csv", index_col="date", parse_dates=True)

series = {}
for c in trends.columns:
    series[f"Trends: {c}"] = trends[c]
for c in cat.columns:
    series[f"Trends: {c}"] = cat[c]
for c in ["Hermès", "Gucci", "Louis Vuitton"]:
    series[f"Wikipedia: {c}"] = wiki[c]

H = 6          # forecast up to 6 months ahead
START = 48     # first forecast origin: after 48 months of history
HORIZONS = (1, 3, 6)


def naive(train, h):
    return np.repeat(train.iloc[-1], h)


def seasonal_naive(train, h):
    last12 = train.iloc[-12:].values
    return np.array([last12[i % 12] for i in range(h)])


def mean12(train, h):
    return np.repeat(train.iloc[-12:].mean(), h)


def ets(train, h):
    y = np.log1p(train.values.astype(float))
    try:
        m = ExponentialSmoothing(
            y, trend="add", damped_trend=True, seasonal="add",
            seasonal_periods=12, initialization_method="estimated",
        ).fit()
        return np.expm1(m.forecast(h))
    except Exception:
        return naive(train, h)


MODELS = {"naive": naive, "seasonal_naive": seasonal_naive, "mean12": mean12, "ets": ets}

rows = []
for name, s in series.items():
    s = s.dropna().astype(float)
    n = len(s)
    for t in range(START, n - H + 1):
        train, actual = s.iloc[:t], s.iloc[t:t + H].values
        for mname, f in MODELS.items():
            fc = f(train, H)
            for h in HORIZONS:
                rows.append({"series": name, "model": mname, "h": h,
                             "abs_error": abs(actual[h - 1] - fc[h - 1])})

df = pd.DataFrame(rows)
mae = df.groupby(["series", "h", "model"])["abs_error"].mean().unstack("model")
mae["ets / naive"] = mae["ets"] / mae["naive"]
mae["ets / best simple"] = mae["ets"] / mae[["naive", "seasonal_naive", "mean12"]].min(axis=1)

pd.set_option("display.width", 250)
print("Mean absolute error by series, horizon (months ahead) and model:")
print(mae.round(2).to_string())
print()
print("Share of series where ETS beats the naive forecast, by horizon:")
print((mae["ets / naive"] < 1).groupby("h").mean().round(2))
print()
print("Share of series where ETS beats the best simple method, by horizon:")
print((mae["ets / best simple"] < 1).groupby("h").mean().round(2))
mae.to_csv("data/processed/forecast_backtest.csv")