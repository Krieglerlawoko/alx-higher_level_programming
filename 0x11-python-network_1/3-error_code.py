#!/usr/bin/python3
"""
script send request to URL and displays the
body of the response (decoded in utf-8).
"""
import urllib.error
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
            print(response_text)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
