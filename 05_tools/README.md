# 05_tools — 工具

| 檔案 | 用途 |
|---|---|
| `tokenize_letter.js` | `node 05_tools/tokenize_letter.js <LETTER.md> out/letter_parts.json`：把信依 `---` 分段，切成 token，輸出每個 token 的 ID、位元組、文字（位元組碎片的文字為 `null`） |

需要先 `npm ci`（`gpt-tokenizer` 2.9.0）。

重新產生 QR code（需要 `pip install segno`）：

```bash
python3 -c "import segno; segno.make('https://github.com/wufangci/README', error='m', micro=False).save('03_assets/qr_readme.svg', scale=1, border=0, dark='#111', xmldecl=False, omitsize=True, nl=False)"
```
