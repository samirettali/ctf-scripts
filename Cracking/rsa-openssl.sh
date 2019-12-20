#!/usr/bin/env bash

if [ "$#" != 2 ]; then
        echo "USAGE: $0 <file> <wordlist>"
else

while read pass; do
    openssl rsautl -decrypt -inkey private.key -in "$1" -out plaintext.txt -passin pass:"$pass" &>/dev/null
    if [ "$?" == 0 ]; then
        echo "SUCESS - $pass"
        break
    fi
done < "$2"
fi
