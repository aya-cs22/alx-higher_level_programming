#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        body = response.read()
        utf8_content = body.decode('utf-8') # Decode the body to a UTF-8 string
        print(f'Body response:')
        print(f'\t- type: {type(body)}')
        print(f'\t- content: {body}')
        print((f'\t- utf8 content:{utf8_content}'))
