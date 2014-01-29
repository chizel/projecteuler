#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

def digits(number):
    count = 0
    digits = []

    while number:
        digits.append(number % 10)
        number /= 10
    return digits

def is_same_digits(numbers):
    digits_list = []
    digits_list.append(digits(numbers[0]))
    digits_list[0].sort()
    digits_count = len(digits_list[0]) 

    for i in range(1, len(numbers)):
        digits_list.append(digits(numbers[i]))
        if not digits_count == len(digits_list[-1]):
            return False
        digits_list[-1].sort()

    for i in range(1, len(digits_list)):
        if not digits_list[0] == digits_list[i]:
            return False
    return True

def main():
    for i in range(100000, 999999):
        if is_same_digits([i * j for j in range(1, 6)]):
            print i
            return

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

