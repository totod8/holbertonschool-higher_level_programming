#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of {} is {} and is {}"
if number >= 0:
    last_dgt = number % 10
    if last_dgt > 5:
        print(string.format(number, last_dgt, "greater than 5"))
    elif last_dgt == 0:
        print(string.format(number, last_dgt, "0"))
    else:
        print(string.format(number, last_dgt, "less than 6 and not 0"))
else:
    last_dgt = number % (-10)
    if last_dgt > 5:
        print(string.format(number, last_dgt, "greater than 5"))
    elif last_dgt == 0:
        print(string.format(number, last_dgt, "0"))
    else:
        print(string.format(number, last_dgt, "less than 6 and not 0"))
