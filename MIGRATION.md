# Skills 分支迁移 · 2026-10-07

Willis AI 是面向微信公众号粉丝的公开 Skill 集合，不限定题材。旧 Skills 的一包一分支维护方式停止使用，18 个包进入本仓库的集合目录。

## 内容与历史

安装目录保留旧包源码；旧分支根 README、manifest、版本记录、release notes、测试和忽略规则等原件保存在 `archive/skills-branches/<branch>/`。需要路径适配的原源码也在那里保留未改原件；逐个文件映射、指纹、mode 和来源 Git blob 见 [迁移索引](migration/skills-branches-2026-10-07.json)。165 个原文件（18 包分支的 164 文件，加旧 main 目录 1 文件）均可通过索引重建。

每个源提交及其可达 Git 历史保存到 `archive/skills-branches/<branch>/2026-10-07` 标签，旧 main 目录亦有标签与原件。历史资料的旧安装命令不作为当前安装指南；当前使用各包 README 的集合地址。

安装包的新 README 和 manifest 适配集合位置，Skill 业务版本沿用源版本。deeply-reader/skill-cleaner 的机器绝对路径改为通用 home 路径；既有 iMessage 测试移入包后同步导入路径；diff-output 的原 description 仅加引号修复 YAML 格式，语义不变。这些适配各有原件和指纹记录，不能把它们说成原树逐字未变。

## 包映射

| 原分支 | 安装目录 | 源版本 | 原提交 |
|---|---|---|---|
| Brainstorm-Skill | [brainstorm](brainstorm/) | 2.2.0 | `df843c83b99a90060691dd53e3d2883c79df027c` |
| Code-QC-UAT-Skill | [code-qc-uat](code-qc-uat/) | 1.1.0 | `e6c21aac914c8c5cf16427caf0a0769f1a63a482` |
| Code-Reviewer-Skill | [code-reviewer](code-reviewer/) | 1.0.0 | `fd1cdcf53a351b2e23bc0f994e117766fafa7bea` |
| Deeply-Reader-Skill | [deeply-reader](deeply-reader/) | 1.0.0 | `57d83426a4567f2cc1a460c8a7ed0a58794c8faf` |
| Diff-Output-Skill | [diff-output](diff-output/) | 1.0.0 | `cacdad25f2134d80badcf39ff3ce77addaa98cdc` |
| HTML-Creator-Skill | [html-creator](html-creator/) | 1.2.1 | `b2cc9fe29b49c41c3e505e16c53384a860b5b6b4` |
| Intelligence-Forge-Skill | [intelligence-forge](intelligence-forge/) | 1.0.0 | `f89cc3ad315f8328abdb94bb05172f2ee7dc77d7` |
| Issue-Analyse-Skill | [issue-analyse](issue-analyse/) | 1.3.0 | `f014c49e3515f1e38989429aced49712eabab9dc` |
| Memory-Governor-Skill | [memory-governor](memory-governor/) | 0.1.0 | `d49972cc4cf51a4997a237dea26dd0d5fa0fbe8e` |
| PM-Consultant-Skill | [pm-consultant](pm-consultant/) | 1.2.0 | `ef29d53d833143cd6d76cb130120966093861586` |
| Red-Team-Skill | [red-team](red-team/) | 1.0.0 | `bfa25cf79dee4e1246107dd1c789aea327ba7492` |
| SDD-Quality-Guarantee-Skill | [sdd-quality-guarantee](sdd-quality-guarantee/) | 1.0.0 | `7e43f8010cef42d7056a77aa2f729489ae24af32` |
| Skill-Cleaner-Skill | [skill-cleaner](skill-cleaner/) | 1.0.0 | `066b1f10218b4a801e77715d69b4f6e16eada455` |
| Skill-Researcher-Skill | [skill-researcher](skill-researcher/) | 1.1.0 | `bacf79312f1ab0ba37c19734650713090e11a47b` |
| TDD-Quality-Guarantee-Skill | [tdd-quality-guarantee](tdd-quality-guarantee/) | 1.0.0 | `4b490dba9362942a01c8907c2a6d08135ba8ff52` |
| Token-Gate-Skill | [token-gate](token-gate/) | 0.1.0 | `2bd1faeaa6dfd4f52094f1ed0b96b82e25490bc5` |
| Wechat-Message-Skill | [wechat-message](wechat-message/) | 1.0.0 | `58163fec2f33ad3a48bb469df57deb46a6ce48e2` |
| Willis-x-AI-iMessage-Gateway-Skill | [imessage-gateway](imessage-gateway/) | 1.0.0 | `34a35e88e1d3d958c2cfd2c14efbb0ae7ca06a87` |

## 查旧版本

```bash
git clone https://github.com/Willis1214/willis-ai.git
cd willis-ai
git show archive/skills-branches/Brainstorm-Skill/2026-10-07:brainstorm/SKILL.md
```

标签指向真正旧提交，不只是记录 SHA；原有两个包及拼贴根 manifest 保持原内容。旧包的许可证状况按原件说明，未统一赋予 MIT。

## 旧分支退役

源分支在迁入内容、文件指纹和历史标签完成远端核验后退役；删除前检查源 HEAD 仍等于索引中的提交，发生并发变化则保留源分支并重新迁移。删除清单仅含此表的 18 个包分支，旧 Skills 默认分支保留迁移指引，不删除整个仓库。
