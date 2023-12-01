#!/usr/bin/python3
"""4-hbtn_status Module"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url).text
    print(f'Body response:\n\t- type: {type(req)}\n\t- content: {req}')
