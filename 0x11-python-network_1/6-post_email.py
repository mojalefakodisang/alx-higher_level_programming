#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    req = requests.post(url, data=data)
    print(req.text)
