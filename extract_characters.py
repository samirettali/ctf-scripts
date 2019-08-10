#!/usr/bin/env pyhton3
from sys import argv
from os import path


"""
This script extracts some characters from a file
"""


if (len(argv) != 3):
    print('Usage: ./%s <src_file> <dst_file>' % argv[0])
    exit(1)

# Characters to extract from the file
characters = '[]+-.,<>'

src_file = argv[1]
dst_file = argv[2]

text = open(src_file).read()
result = ''

# Read the file and keep the chosen characters
for c in text:
    if c in characters:
        result += c

# Ask to overwrite the destination file if it does exist
if (path.isfile(dst_file)):
    print('File %s exists. Do you want to overwrite it? (Y/n)' % dst_file)
    choice = input()
    if (choice == 'n'):
        exit(0)

# Write the extracted content to the destination file
dst = open(dst_file, 'w')
dst.write(result)
dst.close()
print('Output written to %s' % dst_file)
