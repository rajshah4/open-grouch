# Repository Guidelines

## Repository Purpose

**Open Grouch** is a personality fork of [OpenHands-CLI](https://github.com/OpenHands/OpenHands-CLI) that brings Oscar the Grouch's character to the AI coding assistant.

This is a **downstream fork** - we track upstream changes but do NOT contribute back. Our changes are purely personality/theming, not functional.

### Key Principles
1. **Minimize upstream file modifications** - Use imports from `grouch/` package where possible
2. **Centralize personality in `grouch/strings.py`** - All user-facing text lives here
3. **Document all changes** - Update `GROUCH_CHANGES.md` when modifying upstream files
4. **Preserve upstream functionality** - We change tone, not behavior

### References
- Upstream: https://github.com/OpenHands/OpenHands-CLI
- Agent-sdk example: https://github.com/All-Hands-AI/agent-sdk/blob/main/examples/hello_world.py
- Personality strings: `grouch/strings.py`
- Change tracking: `GROUCH_CHANGES.md`

## Fork Structure & Remotes

```
Remotes:
  origin   → github.com/jpshackelford/open-grouch (push here)
  upstream → github.com/OpenHands/OpenHands-CLI   (sync from here)
```

### Syncing with Upstream
```bash
git fetch upstream
git checkout -b sync/upstream-$(date +%Y%m%d)
git merge upstream/main
# Resolve conflicts: keep our personality, take their functionality
git push origin sync/upstream-$(date +%Y%m%d)
# Create PR for review
```

### Automatic Releases (via release-please)
Releases are **automatic** when PRs merge to main:

1. Use conventional commit format in PR titles
2. Merge PR to main
3. release-please creates/updates a "Release PR" with version bump + changelog
4. When Release PR is merged → GitHub Release is created with wheel

**No manual version bumps needed!** Version is determined by commit types:
- `fix:` → patch bump (0.1.0 → 0.1.1)
- `feat:` → minor bump (0.1.0 → 0.2.0)
- `feat!:` or `BREAKING CHANGE:` → major bump (0.1.0 → 1.0.0)

## Project Structure & Module Organization

### Grouch-Specific (OUR CODE)
- `grouch/`: **All personality customizations live here**
  - `grouch/__init__.py` - Package init
  - `grouch/strings.py` - **Centralized user-facing text** (banners, messages, grumbles)
  - `grouch/theme.py` - Trash can green color theme
- `GROUCH_CHANGES.md`: Tracks all modifications to upstream files
- `.github/workflows/upstream-sync.yml`: Automated weekly upstream sync

### Upstream Code (MINIMIZE CHANGES)
- `openhands_cli/`: Core CLI/TUI code - **modify sparingly, prefer imports from grouch/**
  - `openhands_cli/theme.py` - Import `grouch/theme.py` here
  - `openhands_cli/tui/content/splash.py` - Import `grouch/strings.py` for banner/messages
  - `openhands_cli/tui/widgets/` - Import strings for UI text
- `tests/`: Pytest suite - mirrors source layout
- `scripts/acp/`: JSON-RPC helpers; `hooks/`: PyInstaller hooks
- Tooling: `Makefile`, `build.sh`, `build.py`, `openhands-cli.spec`, `uv.lock`

## Setup, Build, and Development Commands
This repository uses **uv** for dependency management and running tooling (such as in `Makefile`, CI workflows, and `uv.lock`). Avoid using `pip install ...` directly if possible.

- install dependencies: `make install` (runs `uv sync`)
- install dev dependencies: `make install-dev` (runs `uv sync --group dev`)
- install pre-commit hooks: `uv run pre-commit install` (included in `make build`)
- build (sync + install hooks): `make build`
- lint (all pre-commit hooks): `make lint`
- format: `make format`
- run the Textual TUI (interactive; prefer running inside tmux so you can detach with `Ctrl+b d`): `make run` (or `uv run openhands`)
- run the Textual TUI (automation-friendly; use for agent-driven runs): `uv run openhands --exit-without-confirmation` (quit with `Ctrl+Q`; `Ctrl+C` does not work once the TUI is running)

- run the browser-served web app (Textual `textual-serve`): `openhands web`
- run the Docker-based OpenHands GUI server: `openhands serve`
- run the ACP entrypoint: `uv run openhands-acp`
- run unit/integration tests: `make test` (for faster runs: `uv run pytest -m "not integration" --ignore=tests/snapshots`)
- run snapshot tests (Textual UI): `make test-snapshots` (or `uv run pytest tests/snapshots -v`; use `--snapshot-update` when updating snapshots)
- run binary tests: `make test-binary` (or `uv run pytest tui_e2e`)
- run unit/integration + snapshot tests together: `make test-all`
- build PyInstaller binaries: `./build.sh --install-pyinstaller`

## Development Guidelines

### Linting Requirements
**Before any commit, run `make lint` and only commit after it passes.** Use `make lint` to run all pre-commit hooks on all files, and do it before every commit (not after) to avoid CI failures.

### Typing Requirements
Prefer modern typing syntax (`X | None` over `Optional[X]`) in new code.

### Documentation Guidelines
- Don’t add new root-level `.md` files or “summary updates” to `README.md` unless explicitly requested (use this `AGENTS.md` for repo guidance).

## Coding Style & Naming Conventions
- Python 3.12, ruff formatting (88-char line limit, double quotes).
- Ruff enforced rules: pycodestyle, pyflakes, isort, pyupgrade, unused-arg checks (tests allow fixture-style args), and guards against mutable defaults.
- Keep modules/dirs snake_case; classes in CapWords; user-facing commands/flags kebab-case as in existing entrypoints.
- Type checking via `pyright` (`uv run pyright`); prefer type hints on new functions and public interfaces.

## Testing Guidelines
- Unit/integration tests live under `tests/` (excluding `tests/snapshots`) and run via `make test`.
- Snapshot tests live under `tests/snapshots/` and run via `make test-snapshots`.
- Binary tests live under `tui_e2e/` and run via `make test-binary`.
- Pytest discovery: files `test_*.py`, classes `Test*`, functions `test_*`. Use `@pytest.mark.integration` for costly flows.
- Match test locations to implementation (`tests/` mirrors `openhands_cli/`); add fixtures in `tests/conftest.py` when shared.
- Run `make test` before PRs; run snapshot/binary tests when relevant to the change.

### Binary Tests with Mock LLM
- Binary tests in `tui_e2e/` can use `mock_llm_server.py` for deterministic testing without real LLM calls.
- The mock LLM server provides OpenAI-compatible endpoints with proper tool call format.
- Use `openai/gpt-4o-mock` as the model name (litellm requires a provider prefix).

## Snapshot Testing with pytest-textual-snapshot
The CLI uses [pytest-textual-snapshot](https://github.com/Textualize/pytest-textual-snapshot) for visual regression testing of Textual UI components. Snapshots are SVG screenshots that capture the exact visual state of the application.

### Running Snapshot Tests

```bash
# Run all snapshot tests
make test-snapshots
# or: uv run pytest tests/snapshots/ -v

# Update snapshots when intentional UI changes are made
uv run pytest tests/snapshots/ --snapshot-update
```

### Snapshot Test Location
- **Test files**: `tests/snapshots/test_app_snapshots.py`, `tests/snapshots/test_visualizer_snapshots.py`
- **Generated snapshots**: `tests/snapshots/__snapshots__/test_app_snapshots/*.svg`, `tests/snapshots/__snapshots__/test_visualizer_snapshots/*.svg`

### Writing Snapshot Tests
Snapshot tests must be **synchronous** (not async). The `snap_compare` fixture handles async internally:

```python
from textual.app import App, ComposeResult
from textual.widgets import Static, Footer


def test_my_widget(snap_compare):
    """Snapshot test for my widget."""

    class MyTestApp(App):
        def compose(self) -> ComposeResult:
            yield Static("Content")
            yield Footer()

    assert snap_compare(MyTestApp(), terminal_size=(80, 24))
```

#### Using `run_before` for Setup
To interact with the app before taking a screenshot:

```python
def test_with_interaction(snap_compare):
    class MyApp(App):
        def compose(self) -> ComposeResult:
            yield InputField(id="input")

    async def setup(pilot):
        input_field = pilot.app.query_one(InputField)
        input_field.input_widget.value = "Hello!"
        await pilot.pause()

    assert snap_compare(MyApp(), terminal_size=(80, 24), run_before=setup)
```

#### Using `press` for Key Simulation

```python
def test_with_focus(snap_compare):
    assert snap_compare(
        MyApp(),
        terminal_size=(80, 24),
        press=["tab", "tab"],  # Press tab twice to move focus
    )
```

### Viewing Snapshots Visually
To view the generated SVG snapshots in a browser:

1. **Start a local HTTP server** in the snapshots directory:
   ```bash
   cd tests/snapshots/__snapshots__/test_app_snapshots
   python -m http.server 12000
   ```

2. **Open in browser** using the work host URL:
   ```
   https://work-1-<id>.prod-runtime.all-hands.dev/<snapshot-name>.svg
   ```

   Example snapshot names:
   - `TestExitModalSnapshots.test_exit_modal_initial_state.svg`
   - `TestVisualizerSnapshots.test_multiple_actions_alignment.svg`

3. **Stop the server** when done:
   ```bash
   pkill -f "python -m http.server 12000"
   ```


### Snapshot Best Practices
- Mock external dependencies so snapshots are deterministic.
- Always pass a fixed `terminal_size=(width, height)`.
- Commit SVG snapshots.
- Review snapshot diffs carefully.


## Commit & Pull Request Guidelines

### Conventional Commits (Required)
All PR titles **must** follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>[optional scope]: <description>

Examples:
  feat: add grouchy welcome banner
  fix(tui): correct splash screen alignment  
  grouch: update Oscar personality strings
  sync: merge upstream OpenHands-CLI changes
  docs: update installation instructions
  ci: add conventional commit linting
```

**Types that trigger releases:**
| Type | Version Bump | Description |
|------|--------------|-------------|
| `feat` | Minor (0.1.0 → 0.2.0) | New feature |
| `fix` | Patch (0.1.0 → 0.1.1) | Bug fix |
| `feat!` | Major (0.1.0 → 1.0.0) | Breaking change |

**Other types (no release):**
| Type | Description |
|------|-------------|
| `grouch` | Personality/theme changes |
| `sync` | Upstream sync |
| `docs` | Documentation |
| `style` | Formatting |
| `refactor` | Code refactoring |
| `test` | Tests |
| `ci` | CI/CD changes |
| `chore` | Maintenance |

### PR Types

**1. Personality PRs** (most common)
- Prefix title with `[grouch]`
- Focus: Adding/modifying personality text, theme colors, UI tone
- Files: Primarily `grouch/`, minimal `openhands_cli/` changes
- **Always update `GROUCH_CHANGES.md`** if touching upstream files

**2. Upstream Sync PRs**
- Created automatically by GitHub Actions or manually
- Title: `Sync with upstream OpenHands-CLI (abc1234)`
- Review carefully for conflicts with personality changes

### Development Workflow for Personality Changes

1. **Check `grouch/strings.py`** - Is the text you need already defined? If not, add it there first.
2. **Modify upstream file minimally** - Just add the import and swap the string reference
3. **Update `GROUCH_CHANGES.md`** - Document what file you changed and why
4. **Run verification** - `make lint && make test`
5. **Update snapshots if needed** - `uv run pytest tests/snapshots --snapshot-update`

### Example: Adding a Grouchy Message

```python
# Step 1: In grouch/strings.py - ADD the new string
CONFIRM_EXIT = "Leaving already? ...Not that I'll miss you or anything."

# Step 2: In openhands_cli/tui/modals/exit_modal.py - IMPORT and USE
from grouch.strings import CONFIRM_EXIT
# ... replace hardcoded string with CONFIRM_EXIT

# Step 3: Update GROUCH_CHANGES.md with the new file modification
```

### Verification Before PR
1. `make lint`
2. `make test`
3. If TUI touched: `make test-snapshots` (use `--snapshot-update` for intentional changes)
4. If ACP/binary touched: `make test-binary`

### PR Submission Checklist
- [ ] Personality changes centralized in `grouch/strings.py` where possible
- [ ] `GROUCH_CHANGES.md` updated if any upstream files modified
- [ ] `make lint` passes
- [ ] `make test` passes
- [ ] (If TUI touched) Snapshots updated and reviewed
- [ ] PR description explains the personality change and lists files modified


## Security & Configuration Tips
- Do not embed API keys or endpoints in code; rely on runtime configuration/env vars when integrating new services.
- When packaging, verify no sensitive files are included in `dist/`; adjust `openhands-cli.spec` if new assets are added.

## TUI State Management Architecture

The TUI uses a reactive state management pattern with clear separation of concerns. Key files are in `openhands_cli/tui/core/`.

### Core Components

**ConversationContainer (`state.py`)** - Reactive state holder
- A Textual `Container` widget that owns all conversation-related reactive properties
- Properties include: `running`, `conversation_id`, `conversation_title`, `confirmation_policy`, `pending_action_count`, `elapsed_seconds`, `metrics`
- UI widgets bind to these properties via `data_bind()` and auto-update when state changes
- Provides thread-safe state update methods (e.g., `set_running()`, `set_conversation_id()`)
- Composes the main UI hierarchy: `ScrollableContent` + `InputAreaContainer`

**ConversationManager (`conversation_manager.py`)** - Message router
- A thin Textual `Container` that listens to messages and delegates to controllers
- Owns: `RunnerRegistry`, `ConfirmationPolicyService`, and all controllers
- Message handlers (`@on(MessageType)`) route to appropriate controllers
- Provides public API methods that post messages internally

**Controllers** - Single-responsibility business logic
- `UserMessageController` - Handles user input, renders messages, queues/processes with runner
- `ConversationCrudController` - Creates new conversations, resets state
- `ConversationSwitchController` - Orchestrates switching (pause current, prepare new)
- `ConfirmationFlowController` - Shows confirmation panel, handles user decisions

**RunnerFactory + RunnerRegistry** - Runner lifecycle
- `RunnerFactory` - Creates `ConversationRunner` instances with dependencies
- `RunnerRegistry` - Caches runners by conversation_id, tracks current runner

### Widget Hierarchy

```
OpenHandsApp
└── ConversationManager(Container)  ← message router
    └── ConversationContainer(#conversation_state)  ← reactive state
        ├── ScrollableContent(#scroll_view)  ← binds to conversation_id, pending_action_count
        │   ├── SplashContent(#splash_content)  ← binds to conversation_id
        │   └── ... dynamically added conversation widgets
        └── InputAreaContainer(#input_area)  ← handles slash commands
            ├── WorkingStatusLine  ← binds to running, elapsed_seconds
            ├── InputField  ← binds to conversation_id, pending_action_count
            └── InfoStatusLine  ← binds to running, metrics
```

### Data Flow

1. **User input** → `InputField` posts `UserInputSubmitted` → bubbles to `ConversationManager` → `UserMessageController.handle_user_message()`
2. **Slash commands** → `InputField` posts `SlashCommandSubmitted` → `InputAreaContainer` routes to command handlers → posts operation messages (e.g., `CreateConversation`)
3. **State changes** → Controllers call `ConversationContainer.set_*()` methods → reactive properties update → bound widgets auto-refresh
4. **Cross-thread updates** → `ConversationContainer._schedule_update()` uses `call_from_thread()` for thread safety

### Key Design Principles

- **Reactive state**: UI components bind to `ConversationContainer` properties via `data_bind()`, auto-update on changes
- **Single source of truth**: `ConversationContainer` owns all conversation state
- **Thread safety**: State updates use `call_from_thread()` when called from background threads
- **Message-based communication**: Components communicate via Textual messages that bubble up the widget tree
- **Controller pattern**: Business logic split into focused controllers, `ConversationManager` is just a router
