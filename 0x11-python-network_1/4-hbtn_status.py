#!/usr/bin/python3
"""my status"""
import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(response))
    print('\t- content: {}'.format(response))
