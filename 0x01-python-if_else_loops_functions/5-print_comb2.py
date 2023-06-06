#!/usr/bin/python3
for numbers in range(0, 99):
    print("{:0>2d}".format(numbers), end=", ")

print(numbers+1)
