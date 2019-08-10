import hashlib
import requests
from sys import argv
from bs4 import BeautifulSoup

"""
This script makes a request to a url, extracts the string inside h3 tags,
computes the md5 and sends it back.
Used to solve Emdeefive challenge from HackTheBox.
"""
# Input check
if len(argv) != 2:
    print('Usage: %s <url>' % argv[0])
    exit(1)

# URL creation
url = argv[1]
if not url.startswith('http://'):
    url = 'http://' + url

# Initializations
m = hashlib.md5()
sess = requests.Session()

# Make the first request to get the string to hash
page = sess.post(url)

# Initialize soup with the received HTML code
soup = BeautifulSoup(page.text, "lxml")

# Parse the page to find the string contained in the h3 tag
s = soup.find('h3').text

# Encode the string in MD5
m.update(s.encode())

# POST payload
data = {'hash': m.hexdigest()}

# Send MD5 hash
page = sess.post(url, data=data)

# Initialize soup with second response
soup = BeautifulSoup(page.text, "lxml")

# Print the flag
print(soup.find('p').text)
