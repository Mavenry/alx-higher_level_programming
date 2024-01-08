#!/usr/bin/python3
def replace_in_list(my_list, idx):
    if idx < 0:
        return None
    elif idx not in my_list:
       return None
    else:
       return my_list[idx]
