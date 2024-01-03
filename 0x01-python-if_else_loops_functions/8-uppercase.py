#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) >= ord('a') and ord(n) <= ord('z'):
            print("{}".format(chr(ord(n) - 32)), end="")
    print()
