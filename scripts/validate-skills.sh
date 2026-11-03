#!/usr/bin/env bash
# Validates every skills/<name>/SKILL.md against docs/skill-standard.md.
set -u

root="$(cd "$(dirname "$0")/.." && pwd)"
status=0

fail() {
  echo "FAIL $1: $2"
  status=1
}

for skill_md in "$root"/skills/*/SKILL.md; do
  [ -e "$skill_md" ] || { echo "No skills found."; exit 1; }
  dir="$(dirname "$skill_md")"
  folder="$(basename "$dir")"

  if [ "$(head -n 1 "$skill_md")" != "---" ]; then
    fail "$folder" "SKILL.md must start with a '---' frontmatter line"
    continue
  fi
  frontmatter="$(awk 'NR == 1 { next } /^---$/ { exit } { print }' "$skill_md")"

  field() { printf '%s\n' "$frontmatter" | sed -n "s/^$1:[[:space:]]*//p" | head -n 1; }
  name="$(field name)"
  description="$(field description)"

  [ -n "$name" ] || fail "$folder" "missing 'name'"
  [ "$name" = "$folder" ] || fail "$folder" "name '$name' does not match folder '$folder'"
  [ "${#name}" -le 64 ] || fail "$folder" "name longer than 64 chars"
  printf '%s' "$name" | grep -Eq '^[a-z0-9]+(-[a-z0-9]+)*$' \
    || fail "$folder" "name must be lowercase alphanumerics separated by single hyphens"

  [ -n "$description" ] || fail "$folder" "missing 'description' (must be a single line)"
  case "$description" in '>'*|'|'*) fail "$folder" "description must be a single line, not a block scalar" ;; esac
  [ "${#description}" -le 1024 ] || fail "$folder" "description longer than 1024 chars"

  [ -n "$(field license)" ] || fail "$folder" "missing 'license'"
  printf '%s\n' "$frontmatter" | grep -Eq '^[[:space:]]+author:' || fail "$folder" "missing 'metadata.author'"
  printf '%s\n' "$frontmatter" | grep -Eq '^[[:space:]]+version:' || fail "$folder" "missing 'metadata.version'"

  lines="$(wc -l < "$skill_md" | tr -d ' ')"
  [ "$lines" -le 500 ] || fail "$folder" "SKILL.md has $lines lines (max 500)"

  # Every relative markdown link in the skill must point to an existing file.
  while IFS= read -r md; do
    while IFS= read -r link; do
      [ -e "$(dirname "$md")/$link" ] || fail "$folder" "broken link '$link' in ${md#"$dir"/}"
    done < <(grep -oE '\]\([^)#[:space:]]+\)' "$md" | sed -E 's/^\]\(//; s/\)$//' | grep -vE '^[a-z]+:')
  done < <(find "$dir" -name '*.md')

  [ "$status" -eq 0 ] && echo "ok   $folder"
done

exit "$status"
