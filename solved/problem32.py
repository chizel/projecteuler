#! /usr/bin/env python
# -*- coding: utf-8 -*-

def num_of_digit(number):
    i = 0

    while number:
        number /= 10
        i += 1
    return i

def is_pandigital(*arg):
    arr = range(1,10)
    for num in arg:
        while num:
            digit = num % 10
            if digit not in arr:
                return False
            num /= 10
            arr.remove(digit)
    if len(arg) == 3:
        if not arr:
            return True
        else:
            return False
    return True

def main():
    arr_res = []
    for i in range(1, 5000):
        for j in range(i, 10 ** (5 - (num_of_digit(i)))):
            if not is_pandigital(i, j):
                continue
            res = i * j
            if not is_pandigital(i, j, res):
                continue
            arr_res.append(res)
    print arr_res
    print sum(list(set(arr_res)))

if __name__ == "__main__":
    main()
