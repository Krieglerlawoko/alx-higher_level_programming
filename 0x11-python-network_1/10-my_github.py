#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and
use GitHub API to display id.
Argument 1 will be username.
The argument 2 will be password
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    password = sys.argv[2]
    username = sys.argv[1]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    json_obj = response.json()
    print(json_obj.get("id"))
