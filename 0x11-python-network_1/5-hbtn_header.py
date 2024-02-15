#!/usr/bin/python3
"sends POST request to url with email parameter and display body response"

import sys
import requests

def get_request_id(url):
    try:
        response = requests.get(url)
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(f"X-Request-Id: {request_id}")
        else:
            print("X-Request-Id header not found in the response.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    get_request_id(url)
    