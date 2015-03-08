#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import itertools

from libpe import generate_primes


def is_prime(lop, number):
    '''Check if 'number' is prime by dividing it
    by numbers in the 'lop' '''
    for div in lop:
        if number % div == 0:
            return False
    return True


def to_int(digits):
    '''Convert tuple of digits into integer'''
    number = 0

    for digit in digits:
        number *= 10
        number += digit

    return number


def main():
    primes = itertools.permutations(range(7, 0, -1))
    lop = generate_primes(31426, lower_bound=2, result_is_tuple=1)

    for digits in primes:
        prime = to_int(digits)

        if is_prime(lop, prime):
            return prime


if __name__ == "__main__":
    start = time.time()
    print main()
    print 'Time: ', time.time() - start
