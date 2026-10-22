# 09 — Z 字三折，三格

信切成 token、標上 ID，印在 A4 雙面，摺成 Z 字三折。信照段落切成三塊，各自落在一格裡；最後那段粗體提問在下格，摺好後露在外面。

## 指令（在 repo 根目錄執行）

```bash
node 05_tools/tokenize_letter.js ../README/LETTER.md out/letter_parts.json
python3 04_active/09-zfold-three-panels/build.py 1     # 第幾封
```

輸出 `out/letter_01.html`、`out/README_letter_01_z.pdf`，並更新這個資料夾的 `stills/`。

每封信用哪一段、三格怎麼分，寫在 `build.py` 開頭的 `LETTERS`。目前只有第一封。

## 成品

`README_letter_01_z.pdf`（就在這個資料夾）：第 1 頁是 token 面，第 2 頁是背面。

## 截圖

| 檔案 | 內容 |
|---|---|
| `stills/front.png` | token 面 |
| `stills/back.png` | 背面（上格是轉了 180° 的封面） |
| `stills/cover.png` | 摺好後的封面 |
| `stills/fold.png` | 摺法示意：攤開 → 上三分之一往前摺 → 下三分之一往後摺 → 翻過來 |

規格見 [`01_source/SPECS.md`](../../01_source/SPECS.md)；過程與決定見 [`06_process/DECISIONS.md`](../../06_process/DECISIONS.md)。
