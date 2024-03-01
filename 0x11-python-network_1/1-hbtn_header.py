#!/usr/bin/python3

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Check if 'X-Request-Id' is present in the response headers
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
        else:
            print("X-Request-Id not found in the response headers.")
except urllib.error.URLError as e:
    print(f"Error: {e.reason}")
