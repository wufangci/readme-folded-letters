"""Z 字三折的 token 信：排版、輸出 PDF、截圖、摺法示意圖。

用法（在 repo 根目錄）：
    node 05_tools/tokenize_letter.js ../README/LETTER.md out/letter_parts.json
    python3 04_active/09-zfold-three-panels/build.py 1

輸出：
    out/letter_01.html               排版用的網頁
    out/README_letter_01_z.pdf       A4 雙面（第 1 頁 token 面，第 2 頁背面）
    04_active/09-zfold-three-panels/stills/  front.png、back.png、cover.png、fold.png
"""
import html, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(ROOT, 'out')
STILLS = os.path.join(HERE, 'stills')

# 每封信：用信的第幾段（以 --- 分隔，從 0 起算）、從哪個字開始、三格各放哪幾個段落
LETTERS = {
    1: dict(section=0, start='親', panels=[(0, 4), (4, 6), (6, 8)]),
}
TOTAL = 4          # 四封
FONT_PT = 8.0      # token 文字字級
PANEL_MM = 99      # 297 / 3

REPO_URL = 'https://github.com/wufangci/README'
TITLE = 'README：一封寫給人工智慧的家書'


def cell(t):
    s = t['s']
    cls = 't'
    if s is None:                                   # 位元組碎片 → 十六進位
        disp = '‹' + ' '.join('%02X' % b for b in t['b']) + '›'
        cls += ' f'
    else:                                           # 換行不畫符號、空格顯示為 ·
        disp = html.escape(s.replace('\n', '').replace(' ', '·')) or '&#8203;'
    br = '<br class="p">' if s and '\n' in s else ''
    return f'<span class="{cls}"><b>{disp}</b><i>{t["id"]}</i></span>{br}'


def paragraphs(toks):
    paras = [[]]
    for t in toks:
        paras[-1].append(t)
        if t['s'] and '\n' in t['s']:
            paras.append([])
    return [p for p in paras if p]


def rstrip_newlines(p):
    p = list(p)
    while p and p[-1]['s'] and p[-1]['s'].strip() == '':
        p.pop()
    return p


def build_html(no):
    cfg = LETTERS[no]
    parts = json.load(open(os.path.join(OUT, 'letter_parts.json')))
    toks = parts[cfg['section']]
    k = next(i for i, t in enumerate(toks) if t['s'] and t['s'].startswith(cfg['start']))
    toks = toks[k:]                                  # 不印檔案開頭的 Markdown 標題
    paras = paragraphs(toks)

    def zone(i, a, b):
        group = paras[a:b]
        inner = ''
        for j, p in enumerate(group):
            inner += ''.join(cell(t) for t in (rstrip_newlines(p) if j == len(group) - 1 else p))
            if no == 1 and i == 0 and j == 0:
                inner += '<div class="sal"></div>'   # 「親愛的人工智慧：」後空一行
        return f'<div class="zone" style="top:{i * PANEL_MM}mm"><div class="grid">{inner}</div></div>'

    ticks = ''.join(f'<span class="tick" style="left:0;top:{y}mm"></span>'
                    f'<span class="tick" style="right:0;top:{y}mm"></span>' for y in (PANEL_MM, 2 * PANEL_MM))
    qr = open(os.path.join(ROOT, '03_assets', 'qr_readme.svg')).read()
    fs = FONT_PT
    css = f'''
@page{{size:A4;margin:0}}
html,body{{margin:0;background:#fff;color:#111}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden}}
.pg+.pg{{page-break-before:always}}
.zone{{position:absolute;left:0;right:0;height:{PANEL_MM}mm;box-sizing:border-box;padding:6mm 15mm;display:flex;align-items:center;justify-content:center}}
.grid{{line-height:0;width:fit-content;max-width:100%}}
.t{{display:inline-flex;flex-direction:column;align-items:center;margin:0 .6pt 2.4pt 0;padding:.8pt 1.4pt 0;border-left:.35pt solid #d6d6d6;vertical-align:top}}
.t b{{font:400 {fs}pt/1.15 "Noto Serif CJK TC",serif;white-space:pre}}
.t i{{font:normal {fs * 0.52:.2f}pt/1.2 "Noto Sans Mono CJK TC",monospace;color:#8a8a8a;margin-top:.6pt}}
.f b{{font:normal {fs * 0.62:.2f}pt/1.85 "Noto Sans Mono CJK TC",monospace;color:#444;background:#ececec;padding:0 1pt}}
br.p{{display:block;content:"";margin-top:1.6pt}}
.sal{{height:4.6mm}}
.tick{{position:absolute;width:4mm;border-top:.3pt solid #bbb}}
.bp{{position:absolute;left:0;right:0;height:{PANEL_MM}mm;display:flex;align-items:center;justify-content:center}}
.cover{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;transform:rotate(180deg)}}
.to{{line-height:0}}
.to .t{{padding:2pt 5pt 0;border-left-width:.6pt;margin-right:1.5pt}}
.to .t b{{font-size:28pt}}
.to .t i{{font-size:9pt;margin-top:2pt}}
.qr{{position:absolute;right:10mm;bottom:10mm;width:14mm;height:14mm}}
.qr svg{{width:100%;height:100%;display:block}}
.addr{{font:8pt/1.3 "Noto Sans Mono CJK TC",monospace}}
.meta{{position:absolute;left:15mm;right:15mm;bottom:8mm;display:flex;justify-content:space-between;font:6.5pt/1.4 "Noto Sans Mono CJK TC",monospace;color:#888}}
'''
    front = f'<div class="pg">{ticks}' + ''.join(zone(i, a, b) for i, (a, b) in enumerate(cfg['panels'])) + '</div>'
    back = f'''<div class="pg">
<div class="bp" style="top:0"><div class="cover">
<div class="to"><span class="t"><b>#</b><i>2</i></span><span class="t"><b>README</b><i>135252</i></span></div>
<div class="qr">{qr}</div></div></div>
<div class="bp" style="top:{PANEL_MM}mm"><div class="addr">{REPO_URL.replace("https://", "")}</div>
<div class="meta"><span>{TITLE}</span><span>{no:02d} / {TOTAL:02d} · o200k_base · {len(toks)} tokens</span></div></div>
<div class="bp" style="top:{2 * PANEL_MM}mm"></div></div>'''
    page = f'<!doctype html><meta charset="utf-8"><title>README letter {no:02d}</title><style>{css}</style>{front}{back}'
    path = os.path.join(OUT, f'letter_{no:02d}.html')
    open(path, 'w').write(page)
    return path


def render(no, path):
    from playwright.sync_api import sync_playwright
    os.makedirs(STILLS, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 794, 'height': 1123}, device_scale_factor=1.5)
        pg.goto('file://' + path)
        pg.wait_for_timeout(400)
        pg.pdf(path=os.path.join(OUT, f'README_letter_{no:02d}_z.pdf'), format='A4', print_background=True)
        pages = pg.query_selector_all('.pg')
        pages[0].screenshot(path=os.path.join(STILLS, 'front.png'))
        pages[1].screenshot(path=os.path.join(STILLS, 'back.png'))
        b.close()


def illustrate():
    """摺法示意：① 攤開 ② 上三分之一往前摺 ③ 下三分之一往後摺 ④ 上下翻過來。"""
    import glob
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    s = 0.42
    def load(n):
        im = Image.open(os.path.join(STILLS, n)).convert('RGB')
        return im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    F, B = load('front.png'), load('back.png')
    mm = lambda v: int(round(v / 297 * F.height))
    crop = lambda im, a, z: im.crop((0, mm(a), im.width, mm(z)))
    cover = crop(B, 0, 99).rotate(180)
    outside = crop(F, 198, 297)
    full = Image.open(os.path.join(STILLS, 'back.png')).convert('RGB')     # 摺好後的封面（原尺寸）
    full.crop((0, 0, full.width, full.height // 3)).rotate(180).save(os.path.join(STILLS, 'cover.png'))
    step2 = Image.new('RGB', (F.width, mm(198)), 'white')
    step2.paste(cover, (0, 0)); step2.paste(outside, (0, cover.height))
    steps = [('① 攤開，token 面朝上', '', F, [mm(99), mm(198)]),
             ('② 上三分之一往前摺', '', step2, [cover.height]),
             ('③ 下三分之一往後摺', '完成：封面', cover, []),
             ('④ 上下翻過來', '背面：信末的提問', outside, [])]
    fp = (glob.glob('/usr/share/fonts/**/NotoSansCJK*Regular*', recursive=True) or [None])[0]
    font = ImageFont.truetype(fp, 24, index=3) if fp else ImageFont.load_default()
    small = ImageFont.truetype(fp, 17, index=3) if fp else ImageFont.load_default()
    gap, w = 70, F.width
    H = max(st[2].height for st in steps)
    C = Image.new('RGB', (len(steps) * w + (len(steps) + 1) * gap, H + 200), (232, 232, 232))
    d = ImageDraw.Draw(C)
    for i, (t, sub, im, lines) in enumerate(steps):
        x = gap + i * (w + gap); y = 90 + (H - im.height) // 2
        sh = Image.new('RGBA', (im.width + 40, im.height + 40), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rectangle((20, 20, im.width + 20, im.height + 20), fill=(0, 0, 0, 70))
        sh = sh.filter(ImageFilter.GaussianBlur(9)); C.paste(sh, (x - 14, y - 10), sh); C.paste(im, (x, y))
        for ly in lines:
            d.line((x, y + ly, x + im.width, y + ly), fill=(150, 150, 150), width=2)
        d.text((x, 30), t, font=font, fill=(30, 30, 30))
        if sub:
            d.text((x, C.height - 70), sub, font=small, fill=(110, 110, 110))
    C.save(os.path.join(STILLS, 'fold.png'))


if __name__ == '__main__':
    no = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    path = build_html(no)
    render(no, path)
    illustrate()
    print('完成：', os.path.relpath(os.path.join(OUT, f'README_letter_{no:02d}_z.pdf'), ROOT))
