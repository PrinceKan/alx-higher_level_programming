#!/usr/bin/python3
""" sends a request to the URL and displays the value
    of the X-Request-Id variable
"""
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urlencode(values).encode('ascii')
    request = Request(url, data)

    with urlopen(request) as response:
        page = response.read()

    print(page.decode("utf-8"))
