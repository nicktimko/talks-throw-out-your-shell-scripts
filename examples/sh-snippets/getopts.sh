#!/bin/sh

while getopts ":x:" o; do
    case "${o}" in
        x)
            x=${OPTARG}
            ;;
        *)
            echo "Unknown argument. Usage: $0 [-x VALUE]"
            exit 1
            ;;
    esac
done

echo "x = ${x-UNSET}"
