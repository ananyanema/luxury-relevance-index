# Findings so far (work in progress)

Last updated: 26 October 2026. Each finding states what the data shows and what it does not show. Sections 1 and 2 use our own data. Sections 3 to 6 are other organisations' findings, paraphrased by us and linked to their source.

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

## Status of the hypotheses (preliminary)

| Question | Status |
|---|---|
| 1. Interest rising or declining? | Mixed so far. Trends and Wikipedia disagree for 2025-2026. |
| 2. Coverage and discussion changing? | Not tested. GDELT access is blocked for now. |
| 3. Shift from status toward craftsmanship, heritage, experience? | Surveys lean toward craft and emotional connection over status, but status has not disappeared. Our own proxy test is not done. |
| 4. Segments and brands differ? | Not tested. |
| 5. Early signals? | Not tested. |
| 6. Strategies worth investigating? | Not started. |