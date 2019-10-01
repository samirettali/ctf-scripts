#!/bin/bash

# Extracts a tar files containg a tar file again and again, until the are no
# more

if [ -z "$1" ]; then
    echo "Usage $0 <archive.tar>"
    exit 1
fi

archive="$1"

while [ -f "$archive" ]; do
    echo "Extracting $archive"
    tar -xf "$archive"
    rm "$archive"
    archive=$(ls -1 *.tar)
done
