#!/usr/bin/python3
""" Fetche website info using urllib library """
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    request = Request(url)
    with urlopen(request) as response:
        with response:
            page_bytes = response.read()
            page_str = page_bytes.decode("utf-8")

    print("Body response:")
    print(f"\t- type: {type(page_bytes)}")
    print(f"\t- content: {page_bytes}")
    print(f"\t- utf8 content: {page_str}")
