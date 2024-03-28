#!/usr/bin/python3
"""
    sends a request to the URL and displays the body of the response
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            decode = content.decode('utf-8')
            print(decode)
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
