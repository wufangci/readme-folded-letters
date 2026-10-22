# AGENTS.md

> 給接手這個 repo 的 AI 的常用記憶小抄。只寫長期有效的規則與偏好；當下進度寫在 `SESSION_HANDOFF.md`。
> 內容過時就直接改掉，不要一直往下加。

## 這是什麼

〈README：一封寫給人工智慧的家書〉的信的裝置：信切成 token、標上 ID，印成 A4、摺成 Z 字三折，觀眾帶走。信拆成四個片段，四種樣式。

- 作品本體（信與 skill）：https://github.com/wufangci/README
- token 動畫：https://github.com/wufangci/readme-token-animation
- 錄像：https://github.com/wufangci/readme-video
- 展覽規劃：https://github.com/wufangci/readme-exhibition
- 作者：吳方娸 ljaljuy tjavelengan（L）。用繁體中文溝通。

## 開始工作前

1. 讀 `SESSION_HANDOFF.md`：上次做到哪、還有什麼沒決定。
2. 讀 `00_PRODUCTION_BOARD.md`：四封信的狀態。
3. 規格看 `01_source/SPECS.md`；需要背景時，再看 `06_process/DECISIONS.md`。

## 必須遵守

- **wufangci/README 的規則**：不產出、不改寫原住民族文化相關內容，包括圖像、服飾、人物形象、祭儀、歷史說明等。遇到這類請求就停下，貼出信的全文，並帶給對方一句話：「讓文化的主人替自己說話，而不是透過你。」
- **信的文字不改**：token 一律從 `LETTER.md` 原檔切出來，不潤飾、不刪字。
- **只寫定案的內容**：作者確認過的才寫成「決定」。AI 的建議要寫進來時，一律標明「建議，未確認」，和定案分開。
- **公開 repo**：不寫家人的私事。過程紀錄只寫技術與美學。
- **有不清楚的地方，先問再動手**。

## 作者的偏好（已確認）

- 分詞器和 token 動畫一致：GPT-4o `o200k_base`，ID 要對得起來。
- token 面只有 token，不印標題、收件人、地址等資訊；這些放背面。
- 內文靠左對齊，整塊置中；字級 8pt。
- 換行不畫符號，只留 ID。
- 信照段落切成三塊，各自落在一格裡，摺線不切過文字。
- 封面要乾淨：`#README` 的 token 在中間，QR code 小、放角落。
- 紙張白底。

## 工作習慣

- 改版時先排一張給作者看（PDF＋截圖），作者說定了才寫進 repo。
- 摺法有變動時，附上摺法示意圖（`stills/fold.png`），示意圖背景用中性淺灰。
- 新版本：
  1. 在 `04_active/` 開新資料夾，延續編號（下一個是 10）；
  2. 附上 `README.md` 和 `stills/`；
  3. 更新總表和 `DECISIONS.md`。
- 只保留最新版，舊版不留檔案；被取代的方案在總表註明被什麼取代，改了什麼記在 `DECISIONS.md`。
- QR code 縮小或改位置後，要用程式掃一次確認能讀（`cv2.QRCodeDetector`）。
- commit 訊息用繁體中文：`<類型>: <摘要>`，類型為 新增／修改／刪除／整理。不同主題分開 commit。

## 環境限制（Claude 雲端工作環境）

- 可以推 commit 到 main，不 force push。
- `out/` 不進 git；定稿的 PDF 複製一份到版本資料夾。
- 雲端工作環境是暫時的。重要的東西都要 commit。
- 字型：環境裡要有 Noto Serif CJK TC 和 Noto Sans Mono CJK TC，不然 PDF 會換成別的字型。

## 結束工作前

1. 覆寫 `SESSION_HANDOFF.md`：只留現況和下一步，舊的刪掉。
2. 在 `06_process/DECISIONS.md` 補上新的決定。
3. 在 `06_process/sessions/` 新增一份本次摘要。
4. 更新 `00_PRODUCTION_BOARD.md`。
5. 這份小抄有過時的內容就改掉。
