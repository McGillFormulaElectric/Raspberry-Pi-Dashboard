# CLAUDE.md

## Purpose
This file captures the team's working norms for using Claude Code effectively. Update it whenever we notice repeatable mistakes, useful workflows, or better defaults.

## Team Practices

1. Start in Plan mode for non-trivial work.
   Use planning before implementation, especially for pull requests. A strong plan usually leads to better one-shot execution.

2. Use parallel sessions when helpful.
   It is normal to run multiple Claude sessions across terminal, web, and mobile to explore tasks in parallel and hand work off between environments.

3. Prefer the strongest model when quality matters.
   Slower models can still be faster overall if they need less steering and make better tool decisions.

4. Keep `CLAUDE.md` in git and treat it as shared team memory.
   When Claude makes a repeated mistake or the team discovers a better workflow, add it here.

5. Use PR review to improve the system.
   During review, add guidance to `CLAUDE.md` when a lesson should become a reusable rule rather than a one-off comment.

6. Turn repeated workflows into slash commands.
   Store common commands in `.claude/commands/` so both humans and Claude can use them consistently.

7. Use subagents for recurring support tasks.
   Examples include verification, cleanup, simplification, or other repeatable post-processing steps.

8. Use hooks to enforce consistency.
   For example, format generated code with a `PostToolUse` hook to reduce CI formatting failures.

9. Pre-approve safe commands where possible.
   Prefer shared permissions settings over unnecessary approval friction. Store safe defaults in `.claude/settings.json` when appropriate.

10. Connect Claude to the team's tools.
    Claude should be able to use shared systems such as Slack, analytics, logs, and other MCP-enabled tooling when useful.

11. Give Claude a way to verify its work.
    Verification is one of the biggest quality multipliers. Prefer workflows where Claude can test, inspect, or validate results directly.

## PySide6 mainwindow.ui Editing Rules

⚠️ **CRITICAL RULES — ALWAYS FOLLOW THESE:**

When editing `mainwindow.ui` files for PySide6:

1. **DO NOT USE ANY LAYOUTS**
   - NO QBoxLayout (horizontal or vertical)
   - NO QGridLayout
   - NO FlowLayout or any other layout manager
   - This is non-negotiable. Always break layouts if they appear.

2. **USE ONLY SIMPLE WIDGETS**
   - Stick to: QFrame, QLabel, QProgressBar, QPushButton, QLineEdit, QComboBox, etc.
   - Simple, individual widgets only.

3. **NEVER SET LAYOUT PROPERTIES**
   - Do not configure spacing, margins, or alignment via layout system
   - Position widgets by absolute coordinates or frame hierarchy only

4. **IF A LAYOUT IS PRESENT, REMOVE IT**
   - Check for any `<layout>` tags in the XML — delete them
   - If Claude detects a layout, stop and flag it immediately

This keeps the UI simple, predictable, and easy to manage programmatically.

## Verification Expectations

Choose the strongest practical feedback loop for the task:
- Run a command
- Run tests
- Check logs
- Use a browser
- Use a simulator
- Use a background verification agent

If Claude can verify its own work, results are usually much better.

## Team-Owned Files
- `CLAUDE.md`: shared operating guidance
- `.claude/commands/`: reusable slash commands
- `.claude/settings.json`: shared safe permissions and settings
- `.mcp.json`: shared MCP tool configuration

## Changelog Requirements

⚠️ **MANDATORY — DO NOT SKIP:**

**ALL changes must be added to `changelog.md`.**

- Every feature, bug fix, update, or modification must have a corresponding entry in `changelog.md`
- Add entries BEFORE committing code
- Format: Clear description of what changed and why
- This is non-negotiable. No PR or commit should merge without a changelog entry.

## Maintenance Rule
If the team sees Claude make the same mistake twice, update this file.
