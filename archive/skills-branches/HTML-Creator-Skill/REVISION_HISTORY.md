# Revision History

## English

### v1.2.1 - 2026-07-12

- Hardened the Design Plan schema with explicit `supporting_patterns`.
- Added a required-data and fallback map for all 25 semantic components.
- Strengthened visual QC for axes, scale, legends, labels, sources, and text takeaways in data figures.
- Updated the demo preview with readable fixed-size typography and an explicit mobile canvas fallback.

### v1.2.0 - 2026-07-12

- Added a Design Layer that creates a visual plan before HTML implementation.
- Added `document` and `canvas` renderer profiles with different layout and validation contracts.
- Added a curated layout atlas with 12 canonical patterns.
- Added a semantic component catalog with 25 components covering framing, comparison, flow, relationship, data, evidence, and detail.
- Added four visual directions, a Design Plan schema, and visual QC for hierarchy, proof objects, responsive fallbacks, accessibility, and anti-card-wall behavior.
- Preserved the existing evidence boundary, Diagram Layer, offline-safe output, and browser/mobile validation requirements.

### v1.1.0 - 2026-05-19

- Added a Diagram Layer for flows, state transitions, architecture maps, dependencies, data movement, and screen journeys.
- Added `references/diagram_patterns.md` with routing, implementation choices, Mermaid handling, and QA rules.
- Updated the output contract to keep diagrams inspectable and preserve diagram source text.
- Updated the build and validation workflow to check diagram rendering, mobile fit, and label readability.

### v1.0.0 - 2026-05-12

- Initial local HTML decision-display skill using Markdown or structured source material as the evidence layer and HTML as the presentation layer.

## 中文

### v1.2.1 - 2026-07-12

- 为 Design Plan schema 增加显式 `supporting_patterns` 字段。
- 为 25 个 semantic component 补充最小 required data 与 fallback 契约。
- 强化 visual QC，对数据图形的坐标轴、刻度、图例、标签、来源和文字 takeaway 做逐项检查。
- 更新 demo，移除 viewport-scaled typography，并补充 canvas 移动端可读 fallback。

### v1.2.0 - 2026-07-12

- 新增 Design Layer，在实现 HTML 前先决定视觉方向、阅读路径、主构图和语义组件。
- 新增 `document` 与 `canvas` 两种 renderer profile，分别服务长页报告和 16:9 单屏视觉页面。
- 新增包含 12 个 canonical layout 的布局 atlas。
- 新增包含 25 个 semantic component 的组件目录，覆盖框架、对比、流程、关系、数据、证据和细节表达。
- 新增 4 个视觉方向、Design Plan schema 和 visual QC，检查层级、证据图形、响应式 fallback、无障碍和反卡片墙。
- 保留原有证据边界、Diagram Layer、离线安全和浏览器/移动端验证要求。

### v1.1.0 - 2026-05-19

- 增加 Diagram Layer，覆盖流程、状态、系统架构、依赖、数据流和页面旅程。
- 新增 `references/diagram_patterns.md`，定义图形路由、实现选择、Mermaid 处理和 QA 规则。
- 更新输出契约，要求图形可检查，并保留图形源码文本。
- 更新构建和验证流程，要求检查图形渲染、移动端适配和标签可读性。

### v1.0.0 - 2026-05-12

- 初始本地版本，把 Markdown 或结构化材料作为证据层，把 HTML 作为展示层和决策层。
