"""
fogsift-icarus CLI entry point.

Usage:
    icarus --version
    icarus info
"""

import argparse
import sys

from . import __version__, __url__


def main():
    parser = argparse.ArgumentParser(
        prog="icarus",
        description="fogsift-icarus — AI-augmented daily workflow system.",
    )
    parser.add_argument(
        "--version", "-V",
        action="version",
        version=f"fogsift-icarus {__version__}",
    )
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("info", help="Print system info and links.")

    args = parser.parse_args()

    if args.cmd == "info" or args.cmd is None:
        print(f"fogsift-icarus v{__version__}")
        print(f"Repo:  {__url__}")
        print(f"Docs:  {__url__}#readme")
        print()
        print("The harness lives at _experiments/SimpleAgentOS/")
        print("Run: python3 preflight.py  (inside SimpleAgentOS/)")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
