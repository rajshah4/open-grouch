# Contributing to Open Grouch 🗑️

Thank you for your interest in contributing to Open Grouch!

## Quick Start

1. **Fork and clone** the repository
2. **Set up** the development environment:
   ```bash
   make install-dev
   ```
3. **Create a branch** for your changes
4. **Make your changes** following the guidelines below
5. **Submit a PR** with a conventional commit title

## The Golden Rules

1. **Use Conventional Commits** - PR titles must follow the format:
   ```
   <type>: <description>
   
   Examples:
     grouch: add grumpy welcome message
     feat: add new command
     fix(tui): correct banner alignment
   ```

2. **Centralize personality text** in `grouch/strings.py`
3. **Minimize changes** to upstream `openhands_cli/` files
4. **Update `GROUCH_CHANGES.md`** when modifying upstream files

## Commit Types

| Type | When to Use | Triggers Release? |
|------|-------------|-------------------|
| `grouch` | Personality/theme changes | No |
| `feat` | New features | Yes (minor bump) |
| `fix` | Bug fixes | Yes (patch bump) |
| `docs` | Documentation | No |
| `sync` | Upstream sync | No |
| `ci` | CI/CD changes | No |
| `chore` | Maintenance | No |

## Automatic Releases

We use **release-please** for automatic releases:
- Your PR merges → release-please analyzes commits
- Creates a "Release PR" with version bump + changelog
- When Release PR merges → GitHub Release created

**You don't need to bump versions manually!**

## Full Documentation

For detailed guidelines on:
- Project structure
- Development workflow
- Testing
- TUI architecture

See **[AGENTS.md](./AGENTS.md)** - the comprehensive contributor guide.

---

*"Now get to work... or don't. See if I care."* 🗑️
