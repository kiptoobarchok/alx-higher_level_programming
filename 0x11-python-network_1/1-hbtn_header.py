#!/usr/bin/python3
"""
Python script to Sends a request to a URL and displays
the value of the X-Request-Id variable
"""

import urllib.request
import sys

url = sys.argv[1]  # Get the URL from the first command-line argument

with urllib.request.urlopen(url) as response:
    response_headers = response.info()
    request_id = response_headers.get("X-Request-Id")

    if request_id:
        print("X-Request-Id:", request_id)
    else:
        print("X-Request-Id header not found in the response.")
