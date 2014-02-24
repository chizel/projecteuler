#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

NUMBER_OF_DIGITS = 5

def digit_position(primes_digits):
    position = [] 

    for i in range(0, NUMBER_OF_DIGITS):
        position.append([[],[], [],[],[],[],[],[],[],[]])

    for prime_index in range(0, len(primes_digits)):
        for digit_pos in range(0, NUMBER_OF_DIGITS):
            position[digit_pos][primes_digits[prime_index][digit_pos]].append(prime_index)
    return position
    

def find_numbers(positions):
    res = []

#positions
    for digit_pos in range(0, NUMBER_OF_DIGITS - 1):
#indecies
        for digit in range(0, 10):

            tmp = set(positions[digit_pos][digit])

            for i in range(digit_pos + 1, NUMBER_OF_DIGITS):
                for j in range(0, len(positions[i])):
                    res = tmp.intersection(positions[i][j])
                    if len(res) == 7:
                        return res

def main():
    primes = libpe.generate_primes(lower_bound = 10000, upper_bound = 99999)
    primes_digits = []

    for prime in primes:
        primes_digits.append(
                libpe.split_number(prime))
    positions = digit_position(primes_digits)

    print find_numbers(positions)

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

