#!/usr/bin/env bash

set -euf -o pipefail

WORDLIST="xato-net-10-million-passwords-100.txt"

while true; do
    for file in $(ls); do
        if [ $(file --mime-type -b "$file") == "application/gzip" ]; then
            echo "Extracting $file as gzip"
            gunzip < "$file" > $(date +%s%N)
            rm "${file}"
        elif [ $(file --mime-type -b "$file") == "application/x-xz" ]; then
            echo "Extracting $file as xz"
            unxz "$file" > /dev/null
            rm "${file}"
        elif [ $(file --mime-type -b "$file") == "application/x-tar" ]; then
            echo "Extracting $file as tar"
            tar -xf "$file" > /dev/null
            rm "${file}"
        elif [ $(file --mime-type -b "$file") == "application/zip" ]; then
            if 7z l -slt "${file}" | grep -q ZipCrypto; then
                echo "Cracking ${file} as zip"
                temp=$(mktemp)
                sudo zip2john "${file}" >> "${temp}" 2>/dev/null
                sudo john --wordlist="${WORDLIST}" "${temp}" > /dev/null 2>/dev/null
                password=$(sudo john ${temp} --show | head -n 1 | cut -d':' -f 2 | tr -d '\n')
                unzip -B -P "${password}" "${file}" > /dev/null
                rm ${temp}
                rm "${file}"
            else
                echo "Extracting $file as zip"
                unzip -B "${file}" > /dev/null
                rm "${file}"
            fi
        fi

    done
done
