#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

def check_mult(number, primes):
    num_div = 0

    for prime in primes:
        if prime > number:
            return 0

        #is number divisible by prime
        if not number % prime:
            number /= prime
            num_div += 1
            
            if num_div > 3:
                return num_div
    return 0

def main():
    primes = libpe.generate_primes(999)
    cons = 0
    i = 646

    while 1:
        if check_mult(i, primes) > 3:
            cons += 1
        else:
            cons = 0
        if cons >= 4:
            print i, i - 1, i - 2, 'answer: ', i - 3
            break
        i += 1

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start
