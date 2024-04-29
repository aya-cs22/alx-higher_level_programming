#!/usr/bin/python3
'''
a Python script that fetches https://alx-intranet.hbtn.io/status
'''


if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    res = response.text
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
# #!/usr/bin/python3
# """my status"""
# import requests
# if __name__ == "__main__":
#     url = "https://alx-intranet.hbtn.io/status"
#     response = requests.get(url)
#     print('Body response:')
#     print('\t- type: {}'.format(type(response.text)))
#     print('\t- content: {}'.format(response.text))
