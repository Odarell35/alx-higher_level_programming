#!/usr/bin/python3
for alphabets in range(ord("a"), ord("z") + 1):
    if chr(alphabets) != 'q' and chr(alphabets) != 'e':
        print("{}".format(chr(alphabets)), end="")
