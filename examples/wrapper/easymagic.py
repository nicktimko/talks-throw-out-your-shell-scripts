#!/usr/bin/env python
"""
Wrapper for the darkmagic executable.
"""
import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("booflark", help="Value of booflark")
    parser.add_argument("-a", "--adjective", help="Adjective", default="tiny")
    parser.add_argument("-n", "--noun", help="Noun", default="cow")
    args = parser.parse_args()

    executable = "./darkmagic"

    # Set up the environment and arguments as needed. This configuration
    # could be stored in a configuration file, or set via your favorite
    # CLI argument parser.
    subenv = {
        **os.environ,  # if we want to pass the parent process's environment
        "WIZ_VAL": args.booflark,
    }
    args = [
        executable,  # typically the 0th argument is the executable itself
        "dummy",
        args.adjective,
        "dummy",
        args.noun,
    ]

    os.execve(path=executable, argv=args, env=subenv)

    print("This NEVER gets run if the above succeeds.")
    print("os.exec* REPLACES this process")


if __name__ == "__main__":
    sys.exit(main())
