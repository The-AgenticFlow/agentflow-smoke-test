#!/usr/bin/env python3
"""Minimal calculator CLI for AgentFlow smoke test."""
import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    if len(sys.argv) != 4:
        print("Usage: calc.py <add|subtract> <num1> <num2>")
        sys.exit(1)
    op = sys.argv[1]
    if op not in ("add", "subtract"):
        print(f"Unknown operation: {op}")
        sys.exit(1)
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    if op == "add":
        print(add(a, b))
    else:
        print(subtract(a, b))


if __name__ == "__main__":
    main()
