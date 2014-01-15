#! /usr/bin/env python
# -*- coding: utf-8 -*-

def num_of_digit(number):
    i = 0

    while number:
        number /= 10
        i += 1
    return i

def is_pandigital(arg):
    arr = range(1,9)
    arg[0] = 3

for i in range(1, 9999):
    for j in range(1, 5 - num_of_digit(i)):
        ubound = 1
    for j in range(1, ubound):
        if not is_pandigital(i, j):
            continue
        res = i * j
        if not is_pandigital(i, j, res):
            continue
        arr_res.append(res)
def main():
    print is_pandigital(13, 27)

if __name__ == "__main__":
    main()
