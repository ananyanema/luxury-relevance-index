L = {
    "trends": ("Google Trends", "https://trends.google.com/trends/"),
    "wiki": ("Wikimedia Pageviews API (CC0)", "https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/documentation/access-policy.html"),
    "bcg": ("BCG-Altagamma, True-Luxury Global Consumer Insights 2026", "https://www.bcg.com/publications/2026/luxury-healthier-foundations-and-genai"),
    "mck": ("McKinsey and The Business of Fashion, State of Luxury 2026", "https://www.mckinsey.com/industries/retail/our-insights/state-of-luxury"),
    "bain": ("Bain and Altagamma, Luxury Goods Worldwide Market Study 2025", "https://www.bain.com/insights/finding-a-new-longevity-for-luxury/"),
    "gs": ("Goldman Sachs, Why Luxury Goods Companies' Revenues Are Forecast to Climb", "https://www.goldmansachs.com/insights/articles/why-luxury-goods-companies-revenues-are-forecast-to-climb"),
    "mg2": ("MG2, How consumers are redefining their relationship with luxury", "https://mg2.com/latest/how-consumers-are-redefining-their-relationship-with-luxury-beyond-the-product-itself/"),
    "kering": ("Kering, 2025 results press release (syndicated copy)", "https://www.nasdaq.com/press-release/kering-2025-results-sequential-improvement-unlocking-next-phase-sustainable"),
    "reuters_k": ("Reuters on Kering, 10 February 2026 (syndicated copy)", "https://d2233.cms.socastsrm.com/2026/02/10/kerings-fourth-quarter-sales-fall-less-than-expected-as-gucci-slide-continues"),
    "reuters_l": ("Reuters on LVMH, 26 July 2026 (syndicated copy)", "https://www.thestandard.com.hk/finance/article/338409/LVMH-sales-tick-up-as-US-luxury-demand-offsets-hit-from-Iran-war"),
    "reuters_s": ("Reuters, European luxury's $350 billion blowout, 13 October 2026", "https://www.reuters.com/business/retail-consumer/european-luxurys-350-billion-blowout-2026-10-13/"),
    "lvmh25": ("LVMH 2025 results, as reported by Sharecast", "https://companyresearch.digitallook.com/news/35659686/Shares_slide_as_LVMH_results_disappoint.html?ac=208341"),
    "repo": ("Project repository: full findings, methods and code", "https://github.com/ananyanema/luxury-relevance-index"),
}


def links(*keys):
    return [L[k] for k in keys]


QUESTIONS = [
    {
        "n": 1, "title": "Is interest in luxury rising or declining?", "verdict": "Mixed",
        "finding": "Searches were higher in 2025 and 2026, but Wikipedia readership fell for brands and unrelated articles alike.",
        "short": "Searches for four luxury terms were higher in 2025 and 2026 than in 2019 to 2024. But Wikipedia readership fell for the brands and for unrelated control articles alike, so most of that fall is site-wide. Hermès held up on both sources, and Gucci fell on searches.",
        "figs": [("+17.2 points", "Quiet luxury searches, 2025 on against 2019 to 2024"),
                 ("92, 50 and 29", "Hermès, Coffee and Bicycle (the two controls), Wikipedia 2026, 2019 = 100"),
                 ("August 2025", "Shared break in four search terms")],
        "findings": [
            "All four search terms were higher in 2025 and 2026 than in 2019 to 2024: quiet luxury by 17.2 points, luxury resale by 12.7, luxury watches by 40.5 and luxury handbags by 9.7. Much of this comes from a surge from mid-2025 whose cause is unknown.",
            "Wikipedia readership fell broadly. Two unrelated control articles, Coffee and Bicycle, ended 2026 at 50 and 29 (2019 average = 100).",
            "After removing seasonality, Gucci's search trend fell from 100 to about 60 by 2025. Hermès rose to 121 by 2026, and Louis Vuitton ended 2026 at 93.",
            "Gucci and Louis Vuitton ended 2026 on Wikipedia at 48 and 50, close to Coffee at 50, so their declines are not evidence of a luxury-specific loss. Hermès stayed at 92.",
            "The early-2026 jump in Gucci and Louis Vuitton searches looks like a burst of about three months that mostly reverted.",
            "Context from company results and market values, not consumer interest: Kering's 2025 revenue fell 13% and Gucci's 22%, and the share prices of Europe's biggest luxury groups fell sharply in 2026.",
        ],
        "how": "Google Trends and Wikipedia page views from 2019 to 2026, seasonally adjusted, with two unrelated Wikipedia articles as controls and change-point detection.",
        "limits": "Attention is not sales. The August 2025 break rests on a single Google Trends pull that we did not repeat.",
        "links": links("trends", "wiki", "kering", "lvmh25", "reuters_k", "reuters_l", "reuters_s", "repo"),
    },
    {
        "n": 2, "title": "Is the way luxury is discussed changing?", "verdict": "Partly",
        "finding": "“Quiet luxury” went from almost nothing to a lasting search term in April 2023.",
        "short": "The vocabulary changed: searches for “quiet luxury” went from near zero to a sustained term, with a clear step in April 2023. We did not measure how news coverage or tone changed.",
        "figs": [("2.6 to 19.8", "Quiet luxury search interest, 2019 to 2024 against 2025 on"),
                 ("April 2023", "Break found under both settings"),
                 ("3,500 a month", "Wikipedia article views, 2024 to 2026")],
        "findings": [
            "“Quiet luxury” searches averaged 2.6 in 2019 to 2024 and 19.8 from 2025.",
            "The change-point test finds a step in April 2023 under both settings, matching the step visible in the chart.",
            "Its Wikipedia article has data only from late 2023 and held at roughly 3,500 to 3,700 views a month from 2024 to 2026.",
            "Searches surged again in 2025 and 2026 while the article's views stayed flat, so searching and reading are different behaviours.",
            "Not measured: how news coverage or its tone changed, because news-data access was rate-limited.",
        ],
        "how": "Google Trends, Wikipedia page views and change-point detection.",
        "limits": "No measure of coverage or tone, because news-data access was rate-limited. Attention data cannot show what people say.",
        "links": links("trends", "wiki", "repo"),
    },
    {
        "n": 3, "title": "Is there a shift from status toward craft and experience?", "verdict": "Partly supported",
        "finding": "Surveys lean toward quality and emotional connection over logos. Our own data cannot show what people value.",
        "short": "Published surveys lean away from logos and toward quality, emotional connection and experiences. One survey shows that status associations remain widespread. Our own data cannot show what people value.",
        "figs": [("Logos last", "Ranked least important driver, BCG-Altagamma"),
                 ("Emotion first", "Emotional connection ranked above craftsmanship, McKinsey"),
                 ("3 in 4", "Still link luxury with rarity or status, MG2")],
        "findings": [
            "BCG-Altagamma (10,000+ True-Luxury consumers, 11 markets): the top purchase drivers are design and aesthetics, craftsmanship and quality, and timelessness. Logo visibility ranked least important.",
            "McKinsey and The Business of Fashion (2,000+ clients in the US and China): emotional connection ranks as a top driver, ahead of craftsmanship, heritage and exclusivity. Craftsmanship and quality are described as the price of entry.",
            "McKinsey also reports that exclusivity is shifting from scarcity toward insider recognition, and that travel ranked as the top use of extra discretionary income.",
            "MG2: 62% name quality and craftsmanship as their top reason to buy, yet more than 3 in 4 still associate luxury with owning something rare or of status. Status has not disappeared.",
            "BCG: 70% of consumers walked away from a purchase because the price seemed unjustified.",
            "Our own data measures attention, so it cannot test this question directly.",
        ],
        "how": "Reading and comparing published surveys and reports, paraphrased and cited.",
        "limits": "Stated preferences, not behaviour. Different samples and questions. One edition each. The reports are produced by consultancies and agencies that work with luxury brands. The MG2 figures come from its summary page only.",
        "links": links("bcg", "mck", "mg2", "repo"),
    },
    {
        "n": 4, "title": "Do segments and brands differ?", "verdict": "Brands partly",
        "finding": "Hermès behaves differently from Gucci and Louis Vuitton. The four search segments move as one.",
        "short": "The four search segments move almost as one series. Hermès behaves differently from Gucci and Louis Vuitton, which move closely together.",
        "figs": [("93%", "Variance in one component across the four segments"),
                 ("0.85", "Gucci and Louis Vuitton, monthly changes"),
                 ("0.43 to 0.46", "Hermès with each of the others")],
        "findings": [
            "The four search segments correlate at 0.84 to 0.97 in levels, and one component explains 93% of their variance, so they move mostly as one series. This largely reflects a shared rise and the August 2025 break.",
            "Month to month, luxury watches and luxury handbags move together (0.73), while quiet luxury and luxury resale are only weakly tied to the others (0.10 to 0.45).",
            "Gucci and Louis Vuitton move closely together (0.85 for monthly changes). Hermès is less tied to both (0.43 to 0.46). One component explains 71% of the three brands' variance.",
            "In the experimental relevance index, the two sources agree only for Hermès (correlation 0.62). For Gucci they are unrelated (0.04), and for Louis Vuitton they move in opposite directions (-0.84).",
            "Caution: the brands share a December peak and the early-2026 spike, which raise their correlations, and there are only three of them.",
        ],
        "how": "Correlations of levels and of month-to-month changes, a principal-component check, and a two-source relevance index with a sensitivity check.",
        "limits": "Three brands and four search terms only. No audience data per brand or segment.",
        "links": links("trends", "wiki", "repo"),
    },
    {
        "n": 5, "title": "Are there early signals of changing preferences?", "verdict": "Not supported",
        "finding": "No consistent lead between Wikipedia and Google, and unrelated control pairs behaved the same way.",
        "short": "No consistent lead between Wikipedia and Google searches in either direction, and unrelated control pairs showed similar correlations. Forecasts beat simple baselines only slightly, and only about one month ahead.",
        "figs": [("0 of 14", "Tests surviving correction"),
                 ("0.27", "Control pair correlation, about as large as the luxury pairs"),
                 ("6 of 10", "Series where forecasts beat baselines, one month ahead")],
        "findings": [
            "None of the 14 lead-lag tests survives the correction for testing many pairs (p below 0.0012). We found no consistent lead in either direction.",
            "The smallest p-value (Hermès, Google Trends leading Wikipedia, 0.026) points opposite to our hypothesis and is consistent with chance.",
            "Gucci's correlation of 0.40 is at lag zero: the two series move in the same month and do not lead each other.",
            "Unrelated control pairs reach correlations (0.27) similar to the luxury pairs, so correlations of this size occur between unrelated series.",
            "In a walk-forward backtest, exponential smoothing beat the best simple method in 6 of 10 series one month ahead, 5 of 10 at three months and only 2 of 10 at six months.",
            "One episode, Gucci's Wikipedia rise from July 2021 ahead of its search break in November 2021, is an observation only.",
        ],
        "how": "Granger tests and cross-correlations on monthly changes with control pairs, and a walk-forward forecast backtest against simple baselines.",
        "limits": "Monthly data cannot show leads shorter than a month. Few real events. Quiet luxury has only 35 months of overlap.",
        "links": links("trends", "wiki", "repo"),
    },
    {
        "n": 6, "title": "Which strategies are worth investigating?", "verdict": "Hypotheses only",
        "finding": "Drawn from cited reports. Our data cannot test whether a strategy works.",
        "short": "These come from the cited reports, not from our tests: lead with quality and discreet codes, invest in experiences, review price increases, develop resale and repair, and focus on top-tier clients.",
        "figs": [("14% to 24%", "Top-tier share of spend over ten years, BCG"),
                 ("70%", "Walked away from an unjustified price, BCG"),
                 ("About 60%", "Estimated price rise, mid-2019 to mid-2026, Goldman Sachs")],
        "findings": [
            "Goldman Sachs attributes the recent slowdown mostly to strategic inertia and to price rises it estimates at around 60% between mid-2019 and mid-2026, and forecasts revenue growth of 6% in 2026 and 7% in 2027 for a basket of listed luxury companies.",
            "Kering's 2025 results show how uneven performance is: group revenue fell 13% and Gucci's 22%, while LVMH's 2025 revenue eased 1% and its operating profit fell 9%.",
            "Reuters reported that European luxury companies lost about USD 350 billion of market value in 2026, with Richemont holding up better than LVMH, Hermès and Kering. Market value reflects investors' expectations, not sales or consumer interest.",
            "Each strategy in the table is taken from a cited report. We did not test any of them.",
        ],
        "how": "Collating the cited reports. We did not test any strategy.",
        "limits": "Our data cannot test whether a strategy works. A brand with its own sales and customer data could.",
        "links": links("bcg", "mck", "bain", "gs", "kering", "lvmh25", "reuters_k", "reuters_l", "reuters_s", "repo"),
    },
]

STRATEGIES = [
    ("Lead with quality, design and discreet codes rather than loud logos", "BCG-Altagamma (drivers); Goldman Sachs (codes need not be logos)"),
    ("Invest in experiences and emotional connection", "McKinsey and The Business of Fashion; BCG-Altagamma; Bain and Altagamma"),
    ("Review price increases", "BCG-Altagamma (70% walked away); Goldman Sachs (about 60% rise)"),
    ("Develop resale and repair, especially for established customers", "McKinsey and The Business of Fashion"),
    ("Focus on top-tier clients", "BCG-Altagamma (14% to 24% of spend)"),
]

PUZZLE = (
    "<b>The unexplained break.</b> Four unrelated search terms (quiet luxury, luxury resale, luxury watches, "
    "luxury handbags) shift level in the same month, August 2025, while the brand terms and the Wikipedia "
    "article on quiet luxury do not. We do not know why. Possible explanations: a real shift in generic luxury "
    "searching, a change in how Google Search works that month, a sampling quirk of the single pull we made, "
    "or something about the word “luxury” itself. We did not test these."
)

LOG = [
    ("01", "Plot Google Trends for three brands and four segments", "Gucci fell. All four search terms rose in 2025 and 2026.", "done", "Done"),
    ("02", "Growth comparison, 2019 to 2024 against 2025 on", "Quiet luxury +17.2 points, resale +12.7, watches +40.5, handbags +9.7.", "done", "Done"),
    ("03", "Plot Wikipedia monthly views", "Brand article views were lower by 2026 than in 2019.", "done", "Done"),
    ("04", "Index Wikipedia views against two control articles", "Controls fell by half or more, so most of the brand decline is site-wide.", "done", "Done"),
    ("05", "Seasonal decomposition (STL)", "Gucci's search trend down about 40% by 2025. Hermès rose.", "done", "Done"),
    ("06", "Change-point detection with two settings", "Four search terms break together in August 2025.", "done", "Done"),
    ("07", "Segment and brand correlations, principal components", "The four segments move as one (93%). Hermès differs from Gucci and Louis Vuitton.", "done", "Done"),
    ("08", "Lead-lag and Granger tests with control pairs", "No lead survives correction.", "done", "Done"),
    ("09", "Repeat the category pull and compare", "Skipped by choice. The August 2025 finding rests on one pull.", "skip", "Skipped"),
    ("10", "Forecast backtest, exponential smoothing against simple baselines", "Forecasts help only about one month ahead.", "done", "Done"),
    ("11", "Inspect a small Mendeley luxury survey", "Dropped before running: 272 responses, unknown origin, a one-off snapshot.", "drop", "Dropped"),
    ("12", "SQL layer with window functions", "Reproduced the Wikipedia table exactly.", "done", "Done"),
    ("13", "Experimental relevance index with a band", "The two sources disagree for Gucci and Louis Vuitton.", "done", "Done"),
    ("GD", "GDELT news collection", "Dropped: access was rate-limited on repeated attempts.", "drop", "Dropped"),
]

SOURCE_GROUPS = [
    ("Own data", [L["trends"], L["wiki"]]),
    ("Cited reports, paraphrased", [L["bcg"], L["mck"], L["bain"], L["gs"], L["mg2"], L["kering"], L["lvmh25"], L["reuters_k"], L["reuters_l"], L["reuters_s"]]),
]

NOT_USED = (
    "GDELT: access was rate-limited on repeated attempts, so no data was collected. "
    "Amazon Reviews 2023: personal data, licence not confirmed, not a luxury channel, and the data ends in September 2023. "
    "A small Mendeley survey: 272 responses of unknown origin, too small to add. "
    "OpenAlex: skipped by choice. Google Keyword Planner, earnings-call transcripts and scraping Google Scholar: terms not checked or likely restrictive."
)

LIMITS = (
    "Attention is not sales. We have no consumer text, no news coverage and no brand-level sales. "
    "The relevance index is experimental and depends on two unrelated control articles. "
    "The shared jump in four search terms in August 2025 is unexplained and rests on a single Google Trends pull. "
    "Published reports are paraphrased and are produced by organisations that work with luxury brands."
)
