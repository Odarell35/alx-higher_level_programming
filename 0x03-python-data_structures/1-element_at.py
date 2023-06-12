#!/usr/bin/python3


def element_at(my_list, idx):
    length = len(my_list)
    for i in my_list:
        if idx < 0:
            return None
        elif idx >= length:
            return None
        else:
            return my_list.pop(idx)


if __name__ == "__main__":
    element_at(my_list, idx)
