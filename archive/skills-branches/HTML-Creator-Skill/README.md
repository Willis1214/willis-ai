# HTML Creator

## English

HTML Creator is a Codex skill for creating standalone, decision-ready HTML artifacts from Markdown drafts, research notes, reports, PRDs, code-review findings, market briefs, and evidence-heavy material. It keeps source material as the evidence layer and uses a design plan to choose a coherent layout, semantic components, and a renderer profile.

## What It Does

- Selects a page archetype such as decision brief, visual PRD, evidence report, status report, or review page.
- Builds a design plan before implementation: visual direction, reading path, focal point, layout, components, responsive fallback, and anti-patterns.
- Supports a scrollable `document` profile and a bounded 16:9 `canvas` profile for HTML-PPT-like pages, posters, and single-screen visual narratives.
- Uses a curated layout atlas and semantic component catalog instead of random template or card-wall generation.
- Adds diagrams and data figures when their relationships or evidence justify them.
- Prefers self-contained HTML with inline CSS, minimal JavaScript, offline-safe behavior, and inspectable source information.

## When To Use

Use this skill when the user needs a local HTML report, decision page, visual PRD, evidence report, workflow/architecture explanation, or a richer HTML visual composition because Markdown is too flat.

Do not use it for production frontend app implementation, PPTX/Word/PDF/Figma delivery, generic landing pages, raw data processing, or short linear notes.

## Install

Copy the `html-creator/` folder from this branch into your Codex skills directory, for example `~/.codex/skills/html-creator/`.

## Quality Checks

This release was validated with the Codex skill quick validator, frontmatter and metadata readback, trigger-fit checks, self-contained preview rendering, desktop/mobile checks, and visual QC focused on hierarchy, semantic components, responsive fallbacks, and anti-card-wall behavior.

## 中文

HTML Creator 用于把 Markdown 草稿、研究笔记、报告、PRD、代码审查结果、市场简报和证据密集材料转换成单文件、可浏览、可决策的 HTML 展示物。它把 HTML 定位为展示层和决策层，不替代 Markdown、JSON、CSV 等源证据层；在生成 HTML 前先建立 Design Plan，决定视觉方向、阅读路径、布局、语义组件和 renderer profile。

## 本版重点

- 新增 Design Layer：先做视觉方向、主构图和组件选择，再实现 HTML。
- 新增 `document` profile：支持长页阅读、证据、表格、移动端重排和打印。
- 新增 `canvas` profile：支持受约束的 16:9 HTML-PPT-like 页面、海报和单屏信息图。
- 新增 10–12 个 canonical layout 的布局 atlas 和 20–25 个 semantic component 的组件目录。
- 新增 visual directions、Design Plan schema 和 visual QC，减少卡片墙、装饰性图表和随机布局。
- 保留 Diagram Layer、证据边界、离线安全和移动端验证合同。

## 适用场景

- 决策页、视觉 PRD、研究报告、状态报告、风险审查页。
- Markdown 太线性，无法表达选项、证据、风险、流程、架构或关系。
- 需要在浏览器中阅读、归档、投屏或展示单一核心观点。

## 不适用场景

- 生产前端应用开发。
- 通用营销落地页。
- PPTX、Word、PDF、Figma 原生输出。
- 很短的一屏文字说明。
- 没有真实数据或关系语义，却只想添加装饰性图表。

## 发布说明

v1.2.1 在 v1.2.0 的基础上补齐 supporting layout schema、逐组件最小数据/fallback 契约和 canvas 移动端 demo fallback，让 HTML Creator 从“能生成页面”升级为“先做构图与组件决策，再生成页面”。
