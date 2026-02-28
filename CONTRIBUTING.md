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

## Code Review Process

We use **automated AI code reviews** powered by [OpenHands](https://github.com/All-Hands-AI/OpenHands). When you open a PR, an AI reviewer will analyze your code and provide feedback.

### When Reviews Happen

Reviews are automatically triggered when:
- A non-draft PR is **opened**
- A draft PR is marked **ready for review**
- You add the **`review-this`** label to a PR
- You request a review from **`@openhands-agent`**

### Review Style: "Roasted" 🔥

Our reviews use the "roasted" style - think Linus Torvalds giving feedback. Expect:
- Direct, no-nonsense commentary
- Focus on **data structures and design** over style nitpicks
- Emphasis on **simplicity and pragmatism**
- Real bugs and issues prioritized over minor suggestions

Don't take it personally - the brutal honesty helps catch real problems!

### Responding to Reviews

- **🔴 Critical** - Must fix before merge (security issues, bugs)
- **🟠 Important** - Should fix (logic errors, missing error handling)
- **🟡 Suggestion** - Worth considering (clarity improvements)
- **🟢 Nit** - Optional (minor style preferences)

You can use GitHub's "suggestion" feature to apply fixes with one click when the reviewer provides code suggestions.

### Manual Review Request

If you want another review after making changes:
1. Add the `review-this` label, or
2. Request a review from `@openhands-agent`

## Full Documentation

For detailed guidelines on:
- Project structure
- Development workflow
- Testing
- TUI architecture

See **[AGENTS.md](./AGENTS.md)** - the comprehensive contributor guide.

---

*"Now get to work... or don't. See if I care."* 🗑️
