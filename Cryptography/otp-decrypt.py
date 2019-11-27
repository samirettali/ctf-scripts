#!/usr/bin/env python3
from sys import argv

# One time pad decrypt


def decrypt(cipher_text, key):
    clear_text = ''
    starting_char = ord('A')
    for i in range(len(cipher_text)):
        # Character to decrypt
        cipher_char = ord(cipher_text[i])

        # Key character to use for decryption
        key_char = ord(key[i % len(key)])

        # Shift calculation
        shift = key_char - starting_char

        # Decryption
        clear_char = cipher_char - shift

        # Check if the decrypted character is between bounds
        if clear_char < starting_char:
            clear_char += 26

        # Adding character to clear text
        clear_text += chr(clear_char)
    return clear_text


def main():
    if len(argv) != 3:
        print('Usage: ./%s <cipher_text> <key>')
        exit(1)

    print(decrypt(argv[1].upper(), argv[2].upper()))


if __name__ == '__main__':
    main()
