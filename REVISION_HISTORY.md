# Revision History

## 集合迁移 — 2026-10-07

- 仓库定位为面向公众号粉丝、不限主题的 Skill 集合。
- 从旧 Skills 迁入 18 个独立包，集合由 2 个包增至 20 个包；原业务版本保持。
- 完整保存原包装资料、164 个包分支源文件及旧 main 目录，旧提交和可达历史由迁移标签保留。
- 更新包安装说明、独立 manifest、catalog 和 README；机器路径、既有测试导入路径作必要适配，并修复 diff-output 的 description 引号，保留原件。
- 许可仍按各包范围记录；原有文章包、拼贴包及根拼贴 manifest 保持兼容。
- 迁移映射、指纹和退役顺序见 MIGRATION.md 及 migration/ 索引。


## AI Article Clarify 1.0.0 — 2026-09-20

- 新增独立中文文章编辑包，从内容、表达和阅读三个层面终修已有稿件。
- 支持指定结构、局部修改和只审阅；保留事实、条件与作者原意。
- 去除公众号账号、固定样式、尾图及私有 Skill 依赖。
- 包含安装说明、构造示例、行为案例和仅适用于新包的 MIT 许可。
- 根 README 扩为包目录，新增 catalog.json；既有拼贴包源文件与根 manifest 保持兼容。


## English

### v1.3.0 - 2026-08-14

| Field | Value |
|---|---|
| Version | v1.3.0 |
| Date | 2026-08-14 |
| Change Type | Initial public release of the local revision |
| Repository | Willis1214/willis-ai |
| Commit | `6bb18d38c7af7ed28d10242621287d6dbc2a39a8` |
| Release | None |

#### Summary

Published the local revision of a source-faithful paper-collage skill as a standalone public package.

#### Source Skill Changes

- Preserve the input orientation and approximate aspect feeling.
- Choose a semantic subject and minimal context halo before defining the torn boundary.
- Preserve source colors and reject global yellow, sepia, or vintage washes.
- Continue subject structure into paper before using sparse, natural fallback curves.
- Suppress generated keywords, captions, metadata, logos, and watermarks.

#### Repository Documentation Changes

- Added a public README and machine-readable manifest.
- Included the workflow reference and Codex metadata.

#### Release Asset Changes

- None.

#### Compatibility and Migration

- Copy the packaged skill directory into the Codex skills directory.

#### Validation

- Skill repository contract: pass before publication.
- Secret scan: pass before publication.
- Remote branch and package readback: pass after push to `main`.

#### Known Gaps

- No license selected.
- No tagged release or ZIP asset generated.

---

## 中文

### v1.3.0 - 2026-08-14

| 字段 | 值 |
|---|---|
| 版本 | v1.3.0 |
| 日期 | 2026-08-14 |
| 变更类型 | 本地修订版首次公开发布 |
| 仓库 | Willis1214/willis-ai |
| Commit | `6bb18d38c7af7ed28d10242621287d6dbc2a39a8` |
| Release | None |

#### 摘要

把本地修订后的纸感拼贴 Skill 整理成独立公开包，重点处理主体边界、原图色彩、纸面过渡和新增文字控制。

#### Source Skill 变更

- 保留原图横竖方向和大致画面感觉。
- 先判断语义主体与最小必要环境，再决定撕纸边界。
- 保留原图色彩，拒绝全局黄色、棕褐色或复古滤镜。
- 优先延伸主体结构线，只有在缺少可用结构时才使用稀疏自然的备用曲线。
- 默认不生成关键词、说明文字、元数据、Logo 或水印。

#### 仓库文档变更

- 增加公开 README 和机器可读 manifest。
- 保留工作流参考文件与 Codex 元数据。

#### Release Asset 变更

- None。

#### 兼容性与迁移

- 将包内 Skill 目录复制到 Codex skills 目录即可使用。

#### 验证

- Skill 仓库合同：发布前通过。
- Secret scan：发布前通过。
- 远端分支与包内容读回：已推送到 `main` 并完成。

#### 已知缺口

- 尚未选择 License。
- 尚未创建 Tag 或 ZIP Release 资产。
