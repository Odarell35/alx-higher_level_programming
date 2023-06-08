#!/usr/bin/python3
import sys


def main(*argv):
    results = 0
    for args in range(len(sys.argv) - 1):
        results = results + int(sys.argv[args + 1])
    print("{:d}".format(results))


if __name__ == "__main__":
    main()
