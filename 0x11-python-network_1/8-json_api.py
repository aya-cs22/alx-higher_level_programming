#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to URL with the letter as a parameter."""
import sys
import requests
import json

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"q": sys.argv[2]}

    response = requests.post("http://0.0.0.0:5000/search_user", json=value)

    try:
        response_json = response.json()
        if response_json:
            for item in response_json:
                print("[{}] {}".format(item['id'], item['name']))
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')
