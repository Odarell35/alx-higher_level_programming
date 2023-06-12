#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0 else 0:
        a = tuple_a[0]
    if len(tuple_a) > 1:
        b = tuple_a[1]
    if len(tuple_b) > 0:
        c = tuple_b[0]
    if len(tuple_b) > 1:
        d = tuple_b[1]
    else:
        0
    results = (a + c, b + d)
    return results
