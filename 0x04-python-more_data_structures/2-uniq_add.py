#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()
    total = 0
    
    for num in my_list:
        if my_list.count(num) == 1 and num not in unique_numbers:
            total += num
            unique_numbers.add(num)
    
    return total
