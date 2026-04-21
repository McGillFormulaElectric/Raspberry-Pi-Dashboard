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

## Maintenance Rule
If the team sees Claude make the same mistake twice, update this file.
