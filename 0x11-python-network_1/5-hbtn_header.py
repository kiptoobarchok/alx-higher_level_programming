#!/usr/bin/python3
"""
sends request to the URL and displays the value of
the variable X-Request-Id in the response header
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)
