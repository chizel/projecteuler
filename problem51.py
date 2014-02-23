#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

NUMBER_OF_DIGITS = 6

def digit_position(primes_digits):
    position = [] 
    position.append([[],[], [],[],[],[],[],[],[],[]])

    for prime_index in range(0, len(primes_digits)):
        for digit_pos in range(0, NUMBER_OF_DIGITS):
            position[digit_pos][primes_digits[prime_index][digit_pos]].append(prime_index)
        print position
        exit()
    return position
    

def family_8(primes_digits):
    pass

def main():
    #primes = libpe.generate_primes(999999, lower_bound = 100000)
    primes_digits = []
    primes = [123456, 789009, 123123, 998877]

    for prime in primes:
        primes_digits.append(
                libpe.split_number(prime))
    res = digit_position(primes_digits)
    for pos in res:
        print pos

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

