# skills

[![skills.sh](https://skills.sh/b/elrincondeldev/skills)](https://skills.sh/elrincondeldev/skills)

Personal [Agent Skills](https://agentskills.io) for Claude Code, Codex, Cursor, and any other compatible agent.

## Install

With [skills.sh](https://skills.sh):

```bash
npx skills add elrincondeldev/skills
```

One skill only:

```bash
npx skills add elrincondeldev/skills --skill learn-codebase
```

As a Claude Code plugin:

```
/plugin marketplace add elrincondeldev/skills
/plugin install skills@elrincondeldev
```

## Skills

| Skill | What it does |
| --- | --- |
| [learn-codebase](skills/learn-codebase/SKILL.md) | Interactive tutor that teaches you a whole repo lesson by lesson, checking that you really understand each part before moving on. Say "teach me this codebase". |
| [create-pr](skills/create-pr/SKILL.md) | Opens a pull request with a clear, professional title and description built from your commits, diff, and linked issue, following the repo's own PR template and conventions when it has them. Say "open a PR". |
| [grilling](skills/grilling/SKILL.md) | Stress-tests a plan, decision, or idea by interviewing you in rounds of numbered questions, each with a recommended answer, until nothing is left assumed. Say "grill me". From [mattpocock/skills](https://github.com/mattpocock/skills). |
| [code-review](skills/code-review/SKILL.md) | Reviews the changes since a commit, branch, or tag on two separate axes, Standards (does it follow the repo's coding rules?) and Spec (does it do what the issue asked?), run as parallel subagents and reported side by side. Say "review since main". From [mattpocock/skills](https://github.com/mattpocock/skills). |
| [tdd](skills/tdd/SKILL.md) | Builds features test-first: agrees the behaviors and where to test them with you, then implements one slice at a time through red → green and refactors with the suite green. Say "build this with TDD". Adapted from [mattpocock/skills](https://github.com/mattpocock/skills). |

## Contributing

Every skill follows [docs/skill-standard.md](docs/skill-standard.md). Start from [template/SKILL.template.md](template/SKILL.template.md) and run `scripts/validate-skills.sh` before committing.
