#!/usr/bin/python3
"""
URL and email made to send POST request to URL with email parameter
the body of response displayed
(decoded in utf-8).
"""

import urllib.parse
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {
        "email": email
    }
    query_string = urllib.parse.urlencode(param)
    data = query_string.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response_text = response.read().decode("utf-8")
        print(response_text)
