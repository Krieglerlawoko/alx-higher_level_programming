#!/usr/bin/python3
"""
py script sends a request to URL and displays value of 
X-Request-Id variable found in the header of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    value = response.headers.get("X-Request-Id")
    print(value)
