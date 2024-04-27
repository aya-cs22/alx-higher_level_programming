#!/usr/bin/python3
"""my status"""
import urllib.request
if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print(('\t- utf8 content:{}').format(body.decode("utf-8")))
        # print("Body response:")
        # print("\t- type: {}".format(type(body)))
        # print("\t- content: {}".format(body))
        # print("\t- utf8 content: {}".format(body.decode("utf-8")))
        # utf8_content = body.decode('utf-8')
        # print(f'Body response:')
        # print(f'\t- type: {type(body)}')
        # print(f'\t- content: {body}')
        # print((f'\t- utf8 content:{utf8_content}'))
