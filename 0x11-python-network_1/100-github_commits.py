#!/usr/bin/python3
"""
2 arguments taken in order to list 10 commits
of the repository "rails" by the user "rails".
Print all commits by: `<sha>: <author name>` (one by line)
The second argument will be the owner name
The first argument will be the repository name
"""
import sys
import requests


if __name__ == "__main__":
    try:
        username = sys.argv[2]
        repo_name = sys.argv[1]
        commmits_url = "https://api.github.com/repos/{}/{}/commits" \
            .format(username, repo_name)
        response = requests.get(commmits_url)
        json_obj = response.json()
        for a, obj in enumerate(json_obj):
            if a == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except ValueError as invalid_json:
        pass
