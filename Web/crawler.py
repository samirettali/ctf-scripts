#!/usr/bin/env python3
import os
import sys
import time
import urllib
import argparse
import requests
import web_pdb
import logging
from termcolor import colored
from urllib import parse
from bs4 import BeautifulSoup


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')



def is_visitable(url, urls):
    for u in urls:
        if u.replace('http://', '').replace('https://', '') in url:
            return True
    return False


def main():
    urls = set()
    visited = set()
    domain = False

    parser = argparse.ArgumentParser('Website crawler, links gatherer')
    parser.add_argument('-f', dest='read', type=str, help='Name of the file containing the urls')
    parser.add_argument('-u', dest='url', type=str, help='The url to start from')
    parser.add_argument('-o', dest='out_file', type=str, default='links.txt', help= 'The name of the file to write results to')
    parser.add_argument('-d', dest='domain', type=str2bool, default=False, help= 'Visit links outside of the domain')

    args = parser.parse_args()

    if args.read:
        with open(args.read) as f:
            urls = set(f.read().splitlines())

    if args.url:
        urls.add(args.url.strip())

    if not args.domain:
        domain = args.domain

    if args.out_file:
        f = open(args.out_file, 'a')

    urllib3_logger = logging.getLogger('urllib3')
    urllib3_logger.setLevel(logging.CRITICAL)

    starting_urls = set()
    for url in urls:
        starting_urls.add(url)

    while urls:
        try:
            url = urls.pop()
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url
            if not domain or (domain and is_visitable(url, starting_urls)):
                response = requests.get(url)

                print('%s Visiting %s status: %d, length: %d' % (colored('[*]', 'blue'), url, response.status_code, len(response.text)))
                if args.out_file:
                    f.write(url + '\n')

                soup = BeautifulSoup(response.text, 'html.parser')
                visited.add(url)
                n = 0

                for link in soup.find_all('a'):
                    new_link = link.get('href')
                    if new_link and len(new_link) > 0 and new_link != '#':
                        if 'http' not in new_link:
                            new_link = urllib.parse.urljoin(url, new_link)
                        if not domain or (domain and is_visitable(url, starting_urls)):
                            if new_link not in visited and new_link not in urls and new_link != url:
                                print('  %s Found new link %s' % (colored('[+]', 'green'), new_link))
                                n += 1
                                urls.add(new_link)

                for link in soup.find_all('link'):
                    new_link = link.get('href')
                    if new_link and len(new_link) > 0 and new_link != '#':
                        if 'http' not in new_link:
                            new_link = urllib.parse.urljoin(url, new_link)
                        if not domain or (domain and is_visitable(url, starting_urls)):
                            if new_link not in visited and new_link not in urls and new_link != url:
                                print('  %s Found new link %s' % (colored('[+]', 'green'), new_link))
                                n += 1
                                urls.add(new_link)
        except Exception as e:
            print('%s Error while visiting %s ' % (colored('[-]', 'red'), url))

    if args.out_file:
        f.close()


if __name__ == '__main__':
        main()
