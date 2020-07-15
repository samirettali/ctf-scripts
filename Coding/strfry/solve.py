#!/usr/bin/env python3

import time
from strfry import *
from pwn import remote, process


r = remote('ctf.umbccd.io', 5100, level='error')

lines = r.recvlines(5)
line = r.recvline()
pid = int(line.decode().split(':')[1].split(',')[0].strip())
r.recvlines(4)

ts = int(time.time())
p = process(f'./scramble {pid} {ts}', shell=True, level='error')

print(f'PID: {pid}')
for i in range(30):
    line = r.recvline().decode()
    if 'Wrong' in line:
        print(line)
        exit()
    flag = line.split(': ')[1].strip()

    p.sendline(flag)
    scrambled = p.recvline()

    print(scrambled.decode())
    r.sendline(scrambled)

print(r.recvall())
