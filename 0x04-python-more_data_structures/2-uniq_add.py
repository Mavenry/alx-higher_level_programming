#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in range(len(my_list)):
        if my_list.count(my_list[i]) == 1:
            total += i
    return total
