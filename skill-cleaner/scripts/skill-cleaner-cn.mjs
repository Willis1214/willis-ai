#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const analyzer = path.join(__dirname, "skill-cleaner.ts");
const rawArgs = process.argv.slice(2);

function takeArg(name) {
  const index = rawArgs.indexOf(name);
  if (index < 0) return null;
  const value = rawArgs[index + 1] ?? null;
  rawArgs.splice(index, value === null ? 1 : 2);
  return value;
}

function hasArg(name) {
  return rawArgs.includes(name);
}

function valueArg(name, fallback) {
  const index = rawArgs.indexOf(name);
  return index >= 0 && rawArgs[index + 1] ? rawArgs[index + 1] : fallback;
}

const outPath = takeArg("--out");
if (!hasArg("--months") && !hasArg("--no-logs")) rawArgs.push("--months", "3");
const analyzerArgs = ["--experimental-strip-types", analyzer, ...rawArgs, "--json"];
const run = spawnSync("node", analyzerArgs, { encoding: "utf8", maxBuffer: 200 * 1024 * 1024 });

if (run.error) {
  console.error(`运行失败: ${run.error.message}`);
  process.exit(1);
}
if (run.status !== 0) {
  console.error(run.stderr || run.stdout);
  process.exit(run.status ?? 1);
}

let data;
try {
  data = JSON.parse(run.stdout);
} catch (error) {
  console.error(`解析上游 JSON 输出失败: ${error instanceof Error ? error.message : String(error)}`);
  process.exit(1);
}

const skills = Array.isArray(data.skills) ? data.skills : [];
const usage = data.usage && typeof data.usage === "object" ? data.usage : {};
const logFiles = Array.isArray(data.logFiles) ? data.logFiles : [];
const budget = data.budget ?? {};
const considered = skills.filter((skill) => skill.enabled !== false);
const months = valueArg("--months", hasArg("--no-logs") ? "0" : "3");

function formatNumber(value) {
  const number = Number(value);
  return Number.isFinite(number) ? Math.round(number).toLocaleString("en-US") : "--";
}

function formatPct(value) {
  const number = Number(value);
  return Number.isFinite(number) ? `${(number * 100).toFixed(1)}%` : "--";
}

function scopeName(scope) {
  return {
    codex: "本地全局",
    "codex-plugin": "插件缓存",
    repo: "项目内",
    "agent-scripts": "agent-scripts",
    dropbox: "Dropbox",
    extra: "额外根目录",
  }[scope] ?? scope ?? "未知";
}

function groupBy(items, key) {
  const map = new Map();
  for (const item of items) {
    const value = key(item);
    map.set(value, [...(map.get(value) ?? []), item]);
  }
  return map;
}

function usageTotal(skill) {
  const item = usage[skill.name] ?? {};
  return Number(item.dollar ?? 0) + Number(item.fileRead ?? 0) + Number(item.text ?? 0);
}

function usageText(skill) {
  const item = usage[skill.name] ?? {};
  return `$${Number(item.dollar ?? 0)}, read=${Number(item.fileRead ?? 0)}, text=${Number(item.text ?? 0)}`;
}

function normalizedWords(input) {
  return String(input ?? "")
    .toLowerCase()
    .replace(/[`"'’().,;:!?/\\[\]{}_-]+/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .split(" ")
    .filter((word) => word.length >= 2);
}

function jaccard(a, b) {
  const setA = new Set(a);
  const setB = new Set(b);
  if (setA.size === 0 && setB.size === 0) return 1;
  let intersection = 0;
  for (const item of setA) if (setB.has(item)) intersection += 1;
  return intersection / (setA.size + setB.size - intersection);
}

function similarity(a, b) {
  if (a.bodyHash && b.bodyHash && a.bodyHash === b.bodyHash) return 1;
  return jaccard(normalizedWords(a.description), normalizedWords(b.description));
}

function bulletRows(items, formatter, empty = "- 无") {
  return items.length ? items.map(formatter).join("\n") : empty;
}

const roots = [...groupBy(skills, (skill) => skill.root).entries()]
  .map(([root, list]) => ({
    root,
    total: list.length,
    disabled: list.filter((skill) => skill.enabled === false).length,
  }))
  .sort((a, b) => b.total - a.total || a.root.localeCompare(b.root));

const scopeRows = [...groupBy(skills, (skill) => skill.scope).entries()]
  .map(([scope, list]) => ({
    scope,
    total: list.length,
    disabled: list.filter((skill) => skill.enabled === false).length,
  }))
  .sort((a, b) => b.total - a.total || String(a.scope).localeCompare(String(b.scope)));

const duplicatesByName = [...groupBy(considered, (skill) => String(skill.baseName ?? skill.name).toLowerCase()).entries()]
  .filter(([, list]) => list.length > 1)
  .sort((a, b) => b[1].length - a[1].length || a[0].localeCompare(b[0]));

const duplicateBody = [...groupBy(considered, (skill) => skill.bodyHash).entries()]
  .filter(([hash, list]) => hash && hash !== "811c9dc5" && list.length > 1)
  .sort((a, b) => b[1].length - a[1].length);

const longDescriptions = considered
  .filter((skill) => Number(skill.descChars ?? 0) >= 110 || Number(skill.lineChars ?? 0) >= 180)
  .sort((a, b) => Number(b.descChars ?? 0) - Number(a.descChars ?? 0))
  .slice(0, 30);

const unused = considered
  .filter((skill) => !["codex", "codex-plugin"].includes(skill.scope))
  .filter((skill) => usageTotal(skill) === 0)
  .sort((a, b) => String(a.scope).localeCompare(String(b.scope)) || String(a.name).localeCompare(String(b.name)))
  .slice(0, 80);
const disabledSkills = skills
  .filter((skill) => skill.enabled === false)
  .sort((a, b) => String(a.scope).localeCompare(String(b.scope)) || String(a.name).localeCompare(String(b.name)));

const exactDeleteSuggestions = [];
for (const [name, list] of duplicatesByName) {
  const [first, ...rest] = list;
  for (const item of rest) {
    const score = similarity(first, item);
    if (score >= 0.95) {
      exactDeleteSuggestions.push({ name, keep: first, candidate: item, score });
    }
  }
}

const generated = new Date().toISOString();
const lines = [];
lines.push("# Skill Cleaner 本机 Skills 审计报告", "");
lines.push(`生成时间: ${generated}`);
lines.push(`扫描窗口: ${hasArg("--no-logs") ? "未读取日志" : `最近 ${months} 个月日志`}`);
lines.push(`扫描模式: 只读审计；未删除、未禁用、未改写任何 skill。`, "");

lines.push("## 结论摘要", "");
lines.push(`- 发现 skills: ${skills.length} 个；纳入预算/重复项分析: ${considered.length} 个。`);
lines.push(`- 扫描日志文件: ${logFiles.length} 个。`);
lines.push(`- 重复名称组: ${duplicatesByName.length} 组；完全/近似重复正文组: ${duplicateBody.length} 组。`);
lines.push(`- 长描述/高预算候选: ${longDescriptions.length} 个。`);
lines.push(`- 疑似未使用候选: ${unused.length} 个。`);
lines.push(`- 预算使用: ${formatNumber(budget.budgetedTokens)} / ${formatNumber(budget.budgetTokens)} tokens (${formatPct(budget.budgetedBudgetUsedRatio)} of 2% budget)。`);
lines.push(`- 预算后包含 skills: ${formatNumber(budget.includedSkills)}；预算后省略 skills: ${formatNumber(budget.omittedSkills)}。`, "");

lines.push("## Prompt Budget", "");
lines.push(`- 模型: ${budget.model ?? "--"}`);
lines.push(`- context tokens: ${formatNumber(budget.contextTokens)}；来源: ${budget.contextSource ?? "--"}`);
lines.push(`- 2% skills 预算: ${formatNumber(budget.budgetTokens)} tokens`);
lines.push(`- 未预算完整列表成本: ${formatNumber(budget.unbudgetedFullTokens)} tokens (${formatPct(budget.unbudgetedBudgetUsedRatio)} of budget)`);
lines.push(`- Codex 预算规则后成本: ${formatNumber(budget.budgetedTokens)} tokens (${formatPct(budget.budgetedBudgetUsedRatio)} of budget)`);
lines.push(`- 剩余 2% 预算: ${formatNumber(budget.remainingBudgetTokens)} tokens`);
if (budget.effectiveBudgetTokens != null) {
  lines.push(`- effective 2% 预算: ${formatNumber(budget.effectiveBudgetTokens)} tokens；剩余: ${formatNumber(budget.remainingEffectiveBudgetTokens)} tokens`);
}
lines.push("");

lines.push("## 根目录分布", "");
lines.push("| 根目录 | skills | disabled |");
lines.push("| --- | ---: | ---: |");
for (const row of roots) lines.push(`| ${row.root} | ${row.total} | ${row.disabled} |`);
lines.push("");

lines.push("## Scope 分布", "");
lines.push("| scope | 含义 | skills | disabled |");
lines.push("| --- | --- | ---: | ---: |");
for (const row of scopeRows) lines.push(`| ${row.scope ?? "--"} | ${scopeName(row.scope)} | ${row.total} | ${row.disabled} |`);
lines.push("");

lines.push("## Disabled Skills", "");
lines.push(bulletRows(disabledSkills, (skill) =>
  `- ${skill.name}: ${scopeName(skill.scope)}；${skill.path}`
));
lines.push("");

lines.push("## 重复名称组", "");
lines.push(bulletRows(duplicatesByName.slice(0, 25), ([name, list]) => {
  const rows = [`- ${name}: ${list.length} 个`];
  for (const skill of list) rows.push(`  - ${scopeName(skill.scope)}: ${skill.path}`);
  return rows.join("\n");
}));
lines.push("");

lines.push("## 完全/近似重复正文组", "");
lines.push(bulletRows(duplicateBody.slice(0, 20), ([, list]) => {
  const rows = [`- ${list.map((skill) => skill.name).join(", ")}`];
  for (const skill of list) rows.push(`  - ${scopeName(skill.scope)}: ${skill.path}`);
  return rows.join("\n");
}));
lines.push("");

lines.push("## 可考虑删除的近似副本", "");
lines.push(bulletRows(exactDeleteSuggestions.slice(0, 20), (item) =>
  `- ${item.name}: 建议保留 ${item.keep.path}；候选副本 ${item.candidate.path}；相似度 ${(item.score * 100).toFixed(0)}%。`
));
lines.push("");

lines.push("## 长描述/高预算候选", "");
lines.push(bulletRows(longDescriptions, (skill) =>
  `- ${skill.name}: description=${formatNumber(skill.descChars)} chars, rendered_line=${formatNumber(skill.lineChars)} chars；${skill.path}`
));
lines.push("");

lines.push("## 疑似未使用候选", "");
lines.push("说明: 这是最近日志启发式判断，只代表未发现显式调用证据，不等于可以删除。");
lines.push(bulletRows(unused, (skill) =>
  `- ${skill.name}: ${scopeName(skill.scope)}；usage=${usageText(skill)}；${skill.path}`
));
lines.push("");

lines.push("## 执行建议", "");
lines.push("- 不建议自动删除任何 skill；重复项和未使用项需要结合业务上下文逐个确认。");
lines.push("- 优先处理长描述候选，因为这类改动风险最低，通常只影响 prompt budget。");
lines.push("- 对重复名称组，先确认保留副本是否已被当前 Codex 会话加载，再决定是否禁用或删除副本。");
lines.push("- 对疑似未使用候选，至少复查最近任务、automations 和用户固定工作流后再做清理。");

const report = `${lines.join("\n")}\n`;
if (outPath) {
  const absoluteOut = path.resolve(outPath.replace(/^~(?=$|\/)/, os.homedir()));
  fs.mkdirSync(path.dirname(absoluteOut), { recursive: true });
  fs.writeFileSync(absoluteOut, report, "utf8");
  console.log(absoluteOut);
} else {
  console.log(report);
}
