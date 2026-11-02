import streamlit as st

from content import LOG
from style import apply_style, nav

st.set_page_config(page_title="Methods log", layout="centered", initial_sidebar_state="collapsed")
apply_style()
nav()

rows = "".join(
    f'<div class="lrow{" lastrow" if i == len(LOG) - 1 else ""}"><span class="ln">{a}</span>'
    f'<span class="lw">{b}</span><span class="lf">{c}</span><span class="st {d}">{e}</span></div>'
    for i, (a, b, c, d, e) in enumerate(LOG)
)
st.markdown(
    '<div class="chap">Methods log</div><div class="ct">Everything we ran, including what we dropped</div>'
    '<p class="dshort">Thirteen numbered steps plus the news-data attempt. Eleven were run as notebooks. Steps 09 and 11 were skipped or '
    'dropped before they were written, which is why those numbers have no notebook. Each row says what was found.</p>'
    f'{rows}',
    unsafe_allow_html=True,
)
