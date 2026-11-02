import streamlit as st

import charts as C
from content import PUZZLE, QUESTIONS, STRATEGIES
from style import apply_style, nav

st.set_page_config(page_title="Question", layout="centered", initial_sidebar_state="collapsed")
apply_style()
nav()

try:
    n = int(st.query_params.get("q", "1"))
except ValueError:
    n = 1
n = min(max(n, 1), 6)
q = QUESTIONS[n - 1]


def plate(title, caption, fn):
    st.markdown(f'<div class="ptitle">{title}</div>', unsafe_allow_html=True)
    try:
        st.plotly_chart(fn(), config={"displayModeBar": False})
    except FileNotFoundError as e:
        st.markdown(
            f'<span class="care">This chart needs a data file that was not found ({e.filename}). '
            f'Run the matching notebook, then refresh.</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="pc">{caption}</div>', unsafe_allow_html=True)


prev_link = f'<a class="pn" href="/Question?q={n-1}" target="_self">Previous question</a>' if n > 1 else ""
next_link = f'<a class="pn" href="/Question?q={n+1}" target="_self">Next question</a>' if n < 6 else ""
st.markdown(
    f'<div class="crumbs"><a class="pn" href="/" target="_self">Back to the rack</a>{prev_link}{next_link}</div>',
    unsafe_allow_html=True,
)

figs = "".join(f'<div class="fig"><div class="fn foil">{a}</div><div class="fl">{b}</div></div>' for a, b in q["figs"])
st.markdown(
    f'<div class="chap">No. 0{n}</div><div class="dtitle">{q["title"]}</div>'
    f'<span class="stamp inline">{q["verdict"]}</span><p class="dshort">{q["short"]}</p>'
    f'<div class="figs">{figs}</div>',
    unsafe_allow_html=True,
)

if n == 1:
    c1, c2 = st.columns(2)
    with c1:
        plate("Google Trends, seasonally adjusted trend (2019 = 100)",
              "Gucci's search trend fell about 40% by 2025. Hermès dipped, then rose.", C.trend_chart)
    with c2:
        plate("Wikipedia views against two control articles (2019 = 100)",
              "Both control articles fell by half or more. Gucci's 2021 to 2022 episode stands out.", C.wiki_chart)
    c3, c4 = st.columns(2)
    with c3:
        plate("Search terms: average interest before and after 2025",
              "All four terms rose. Resale started near zero, so compare points, not percentages.", C.category_chart)
    with c4:
        st.markdown(f'<div class="ptitle">A puzzle we did not solve</div><span class="care">{PUZZLE}</span>',
                    unsafe_allow_html=True)
    plate("Where the series break (stricter setting)",
          "Four search terms shift in the same month, August 2025 (dark red). The cause is unexplained. Breaks in near-zero series, such as quiet luxury before 2023, are not meaningful.", C.break_chart)

elif n == 2:
    c1, c2 = st.columns(2)
    with c1:
        plate("“Quiet luxury” searches, monthly",
              "Near zero until a step in April 2023, then a larger surge from August 2025.", C.quiet_search_chart)
    with c2:
        plate("Wikipedia article on quiet luxury, monthly views",
              "Data begins in late 2023. Views stayed flat while searches surged again.", C.quiet_wiki_chart)

elif n == 3:
    plate("What published surveys report (percent of respondents)",
          "Different surveys, samples and questions, so the bars are not directly comparable. "
          "Brass: MG2. Black: BCG-Altagamma. Brown: McKinsey.", C.survey_chart)
    c1, c2 = st.columns(2)
    with c1:
        plate("Top-tier clients' share of luxury spend (BCG)",
              "Over ten years, according to BCG-Altagamma.", C.toptier_chart)
    with c2:
        st.markdown('<div class="ptitle">Reading these numbers</div>'
                    '<span class="care">These are what people say, not what they do, and they come from different '
                    'samples. Together they lean away from logos and toward quality and emotional connection, '
                    'but status has not disappeared. Our own attention data cannot test this question.</span>',
                    unsafe_allow_html=True)

elif n == 4:
    c1, c2 = st.columns(2)
    with c1:
        plate("Four search segments: correlation of monthly changes",
              "Watches and handbags move together. Resale and quiet luxury are only weakly tied to the rest.",
              C.segment_heat)
    with c2:
        plate("Three brands: correlation of monthly changes",
              "Gucci and Louis Vuitton move closely together. Hermès is less tied to both.", C.brand_heat)
    plate("How much of the movement one pattern explains",
          "One component explains 93% of the segments' variance and 71% of the brands'.", C.pc_chart)
    st.markdown('<div class="pc">The two-source relevance index for each brand is on the '
                '<a href="/Relevance_index" target="_self">relevance index page</a>.</div>', unsafe_allow_html=True)

elif n == 5:
    plate("Lead-lag correlations of monthly changes",
          "Each row is a pair of Wikipedia and Google Trends series. Unrelated control pairs (bottom three) "
          "show correlations as large as the luxury pairs, and none survives the correction for testing many pairs.",
          C.leadlag_chart)
    plate("Forecast backtest: error relative to the best simple method",
          "Below the dotted line means exponential smoothing did better. It helps mostly one month ahead.",
          C.backtest_chart)

elif n == 6:
    plate("Reported changes in company results (percent)",
          "Company-wide results, except Gucci where stated. Different periods. These are company results, "
          "not consumer interest, so they are not comparable with our attention data.", C.results_chart)
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in STRATEGIES)
    st.markdown(f'<div class="ptitle">Strategies named in the cited reports, and where each comes from</div>'
                f'<table class="stbl">{rows}</table>', unsafe_allow_html=True)

flist = "".join(f"<li>{f}</li>" for f in q["findings"])
llist = "".join(f'<li><a href="{u}" target="_blank">{t}</a></li>' for t, u in q["links"])
st.markdown(
    f'<div class="sec">What we found</div><ol class="flist">{flist}</ol>'
    f'<div class="sec">How we tested it</div><div class="txt">{q["how"]}</div>'
    f'<div class="sec">What it cannot tell us</div><span class="care">{q["limits"]}</span>'
    f'<div class="sec">Sources</div><ul class="links">{llist}</ul>',
    unsafe_allow_html=True,
)
