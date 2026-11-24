#!/usr/bin/env python3
"""Generate the five Good (好) placeholder pages for ai-china.xyz.

Each page is a standalone HTML file (skip_render in Hexo) with a UI built
around its five-element theme: gold/metal, wood, water, fire, earth.
Output: <out>/source/good-<slug>/index.html
"""
import os

OUT = os.path.expanduser("~/workspace/ai-china-good-pages")

SHARED_CSS = """
@import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/style.css');
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: #fdf8ef; color: #2b2118; font-family: Georgia, 'Times New Roman', serif; }
.han { font-family: 'LXGW WenKai', 'Songti SC', 'Noto Serif SC', serif; }
a { color: var(--deep); }
.topbar { max-width: 860px; margin: 0 auto; padding: 20px 22px 0; display: flex; justify-content: space-between; align-items: baseline; font-size: 14px; }
.topbar a.home { text-decoration: none; color: #2b2118; }
.topbar a.home:hover { color: var(--deep); }
.topbar a.home .han { font-size: 1.25em; color: var(--accent); }
.topbar .site { color: #8a7a6a; letter-spacing: .08em; font-size: 12px; text-transform: uppercase; }
main { max-width: 860px; margin: 0 auto; padding: 6px 22px 40px; }
.hero { text-align: center; padding: 30px 0 6px; }
.hao-wrap { position: relative; display: inline-block; }
.hao { font-size: 120px; line-height: 1.1; }
h1 { font-size: 34px; margin-top: 12px; font-weight: 400; }
h1 .en { display: block; font-size: 14px; letter-spacing: .22em; text-transform: uppercase; color: #8a7a6a; margin-top: 8px; }
.badge { display: inline-block; margin-top: 16px; padding: 5px 14px; border: 1.5px solid var(--accent); border-radius: 999px; color: var(--deep); font-size: 13px; letter-spacing: .12em; background: #fffdf9; }
.intro { max-width: 580px; margin: 18px auto 0; font-size: 17px; line-height: 1.65; color: #4a3f33; }
.motif { margin: 28px auto 0; }
.grid { margin-top: 40px; }
.grid h2 { font-size: 13px; letter-spacing: .22em; text-transform: uppercase; color: #8a7a6a; text-align: center; font-weight: 400; }
.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 18px; }
.card { border: 1.5px dashed var(--accent); border-radius: 14px; background: #fffdf9; padding: 22px 18px; min-height: 150px; }
.card.live { border-style: solid; border-color: var(--accent); }
.card .tag { font-size: 12px; letter-spacing: .18em; text-transform: uppercase; color: var(--deep); }
.card p { margin-top: 10px; font-size: 15px; line-height: 1.6; color: #6b5d4f; }
.card a { text-decoration: none; }
.card a:hover p { color: var(--deep); }
footer { max-width: 860px; margin: 0 auto; padding: 0 22px 30px; text-align: center; font-size: 13px; color: #8a7a6a; line-height: 1.8; }
footer a { color: #8a7a6a; }
@media (max-width: 640px) {
  .hao { font-size: 84px; }
  h1 { font-size: 26px; }
  .intro { font-size: 16px; }
  .cards { grid-template-columns: 1fr; }
  .card { min-height: 0; }
}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{zh} · {en} — ai-china.xyz</title>
<style>
:root {{ --accent: {accent}; --deep: {deep}; --soft: {soft}; }}
{shared}
{motif_css}
</style>
</head>
<body>
  <div class="topbar">
    <a class="home" href="/">&larr; <span class="han">好</span> · Home</a>
    <span class="site">ai-china.xyz</span>
  </div>
  <main>
    <section class="hero">
      <div class="hao-wrap">
        <div class="hao han">{hao}</div>
        {hao_extra}
      </div>
      <h1><span class="han">{zh}</span><span class="en">{en}</span></h1>
      <div class="badge">{el_zh} &middot; {el_en}</div>
      <p class="intro">{intro}</p>
    </section>
    <div class="motif">{motif}</div>
    <section class="grid">
      <h2>{grid_title}</h2>
      <div class="cards">
{cards}
      </div>
    </section>
  </main>
  <footer>
    <a href="/">ai-china.xyz</a> &mdash; Every good, a feeling.<br>
    <span class="han">世间万般好，皆留一段情。</span>
  </footer>
</body>
</html>
"""

PLACEHOLDER_CARD = """        <div class="card">
          <div class="tag">&#10022; Coming soon</div>
          <p>{text}</p>
        </div>"""

LIVE_CARD = """        <div class="card live">
          <div class="tag">&#10022; Already live</div>
          <a href="/blog/"><p><b>The General Under the Big Tree</b> &mdash; the story of Feng Yi, the general who lost the east and gained the west. Read it on the blog &rarr;</p></a>
        </div>"""

PAGES = [
    dict(
        slug="good-people", zh="好人物", en="Good People",
        el_zh="金", el_en="Metal",
        accent="#c9a227", deep="#8a6d1a", soft="#f9efc9",
        intro="People who made China what it is &mdash; generals and poets, thinkers and makers, and the ones history almost forgot. Each one gets a story.",
        hao="好",
        hao_extra='<span class="spark s1">&#10022;</span><span class="spark s2">&#10022;</span>',
        motif_css="""
/* gold: brushed-gold 好 with two twinkling gold-dust sparkles */
.hao { background: linear-gradient(135deg, #f7e08a 0%, #c9a227 45%, #8a6d1a 70%, #e9c766 100%); -webkit-background-clip: text; background-clip: text; color: transparent; }
.spark { position: absolute; color: #f7e08a; text-shadow: 0 0 6px #f5c542; animation: twinkle 2s ease-in-out infinite; }
.spark.s1 { top: 6px; right: -14px; font-size: 22px; }
.spark.s2 { bottom: 14px; left: -16px; font-size: 16px; animation-delay: -1s; }
@keyframes twinkle { 0%,100% { opacity: .35; transform: scale(.8); } 50% { opacity: 1; transform: scale(1.15); } }
.motif .gold-line { height: 3px; max-width: 420px; margin: 0 auto; border-radius: 99px; background: linear-gradient(90deg, transparent, #c9a227, #f7e08a, #c9a227, transparent); }
""",
        motif='<div class="gold-line"></div>',
        grid_title="Stories coming soon",
        cards=[
            "The first story in this series is on its way.",
            "A new person, a new story &mdash; this page grows one story at a time.",
            "More to come. Check back soon.",
        ],
    ),
    dict(
        slug="good-places", zh="好地方", en="Good Places",
        el_zh="木", el_en="Wood",
        accent="#4e7a51", deep="#2f5233", soft="#e2ecdc",
        intro="Places with a story &mdash; mountains and rivers, old streets and quiet towns. The land remembers what people forget.",
        hao="好",
        hao_extra='<svg class="sprout" viewBox="0 0 40 44" aria-hidden="true"><path d="M20 42 C20 30 20 22 20 14" stroke="#4e7a51" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M20 22 C12 20 8 14 8 8 C14 8 19 12 20 18" fill="#6a9a6d"/><path d="M20 18 C28 16 32 10 32 4 C26 4 21 8 20 14" fill="#4e7a51"/></svg>',
        motif_css="""
/* wood: green 好 with a little sprout swaying on top */
.hao { color: #4e7a51; }
.sprout { position: absolute; top: -26px; left: 50%; margin-left: -20px; width: 40px; height: 44px; transform-origin: 50% 100%; animation: sway 3.2s ease-in-out infinite; }
@keyframes sway { 0%,100% { transform: rotate(-4deg); } 50% { transform: rotate(4deg); } }
.motif .leaf-row { display: flex; justify-content: center; gap: 10px; color: #4e7a51; font-size: 18px; }
""",
        motif='<div class="leaf-row"><span>&#10087;</span><span>&#10087;</span><span>&#10087;</span></div>',
        grid_title="Stories coming soon",
        cards=[
            "The first story in this series is on its way.",
            "A new place, a new story &mdash; this page grows one story at a time.",
            "More to come. Check back soon.",
        ],
    ),
    dict(
        slug="good-things", zh="好东西", en="Good Things",
        el_zh="水", el_en="Water",
        accent="#2f6f8f", deep="#1e4a63", soft="#d9e9f1",
        intro="Things worth knowing &mdash; objects, inventions, food, and everyday wonders. Small things, big stories.",
        hao="好",
        hao_extra="",
        motif_css="""
/* water: flowing blue gradient on 好, plus a scrolling wave band */
.hao { background: linear-gradient(90deg, #2f6f8f, #5aa3c4, #2f6f8f); background-size: 200% 100%; -webkit-background-clip: text; background-clip: text; color: transparent; animation: flow 6s linear infinite; }
@keyframes flow { 0% { background-position: 0% 0; } 100% { background-position: 200% 0; } }
.waves { overflow: hidden; max-width: 560px; margin: 0 auto; }
.waves .track { display: flex; width: 200%; animation: scroll 7s linear infinite; }
.waves svg { width: 50%; flex: none; display: block; }
@keyframes scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
""",
        motif='''<div class="waves"><div class="track"><svg viewBox="0 0 560 34" preserveAspectRatio="none" aria-hidden="true"><path d="M0 18 Q35 4 70 18 T140 18 T210 18 T280 18 T350 18 T420 18 T490 18 T560 18 V34 H0 Z" fill="#2f6f8f" opacity=".55"/></svg><svg viewBox="0 0 560 34" preserveAspectRatio="none" aria-hidden="true"><path d="M0 18 Q35 4 70 18 T140 18 T210 18 T280 18 T350 18 T420 18 T490 18 T560 18 V34 H0 Z" fill="#2f6f8f" opacity=".55"/></svg></div></div>''',
        grid_title="Stories coming soon",
        cards=[
            "The first story in this series is on its way.",
            "A new thing, a new story &mdash; this page grows one story at a time.",
            "More to come. Check back soon.",
        ],
    ),
    dict(
        slug="good-tools", zh="好工具", en="Good Tools",
        el_zh="火", el_en="Fire",
        accent="#c0392b", deep="#8e2a1f", soft="#f7ddd6",
        intro="Tools that changed the game &mdash; from ancient inventions to the apps and ideas people reach for today.",
        hao="好",
        hao_extra="",
        motif_css="""
/* fire: cinnabar-red 好 with a warm glow, over a warm ember band */
.hao { color: #c0392b; text-shadow: 0 0 22px rgba(192, 57, 43, .35); }
.motif .ember { height: 4px; max-width: 420px; margin: 0 auto; border-radius: 99px; background: linear-gradient(90deg, transparent, #e07a3f, #c0392b, #e07a3f, transparent); }
""",
        motif='<div class="ember"></div>',
        grid_title="Stories coming soon",
        cards=[
            "The first story in this series is on its way.",
            "A new tool, a new story &mdash; this page grows one story at a time.",
            "More to come. Check back soon.",
        ],
    ),
    dict(
        slug="good-stories", zh="好故事", en="Good Stories",
        el_zh="土", el_en="Earth",
        accent="#9e6b2a", deep="#6f4a1a", soft="#f3e8d2",
        intro="Every good thing has a good story. This is where they gather &mdash; the people, the places, the things, and the tools, told one story at a time.",
        hao="好",
        hao_extra="",
        motif_css="""
/* earth: warm ochre 好 with a terracotta glow, under a little knot pendant */
.hao { background: linear-gradient(160deg, #f2c14e 0%, #c08a2d 55%, #9e6b2a 100%); -webkit-background-clip: text; background-clip: text; color: transparent; }
.knot { display: flex; flex-direction: column; align-items: center; gap: 0; }
.knot .disc { width: 74px; height: 74px; border-radius: 50%; background: #f2c14e; color: #8a2f24; display: flex; align-items: center; justify-content: center; font-size: 34px; box-shadow: 0 0 0 3px #fdf8ef, 0 0 0 4.5px #c08a2d; }
.knot .tassel { width: 2px; height: 26px; background: #c0392b; position: relative; }
.knot .tassel::after { content: ''; position: absolute; left: -5px; right: -5px; bottom: -14px; height: 16px; background: repeating-linear-gradient(90deg, #c0392b 0 2px, transparent 2px 4px); }
""",
        motif='<div class="knot"><div class="disc han">好</div><div class="tassel"></div></div>',
        grid_title="Stories",
        cards=None,  # first card is the live Feng Yi story, then placeholders
    ),
]


def build():
    for p in PAGES:
        if p["cards"] is None:
            cards_html = "\n".join([
                LIVE_CARD,
                PLACEHOLDER_CARD.format(text="A new story will appear here."),
                PLACEHOLDER_CARD.format(text="More to come &mdash; this page grows one story at a time."),
            ])
        else:
            cards_html = "\n".join(
                PLACEHOLDER_CARD.format(text=t) for t in p["cards"]
            )
        html = TEMPLATE.format(
            zh=p["zh"], en=p["en"], el_zh=p["el_zh"], el_en=p["el_en"],
            accent=p["accent"], deep=p["deep"], soft=p["soft"],
            shared=SHARED_CSS.strip(), motif_css=p["motif_css"].strip(),
            hao=p["hao"], hao_extra=p["hao_extra"],
            intro=p["intro"], motif=p["motif"],
            grid_title=p["grid_title"], cards=cards_html,
        )
        d = os.path.join(OUT, "source", p["slug"])
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "index.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", path, len(html), "bytes")


if __name__ == "__main__":
    build()
