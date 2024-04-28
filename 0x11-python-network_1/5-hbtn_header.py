#!/usr/bin/python3
"""Response header value"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    head = requests.headers.get("X-Request-Id")
    print(head)
