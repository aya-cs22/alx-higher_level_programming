#!/usr/bin/python3
"""Response header value"""
import urllib.request
import sys
if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        head = response.getheader('X-Request-Id')
        if head:
            print(head)
