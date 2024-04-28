#!/usr/bin/python3
"""POST an email"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    response = requests.post(url, data = value)
    print('Your email is: {}'.format(response))
