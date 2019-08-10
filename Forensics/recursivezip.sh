#!/bin/sh

# Recursively exctract encrypted archives using the contained archive name as
# password until it fails

if [ -z "$1" ]; then
    echo "Usage: $0 <archive.zip>"
    exit 1
fi

archive=$1

while [ -f $archive ]; do
    file=$(zipinfo $archive | grep "\--" | awk '{print $9}')
    pass=$(echo $file | awk -F"." '{print $1}')
    unzip -P $pass $archive
    archive=$file
done
