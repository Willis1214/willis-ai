# Willis AI

用于写作与视觉创作的 Skill 集合。每个目录都是独立包，安装与使用说明在对应 README 中。

| Skill | 版本 | 适用任务 | 许可 |
| --- | --- | --- | --- |
| [AI Article Clarify](ai-article-clarify/) | 1.0.0 | 从内容、表达、阅读三层编辑已有中文文章，处理 AI 味并保住事实与原意。适合整篇终修、局部修改和只审阅。 | [MIT，仅此包](ai-article-clarify/LICENSE) |
| [拾景纸刊](scenes-gathered-zine-v1-3/) | 1.3.0 | 将提供的照片整理成保留主体与原色的纸感拼贴。 | 尚未指定开源许可 |

## 开始使用

打开对应目录的 README，按宿主的 Skill 安装规则复制完整目录。两个包互不依赖，不需要一起安装。

- [文章编辑：安装、示例与方法](ai-article-clarify/README.md)
- [照片拼贴：用途与安装](scenes-gathered-zine-v1-3/README.md)
- [版本记录](REVISION_HISTORY.md)

`catalog.json` 是本仓库的包目录。根目录历史 `manifest.json` 保持原有拼贴包入口兼容；新包在自己的目录中维护 manifest。

## 许可

各包独立说明许可。`ai-article-clarify` 采用 MIT；原有拼贴包未指定许可，不能把新包许可推广到整个仓库。
