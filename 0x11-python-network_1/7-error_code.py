#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code != 200:
        print(f'Error code: {req.status_code}')
    else:
        print(req.text)
