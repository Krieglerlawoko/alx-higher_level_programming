#!/usr/bin/python3
"""
Python script sends POST request to URL with email as 
parameter and body of response displayed
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {
        "email": email
    }
    response = requests.post(url, data=payload)
    print(response.text)
