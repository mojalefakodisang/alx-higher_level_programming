#!/usr/bin/python3
import urllib.request

url = 'http://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content_type = response.headers.get('Content-Type')
        content = response.read()
        utf_content = content.decode('utf8')
        heading = f"Body response:\n"
        c_type = f"\t- type: {type(content)}\n"
        c_content = f"\t- content {content}\n"
        c_utf = f"\t- utf8 content: {utf_content}"

        print(heading + c_type + c_content + c_utf)
except Exception as e:
    print(e)
