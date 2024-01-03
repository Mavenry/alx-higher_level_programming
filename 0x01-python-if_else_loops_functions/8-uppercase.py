#!/usr/bin/python3
def uppercase(str):
    for b in str:
        if ord(b) >= ord('a') and ord(b) <= ord('z'):
        print("{}".format(chr(ord(b) - 32)))
