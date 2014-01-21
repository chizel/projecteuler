#! /usr/bin/env python
# -*- coding: utf-8 -*-

def number_of_digits(number):
    #number is 0 and has 1 digit
    if not number:
        return 1
    res = 0
    while number:
        res += 1
        number /= 10
    return res

def main():
    return

if __name__ == "__main__":
    main()

