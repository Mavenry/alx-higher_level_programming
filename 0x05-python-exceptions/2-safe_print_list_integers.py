#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(i) == int:
                print("{:d}".format(my_list[]), end="")
                count += 1
            else:
                continue
    except IndexError:
        pass
    finally:
        print()
        return count

