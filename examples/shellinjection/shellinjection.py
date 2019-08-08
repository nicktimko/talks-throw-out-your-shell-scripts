#!/usr/bin/env python3
"""
Why shell=True can be dangerous

echo '%an\' > /tmp/wuzhere #'
"""
import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-u", "--unsafe", action="store_true")
    args = parser.parse_args()

    # get desired log format
    default = "%an|%ae"
    fmt = input(f"git-log format (default: {default}): ")
    fmt = fmt.strip()
    if not fmt:
        fmt = default

    if args.unsafe:
        subprocess.run(f"git log -n1 --format='{fmt}'", shell=True)
    else:
        subprocess.run(["git", "log", "-n1", f"--format={fmt}"])


if __name__ == "__main__":
    sys.exit(main())
