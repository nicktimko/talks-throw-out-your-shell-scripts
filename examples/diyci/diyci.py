#!/usr/bin/env python3
"""
A DIY CI toolchain.
"""
import subprocess
import sys


target = "pylint_target_file.py"


def main():
    proc = subprocess.run(["python3", "-m", "pylint", target])

    # Pylint exit codes: 1=fatal, 2=error, 4=warning, 32=usage error
    if proc.returncode & (1 | 2 | 32):
        print("pylint found an error", file=sys.stderr)
        return 1

    print("success")


if __name__ == "__main__":
    sys.exit(main())
