# readme-folded-letters

這個 repo 是〈README：一封寫給人工智慧的家書〉的**信的裝置**：把信切成 token、每個 token 標上 ID，印在 A4 上、摺成 Z 字三折，讓觀眾帶走。信拆成四個片段，所以有四種樣式。目前**第一封已定稿**，其他三封還沒排。

- 作品本體（信與 skill）：[wufangci/README](https://github.com/wufangci/README)
- token 動畫：[wufangci/readme-token-animation](https://github.com/wufangci/readme-token-animation)
- 錄像：[wufangci/readme-video](https://github.com/wufangci/readme-video)
- 展覽規劃：[wufangci/readme-exhibition](https://github.com/wufangci/readme-exhibition)

## 從這裡開始

| 檔案 | 用途 |
|---|---|
| [`00_PRODUCTION_BOARD.md`](00_PRODUCTION_BOARD.md) | 製作總表：四封信的狀態、版本、下一步 |
| [`SESSION_HANDOFF.md`](SESSION_HANDOFF.md) | 交接：上次做到哪、下次從哪開始 |
| [`AGENTS.md`](AGENTS.md) | 給 AI 的常用記憶：規則、偏好、工作習慣 |

## 資料夾

| 資料夾 | 內容 |
|---|---|
| `01_source/` | 規格：分詞、紙張、摺法、正反面版面 |
| `03_assets/` | 素材：QR code |
| `04_active/` | 主線：目前定稿的版本（09，Z 字三折） |
| `05_tools/` | 工具：切 token |
| `06_process/` | 創作歷程：決策紀錄、每次工作摘要 |
| `90_archive/` | 封存：沒有採用的摺法（信紙三折、對開門摺） |
| `out/` | 輸出（不進 git） |

## 重新產生

需要 Node 18 以上、Python 3、Playwright（Chromium）、Pillow，以及思源字型（Noto Serif CJK TC、Noto Sans Mono CJK TC）。信的原文在 [wufangci/README](https://github.com/wufangci/README) 的 `LETTER.md`。

```bash
npm ci
pip install playwright pillow && playwright install chromium

node 05_tools/tokenize_letter.js ../README/LETTER.md out/letter_parts.json
python3 04_active/09-zfold-three-panels/build.py 1     # → out/README_letter_01_z.pdf
```

## 列印與摺法

A4 雙面列印（長邊翻頁），白底。token 面朝上，上三分之一往前摺、下三分之一往後摺。摺好是 210 × 99 mm。示意圖見 [`04_active/09-zfold-three-panels/stills/fold.png`](04_active/09-zfold-three-panels/stills/fold.png)。

## 授權

信的文字與影像屬於作者吳方娸 ljaljuy tjavelengan，保留一切權利。若要使用，請先聯繫作者。
