#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in my_list:
        if i.count(i) == 1:
            total += i
    return total
