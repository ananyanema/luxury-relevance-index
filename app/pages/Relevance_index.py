import streamlit as st

import charts as C
from style import apply_style, nav

st.set_page_config(page_title="Relevance index", layout="centered", initial_sidebar_state="collapsed")
apply_style()
nav()

st.markdown('<div class="chap">Relevance index</div><div class="dtitle">Do the two sources agree?</div>'
            '<p class="dshort">For each brand, Google Trends and Wikipedia are put on the same scale (2019 average = 100). '
            'The Wikipedia line divides the brand\'s views by two unrelated articles, Coffee and Bicycle, to remove '
            'site-wide changes. The shaded band is the gap between the two sources, and a wide band means they disagree.</p>',
            unsafe_allow_html=True)

LABELS = {"Hermes": "Hermès", "Gucci": "Gucci", "Louis Vuitton": "Louis Vuitton"}
brand = st.radio("Brand", list(LABELS), format_func=LABELS.get, horizontal=True, label_visibility="collapsed")

try:
    fig, d = C.band_chart(brand)
except FileNotFoundError as e:
    st.markdown(f'<span class="care">This page needs {e.filename}. Run notebook 13, then refresh.</span>',
                unsafe_allow_html=True)
    st.stop()

st.markdown('<div class="ptitle">Index by month</div>', unsafe_allow_html=True)
st.plotly_chart(fig, config={"displayModeBar": False})

year = d["month"].dt.year.max()
sub = d[d["month"].dt.year == year]
r = d["trends"].corr(d["wiki_rel"])
if r > 0.5:
    agree = "The two sources broadly move together."
elif r < -0.3:
    agree = "The two sources move in opposite directions, so their average says little."
else:
    agree = "The two sources show no clear relationship."
st.markdown(
    f'<div class="pc">{year} so far: Google Trends {sub["trends"].mean():.0f}, Wikipedia vs controls '
    f'{sub["wiki_rel"].mean():.0f}, average of the two {sub["midpoint"].mean():.0f}. '
    f'Correlation of the two: {r:.2f}. {agree}<br>Using Coffee alone as the control gives '
    f'{sub["wiki_rel_coffee"].mean():.0f}, and Bicycle alone gives {sub["wiki_rel_bicycle"].mean():.0f}.</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="ptitle">Category composite: the four luxury search terms together</div>', unsafe_allow_html=True)
try:
    st.plotly_chart(C.composite_chart(), config={"displayModeBar": False})
except FileNotFoundError as e:
    st.markdown(f'<span class="care">This chart needs {e.filename}. Run notebook 13, then refresh.</span>',
                unsafe_allow_html=True)
st.markdown(
    '<div class="pc">The average z-score of the four terms, smoothed over 12 months. It rises mostly after 2025 and '
    'inherits the shared August 2025 break and the early-2026 surge from a single Google Trends pull, so it should '
    'not be read as a lasting rise in relevance.</div>'
    '<div class="sec">What it cannot tell us</div>'
    '<span class="care">This is an experimental measure of attention, not of sales. It depends on two unrelated '
    'control articles being a fair gauge of site-wide change, and no significance tests are attached.</span>',
    unsafe_allow_html=True,
)
