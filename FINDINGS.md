# Findings so far (work in progress)

Last updated: 29 October 2026. Each finding states what the data shows and what it does not show. Sections 1 and 2 use our own data. Sections 3 to 6 are other organisations' findings, paraphrased by us and linked to their source.

## 1. Own data: Google Trends (2019 to 2026)

Data source: Google Trends (https://www.google.com/trends). Brand terms and category terms came from separate pulls, so their scales cannot be compared with each other.

Category terms, average interest in 2019-2024 compared with 2025 onward (0 to 100 scale, one pull, so comparable with each other):

| Term | 2019-2024 | 2025 onward | Change (points) |
|---|---|---|---|
| quiet luxury | 2.6 | 19.8 | +17.2 |
| luxury resale | 1.3 | 14.1 | +12.7 |
| luxury watches | 17.8 | 58.3 | +40.5 |
| luxury handbags | 3.4 | 13.1 | +9.7 |

1. All four category terms were higher in 2025-2026 than in 2019-2024. Much of this comes from a surge starting in mid-2025 whose cause is unknown.
2. Gucci's search interest was lower in 2025 than in 2019, while Hermes was higher and Louis Vuitton slightly lower (see section 2b for the seasonally adjusted figures). December bumps appear in the charts, but see section 2b for how strong the seasonal pattern really is.
3. Quiet luxury was near zero until early 2023, stepped up then, and surged again in 2025-2026.
4. A control term (sneakers) did not show the same surge, but it had its own spike in 2026, so this check is suggestive, not proof.

Limits: search interest is attention, not sales. "Luxury watches" may include ordinary watch shoppers. The latest, incomplete month was dropped. Exact figures are in data/processed.

## 2. Own data: Wikipedia attention

Data source: Wikimedia Pageviews API (CC0). Human readers only. Index: 2019 average = 100. The 2026 row covers January to September.

| Year | Hermes | Gucci | Louis Vuitton | Coffee (control) | Bicycle (control) |
|---|---|---|---|---|---|
| 2019 | 100 | 100 | 100 | 100 | 100 |
| 2020 | 100 | 81 | 89 | 94 | 135 |
| 2021 | 105 | 289 | 105 | 92 | 64 |
| 2022 | 98 | 353 | 107 | 104 | 65 |
| 2023 | 142 | 129 | 123 | 105 | 77 |
| 2024 | 137 | 95 | 95 | 83 | 58 |
| 2025 | 121 | 64 | 78 | 59 | 35 |
| 2026 | 92 | 48 | 50 | 50 | 29 |

1. The control articles fell sharply (Coffee to 50, Bicycle to 29 by 2026), so part of any fall in the brand articles reflects Wikipedia readership overall, not luxury.
2. Gucci (48) and Louis Vuitton (50) ended 2026 at about the same level as Coffee (50), so their declines are not evidence of a luxury-specific loss of interest.
3. Hermes (92) stayed well above the controls and was above its 2019 level in 2023 to 2025.
4. Gucci's views were about three times its 2019 level in 2021 and 2022. The cause is not yet established.
5. The Quiet luxury article has data only from late 2023. Its views stayed at roughly 3,500 to 3,700 a month from 2024 to 2026.

Limits: two control articles are a small basis, and Bicycle rose in 2020, so it may reflect its own events. Page views are attention, not sales or purchase intent. Wikimedia's human-reader filter excludes bots as classified by Wikimedia.

Comparing sections 1 and 2: in 2025-2026 Google Trends shows a surge for the category terms, while Wikipedia views for the brands fell and the Quiet luxury article stayed flat. Searching and reading an article are different behaviours, so question 1 is "mixed" for now.

## 2b. Own data: seasonally adjusted trends (STL)

Method: STL decomposition (yearly period, robust fit) of the monthly series, with the trend component indexed to its 2019 average = 100. The 2026 row covers January to September. Data sources: Google Trends; Wikimedia Pageviews API (CC0).

Google Trends, trend component:

| Year | Hermes | Gucci | Louis Vuitton |
|---|---|---|---|
| 2019 | 100 | 100 | 100 |
| 2020 | 109 | 92 | 102 |
| 2021 | 110 | 87 | 101 |
| 2022 | 99 | 82 | 97 |
| 2023 | 95 | 70 | 90 |
| 2024 | 103 | 63 | 89 |
| 2025 | 111 | 60 | 91 |
| 2026 | 121 | 61 | 93 |

Wikipedia, trend component:

| Year | Hermes | Gucci | Louis Vuitton | Coffee (control) | Bicycle (control) |
|---|---|---|---|---|---|
| 2019 | 100 | 100 | 100 | 100 | 100 |
| 2020 | 99 | 87 | 90 | 92 | 95 |
| 2021 | 103 | 174 | 92 | 90 | 86 |
| 2022 | 105 | 218 | 104 | 102 | 90 |
| 2023 | 122 | 136 | 116 | 103 | 100 |
| 2024 | 128 | 91 | 95 | 78 | 70 |
| 2025 | 116 | 63 | 73 | 58 | 47 |
| 2026 | 92 | 52 | 52 | 47 | 38 |

Seasonal strength (0 = none, 1 = very strong). Google Trends: Hermes 0.58, Gucci 0.05, Louis Vuitton 0.07. Wikipedia: Hermes 0.26, Gucci 0.00, Louis Vuitton 0.24, Coffee 0.30, Bicycle 0.05.

1. After removing seasonality, Gucci's search-interest trend fell from 100 to about 60 by 2025 and was 61 in 2026. Louis Vuitton drifted to about 89-93. Hermes dipped to 95 in 2023 and rose to 121 in 2026.
2. Hermes is the only brand that looks resilient on both sources: rising on Google Trends and well above the Wikipedia controls.
3. Gucci declined on both sources, but its Wikipedia fall (to 52) is close to Coffee's (47), so that fall alone is not evidence of a brand-specific loss.
4. A seasonal pattern is clear only for Hermes on Google Trends. For Gucci and Louis Vuitton, large irregular spikes dominate.
5. The early-2026 surge in Gucci and Louis Vuitton searches barely moves their trend components, which is consistent with the robust method treating a short burst as irregular. Whether it is a short spike or a new level cannot yet be settled.

Limits: seasonal strength is a variance ratio, so large spikes lower it. Trend estimates near the end of a series are less stable. Robust smoothing downweights short bursts. Three brands only. Google Trends values are relative.
## 2c. Own data: change points

Method: PELT change-point detection (ruptures library) on log-transformed monthly series, minimum segment 4 months. A date is the first month of a new level. The direction of the change is not shown. Two penalty settings (6x and 12x a baseline penalty we chose) were used, and a break counts as robust only if it appears under both. 2026 data runs to September. Data sources: Google Trends; Wikimedia Pageviews API (CC0).

| Series | Robust breaks (both settings) | Only under the looser setting |
|---|---|---|
| Trends: Hermes | 2026-04 | 2020-04, 2022-02, 2024-06 |
| Trends: Gucci | 2023-01, early 2026 (Feb or Mar) | 2026-06 |
| Trends: Louis Vuitton | early 2026 (Feb or Mar) | 2026-06 |
| Trends: quiet luxury | 2021-06 (near-zero values, ignore), 2023-04, 2025-08 | 2026-02 |
| Trends: luxury resale | 2025-08 | 2023-01 or 2023-06, 2025-02 |
| Trends: luxury watches | 2023-07, 2024-08, 2025-08 | none |
| Trends: luxury handbags | 2025-08 | 2021-08, 2024-11, 2023-04 |
| Wikipedia: Hermes | none | 2022-12, 2025-05 |
| Wikipedia: Gucci | 2021-07, 2022-11, 2024-08 | none |
| Wikipedia: Louis Vuitton | 2022-10, 2024-05, 2025-10 | none |
| Wikipedia: Quiet luxury | 2024-02 | none |
| Wikipedia: Coffee (control) | 2024-05, 2025-04 | none |
| Wikipedia: Bicycle (control) | 2019-11, 2020-05, 2024-06 | 2025-07 |

1. All four category terms break in 2025-08 under both settings. They come from one Google Trends pull. The brand terms and the Wikipedia Quiet luxury article show no break that month. The cause is unknown: it could be a real shift in generic luxury searches or a measurement effect in that pull. A repeat pull on another day is needed.
2. Gucci and Louis Vuitton searches break in early 2026, and under the looser setting again in June, consistent with a short burst that reverted rather than a lasting new level. Under the stricter setting only the first break appears, so this is suggestive only.
3. Quiet luxury searches break in 2023-04 under both settings, matching the step visible in the chart.
4. Louis Vuitton's Wikipedia break in 2024-05 coincides with Coffee (2024-05) and Bicycle (2024-06), pointing to a site-wide shift, not a luxury-specific one.
5. Gucci's Wikipedia breaks (2021-07, 2022-11) indicate a long elevated period, while Google Trends shows only a short spike in late 2021. The two sources disagree on this episode.

Limits: the penalty settings are our choice and no significance test is attached. Breaks near the end of the series are less reliable. Direction is not shown. Several breaks in near-zero series are not meaningful.
## 2d. Own data: how closely the series move together

Method: correlation of monthly levels, correlation of month-to-month changes, and the share of variance explained by the first principal component (series standardised). Each Google Trends pull is analysed separately because scales differ between pulls. Data source: Google Trends.

Category terms (one pull): levels correlate at 0.84 to 0.97. Month-to-month changes: luxury watches and luxury handbags 0.73, quiet luxury with the others 0.14 to 0.45, luxury resale with the others 0.10 to 0.36. First principal component: 93% of variance.

Brand terms (a separate pull): levels: Gucci and Louis Vuitton 0.74, Hermes and Louis Vuitton 0.55, Hermes and Gucci 0.36. Month-to-month changes: Gucci and Louis Vuitton 0.85, Hermes with each of the others 0.43 to 0.46. First principal component: 71% of variance.

1. The four category terms move mostly as one series. This largely reflects a shared rise and the 2025-08 break, and correlations between trending series are inflated, so the monthly-changes figures are more informative.
2. Watches and handbags move together month to month, while resale and quiet luxury are only weakly tied to the others.
3. Gucci and Louis Vuitton move closely together, while Hermes is less tied to both, partly supporting the idea that heritage-led and trend-led brands behave differently.
4. A single index can summarise the category terms, but it would inherit the 2025-08 shift.

Limits: three brands and four category terms only. All three brands share a December peak and the early-2026 spike, which raise correlations. The category terms all contain the word "luxury" and may share query effects. Correlation is not causation.
## 2e. Own data: lead-lag and Granger tests

Method: monthly log changes (to make the series steady), cross-correlation at lags of -3 to +3 months, and Granger tests at lags 1 to 3 for Wikipedia and Google Trends in both directions. Seven pairs: four luxury pairs and three control pairs (unrelated Wikipedia articles against luxury Trends terms). Bonferroni correction for 14 tests: p < 0.0012. A positive best lag means Wikipedia moves first. Data sources: Google Trends; Wikimedia Pageviews API (CC0).

| Pair | Months | Corr at lag 0 | Best lag | Corr at best lag | p: Wikipedia leads | p: Trends leads |
|---|---|---|---|---|---|---|
| Hermes | 92 | 0.28 | 0 | 0.28 | 0.130 | 0.026 |
| Gucci | 92 | 0.40 | 0 | 0.40 | 0.138 | 0.607 |
| Louis Vuitton | 92 | 0.03 | -3 | 0.16 | 0.397 | 0.176 |
| Quiet luxury | 35 | -0.06 | 2 | 0.12 | 0.641 | 0.745 |
| Control: Coffee vs Hermes | 92 | -0.20 | 2 | 0.27 | 0.120 | 0.476 |
| Control: Coffee vs Gucci | 92 | -0.14 | 0 | -0.14 | 0.157 | 0.224 |
| Control: Bicycle vs Louis Vuitton | 92 | -0.17 | 0 | -0.17 | 0.386 | 0.295 |

1. No pair, luxury or control, survives the correction. We found no consistent lead in either direction.
2. The smallest p-value (Hermes, Google Trends leading Wikipedia, 0.026) points opposite to our hypothesis and is consistent with chance given 14 tests.
3. Gucci's correlation of 0.40 is at lag 0, so the series move together in the same month and do not lead each other. Shared spikes can inflate it.
4. Control pairs reach correlations (0.27) similar to the luxury pairs, so correlations of this size occur between unrelated series.
5. Hypothesis 5 (Wikipedia moves before other signals) is not supported. One episode, Gucci's Wikipedia rise from 2021-07 ahead of its Trends break in 2021-11, is an observation only.

Limits: monthly data cannot show leads shorter than a month. Each p-value is the smallest over three lags. Bonferroni is strict and lowers power. Quiet luxury has only 35 months of overlap. Google Trends values are sampled and relative. Granger tests show predictive usefulness, not causation.
## 2f. Own data: forecast backtest

Method: walk-forward backtest. For each of 10 series, forecasts were made from every origin after the first 48 months, and the absolute error at 1, 3 and 6 months ahead was averaged. Four methods: naive (next month equals this month), seasonal naive (same month last year), 12-month average, and damped-trend exponential smoothing with yearly seasonality (ETS), fitted on a log scale. The table shows ETS error divided by the error of the best of the three simple methods: below 1 means ETS was better. Origins overlap, so they are not independent, and no significance test was run. Data sources: Google Trends; Wikimedia Pageviews API (CC0).

| Series | 1 month | 3 months | 6 months |
|---|---|---|---|
| Trends: Gucci | 0.85 | 0.99 | 0.99 |
| Trends: Hermes | 0.89 | 1.02 | 1.02 |
| Trends: Louis Vuitton | 0.89 | 0.94 | 1.03 |
| Trends: luxury handbags | 0.83 | 1.11 | 1.47 |
| Trends: luxury resale | 1.40 | 1.42 | 1.82 |
| Trends: luxury watches | 0.94 | 0.99 | 1.39 |
| Trends: quiet luxury | 1.06 | 1.04 | 1.12 |
| Wikipedia: Gucci | 1.46 | 0.97 | 1.09 |
| Wikipedia: Hermes | 0.85 | 0.97 | 1.00 |
| Wikipedia: Louis Vuitton | 1.08 | 1.18 | 1.17 |

1. ETS beat the best simple method in 6 of 10 series at 1 month, 5 of 10 at 3 months and 2 of 10 at 6 months. It beat the naive forecast in 6, 6 and 4 of 10.
2. Wins at 3 months were small (1% to 6%). For luxury resale, ETS was worse at every horizon.
3. Forecasts beyond one month from a series' own history are not reliable for these data. The test window includes the 2025-08 shift and the early-2026 spike, which the history could not foretell.
4. Series where ETS beat the best simple method at both 1 and 3 months: Trends Gucci, Trends Louis Vuitton, Trends luxury watches, Wikipedia Hermes. Only these will get a next-month outlook in the dashboard.

Limits: ten series and overlapping origins. No significance test. Results depend on the four methods tried. Google Trends values are sampled and relative.
## 2g. SQL layer and cross-checks

Method: the series are stored in a SQLite database (tables: series, observations, change_points) built by src/db/build_db.py and queried with SQL (joins, CTEs, window functions) in notebooks/12_sql_queries.py. The database is rebuilt from the CSV files and is not committed. Data sources: Google Trends; Wikimedia Pageviews API (CC0).

1. The SQL queries reproduce the Wikipedia indexed table in section 2 exactly, which checks the database against the earlier results.
2. Largest month-to-month moves in the Google Trends brand series: Gucci +50 and Louis Vuitton +56 in April 2026, reversing by about -53 each in June 2026. Also Gucci +40 in November 2021 and -26 in January 2022.
3. Gucci's monthly value was 28 in January 2026, 100 in April (the highest value in the whole 2019-2026 pull of three brands), 92 in May, 39 in June and 34 in September, about 21% above January. The early-2026 episode was a burst of about three months that mostly reverted. Hermes rose more gently (29 to 42, then 35 in September). The cause is not established.
4. A trailing 12-month average still read about 49 for Gucci in September 2026 against a raw value of 34, because the window still contains the April and May burst. Smoothing can hide a reversion.
5. Under the stricter change-point setting, months where more than one series breaks: 2023-04 (quiet luxury and luxury handbags searches), 2024-05 (Louis Vuitton and Coffee on Wikipedia), 2024-08 (luxury watches searches and Gucci on Wikipedia), 2025-08 (all four category terms) and 2026-03 (Gucci and Louis Vuitton searches).

Limits: grouping by exact month misses breaks one month apart (for example Bicycle in 2024-06 next to the 2024-05 pair). The 2024-08 match across different sources is probably chance. Google Trends values are relative: 100 is the peak within that one pull.
## 2g. SQL layer and cross-checks

Method: the series are stored in a SQLite database (tables: series, observations, change_points) built by src/db/build_db.py and queried with SQL (joins, CTEs, window functions) in notebooks/12_sql_queries.py. The database is rebuilt from the CSV files and is not committed. Data sources: Google Trends; Wikimedia Pageviews API (CC0).

1. The SQL queries reproduce the Wikipedia indexed table in section 2 exactly, which checks the database against the earlier results.
2. Largest month-to-month moves in the Google Trends brand series: Gucci +50 and Louis Vuitton +56 in April 2026, reversing by about -53 each in June 2026. Also Gucci +40 in November 2021 and -26 in January 2022.
3. Gucci's monthly value was 28 in January 2026, 100 in April (the highest value in the whole 2019-2026 pull of three brands), 92 in May, 39 in June and 34 in September, about 21% above January. The early-2026 episode was a burst of about three months that mostly reverted. Hermes rose more gently (29 to 42, then 35 in September). The cause is not established.
4. A trailing 12-month average still read about 49 for Gucci in September 2026 against a raw value of 34, because the window still contains the April and May burst. Smoothing can hide a reversion.
5. Under the stricter change-point setting, months where more than one series breaks: 2023-04 (quiet luxury and luxury handbags searches), 2024-05 (Louis Vuitton and Coffee on Wikipedia), 2024-08 (luxury watches searches and Gucci on Wikipedia), 2025-08 (all four category terms) and 2026-03 (Gucci and Louis Vuitton searches).

Limits: grouping by exact month misses breaks one month apart (for example Bicycle in 2024-06 next to the 2024-05 pair). The 2024-08 match across different sources is probably chance. Google Trends values are relative: 100 is the peak within that one pull.
## 2h. Own data: experimental relevance index

Method: for each brand, two components rebased to a 2019 average of 100. (a) The seasonally adjusted Google Trends component. (b) The seasonally adjusted Wikipedia component divided by the average of the Coffee and Bicycle control articles. The midpoint is the average of the two and the band is the range between them. Sensitivity: the Wikipedia component recomputed using each control alone. Category composite: the average z-score of the four category search terms, smoothed over 12 months. 2026 covers January to September. Data sources: Google Trends; Wikimedia Pageviews API (CC0).

| Year | Hermes: Trends | Hermes: Wikipedia vs controls | Hermes: midpoint | Gucci: Trends | Gucci: Wikipedia vs controls | Gucci: midpoint | Louis Vuitton: Trends | Louis Vuitton: Wikipedia vs controls | Louis Vuitton: midpoint |
|---|---|---|---|---|---|---|---|---|---|
| 2019 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| 2020 | 109 | 106 | 108 | 92 | 94 | 93 | 102 | 96 | 99 |
| 2021 | 110 | 116 | 113 | 87 | 197 | 142 | 101 | 104 | 103 |
| 2022 | 99 | 109 | 104 | 82 | 229 | 155 | 97 | 108 | 103 |
| 2023 | 95 | 120 | 108 | 70 | 134 | 102 | 90 | 115 | 102 |
| 2024 | 103 | 176 | 140 | 63 | 123 | 93 | 89 | 130 | 109 |
| 2025 | 111 | 220 | 166 | 60 | 119 | 89 | 91 | 138 | 115 |
| 2026 | 121 | 219 | 170 | 61 | 124 | 93 | 93 | 124 | 109 |

Correlation between the two components: Hermes 0.62, Gucci 0.04, Louis Vuitton -0.84.

Sensitivity, 2026 Wikipedia component by choice of control (both, Coffee only, Bicycle only): Hermes 219, 198, 245. Gucci 124, 112, 139. Louis Vuitton 124, 112, 139.

Category composite, yearly average (z-score): 2019 -0.59, 2020 -0.58, 2021 -0.56, 2022 -0.49, 2023 -0.32, 2024 -0.02, 2025 0.33, 2026 2.64.

1. The two components agree in direction only for Hermes. For Gucci they are unrelated and for Louis Vuitton they move in opposite directions. Correlations between smoothed series rest on few independent observations, so they show the direction of drift and not its strength.
2. Hermes' midpoint rises to 170 by 2026, but this depends on dividing by control articles whose views fell by more than half. Hermes' raw Wikipedia views in 2026 are below the 2019 level (index 92), so "held up" is more accurate than "grew".
3. The choice of control changes the Wikipedia component by roughly 10% either way around the two-control value.
4. The category composite rises mostly after 2025 and inherits the shared August 2025 break and the early-2026 surge from a single Google Trends pull, whose cause is unknown. It should not be read as a lasting rise in relevance.
5. Because the two sources disagree, the dashboard shows the band and labels the midpoint as the average of the two sources.

Limits: two control articles, and the assumption that they reflect site-wide changes in Wikipedia readership. One Google Trends pull for the categories. Experimental, with no significance tests.

## 3. Survey evidence: BCG-Altagamma True-Luxury Global Consumer Insights 2026

Source: https://www.bcg.com/publications/2026/luxury-healthier-foundations-and-genai (published 7 July 2026). Survey of 10,000+ True-Luxury consumers in 11 markets.

1. Top purchase drivers: design and aesthetics, craftsmanship and quality, timelessness. Logo visibility ranked least important.
2. BCG describes a healthier revenue mix in which traditional personal-luxury categories fall from about 80% toward 60%, with growth in lifestyle and experiential luxury.
3. Top-tier clients rose from 14% to 24% of spend over ten years. Aspirational consumers drove most of the market's volatility.
4. 70% of consumers walked away from a purchase because the price seemed unjustified.
5. 56% of aspirational consumers barely know the creative director's name, against 70% informed among top-tier consumers.

Limits: stated preferences, not observed behaviour. True-Luxury buyers only. One edition. Produced by a consultancy that advises luxury brands.

## 4. Survey evidence: McKinsey and The Business of Fashion, State of Luxury 2026

Source: https://www.mckinsey.com/industries/retail/our-insights/state-of-luxury (29 June 2026). Survey of 2,000+ luxury clients in the US and China, plus interviews.

1. In both markets, emotional connection ranks as a top driver of desirability, ahead of craftsmanship, heritage and exclusivity. Craftsmanship and quality are described as the price of entry.
2. Exclusivity is shifting from scarcity toward insider recognition. Few consumers say a hard-to-find product motivates full-price buying.
3. Travel ranked as the top use of extra discretionary income in both markets, ahead of any luxury product category.
4. Established luxury consumers, not aspirational ones, are the most active resale buyers.
5. In the US, 68% said newer brands better reflect their identity, against 63% for established houses.

Note: BCG ranks craftsmanship and quality first and logos last, while McKinsey ranks emotional connection above craftsmanship. Samples and questions differ. Both place status and logos lower.

Limits: US and China only. Stated preferences, not observed behaviour. One edition. Produced by a consultancy that advises luxury brands.

## 5. Industry context: Goldman Sachs and Bain-Altagamma

Goldman Sachs, "Why Luxury Goods Companies' Revenues Are Forecast to Climb" (22 October 2026): https://www.goldmansachs.com/insights/articles/why-luxury-goods-companies-revenues-are-forecast-to-climb

1. Goldman Sachs Research forecasts revenue growth of 7% in 2027 and 6% in 2026 for a basket of listed luxury-goods companies.
2. It attributes the recent slowdown mostly to strategic inertia and to price rises it estimates at around 60% between mid-2019 and mid-2026.
3. It notes that a brand's codes and icons need not be loud logos.

Bain & Company with Altagamma, Luxury Goods Worldwide Market Study, 24th edition (20 November 2025): https://www.bain.com/insights/finding-a-new-longevity-for-luxury/

4. Overall luxury spending was about EUR 1.44 trillion in 2025, roughly flat on 2024.
5. Personal luxury goods were forecast at EUR 358 billion in 2025, against EUR 364 billion in 2024.
6. The study describes a shift toward luxury experiences and away from traditional goods.

Limits: Goldman's figures are an investment-research forecast on listed companies, not consumer data. Both are views of a bank and a consultancy. Goldman's page prohibits copying, so we paraphrase and link only.

## 6. Contrasting evidence: MG2

Source: https://mg2.com/latest/how-consumers-are-redefining-their-relationship-with-luxury-beyond-the-product-itself/ (June 2026). Read from the page summary only, not the full report.

1. 62% of respondents named quality and craftsmanship as their top reason to buy luxury.
2. More than 3 in 4 still associate luxury with owning something rare or of status.

This suggests status has not disappeared, so the verdict on question 3 may be "partly supported".
## 7. Performance context: company results and press reports

Company-wide results, not brand-level except Gucci. Facts paraphrased by us. Kering figures come from its own press release. LVMH figures come from press reports and still need checking against LVMH's own releases.

Kering, 2025 results press release (10 February 2026): https://www.nasdaq.com/press-release/kering-2025-results-sequential-improvement-unlocking-next-phase-sustainable

1. Kering revenue was EUR 14.7 billion, down 13% as reported and 10% on a comparable basis.
2. Recurring net income from continuing operations was EUR 532 million, down 56%. After non-recurring items, mostly restructuring, net income from continuing operations was a loss of EUR 29 million, against a profit of EUR 1,025 million in 2024.
3. Gucci revenue was about EUR 6 billion, down 22% as reported and 19% on a comparable basis. Gucci's recurring operating income was EUR 966 million, down 40%.

Reuters reporting, read through syndicated copies:
- Kering, 10 February 2026: https://d2233.cms.socastsrm.com/2026/02/10/kerings-fourth-quarter-sales-fall-less-than-expected-as-gucci-slide-continues
- LVMH, 26 July 2026: https://www.thestandard.com.hk/finance/article/338409/LVMH-sales-tick-up-as-US-luxury-demand-offsets-hit-from-Iran-war

4. Reuters reported that Kering's operating income of EUR 1.63 billion was less than a third of its 2022 level, with Gucci's operating margin at 16% against 36% three years earlier.
5. Reuters reported that LVMH's first-half 2026 profit from operations fell 4% to EUR 8.7 billion with a broadly stable operating margin, and that its shares were down 28% for the year to that date.
6. Press reports of LVMH's 2025 results: revenue down 1% to EUR 80.8 billion and operating profit down 9% to EUR 17.8 billion.
Reuters, "European luxury's $350 billion blowout" (13 October 2026): https://www.reuters.com/business/retail-consumer/european-luxurys-350-billion-blowout-2026-10-13/ . Reuters blocks automated access, so we read the article through syndicated copies.

7. Reuters reported that the ten largest listed European luxury companies lost about USD 350 billion of combined market value since the start of 2026, as hopes of a sector rebound faded and weakness in China persisted.
8. The combined market value of LVMH, Hermes, Kering and Richemont has nearly halved since around 2024. Richemont, focused on watches and jewellery, held up better. LVMH shares were down more than 40% for the year.
9. LVMH's third-quarter fashion and leather goods sales missed expectations, with China in focus. A secondary summary gives a 5% organic decline against an expected 1.8% fall. We have not yet checked this against LVMH's own release.

Market values reflect investors' expectations, not sales, profits or consumer interest. In early 2026, searches for Gucci and Louis Vuitton spiked (section 2g) while market values fell, so attention and valuation moved differently. This is an observation, not an explanation. Our attention data is global and cannot isolate China.

How this compares with our data: Gucci's search-interest trend fell about 40% from 2019 to 2025 (section 2b) and its reported 2025 revenue fell 22%. The direction is the same. This is a description and not evidence that attention causes or predicts sales.

Limits: company-wide figures except Gucci. "Recurring" figures exclude items the company classes as non-recurring. Hermes is not covered. Reuters content is copyrighted, so we paraphrase facts and link, and do not copy. LVMH figures are not yet checked against LVMH's own releases.

## Status of the hypotheses (preliminary)
## Conclusions (current)

These match the README. Question 1 may be revised after the experimental relevance index is added.

| Question | Conclusion | Where the evidence is |
|---|---|---|
| 1. Is interest rising or declining? | Mixed. Searches for four luxury terms were higher in 2025-2026 than in 2019-2024, but Wikipedia readership fell for the brands and for unrelated control articles alike. Hermes held up on both sources, while Gucci fell on searches. A shared jump across the four search terms in August 2025 is unexplained. | Sections 1, 2, 2b, 2c, 2g. Context in section 7. |
| 2. Is the way luxury is discussed changing? | Partly. "Quiet luxury" went from near zero to a sustained search term, with a robust break in April 2023. No measure of news coverage or tone over time, because news-data access was rate-limited. | Sections 1, 2, 2c. |
| 3. Is there a shift from status toward craftsmanship, heritage or experience? | Partly supported. Published surveys point away from logos and toward quality, emotional connection and experiences, though status associations remain widespread. Our own data measures attention and cannot show what people value. | Sections 3, 4, 5, 6. |
| 4. Do segments and brands differ? | Brands partly, segments not. The four search-term segments move mostly as one series. Hermes behaves differently from Gucci and Louis Vuitton. Three brands only, and no audience data per brand. | Sections 2b, 2c, 2d. |
| 5. Are there early signals? | Not supported. No consistent lead between Wikipedia and Google Trends, and unrelated control pairs showed similar correlations. Forecasts beat simple baselines only slightly, and only about one month ahead. | Sections 2e, 2f. |
| 6. Which strategies are worth investigating? | Hypotheses only, drawn from cited reports. Our data cannot test whether a strategy works. | Sections 3, 4, 5, 7. |