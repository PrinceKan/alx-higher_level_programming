#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    request = Request(url)

    try:
        with urlopen(request) as response:
            page = response.read()
    except HTTPError as e:
        print(f"Error code: {e.code}")
    else:
        print(page.decode("utf-8"))
