#!/usr/bin/python3
"""Search API"""
import requests
import sys
if __name__ == "__main__":
    if (len(sys.argv[1] == 1)):
        q = ""
    else:
        q = sys.argv[1]
    value = {"q": q}
    response = requests.post("http://0.0.0.0:5000/search_user",json = value)
    try:
        response_json = response.json
        if isinstance(response_json, dict):
            if response_json:
                print("[{}] {}".format(response_json['id'], response_json['name']))
            else:
                print("No result")
        else:
            print("Not a valid JSON")
    except ValueError:
        print("Not a valid JSON")
