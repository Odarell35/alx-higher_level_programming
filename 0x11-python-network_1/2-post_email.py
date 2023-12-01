#!/usr/bin/python3
"""2-post_emai Module"""
import urllib.parse
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    value = { 'email' : sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    result = urllib.request.Request(url, data)
    with urllib.request.urlopen(result) as response:
        result_page = response.read().decode('utf-8')
        print(result_page)
