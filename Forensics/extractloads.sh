#!/bin/sh

# Extract all loads from elf dump

if [ -z "$1" ]; then
    echo "Usage: $0 file.elf"
    exit 1
fi

filename=$1
loads=$(objdump -h $1 | grep load)

mkdir -p loads;
while read -r line;
do
    loadname=$(echo $line | awk {'print $2'})
    size=$(echo $line | awk {'print $3'})
    offset=$(echo $line | awk {'print $6'})
    size="0x$size"
    offset="0x$offset"
    echo "Extracting $loadname"
    head -c $(($size+$offset)) $filename | tail -c +$(($offset+1)) > loads/$loadname.raw
done <<< "$loads"
