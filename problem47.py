#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

def check_mult(number, primes):
    num_div = 0

    for prime in primes:
        if prime > number:
            return 0

        #number divisible by prime
        if not number % prime:
            number /= prime
            num_div += 1
            
            if num_div > 3:
                return num_div
    return 0

def main():
    primes = libpe.generate_primes(999)
    cons = 0

    for i in range(1000, 9999):
        if check_mult(i, primes) > 3:
            cons += 1
        else:
            cons = 0
        if cons >= 2:
            print i, i - 1, i - 2, 'answer: ', i - 3

    return

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

