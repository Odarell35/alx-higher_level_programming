#!/usr/bin/python3
import sys


def main(*argv):
    len_av = len(sys.argv) - 1
    if len_av == 1:
        print("{:d} argument:".format(len_av))
    elif len_av == 0:
        print("{:d} arguments.".format(len_av))
    else:
        print("{:d} arguments:".format(len_av))
    for len_av in range(len_av):
        print("{}: {}".format(len_av + 1, sys.argv[len_av + 1]))


if __name__ == "__main__":
    main()
