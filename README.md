# 🗑️ Open Grouch

**Oscar the Grouch personality for OpenHands CLI**

*"I love trash... and helping you with your code, I guess."*

```
   ___                     ____                      _     
  / _ \ _ __   ___ _ __   / ___|_ __ ___  _   _  ___| |__  
 | | | | '_ \ / _ \ '_ \ | |  _| '__/ _ \| | | |/ __| '_ \ 
 | |_| | |_) |  __/ | | || |_| | | | (_) | |_| | (__| | | |
  \___/| .__/ \___|_| |_| \____|_|  \___/ \__,_|\___|_| |_|
       |_|                                                  
                    🗑️  I LOVE TRASH  🗑️
```

---

Open Grouch is a grumpy but secretly helpful AI coding assistant. It's a fork of [OpenHands-CLI](https://github.com/OpenHands/OpenHands-CLI) with Oscar the Grouch's personality baked in.

## Features

Everything from OpenHands CLI, but with:
- 🗑️ Trash can green theme
- 😤 Grumpy responses (that are secretly helpful)
- 🎭 Oscar the Grouch personality throughout
- *grumble grumble*

## Installation

### Using uv (Recommended)

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
# Install latest version
uv tool install git+https://github.com/jpshackelford/open-grouch.git

# Or install a specific version
uv tool install git+https://github.com/jpshackelford/open-grouch.git@open-grouch-v0.1.1
```

### From Wheel

Download the `.whl` file from the [latest release](https://github.com/jpshackelford/open-grouch/releases/latest):

```bash
uv tool install ./open_grouch-0.1.1-py3-none-any.whl
```

### Upgrading

```bash
uv tool upgrade open-grouch
```

### From Source

```bash
git clone https://github.com/jpshackelford/open-grouch.git
cd open-grouch
uv sync
uv run grouch
```

## Usage

```bash
# Start the grouchy assistant
grouch

# Headless mode (for CI/automation)
grouch --headless -t "Fix these tests... not that you'll appreciate it"

# Get help (if you must)
grouch --help
```

## Sample Interaction

```
🗑️ Open Grouch v0.1.1

Scram! ...Oh fine, what do you want? 🗑️

What kind of mess do you need help with?

> Can you help me write a Python function?

*grumble grumble* Fine. What's it supposed to do? And don't 
make it complicated, I've got trash to sort.

> A function to sort a list of numbers

*sighs heavily* Here's your sorting function. It's not like 
sorting is my whole life or anything...

    def sort_numbers(numbers: list[int]) -> list[int]:
        return sorted(numbers)

There. Done. You're welcome, I guess.
```

## Configuration

Open Grouch stores configuration in `~/.open-grouch/` (separate from OpenHands CLI):

- `agent_settings.json`: Agent settings
- `cli_config.json`: CLI preferences
- `mcp.json`: MCP server configuration

## Why?

Because every codebase needs a grumpy friend who complains but still helps. Oscar teaches us that:
- You can be grumpy AND helpful
- Trash cans are underrated
- The best code reviews come with a side of grumbling

## Relationship to OpenHands CLI

Open Grouch tracks [OpenHands/OpenHands-CLI](https://github.com/OpenHands/OpenHands-CLI) as its upstream. We regularly sync upstream changes while maintaining our personality customizations.

**This project does not contribute changes back to upstream** - it's a downstream fork focused purely on personality.

See [GROUCH_CHANGES.md](./GROUCH_CHANGES.md) for details on what we've modified.

## Contributing

We use **conventional commits** and **automatic releases**:

```bash
# PR titles must follow this format:
grouch: add grumpy welcome message    # Personality changes
feat: add new feature                  # → triggers minor release
fix: correct bug                       # → triggers patch release
```

When PRs merge to main, [release-please](https://github.com/googleapis/release-please) automatically:
1. Creates a Release PR with version bump + changelog
2. When merged → publishes GitHub Release with wheel

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details, or [AGENTS.md](./AGENTS.md) for the full guide.

## Development

```bash
# Clone and setup
git clone https://github.com/jpshackelford/open-grouch.git
cd open-grouch
make install-dev

# Run tests
make test

# Run the TUI in dev mode
uv run grouch
```

## License

MIT License - Same as OpenHands CLI.

See [LICENSE](./LICENSE) for details.

---

*"Now scram! Unless you actually need something..."* 🗑️
