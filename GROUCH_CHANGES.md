# Open Grouch - Modification Tracking

This document tracks all files modified from the upstream [OpenHands-CLI](https://github.com/OpenHands/OpenHands-CLI) to implement the Oscar the Grouch personality.

## Guiding Principles

1. **Minimize upstream file changes** - Use imports from `grouch/` where possible
2. **Document all modifications** - Update this file when changing upstream files
3. **Keep functional changes separate** - Personality is text/theme only, not behavior

## Directory Structure

```
open-grouch/
├── grouch/                     # NEW - All personality customizations
│   ├── __init__.py
│   ├── strings.py              # Centralized user-facing text
│   └── theme.py                # Color theme (trash can green)
├── openhands_cli/              # UPSTREAM - Minimize changes
│   └── ...
├── GROUCH_CHANGES.md           # This file
└── ...
```

## Modified Files

### New Files (Grouch-specific)

| File | Purpose |
|------|---------|
| `grouch/__init__.py` | Package initialization |
| `grouch/strings.py` | All personality text (banners, messages, responses) |
| `grouch/theme.py` | Trash can green color theme |
| `.github/workflows/upstream-sync.yml` | Automated upstream tracking |
| `GROUCH_CHANGES.md` | This documentation |

### Modified Upstream Files

| File | Change Type | Conflict Risk | Notes |
|------|-------------|---------------|-------|
| `pyproject.toml` | Package rename, metadata | Low | Change name, description, entry points |
| `README.md` | Complete replacement | None | Use `.gitattributes` merge=ours |
| `openhands_cli/__init__.py` | Package version source | Low | Get version from `open-grouch` package instead of `openhands` |
| `openhands_cli/theme.py` | Import grouch theme | Low | Simple import swap |
| `openhands_cli/tui/content/splash.py` | Import grouch strings, rename function | Medium | Use `GROUCH_BANNER` from `grouch/strings.py`, display "Open Grouch" in version |
| `openhands_cli/tui/widgets/status_line.py` | Import grouch strings | Low | Status messages |
| `openhands_cli/version_check.py` | PyPI package name | Low | Check `open-grouch` on PyPI instead of `openhands` |
| `openhands_cli/locations.py` | Config directory path | Low | Default to `~/.open-grouch` instead of `~/.openhands` |
| `openhands_cli/stores/cli_settings.py` | Config directory path | Low | Default to `~/.open-grouch` |
| `openhands_cli/acp_impl/utils/resources.py` | Cache directory path | Low | Default to `~/.open-grouch/cache/acp` |
| `openhands_cli/mcp/mcp_commands.py` | User messages | Low | Reference `~/.open-grouch` and `grouch` command |
| `openhands_cli/tui/panels/mcp_side_panel.py` | User messages | Low | Reference `~/.open-grouch` |
| `openhands_cli/argparsers/main_parser.py` | Import grouch strings | Low | Use `PRODUCT_NAME` from `grouch/strings.py` for `--version` output |
| `openhands_cli/acp_impl/agent/local_agent.py` | User messages, comments | Low | Reference `~/.open-grouch` |
| `openhands_cli/acp_impl/agent/remote_agent.py` | User messages, comments | Low | Reference `~/.open-grouch` |
| `openhands_cli/setup.py` | Comment only | Very Low | Reference `~/.open-grouch` in comment |
| `tests/tui/test_splash.py` | Test updates | Low | Updated to test `get_grouch_banner()` and "Open Grouch" version string |

### Files to Watch

These files may need modification as we expand the personality:

| File | Potential Changes |
|------|-------------------|
| `openhands_cli/tui/modals/confirmation_modal.py` | Grouchy confirmation prompts |
| `openhands_cli/tui/modals/exit_modal.py` | Exit messages |
| `openhands_cli/argparsers/*.py` | CLI help text |
| `openhands_cli/setup.py` | Setup wizard messages |

## Merge Strategy

When syncing with upstream:

1. **Always preserve our changes to:**
   - `README.md` (completely ours)
   - `pyproject.toml` (metadata is ours, deps follow upstream)
   - `grouch/*` (entirely ours)

2. **Take upstream changes for:**
   - `uv.lock` (dependency versions)
   - `tests/*` (test infrastructure)
   - Core functionality in `openhands_cli/`

3. **Merge carefully:**
   - Files in the "Modified Upstream Files" table above
   - Review both versions, keep our imports, take their logic changes

## Version Tracking

| Open Grouch Version | Based on OpenHands-CLI | Sync Date |
|---------------------|------------------------|-----------|
| 0.1.0 | 1.12.2 | 2026-02-25 |

---

*Update this document whenever you modify upstream files or sync with upstream.*
