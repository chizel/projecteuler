#! /usr/bin/env python
# -*- coding: utf-8 -*-

def find_powers(n):
    power = 0
    number = 3
    num_of_powers = 0
    while 1:
        power = number**n
        digits_count = len(str(power)) 

        if digits_count == n:
            num_of_powers += 1
            print number, '**', n , power
        elif digits_count > n:
            break
        number += 1
    return num_of_powers

def main():
    #1**1, 2**1
    num_of_powers = 2
    for i in range(1, 25):
        num_of_powers += find_powers(i)
    print num_of_powers
    return

if __name__ == "__main__":
    main()

