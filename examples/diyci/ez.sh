#!/bin/sh

set -o errexit
set -o nounset

TARGET="pylint_target_file.py"

echo "linting..."

pylint ${TARGET}

echo "eh, good enough."

black --check ${TARGET}

echo "SUCCESS"
