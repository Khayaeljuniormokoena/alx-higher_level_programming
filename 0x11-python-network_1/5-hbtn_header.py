#!/usr/bin/python3

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    try:
        r_id = r.headers['X-Request-Id']
        print(r_id)
    except:
        pass
