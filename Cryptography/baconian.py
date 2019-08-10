#!/usr/bin/env python3
from sys import argv

def decode_baconian(ciphertext):
    alphabet = {
        'AAAAA': 'A',
        'AAAAB': 'B',
        'AAABA': 'C',
        'AAABB': 'D',
        'AABAA': 'E',
        'AABAB': 'F',
        'AABBA': 'G',
        'AABBB': 'H',
        'ABAAA': '[I|J]',
        'ABAAB': 'K',
        'ABABA': 'L',
        'ABABB': 'M',
        'ABBAA': 'N',
        'ABBAB': 'O',
        'ABBBA': 'P',
        'ABBBB': 'Q',
        'BAAAA': 'R',
        'BAAAB': 'S',
        'BAABA': 'T',
        'BAABB': '[U|V]',
        'BABAA': 'W',
        'BABAB': 'X',
        'BABBA': 'Y',
        'BABBB': 'Z'
    }

    for i in range(0, len(ciphertext), 5):
        try:
            print(alphabet[ciphertext[i:i + 5]], end='')
        except KeyError:
            print(' ', end='')
    print('')

def baconian(ciphertext):
    first_char = ciphertext[0]

    index = 0

    while index < len(ciphertext) and ciphertext[index] == first_char:
        index += 1

    second_char = ciphertext[index]

    first_ciphertext = ciphertext.replace(first_char, 'A')
    first_ciphertext = first_ciphertext.replace(second_char, 'B')

    second_ciphertext = ciphertext.replace(first_char, 'B')
    second_ciphertext = second_ciphertext.replace(second_char, 'A')

    decode_baconian(first_ciphertext)
    decode_baconian(second_ciphertext)

def main():
    if len(argv) != 2:
        print('Usage: %s <ciphertext>' % argv[0])
        exit(0)

    baconian(argv[1])

if __name__ == '__main__':
    main()
