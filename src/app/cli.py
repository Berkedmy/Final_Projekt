import argparse
from .core import run_demo

def main() -> int:
    parser = argparse.ArgumentParser(prog="app")
    parser.add_argument("command", choices=["demo"])
    args = parser.parse_args()

    if args.command == "demo":
        run_demo()
        return 0

    return 0