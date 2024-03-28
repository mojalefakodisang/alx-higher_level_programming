#!/usr/bin/python3
""" Script that fetches a URL"""


if __name__ == "__main__":
    import urllib.request
    url = 'http://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    print("Body response:")
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf8')}")
