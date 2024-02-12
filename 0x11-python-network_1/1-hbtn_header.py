#!/usr/bin/python3
"""
Python script to Sends a request to a URL and displays
the value of the X-Request-Id variable
"""


import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            print(x_request_id)
