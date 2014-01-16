#! /usr/bin/env python
# -*- coding: utf-8 -*-

def number_of_digits(number):
    i = 0
    while number:
        number /= 10
        i += 1
    return i

def give_digit(number, position):
    #0 = last digit, len(number) - 1 = first digit
    for i in range(0, position):
        number /= 10
    return number % 10

def main():
    i = 1
    result = 1
    digits_count = 0
    point = 10

    while(digits_count <= 1000000):
        nod_i = number_of_digits(i)
        digits_count += nod_i

        if digits_count >= point:
            dig_pos = digits_count - point
            digit = give_digit(i, dig_pos)
            result *= digit
            point *= 10
        i += 1
    print result

if __name__ == "__main__":
    main()

