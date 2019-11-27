#!/usr/bin/env python3
import itertools
import threading
import hashlib
import time
from sys import argv

# This script calculates the hashes of all the combinations of two words in a
# wordlist, searching for a given one

def thread_function(words, md5, i):
    for combination in words:
        word = combination[0] + combination[1]
        if md5 == hashlib.md5(word).hexdigest():
            print('Found %s' % word)
            return

        word = combination[1] + combination[0]
        if md5 == hashlib.md5(word).hexdigest():
            print('Found %s' % word)
            return


def solve(md5, filename):
    words = open(filename, 'r').read().split('\n')[:-1]

    for combination in itertools.combinations_with_replacement(words, 2):
        word = combination[0] + combination[1]
        if md5 == hashlib.md5(word).hexdigest():
            print('Found %s' % word)
            return

        word = combination[1] + combination[0]
        if md5 == hashlib.md5(word).hexdigest():
            print('Found %s' % word)
            return


def main():
    if len(argv) != 3:
        print('Usage: ./%s <hash> <file>' % argv[0])
        exit(1)

    md5 = argv[1]
    wordlist = argv[2]
    solve(md5, wordlist)


if __name__ == '__main__':
    main()
