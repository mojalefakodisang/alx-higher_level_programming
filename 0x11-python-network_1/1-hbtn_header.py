#!/usr/bin/python3
"""
    Script that sends a request to the URL and
    displays the value of the X-Request-Id
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
