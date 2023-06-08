#!/usr/bin/python3
import sys
def main(*argv):
    ac = 0
    len_av = len(sys.argv) - 1
    if len_av == 1:
        print(" {:d} argument:".format(len_av))
    elif len_av == 0:
        print(" {:d} arguments.".format(len_av))
    else:
        print(" {:d} arguments:".format(len_av))
    for x in sys.argv:
        if (ac != 0):
            print("{}: {}".format(ac, x))
            ac = ac + 1

if __name__ == "__main__":
    main()



