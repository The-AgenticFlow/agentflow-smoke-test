#!/usr/bin/env python3
"""Minimal calculator CLI for AgentFlow smoke test."""
import argparse
import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def parse_args():
    """Parse command line arguments, handling negative numbers correctly."""
    parser = argparse.ArgumentParser(
        description="Minimal calculator CLI",
        usage="calc.py <add|subtract> <num1> <num2>",
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract"],
        help="Operation to perform ('add' or 'subtract')",
    )
    parser.add_argument(
        "num1",
        type=int,
        help="First number",
    )
    parser.add_argument(
        "num2",
        type=int,
        help="Second number",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.operation == "add":
        print(add(args.num1, args.num2))
    elif args.operation == "subtract":
        print(subtract(args.num1, args.num2))


if __name__ == "__main__":
    main()
