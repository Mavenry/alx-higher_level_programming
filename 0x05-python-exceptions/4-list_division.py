#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div_element = 0
    for i in range(list_length):
        try:
            div_elememt = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_element = 0
        except ZeroDivisionError:
            print("division by 0")
            div_element = 0
        except IndexError:
            print("out of range")
            div_element = 0
        finally:
            new_list.append(div_element)
    return new_list
