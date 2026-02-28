#!/usr/bin/env python3
"""Entry point for Open Grouch CLI.

This module provides the main entry point for the 'grouch' command,
wrapping the OpenHands CLI with Oscar the Grouch personality.
"""

from openhands_cli.entrypoint import main as openhands_main


def main() -> None:
    """Main entry point for the Open Grouch CLI."""
    openhands_main()


if __name__ == "__main__":
    main()
