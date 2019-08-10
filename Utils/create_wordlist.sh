#!/bin/bash

# This script creates a wordlist from a file
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <file> <wordlist>"
    exit 1
fi

grep -o -E '\w+' "$1" | sort -u > "$2"
