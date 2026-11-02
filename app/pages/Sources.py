import streamlit as st

from content import LIMITS, NOT_USED, SOURCE_GROUPS
from style import apply_style, nav

st.set_page_config(page_title="Sources and limits", layout="centered", initial_sidebar_state="collapsed")
apply_style()
nav()

st.markdown('<div class="chap">Sources and limits</div><div class="ct">What this rests on, and what it cannot say</div>',
            unsafe_allow_html=True)
for title, items in SOURCE_GROUPS:
    lis = "".join(f'<li><a href="{u}" target="_blank">{t}</a></li>' for t, u in items)
    st.markdown(f'<div class="sec">{title}</div><ul class="links">{lis}</ul>', unsafe_allow_html=True)
st.markdown(
    f'<div class="sec">Considered and not used</div><div class="txt">{NOT_USED}</div>'
    f'<div class="sec">Limits</div><span class="care">{LIMITS}</span>'
    '<div class="foot">Independent student project &nbsp;·&nbsp; Not affiliated with any brand<br>'
    'Published reports are paraphrased, with links to the originals</div>',
    unsafe_allow_html=True,
)
