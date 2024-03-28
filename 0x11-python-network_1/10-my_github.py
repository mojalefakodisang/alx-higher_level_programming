#!/usr/bin/python3
"""
takes your GitHub credentials
"""


if __name__ == '__main__':
    import requests
    import sys
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))
    if 'id' in response.json():
        print(response.json()['id'])
    else:
        print(None)
