# Issue Analyse Skill

`issue-analyse` helps analyze customer or stakeholder issues without jumping directly to blame, local self-defense, or unsupported responsibility acceptance.

It follows a Chinese-first workflow:

1. 先质疑问题提出: who raised it, what they compared against, whether it existed before, whether it exists now, and whether related projects show the same behavior.
2. 再还原现场: known facts, timeline, gaps, and provisional hypotheses.
3. 再审合同和证据: POR, SOP, Email, QC, Policy, handoff agreement, release checklist, waiver, and proof strength.
4. 再判断是否构成交付问题: expected behavior, actual behavior, and material impact.
5. 再选择破局策略: conflict expansion, root-baseline tracing, attribution defense for mature systems, or corner-case transformation.
6. 最后做归因和沟通: attribution matrix, Owner / RACI, 结论把握度, Chinese communication boundaries, and external-facing solution path.

## When To Use

Use this skill when you need to:

- restore what happened before deciding whether an issue exists;
- challenge whether the reported problem is established before discussing responsibility;
- provide customer or stakeholder support without accepting responsibility that is not supported by evidence;
- break out of single-issue self-defense, surface-level debugging, premature self-blame, or corner-case deadlocks while still giving an actionable solution path;
- analyze whether a customer complaint, upstream input, release mismatch, legacy behavior, or owner handoff is actually a defect;
- separate `我方责任`, `其他 Owner 责任`, `上游依赖`, `流程 / 约定缺口`, `需求方 / 范围漂移`, and `证据缺口`;
- prepare safe Chinese wording and external-facing support actions for sensitive responsibility discussions.

## Output Style

Default output labels are Chinese. Technical terms such as `Owner`, `RACI`, `baseline`, `waiver`, `special handle`, and `release gate` are preserved when useful.

Complex communication output uses:

- `可说`
- `不应说`
- `待补证据`
- `稳妥表达`
- `对外解决方案`
- `双赢路径`

## Version

Current version: `1.3.0`

Revision history summary:

- `1.3.0`: Realigns the workflow for customer issue support: contract/evidence review now precedes delivery-issue judgment, breakthrough strategy becomes a post-evidence support-path choice, and output adds `对外解决方案` plus `双赢路径` so users can support customers without accepting unsupported responsibility.
- `1.2.0`: Adds a breakthrough strategy gate with `冲突扩大法`, `底层溯源法`, `归因防御策略`, and `困境转化法`; updates output templates and communication boundaries so disputed issues move from immediate bug-taking to evidence challenge, baseline tracing, external-variable testing, and cross-owner review when needed.
- `1.1.0`: Makes complaint / feedback challenge the first gate, adds past/current/related-project checks, and replaces default mixed English fields with Chinese output terms such as `结论把握度`, `待补证据`, and `证据链`.
- `1.0.0`: Initial central `Skills` publication. Adds the reconstruction-first workflow, Chinese-first output templates, and investigation methods for legacy issues, baseline drift, complaint validity, waiver / special handle search, change control, RACI handoff, and fix-owner versus root-cause-owner separation.
