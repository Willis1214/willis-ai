# Skill Researcher Methodology

## Source Ideas

This methodology combines two public patterns:

- `find-skills`: discover open ecosystem skills, check leaderboard/search results, verify install count, source reputation, GitHub stars, and audit signals before recommending anything.
- `skill-creator`: design skills from concrete examples, keep `SKILL.md` concise, use progressive disclosure, generate only needed resources, validate structure, and forward-test realistic usage.

Useful source URLs:

- https://skills.sh/vercel-labs/skills/find-skills
- https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md
- https://skills.sh/anthropics/skills/skill-creator

## Reproducible Discovery Path

Use this order:

1. Local precedent:
   - `find ~/.codex/skills -maxdepth 2 -name SKILL.md -print`
   - Read only likely comparable skill metadata and short bodies.
2. Web discovery:
   - Search `skills.sh <domain> skill`
   - Search `site:github.com "SKILL.md" "<domain>" "skill"`
   - Search `<domain> agent skill skills.sh`
3. Skills CLI discovery:
   - Prefer not to run during the gate.
   - If needed, ask before running `npx skills find <query>`.
4. Candidate source read:
   - `SKILL.md`
   - README or package page
   - audit/security badges
   - scripts only when the candidate's behavior depends on them

## Candidate Scoring

Use a lightweight 0-3 score per dimension:

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Task fit | unrelated | adjacent | partial fit | direct fit |
| Trigger fit | vague | broad | usable | precise positive and negative triggers |
| Source trust | unknown | individual only | known repo | official/high-reputation source |
| Ecosystem signal | none | low installs/stars | moderate | high installs/stars |
| Security clarity | opaque | scripts unchecked | mostly inspectable | audits or simple low-risk design |
| Method value | none | minor wording | useful pattern | strongly reusable workflow |

Prefer candidates with strong task fit, clear triggers, trusted source, and inspectable behavior. A lower-score candidate can still be useful as a negative example.

## Research Brief Rules

The brief must help the user decide before implementation:

- no code or skill edits before the brief
- no third-party installation during the brief
- one recommended path, with alternatives only when they materially affect outcome
- clear file scope
- clear "do not touch" boundaries
- explicit QC plan
- explicit confirmation request

## Skill Design Extraction

When adapting from candidates, extract:

- frontmatter description structure
- trigger and non-trigger examples
- workflow steps
- resource layout
- bundled script criteria
- reference split strategy
- validation commands
- confirmation gates
- safety language

Do not copy irrelevant categories, future extension hooks, README clutter, or broad marketplace language unless the requested skill actually needs it.

## QC Checklist

For a newly created skill, verify:

- `SKILL.md` frontmatter has only `name` and `description`.
- Skill name is lowercase letters, digits, and hyphens.
- Description includes specific triggers.
- Body states what to do before implementation.
- Resource folders exist only when used.
- `agents/openai.yaml` has a correct `$skill-name` default prompt.
- `quick_validate.py <skill-folder>` passes.
- Scenario checks cover:
  - should trigger: "create a new skill for X"
  - should trigger: "turn this workflow into a reusable skill"
  - should not block: "rename this skill display name only"
  - should pause: "install this third-party skill" without prior approval

If AGENTS is updated, verify the rule mentions the skill by name and does not conflict with `Context Tracker`, `Token Gate`, or `Memory Governor`.
