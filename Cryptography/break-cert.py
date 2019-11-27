#!/usr/bin/env python3
import primefac
import OpenSSL.crypto
from sys import argv

# This script tries to break a PEM certificate that uses weak primes

def main():
    if len(argv) != 2:
        print('Usage: ./%s <pem_file>')
        exit(1)

    cert = OpenSSL.crypto.load_certificate(
        OpenSSL.crypto.FILETYPE_PEM,
        open(argv[1]).read()
    )

    pubkey = cert.get_pubkey().to_cryptography_key().public_numbers()

    factors = primefac.factorint(pubkey.n)
    factors = [int(n) for n in factors.keys()]

    print(factors)

if __name__ == '__main__':
    main()
