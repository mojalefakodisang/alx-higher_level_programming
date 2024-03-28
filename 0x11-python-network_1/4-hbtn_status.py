#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    req_content = req.content.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(req_content)}")
    print(f"\t- content: {req_content}")
