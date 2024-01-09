#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenght_a = len(tuple_a)
    lenght_b = len(tuple_b)
    if lenght_a < 2:
        if lenght_a == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0

    if lenght_b < 2:
        if lenght_b == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    added_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return added_tuple
