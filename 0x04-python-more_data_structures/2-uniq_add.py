#!/usr/bin/python3
def uniq_add(my_list = []):
    sorted_list = list(set(my_list))
    addition = 0
    for x in sorted_list:
        addition = addition + x
    return addition
