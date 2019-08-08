#!/bin/bash
# ^ sh doesn't have the math

set -o errexit
set -o nounset

TARGET="pylint_target_file.py"

echo "linting..."

# http://www.catb.org/~esr/jargon/html/V/voodoo-programming.html
(
    rc=0;
    pylint ${TARGET} || rc=$?;
    exit $(($rc & 35 )) # fatal=1 | error=2 | usage error=32
)

echo "eh, good enough."

black --check ${TARGET}
