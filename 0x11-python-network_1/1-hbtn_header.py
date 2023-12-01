#!/usr/bin/python3
"""1-hbtn_header Module"""
import urllib.request
import sys


if __name__ == '__main__':
    result = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(result) as response:
        result_page = response.getheader("X-Request-Id")
        print(result_page)
