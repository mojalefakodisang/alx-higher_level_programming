#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the variable X-Request-Id
"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    if 'X-Request-Id' in req.headers:
        print(req.headers['X-Request-Id'])
