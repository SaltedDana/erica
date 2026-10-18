#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Regenerate the README images and badges in assets/.

Writes assets/badges/*.svg directly and renders assets/*.png from small HTML
templates with headless Chrome.
Usage: python3 scripts/build_assets.py   (from anywhere)
Requires: Google Chrome (set CHROME to override the path).
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
BADGES = ASSETS / "badges"
FONT = ROOT / "docs" / "assets" / "fonts" / "Virgil.woff2"
CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)

INK, INK_SOFT, CREAM, PAPER = "#1F2328", "#4A4A4D", "#FBF8F1", "#F5F9FC"
LAV, SAGE, SLATE, ORANGE, SAGE_TEXT = "#CDACFE", "#D1DDD4", "#7BA3AD", "#FC7142", "#6C8F8A"

STRUCTURES = 4
BEATS = 9
RUBRIC = 20

HEAD = f"""<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
@font-face{{font-family:'Virgil';src:url('file://{FONT}') format('woff2')}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Space Grotesk',system-ui,sans-serif;color:{INK}}}
.mono{{font-family:'IBM Plex Mono',ui-monospace,monospace}}
</style>"""


def badge(name, label, value, color):
    """Two-tone label/value badge, same layout as the Personal AGI Standard badges."""
    lw = round(len(label) * 6.3 + 16)
    vw = round(len(value) * 6.9 + 14)
    w = lw + vw
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="20" viewBox="0 0 {w} 20" '
        f'role="img" aria-label="{label}: {value}"><title>{label}: {value}</title>'
        f'<rect width="{lw}" height="20" rx="3" fill="{INK_SOFT}"/>'
        f'<rect x="{lw}" width="{vw}" height="20" rx="3" fill="{color}"/>'
        f'<rect x="{lw - 3}" width="3" height="20" fill="{INK_SOFT}"/>'
        f'<rect x="{lw}" width="3" height="20" fill="{color}"/>'
        f'<g font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">'
        f'<text x="8" y="14" fill="{PAPER}" textLength="{lw - 16}" lengthAdjust="spacingAndGlyphs">{label}</text>'
        f'<text x="{lw + 7}" y="14" fill="{INK}" textLength="{vw - 14}" lengthAdjust="spacingAndGlyphs">{value}</text>'
        f"</g></svg>\n"
    )


def write_badges():
    BADGES.mkdir(parents=True, exist_ok=True)
    items = [
        ("structures", "structures", str(STRUCTURES), LAV),
        ("beats", "beats", str(BEATS), SAGE),
        ("rubric", "rubric", f"{RUBRIC} points", SLATE),
        ("license", "license", "MIT", ORANGE),
    ]
    for fname, label, value, color in items:
        (BADGES / f"{fname}.svg").write_text(badge(fname, label, value, color))


def social_preview():
    stripe = "".join(
        f'<i style="flex:{f};background:{c}"></i>'
        for f, c in ((3, LAV), (3, SAGE), (2, SLATE), (2, ORANGE))
    )
    stats = "".join(
        f'<div><b>{n}</b><span>{t}</span></div>'
        for n, t in ((STRUCTURES, "structures"), (BEATS, "beats"), (RUBRIC, "point rubric"), (2, "modes"))
    )
    return f"""<html><head>{HEAD}<style>
body{{width:2560px;height:1280px;background:{CREAM};position:relative;border:6px solid {INK};border-radius:14px;overflow:hidden}}
.stripe{{display:flex;height:32px}} .stripe i{{display:block;height:100%}}
.t{{position:absolute;left:200px;top:300px;font-family:'Virgil',cursive;font-size:330px;line-height:1;white-space:nowrap}}
.s{{position:absolute;left:204px;top:700px;font-size:56px;line-height:1.35;color:{SAGE_TEXT};width:1500px}}
.stats{{position:absolute;left:204px;top:920px;display:flex;gap:150px}}
.stats b{{display:block;font-family:'Virgil',cursive;font-weight:400;font-size:100px;line-height:1}}
.stats span{{font-size:40px;color:{SAGE_TEXT}}}
.f{{position:absolute;left:204px;bottom:70px;font-family:'Virgil',cursive;font-size:38px;color:{SAGE_TEXT}}}
.r{{position:absolute;right:204px;bottom:70px;font-family:'Virgil',cursive;font-size:38px;color:{SAGE_TEXT}}}
</style></head><body>
<div class="stripe">{stripe}</div>
<div class="t">erica</div>
<div class="s">A Claude Code skill that coaches you to explain an idea so people listen.</div>
<div class="stats">{stats}</div>
<div class="f">Dana Maman · interpretation of Erica Mallett's public videos</div>
<div class="r">MIT</div>
</body></html>"""


def beats_figure():
    beats = [
        ("01", "Scene first", LAV), ("02", "Puzzle", LAV), ("03", "Name it", LAV),
        ("04", "Everywhere", SAGE), ("05", "Mechanism", SAGE), ("06", "Open loop", SAGE),
        ("07", "Steps", SLATE), ("08", "Chain formula", SLATE), ("09", "Hand back", ORANGE),
    ]
    cells = "".join(
        f'<div class="c"><div class="blk" style="background:{c}"></div>'
        f'<div class="n mono">{n}</div><div class="l">{t}</div></div>'
        for n, t, c in beats
    )
    return f"""<html><head>{HEAD}<style>
body{{width:1736px;height:420px;background:{PAPER};padding:56px}}
.row{{display:flex;gap:6px}}
.c{{flex:1}}
.blk{{height:116px;border:3px solid {INK_SOFT}}}
.n{{margin-top:14px;font-size:20px;color:{INK_SOFT}}}
.l{{font-weight:700;font-size:22px;color:{INK_SOFT};margin-top:2px}}
.rule{{border-top:3px solid {INK_SOFT};margin-top:34px}}
.cap{{margin-top:18px;font-size:20px;letter-spacing:.08em;text-transform:uppercase;color:{INK_SOFT}}}
</style></head><body>
<div class="row">{cells}</div>
<div class="rule"></div>
<div class="cap mono">Nine beats · inside any of four structures</div>
</body></html>"""


def structures_figure():
    cards = [
        ("Story-vehicle", "A behavior or effect in people", LAV),
        ("Myth-bust", "A belief that holds people back", SAGE),
        ("Playbook", "A skill the listener must run", SLATE),
        ("Case breakdown", "A person or company that won", ORANGE),
    ]
    html = "".join(
        f'<div class="card" style="border-top-color:{c}"><div class="mono id">0{i + 1}</div>'
        f'<div class="h">{t}</div><div class="mono u">{u}</div></div>'
        for i, (t, u, c) in enumerate(cards)
    )
    return f"""<html><head>{HEAD}<style>
body{{width:1736px;height:380px;background:{PAPER};padding:56px}}
.row{{display:flex;gap:20px}}
.card{{flex:1;background:#fff;border:3px solid {INK_SOFT};border-top-width:18px;padding:22px 24px;height:210px}}
.id{{font-size:20px;color:{INK_SOFT}}}
.h{{font-weight:700;font-size:34px;margin-top:10px;color:{INK_SOFT}}}
.u{{font-size:21px;margin-top:14px;color:{INK_SOFT};line-height:1.4}}
.rule{{border-top:3px solid {INK_SOFT};margin-top:30px}}
.cap{{margin-top:16px;font-size:20px;letter-spacing:.08em;text-transform:uppercase;color:{INK_SOFT}}}
</style></head><body>
<div class="row">{html}</div>
<div class="rule"></div>
<div class="cap mono">Four structures · pick one per piece, do not mix</div>
</body></html>"""


def rubric_figure():
    rows = [("17 to 20", 100, "ship", LAV), ("12 to 16", 70, "fix the two lowest beats", SAGE), ("under 12", 35, "restart from the structure", ORANGE)]
    out = "".join(
        f'<div class="r"><div class="b mono">{b}</div>'
        f'<div class="track"><div class="fill" style="width:{w}%;background:{c}"></div></div>'
        f'<div class="v mono">{v}</div></div>'
        for b, w, v, c in rows
    )
    return f"""<html><head>{HEAD}<style>
body{{width:1736px;height:420px;background:{PAPER};padding:56px}}
.r{{display:grid;grid-template-columns:200px 1fr 440px;gap:24px;align-items:center;margin-bottom:26px}}
.b{{font-size:24px;font-weight:500;color:{INK_SOFT}}}
.track{{height:48px;border:3px solid {INK_SOFT};background:repeating-linear-gradient(135deg,#fff 0 9px,{SAGE} 9px 12px)}}
.fill{{height:100%;border-right:3px solid {INK_SOFT}}}
.v{{font-size:22px;color:{INK_SOFT}}}
.rule{{border-top:3px solid {INK_SOFT};margin-top:6px}}
.cap{{margin-top:18px;font-size:20px;letter-spacing:.08em;text-transform:uppercase;color:{INK_SOFT}}}
</style></head><body>
{out}
<div class="rule"></div>
<div class="cap mono">Review rubric · ten checks scored 0, 1 or 2 · {RUBRIC} points total</div>
</body></html>"""


def example_figure():
    """README example: the same request run without and with context (counts from the saved raw outputs)."""
    plain = [('"A shared knowledge base fixes that"', 5), ("a person named Sarah, never mentioned", 3), ('"walks out the door"', 3), ("ends on a question", 4)]
    ctx = [('"A shared knowledge base fixes that"', 0), ("a person named Sarah, never mentioned", 1), ('"walks out the door"', 0), ("ends on a question", 0)]

    def rows(items, total, color):
        out = ""
        for label, n in items:
            out += (
                f'<div class="r"><div class="l">{label}</div>'
                f'<div class="track"><div class="fill" style="width:{100 * n / total}%;background:{color}"></div></div>'
                f'<div class="v mono">{n}/{total}</div></div>'
            )
        return out

    return f"""<html><head>{HEAD}<style>
body{{width:1736px;height:760px;background:{PAPER};padding:56px}}
.cap{{font-size:20px;letter-spacing:.08em;text-transform:uppercase;color:{INK_SOFT}}}
.cols{{display:flex;gap:32px;margin-top:22px}}
.col{{flex:1;background:#fff;border:3px solid {INK_SOFT};border-top-width:18px;padding:24px}}
.h{{font-weight:700;font-size:30px;color:{INK_SOFT}}}
.s{{font-size:19px;color:{INK_SOFT};margin:6px 0 20px}}
.r{{display:grid;grid-template-columns:340px 1fr 56px;gap:14px;align-items:center;margin:14px 0}}
.l{{font-size:21px;color:{INK_SOFT};line-height:1.25}}
.track{{height:34px;border:3px solid {INK_SOFT};background:repeating-linear-gradient(135deg,#fff 0 9px,{SAGE} 9px 12px)}}
.fill{{height:100%;border-right:3px solid {INK_SOFT}}}
.v{{font-size:22px;color:{INK_SOFT};text-align:right}}
.warn{{margin-top:26px;background:#fff;border:3px solid {INK_SOFT};border-top:18px solid {ORANGE};padding:18px 24px;font-size:26px;color:{INK_SOFT}}}
.warn b{{font-weight:700}}
.rule{{border-top:3px solid {INK_SOFT};margin-top:28px}}
</style></head><body>
<div class="cap mono">Example · the same request, run 8 times · claude-sonnet-5-5 · 2026-10-18 · one prompt, small sample</div>
<div class="cols">
  <div class="col" style="border-top-color:{LAV}"><div class="h">No context · 5 runs</div><div class="s mono">Write a LinkedIn post of about 90 words on why teams need a shared knowledge base.</div>{rows(plain, 5, LAV)}</div>
  <div class="col" style="border-top-color:{SAGE}"><div class="h">Three lines of own writing and two facts · 3 runs</div><div class="s mono">Same request, with a made-up consultant's voice sample added.</div>{rows(ctx, 3, SAGE)}</div>
</div>
<div class="warn"><b>Context changed the voice. It did not supply the truth.</b> The details in all three posts were invented: a departed accountant, a shared drive with 41 folders, a dormant client.</div>
<div class="rule"></div>
</body></html>"""


def render(name, html, w, h):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
        path = f.name
    try:
        subprocess.run(
            [
                CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                "--allow-file-access-from-files", "--force-device-scale-factor=1",
                f"--window-size={w},{h}", "--virtual-time-budget=8000",
                f"--screenshot={ASSETS / name}", f"file://{path}",
            ],
            check=True, capture_output=True,
        )
    finally:
        os.unlink(path)


def main():
    if not Path(CHROME).exists():
        sys.exit("Chrome not found. Set CHROME to the browser binary path.")
    ASSETS.mkdir(exist_ok=True)
    write_badges()
    render("social-preview.png", social_preview(), 2560, 1280)
    render("beats.png", beats_figure(), 1736, 420)
    render("structures.png", structures_figure(), 1736, 380)
    render("rubric.png", rubric_figure(), 1736, 420)
    render("example.png", example_figure(), 1736, 760)
    print("wrote assets/badges/*.svg and assets/*.png")


if __name__ == "__main__":
    main()
