#!/usr/bin/python3
"""Module"""
import sys
import requests


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        r = requests.post(url, data={'q': sys.argv[1][0]})
        try:
            res = r.json()
            if res is  None:
                print("No result")
            else:
                print(f'[{res.get("id")}] {res.get("name")}')
        except ValueError:
            print("Not a Valid JSON")
    else:
        print("No result")
