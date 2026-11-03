import streamlit as st

PAGES = [("Scorecard", "/"), ("Relevance index", "/Relevance_index"), ("Methods log", "/Methods"), ("Sources and limits", "/Sources")]

CSS = """
<style>
.block-container, [data-testid="stMainBlockContainer"] { max-width: 880px; padding-top: 2.2rem; }
#MainMenu, footer { visibility: hidden; }
.hero-title, .dtitle, .ct, .q, .fn, .ptitle, .note p { font-family: Georgia, 'Times New Roman', serif; font-weight: 400; }
.foil { background: linear-gradient(135deg,#8F7440 0%,#E9D197 42%,#B8995F 68%,#F2E2B0 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; color: #B8995F; }
.bar { position: relative; border-radius: 6px; padding: 24px 32px; min-height: 76px; background: linear-gradient(145deg,#6A4630,#3A2417); display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 8px; box-shadow: 0 6px 16px rgba(58,36,23,.25); }
.bar::after { content: ""; position: absolute; inset: 7px; border: 1.5px dashed rgba(230,211,176,.55); border-radius: 3px; pointer-events: none; }
.bar .mark { font-size: 11px; letter-spacing: .3em; text-transform: uppercase; color: #E9D197; }
.bar a { color: #E6D3B0 !important; font-size: 11px; letter-spacing: .22em; text-transform: uppercase; text-decoration: none !important; margin-left: 18px; border-bottom: 1px solid transparent; padding: 4px 0; }
.bar a:hover { border-bottom-color: #E9D197; color: #F6EBD6 !important; }
.leather { position: relative; border-radius: 6px; padding: 40px 36px 38px; margin-top: 16px; background: linear-gradient(145deg,#6A4630 0%,#4A2F1F 55%,#3A2417 100%); box-shadow: 0 10px 24px rgba(58,36,23,.28), inset 0 1px 0 rgba(255,255,255,.10); }
.leather::after { content: ""; position: absolute; inset: 10px; border: 1.5px dashed rgba(230,211,176,.7); border-radius: 3px; pointer-events: none; }
.kick { font-size: 10px; letter-spacing: .3em; text-transform: uppercase; color: #D2B67E; }
.hero-title { font-size: 42px; line-height: 1.08; margin: 14px 0 0; color: #F6EBD6; text-shadow: 0 1px 0 rgba(255,255,255,.14), 0 -1px 0 rgba(0,0,0,.4); max-width: 500px; }
.hero-title em { font-style: italic; text-shadow: none; }
.lede { margin: 16px 0 0 !important; max-width: 460px; font-size: 13.5px; line-height: 1.7; color: #E6D3B0 !important; }
.chap { margin-top: 28px; font-size: 10px; letter-spacing: .3em; text-transform: uppercase; color: #8F7440; }
.ct { font-style: italic; font-size: 23px; margin: 6px 0 6px; }
.rack { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.hang { position: relative; padding: 32px 11px 8px; }
.hang::before { content: ""; position: absolute; left: 0; right: 0; top: 0; height: 6px; background: linear-gradient(180deg,#F0DDA8,#B8995F 48%,#8F7440); }
a.tag { position: relative; display: flex; flex-direction: column; text-align: center; text-decoration: none !important; color: inherit !important; background: #FBF8F1; border: 1px solid #DDD2BC; border-radius: 6px; padding: 32px 18px 16px; transform-origin: top center; transition: transform .4s ease, box-shadow .4s; box-shadow: 0 1px 0 #fff inset, 0 8px 16px rgba(60,40,20,.12); min-height: 210px; }
a.tag.r1 { transform: rotate(-.9deg); } a.tag.r2 { transform: rotate(.7deg); } a.tag.r3 { transform: rotate(.6deg); }
a.tag.r4 { transform: rotate(-.7deg); } a.tag.r5 { transform: rotate(-.5deg); } a.tag.r6 { transform: rotate(.9deg); }
a.tag:hover { transform: rotate(0deg) translateY(-3px); box-shadow: 0 1px 0 #fff inset, 0 12px 22px rgba(60,40,20,.18); }
a.tag::before { content: ""; position: absolute; left: 50%; top: -32px; width: 1.5px; height: 32px; background: #8F7440; transform: translateX(-50%); }
a.tag::after { content: ""; position: absolute; left: 50%; top: 10px; width: 11px; height: 11px; border-radius: 50%; background: #F6F1E6; box-shadow: inset 0 1px 2px rgba(0,0,0,.35), 0 0 0 2px #B8995F; transform: translateX(-50%); }
.no { font-size: 10px; letter-spacing: .28em; text-transform: uppercase; color: #8F7440; }
.q { font-size: 16.5px; line-height: 1.35; margin: 9px 0 7px; color: #1F1B17; }
.f { font-size: 12.5px; line-height: 1.5; color: #6B655B; flex: 1; }
.stamp { align-self: center; margin-top: 10px; padding: 4px 12px; border: 1.5px solid #7A2430; border-radius: 3px; color: #7A2430; font-size: 10px; letter-spacing: .2em; text-transform: uppercase; font-weight: 600; transform: rotate(-2deg); }
.stamp.inline { display: inline-block; margin: 0 0 12px; }
.more { margin-top: 8px; font-size: 11px; font-style: italic; color: #8F7440; }
.note { margin: 30px 0 4px; max-width: 580px; display: flex; gap: 18px; align-items: flex-start; }
.seal { flex: 0 0 54px; width: 54px; height: 54px; border-radius: 50%; background: radial-gradient(circle at 35% 30%,#A3374A 0%,#7A2430 55%,#4D1219 100%); box-shadow: 0 3px 8px rgba(77,18,25,.4), inset 0 0 0 4px rgba(77,18,25,.35), inset 0 0 0 5px rgba(255,255,255,.12); display: flex; align-items: center; justify-content: center; font-family: Georgia, serif; font-style: italic; font-size: 18px; color: #F2D9D2; }
.note p { font-style: italic; font-size: 17px; line-height: 1.6; margin: 0 0 6px; }
.sig { font-size: 10px; letter-spacing: .24em; text-transform: uppercase; color: #6B655B; }
.crumbs { margin: 22px 0 0; }
a.pn { color: #1F1B17 !important; border-bottom: 1px solid #1F1B17; text-decoration: none !important; margin-right: 22px; font-size: 13px; }
.dtitle { font-size: 28px; line-height: 1.2; margin: 8px 0 12px; max-width: 580px; }
.dshort { font-size: 14.5px; line-height: 1.7; max-width: 640px; margin: 0 0 6px; }
.figs { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; margin: 18px 0; }
.fig { background: #FBF8F1; border: 1px solid #DDD2BC; border-radius: 6px; padding: 14px; }
.fn { font-size: 21px; line-height: 1.15; }
.fl { font-size: 11.5px; line-height: 1.45; color: #6B655B; margin-top: 6px; }
.ptitle { border-top: 5px solid #B8995F; padding-top: 10px; font-size: 15px; margin: 18px 0 6px; }
.pc { font-size: 12px; line-height: 1.55; color: #6B655B; margin-top: 4px; }
.sec { margin: 22px 0 4px; font-size: 10px; letter-spacing: .26em; text-transform: uppercase; color: #8F7440; }
.txt { font-size: 13.5px; line-height: 1.65; max-width: 640px; }
.care { display: block; max-width: 640px; border: 1px dashed #BDB29C; background: #FBF8F1; padding: 10px 14px; font-size: 12.5px; line-height: 1.6; color: #4A443B; }
.foot { display: inline-block; margin-top: 26px; border: 1px dashed #BDB29C; background: #FBF8F1; padding: 10px 14px; font-size: 10px; letter-spacing: .16em; text-transform: uppercase; line-height: 1.8; color: #6B655B; }

[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stSidebar"], [data-testid="stExpandSidebarButton"], [data-testid="stSidebarCollapseButton"], [data-testid="stSidebarCollapsedControl"], [data-testid="collapsedControl"] { display: none !important; }
.flist { max-width: 680px; margin: 4px 0 0; padding-left: 22px; font-size: 13.5px; line-height: 1.65; }
.flist li { margin-bottom: 7px; }
.links { max-width: 680px; margin: 4px 0 0; padding-left: 18px; font-size: 13px; line-height: 1.6; }
.links li { margin-bottom: 5px; }
.links a, .txt a { color: #1F1B17 !important; border-bottom: 1px solid #B8995F; text-decoration: none !important; }
.lrow { display: flex; flex-wrap: wrap; gap: 10px 14px; align-items: flex-start; padding: 12px 6px; border-top: 1px solid #DDD2BC; font-size: 13px; line-height: 1.5; }
.lrow.lastrow { border-bottom: 1px solid #DDD2BC; }
.ln { flex: 0 0 40px; font-family: Georgia, serif; font-style: italic; color: #8F7440; font-size: 16px; }
.lw { flex: 1 1 200px; min-width: 0; }
.lf { flex: 1 1 230px; min-width: 0; color: #6B655B; }
.st { flex: 0 0 auto; padding: 3px 10px; border-radius: 3px; font-size: 10px; letter-spacing: .16em; text-transform: uppercase; font-weight: 600; white-space: nowrap; }
.st.done { border: 1.5px solid #8F7440; color: #6B5320; }
.st.skip { border: 1.5px dashed #8C8473; color: #5B554B; }
.st.drop { border: 1.5px solid #7A2430; color: #7A2430; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; }
.chip { border: 1px solid #BDB29C; border-radius: 3px; padding: 4px 10px; font-size: 11px; letter-spacing: .06em; background: #FBF8F1; }
.stbl { width: 100%; max-width: 680px; border-collapse: collapse; font-size: 13px; line-height: 1.5; margin-top: 6px; }
.stbl td { padding: 9px 8px; border-top: 1px solid #DDD2BC; vertical-align: top; }
.stbl tr:last-child td { border-bottom: 1px solid #DDD2BC; }
.stbl td:first-child { font-family: Georgia, serif; width: 46%; }
.stbl td:last-child { color: #6B655B; }
</style>
"""


def apply_style():
    st.markdown(CSS, unsafe_allow_html=True)


def nav():
    links = "".join(f'<a href="{href}" target="_self">{name}</a>' for name, href in PAGES)
    st.markdown(
        f'<div class="bar"><span class="mark">Luxury Relevance Index</span><span>{links}</span></div>',
        unsafe_allow_html=True,
    )
