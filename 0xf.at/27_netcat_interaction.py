#!/usr/bin/env python3
import socket


# This script connects to a server and receives math expressions and solves them


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('212.17.118.125', 2727))
    print(s.recv(1024))
    s.send('GO'.encode())

    # Get the first question
    question = s.recv(1024).decode().replace('=?\n', '')

    while '*' in question:
        s.send(str(eval(question)).encode())
        print(s.recv(1024).decode())
        question = s.recv(1024).decode().replace('=?\n', '')

if __name__ == '__main__':
    main()
