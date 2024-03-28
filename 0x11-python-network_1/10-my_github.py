#!/usr/bin/python3
"""
takes your GitHub credentials
"""


if __name__ == '__main__':
    import requests
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    url = f'https://api.github.com/users'
    response = requests.get(url, auth=(username, password))
    json = response.json()
    if 'id' in json:
        print(json['id'])
    else:
        print(None)
