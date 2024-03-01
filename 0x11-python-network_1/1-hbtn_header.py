#!/usr/bin/python3
"""
Request sent to the URL and displayed value of X-Request-Id by Python script
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        value = html.get('X-Request-Id')
        print(value)
