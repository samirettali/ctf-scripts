import requests
import time
from stem import Signal
from stem.control import Controller
from scapy.all import *


# This script visits a url using tor network and changing identity for every
# visit


def visit(url, times):
    for i in range(times):
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate('password')
            controller.signal(Signal.NEWNYM)
            session = requests.session()
            session.proxies = {}
            session.proxies['http'] = 'socks5h://localhost:9050'
            session.proxies['https'] = 'socks5h://localhost:9050'
            r = session.get(url)
            ip = session.get('http://httpbin.org/ip').text
            print('[*] Visited %s from %s' % (url, ip))
            time.sleep(10)


def main():
    if len(argv) != 3:
        print('Usage: ./%s <url> <times>' % argv[0])
        exit(1)

    url = argv[1]
    times = argv[2]

    visit(url, times)


if __name__ == '__main__':
    main()
