#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    cpy_list = my_list.copy()
    if idx < 0 or idx >= len(cpy_list):
        return cpy_list
    else:
        cpy_list[idx] = element
        return cpy_list
        return my_list


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
