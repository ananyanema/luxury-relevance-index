import streamlit as st

from content import QUESTIONS
from style import apply_style, nav

st.set_page_config(page_title="Luxury Relevance Index", layout="centered", initial_sidebar_state="collapsed")
apply_style()
nav()

st.markdown(
    '<div class="leather"><div class="kick">An independent study &nbsp;·&nbsp; Updated November 2026</div>'
    '<div class="hero-title">How <em class="foil">relevant</em> is luxury today?</div>'
    '<p class="lede">And is what people value in it changing? Six questions, tested on open public data, '
    'with the answers written down honestly, including the ones that did not hold up.</p></div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="chap">Chapter I</div><div class="ct">Six questions, six honest answers</div>',
            unsafe_allow_html=True)

tags = "".join(
    f'<div class="hang"><a class="tag r{q["n"]}" href="/Question?q={q["n"]}" target="_self">'
    f'<span class="no">No. 0{q["n"]}</span><span class="q">{q["title"]}</span>'
    f'<span class="f">{q["finding"]}</span><span class="stamp">{q["verdict"]}</span>'
    f'<span class="more">Read the evidence</span></a></div>'
    for q in QUESTIONS
)
st.markdown(f'<div class="rack">{tags}</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="note"><div class="seal">AN</div><div><p>I wanted to know whether luxury still matters the '
    'way it used to, and whether what people prize in it is changing. I followed public attention, tested my '
    'own assumptions, and wrote down what did not hold up.</p>'
    '<div class="sig">Ananya Nema &nbsp;·&nbsp; B.Tech, Data Science</div></div></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="foot">Data sources: Google Trends &nbsp;·&nbsp; Wikimedia Pageviews API (CC0)<br>'
    'Independent student project &nbsp;·&nbsp; Not affiliated with any brand</div>',
    unsafe_allow_html=True,
)
