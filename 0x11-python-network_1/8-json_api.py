#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to URL with the letter as a parameter."""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    value = {"q": q}

    response = requests.post("http://0.0.0.0:5000/search_user", json=value)

    try:
        response_json = response.json()
        if isinstance(response_json, dict):
            if response_json:
                print("[{}] {}".format(response_json['id'], response_json['name']))
            else:
                print("No result")
        else:
            print("Not a valid JSON")
    except ValueError:
        print('Not a valid JSON')
