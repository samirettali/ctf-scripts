#!/usr/bin/env python3
import string
from sys import argv


# This scripts takes a list of scrambled words and returns a list of unscrambled words searching in a given wordlist, example:
# Input: masmei;ixamme;ineram;vpamrie
# Output: sammie;maxime;marine;vampire


def find_correct_word(word, sorted_wordlist):
    word = sorted(word)
    for i in range(len(sorted_wordlist)):
        if word == sorted_wordlist[i]:
            return i
    return -1


def find_words(words, wordlist):
    wordlist = open(wordlist, 'r').read().split('\n')[:-1]
    sorted_wordlist = wordlist[:]
    words = words.split(';')

    for i in range(len(wordlist)):
        sorted_wordlist[i] = sorted(sorted_wordlist[i])

    correct_words = ''
    for word in words:
        correct_word_index = find_correct_word(word, sorted_wordlist)
        correct_words += wordlist[correct_word_index] + ';'

    return correct_words[:-1]


def main():
    if len(argv) != 3:
        print('Usage: ./%s <string> <wordlist>' % argv[0])
        exit(1)

    words = argv[1]
    wordlist = argv[2]
    print(find_words(words, wordlist))


if __name__ == '__main__':
    main()
