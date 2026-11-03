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

## Contributing

Every skill follows [docs/skill-standard.md](docs/skill-standard.md). Start from [template/SKILL.template.md](template/SKILL.template.md) and run `scripts/validate-skills.sh` before committing.
