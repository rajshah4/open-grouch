"""OpenHands ACP Entry Point.

This module provides the entry point for the grouch-acp CLI command.
"""

import asyncio

from openhands_cli.acp_impl.agent import run_acp_server


def main():
    """Run the ACP server."""
    asyncio.run(run_acp_server())


if __name__ == "__main__":
    main()
