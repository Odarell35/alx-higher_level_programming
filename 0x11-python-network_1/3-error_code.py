#!/usr/bin/python3
"""3-error_code Module"""
import urllib.error
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    res = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(res) as response:
            res_page = response.read()
            print(res_page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
