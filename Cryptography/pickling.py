#!/usr/bin/env python3
import pickle
from sys import argv


def main():
    if len(argv) != 2:
        print('Usage: ./%s <file>' % argv[0])
        exit(1)

    with open(argv[1], 'rb') as f:
        o = pickle.load(f)

    outstr = ''
    for line in o:
        for char, n in line:
            outstr += char * n
        outstr += '\n'
    print(outstr)


if __name__ == '__main__':
    main()
