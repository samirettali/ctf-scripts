#!/usr/bin/env python3
import string
from sys import argv

# This script replaces symbols that represent a character with a single
# character, useful to solve substitution ciphers.

def main():
    if len(argv) < 2:
        print('Usage: ./%s <string>')

    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()-=\\_+|[]{};\':",./<>?'
    s = ' '.join(s for s in argv[1:])

    converted = ''
    d = {}

    try:
        for symbol in s.split(' '):
            if not symbol in d:
                d[symbol] = alphabet[len(d)]
            converted += d[symbol]
    except:
        print('String has too many symbols, here is the first part: %s' %
                converted)
        exit(1)

    print(converted)

if __name__ == '__main__':
    main()
