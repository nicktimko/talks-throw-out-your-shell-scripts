#!/usr/bin/env python
"""
If this script is called outside of the directory it's in (alongside
the roman-numerals.txt file), it will fail, because it's a relative path,
relative with respect to the current working directory.
"""
import argparse
import sys

def main():
    with open("roman-numerals.txt") as f:
        lines = (line.strip() for line in f)
        numerals = [line.upper() for line in lines if line]

    try:
        n = int(input("Enter an integer between 1 and 10: "))
    except ValueError:
        print("That wasn't a number.", file=sys.stderr)
        return 1

    print(numerals[n-1])

if __name__ == "__main__":
    sys.exit(main())
