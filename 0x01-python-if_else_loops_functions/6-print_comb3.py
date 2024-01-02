#!/usr/bin/python3
for n in range(0, 9):
    for j in range(n + 1, 10):
        if n == 8:
            print("{}{}".format(n, j))
        else:
            print("{}{}".format(n, j), end=", ")

