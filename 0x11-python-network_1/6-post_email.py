#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email."""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
# #!/usr/bin/python3
# """POST an email"""
# import requests
# import sys
# if __name__ == "__main__":
#     url = sys.argv[1]
#     value = {"email": sys.argv[2]}
#     response = requests.post(url, data=value)
#     print(response.text)
