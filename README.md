# Willis AI · Skill 集合

面向 Willis 微信公众号粉丝的公开 Skill 集合。主题不限写作或视觉，覆盖内容表达、开发与质量、研究与知识、Skill 管理和日常工具。

当前共有 **20 个 Skill**。先按任务选择一个目录，阅读包内说明后安装；无需全部安装，环境与外部依赖以各包方法为准。

## 选择 Skill

| Skill | 版本 | 用途 | 许可 |
|---|---|---|---|
| [ai-article-clarify](ai-article-clarify/) | 1.0.0 | 中文文章终修、局部编辑与表达检查。 | MIT，仅此包 |
| [scenes-gathered-zine-v1-3](scenes-gathered-zine-v1-3/) | 1.3.0 | 保留照片主体与原色的纸感拼贴。 | 未指定 |
| [brainstorm](brainstorm/) | 2.2.0 | 把模糊的产品或工程想法梳理成需求、流程和验收方案。 | 未指定 |
| [code-qc-uat](code-qc-uat/) | 1.1.0 | 为可执行程序设计并运行功能、边界和回归检查。 | 未指定 |
| [code-reviewer](code-reviewer/) | 1.0.0 | 基于源代码和差异进行静态审查，说明问题与发布判断。 | 未指定 |
| [deeply-reader](deeply-reader/) | 1.0.0 | 从整本书或长文档提炼主张、方法及反思，形成有证据的阅读报告。 | 未指定 |
| [diff-output](diff-output/) | 1.0.0 | 用统一比较表说明前后变化及改变的原因。 | 未指定 |
| [html-creator](html-creator/) | 1.2.1 | 把报告、方案、证据和比较材料制作成独立 HTML 页面。 | 未指定 |
| [intelligence-forge](intelligence-forge/) | 1.0.0 | 从同领域资料提炼有证据、可复用的知识和约束。 | 未指定 |
| [issue-analyse](issue-analyse/) | 1.3.0 | 梳理客户或相关方问题、责任证据、支持策略和沟通方案。 | 未指定 |
| [memory-governor](memory-governor/) | 0.1.0 | 识别需要长期记住的用户规则，并在确认后维护记忆。 | 未指定 |
| [pm-consultant](pm-consultant/) | 1.2.0 | 需求咨询与 PRD 工作流的历史版本；后续演进见 Brainstorm。 | 未指定 |
| [red-team](red-team/) | 1.0.0 | 对方案、提示词和决策作对抗性审阅，指出实际风险。 | 未指定 |
| [sdd-quality-guarantee](sdd-quality-guarantee/) | 1.0.0 | 形成 Spec、架构、验收和证据之间的可追溯记录。 | 未指定 |
| [skill-cleaner](skill-cleaner/) | 1.0.0 | 只读审计 Skill 根目录、重复包、使用情况和清理候选。 | 未指定 |
| [skill-researcher](skill-researcher/) | 1.1.0 | 在创建、更新或安装 Skill 前研究已有能力和适配缺口。 | 未指定 |
| [tdd-quality-guarantee](tdd-quality-guarantee/) | 1.0.0 | 整理详细测试场景、执行证据及 Spec 对应关系。 | 未指定 |
| [token-gate](token-gate/) | 0.1.0 | 在大扫描、长材料或高消耗任务前选择能保留结果的节省路径。 | 未指定 |
| [wechat-message](wechat-message/) | 1.0.0 | 通过可见的 macOS 微信界面向指定对象发送已授权消息。 | 未指定 |
| [imessage-gateway](imessage-gateway/) | 1.0.0 | 在 macOS 上做限定会话读取、明确发送及 iMessage 状态核验。 | MIT 声明，LICENSE 文件缺失 |

## 开始使用

1. 点击上表对应目录，阅读 README 中的用途、安装和使用入口。
2. 下载仓库，复制该 Skill 的整个目录到宿主的 Skill 目录。Codex 默认位置是 `~/.codex/skills/`；自定义 CODEX_HOME 时使用对应目录。
3. 让宿主重新加载，然后用包内给出的提示开始任务。已有同名包先保存旧版，再替换完整目录。

`catalog.json` 提供机器可读目录，每个条目给出安装目录和 manifest。新迁入包采用独立 manifest；根 `manifest.json` 保留原拼贴入口兼容。

## 版本与来源

2026-10-07 将旧 Skills 仓库的 18 个独立分支包汇入此集合，保留其源码、原始说明、版本记录和 Git 历史。迁入内容及历史核验后，18 个旧包分支已删除，`Skills` 仅保留主分支迁移指引。源分支版与本机当前工作版不是同一承诺；此次迁移没有批量改写业务方法。

- [更新记录](REVISION_HISTORY.md)
- [完整迁移说明与旧版本访问](MIGRATION.md)
- [原文件、提交与安装目录映射](migration/skills-branches-2026-10-07.json)
- [旧分支原始包装资料](archive/skills-branches/)

## 许可

许可按包分别说明。`ai-article-clarify` 的 MIT 只覆盖该包。其余包没有 LICENSE 文件；iMessage Gateway 的旧说明声明 MIT，但许可证文件缺失，迁移保留该事实，不将任何许可扩大到整个集合。
