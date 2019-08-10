#!/usr/bin/env python3
from sys import argv

# This script reads a file containing binary bits as a string and converts them
# in ASCII grouping by 7 bits (similar to base64)

def convert(binary):
    if len(binary) % 7 != 0:
        print('Error: the text length must be a multiple of 7')
        exit(1)

    for i in range(0, len(binary), 7):
        char_hex = int(binary[i:i+7], 2)
        print(chr(char_hex).lower(), end='')
    print()

def main():
    if len(argv) != 2:
        print('Usage: ./%s <file>' % argv[0])
        exit(1)

    text = open(argv[1], 'r').read()
    convert(text)

if __name__ == '__main__':
    main()
