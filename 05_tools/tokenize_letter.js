// 把信切成 token，依 `---` 分段輸出成 JSON。
// 用法（在 repo 根目錄）：node 05_tools/tokenize_letter.js <LETTER.md> out/letter_parts.json
// 分詞器：GPT-4o o200k_base（gpt-tokenizer 2.9.0），和 readme-token-animation 相同。
const fs = require('fs');
const { encode } = require('gpt-tokenizer/encoding/o200k_base');
const ranks = require(require('path').join(__dirname, '..', 'node_modules/gpt-tokenizer/cjs/bpeRanks/o200k_base.js')).default;

const [src, dst] = process.argv.slice(2);
if (!src || !dst) {
  console.error('用法：node 05_tools/tokenize_letter.js <LETTER.md> <輸出.json>');
  process.exit(1);
}

// 去掉第一行的語言切換連結，其餘照原檔
const text = fs.readFileSync(src, 'utf8').replace(/^\*\[.*?\]\(.*?\)\*\s*\n/, '');
const sections = text.split(/\n\s*---\s*\n/).map(s => s.trim());

const out = sections.map(sec => encode(sec).map(id => {
  const r = ranks[id];
  const bytes = typeof r === 'string' ? [...Buffer.from(r, 'utf8')] : r;
  let str = null;
  try { str = new TextDecoder('utf-8', { fatal: true }).decode(Uint8Array.from(bytes)); } catch (e) { str = null; }
  return { id, b: bytes, s: str }; // s 為 null：無法單獨成字的位元組碎片
}));

fs.mkdirSync(require('path').dirname(dst), { recursive: true });
fs.writeFileSync(dst, JSON.stringify(out));
out.forEach((p, i) => console.log(`段 ${i}：${p.length} tokens，碎片 ${p.filter(t => t.s === null).length}`));
