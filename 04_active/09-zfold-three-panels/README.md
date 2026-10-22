# 09 — Z 字三折，三格

信切成 token、標上 ID，印在 A4 雙面，摺成 Z 字三折。信照段落切成三塊，各自落在一格裡；下格摺好後露在外面。

整封信依原文的 `---` 分成六封（最後一段併入第六封）。第一封定稿，第二到第六封暫定。

## 指令（在 repo 根目錄執行）

```bash
node 05_tools/tokenize_letter.js ../README/LETTER.md out/letter_parts.json
python3 04_active/09-zfold-three-panels/build.py        # 全部六封，另外合成一份
python3 04_active/09-zfold-three-panels/build.py 3      # 只排第三封
```

輸出到 `out/`，並更新這個資料夾的 `stills/`。內文太高、碰到摺線時腳本會停下來報錯。

每封信用哪幾段、三格怎麼分，寫在 `build.py` 開頭的 `LETTERS`。合併 PDF 需要 `pypdf`。

## 成品（就在這個資料夾）

| 檔案 | 內容 |
|---|---|
| `README_letter_01_z.pdf` … `README_letter_06_z.pdf` | 每封兩頁：第 1 頁 token 面，第 2 頁背面 |
| `README_letters_all_z.pdf` | 六封合成一份（12 頁），一次雙面印完 |

## 截圖（`stills/01/` … `stills/06/`）

| 檔案 | 內容 |
|---|---|
| `front.png` | token 面 |
| `back.png` | 背面（上格是轉了 180° 的封面） |
| `cover.png` | 摺好後的封面 |
| `fold.png` | 摺法示意：攤開 → 上三分之一往前摺 → 下三分之一往後摺 → 翻過來 |

規格見 [`01_source/SPECS.md`](../../01_source/SPECS.md)；過程與決定見 [`06_process/DECISIONS.md`](../../06_process/DECISIONS.md)。
