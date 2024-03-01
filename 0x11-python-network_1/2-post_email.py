#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: {} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

print("Your email is:", email)

data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')

with urllib.request.urlopen(url, data) as response:
    body = response.read().decode('utf-8')
    print(body)
