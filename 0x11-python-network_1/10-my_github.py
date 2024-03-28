#!/usr/bin/python3
"""
takes your GitHub credentials
"""


if __name__ == '__main__':
    import requests
    import sys
    user = sys.argv[1]
    passwrd = sys.argv[2]
    url = f'https://api.github.com/users/{user}'
    response = requests.get(url, auth=(user, passwrd))
    print(response.json())
    if 'id' in response.json():
        print(response.json()['id'])
    else:
        print(None)
