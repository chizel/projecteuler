#! /usr/bin/env python
# -*- coding: utf-8 -*-

def number_of_digits(number):
    i = 0
    while number:
        number /= 10
        i += 1
    return i

def main():
    i = 1
    point = 10
    result = 1

    while(digits <= 1000000):
        nod_i = number_of_digits(i)
        digits += nod_i

        if digits >= point:
            dig_pos = digits - point

            if dig_pos:
                pass
            else:
                result *= 
            point *= 10

        i += 1

if __name__ == "__main__":
    main()

