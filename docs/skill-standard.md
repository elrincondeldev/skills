# Skill standard

Every skill in this repo follows the [Agent Skills specification](https://agentskills.io/specification) so it installs with `npx skills add` (skills.sh) and works in Claude Code, Codex, Cursor, and any other compatible agent. On top of the spec, this repo adds the house rules below. `scripts/validate-skills.sh` enforces the mechanical ones.

## Layout

```
skills/<name>/
├── SKILL.md          # required: frontmatter + steps
├── references/       # optional: docs loaded on demand
├── scripts/          # optional: executable helpers
└── assets/           # optional: templates and static files
```

- One folder per skill, directly under `skills/`. The folder name equals the `name` field.
- File references from `SKILL.md` stay one level deep (`references/x.md`, never `references/a/b.md`).
- Skills taken from other authors keep their original `license` and add `metadata.source: <owner/repo>`.

## Frontmatter

| Field | Rule |
| --- | --- |
| `name` | Required. 1-64 chars, `a-z`, `0-9`, single hyphens, no leading/trailing hyphen. Matches the folder. |
| `description` | Required, single line, max 1024 chars. Leads with *what it is*, then *when to use it*, one trigger per distinct case. |
| `license` | Required in this repo. `MIT` for original skills. |
| `metadata.author` | Required in this repo. |
| `metadata.version` | Required in this repo. Semver as a quoted string; bump on behavior change. |
| `compatibility` | Only when the skill truly needs a specific environment (a CLI, network access). |
| `allowed-tools` | Avoid; it's experimental and agent-specific. |

## Writing the body

- **Under 500 lines; aim for under 200.** Push anything only some runs need into `references/` behind a link that says when to read it.
- **Steps first.** Number the steps the agent performs. End each step with a **done when** condition the agent can check.
- **Prompt the positive.** State the behavior you want; reserve "never" for hard guardrails, and pair each one with what to do instead.
- **Agent-neutral.** Name capabilities ("the structured-question tool if your harness has one", "a subagent if supported"), not one vendor's tool names.
- **Cache only what the environment can't tell.** Don't restate what a `--help`, a config file, or the directory layout already says.
- **No no-ops.** Delete any sentence the model would follow by default anyway.

## Adding a skill

1. Copy `template/SKILL.template.md` to `skills/<name>/SKILL.md` and fill it in. (The template has a different filename so skills.sh does not list it as a skill.)
2. Add the skill's path to `.claude-plugin/marketplace.json` and a row to the README table.
3. Run `scripts/validate-skills.sh`.
4. Try it in a real session on a real task before committing.
