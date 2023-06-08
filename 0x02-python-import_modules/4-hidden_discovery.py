#!/usr/bin/python3
import hidden_4


def main():
    name_list = dir(hidden_4)
    for the_name in name_list:
        if the_name[:2] != "_":
            print(the_name)
