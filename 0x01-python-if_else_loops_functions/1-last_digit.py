#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_di = number % -10
else:
    last_di = number % 10
if last_di > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last_di))
elif last_di < 6 and last_di != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_di))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
