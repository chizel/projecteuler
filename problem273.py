#! /usr/bin/env python
# -*- coding: utf-8 -*-

import libpe
import math

def check_divisors(primes, number):
    if not number % 2:
        return False
    if not number % 3:
        return False

    i = 7
    while i**2 < number:
        if not number % i and i not in primes:
            return False
        i += 6
    return True

def main():
    primes = libpe.generate_primes(150, result_is_tuple=0)
    tmp_primes = []
    for i in range(0, len(primes)):
        if not (primes[i] - 1) % 4:
            tmp_primes.append(primes[i])

    res_primes = []

    for i in range(0, len(tmp_primes)):
        for j in range(i, len(tmp_primes)):
            tmp_num = tmp_primes[i] * tmp_primes[j]
            if check_divisors(primes, tmp_num):
                res_primes.append(tmp_num)
    print res_primes
    print '_____________'

    squares = libpe.generate_squares(12)
    sum_of_a = 0

    for number in res_primes:
        for a in squares:
            max_a = squares[-1]
            index_b = squares.index(a)
            
            while index_b < len(squares) and number >= (a + squares[index_b]):
                if number == (a + squares[index_b]):
                    if max_a == squares[-1]:
                        max_a = squares[index_b]
                    sum_of_a += squares.index(a)
                    break
                index_b += 1
        if a > max_a:
            break
    print sum_of_a 

if __name__ == "__main__":
    main()

