import requests
import time
from stem import Signal
from stem.control import Controller
from scapy.all import *


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
    visit('https://www.0xf.at/data/imgs/66b43ad6d3f3560b210c1f94171dee61.jpg', 50)


if __name__ == '__main__':
    main()
