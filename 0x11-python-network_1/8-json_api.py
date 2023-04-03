#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
   with the letter as a paramete
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) != 2:
        q = ""
    else:
        q = argv[1]
    values = {'q': q}
    r = requests.post(url, values)
    try:
        json_content = r.json()
    except Exception as e:
        print("Not a valid JSON")
    else:
        if len(json_content) < 1:
            print("No result")
        else:
            print(f"[{json_content['id']}] {json_content['name']}")
