#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            if j != 9:
                print('{:d}{:d}, '.format(i, j), end="")
            else:
                print('{:d}{:d}'.format(i, j))

