#!/usr/bin/env python2
from sys import argv
from pwn import *
import magic


# This script runs a bruteforce againts xor encrypted files and tries to
# recognize them by the header


def xor_brute(filename):
    data = open(filename, 'rb').read()
    for i in range(256):
        xor_data = xor(data, i)
        filetype = magic.from_buffer(xor_data)
        if filetype != 'data':
            print('0x%x -> %s' % (i, filetype))


def xor_key(filename, key):
    data = open(filename, 'rb').read()
    dst_file = filename + '.xor'
    destination = open(dst_file, 'wb')
    xor_data = xor(data, key)
    filetype = magic.from_buffer(xor_data)
    if filetype != 'data':
        print('Written to %s' % dst_file)
    destination.write(xor_data)


def main():
    if len(argv) != 2 and len(argv) != 3:
        print('Usage: ./%s <file> [hex key]' % argv[0])
        exit(1)

    filename = argv[1]
    if len(argv) == 2:
        xor_brute(filename)
    else:
        key = int(argv[2], 16)
        if key < 0x0 or key > 0xFF:
            print('Error: the key must be between 0x00 and 0xFF')
            exit(1)
        xor_key(filename, key)


if __name__ == '__main__':
    main()

