#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

BOUND = 10

def main():
    primes = libpe.generate_primes(BOUND)#, include_1=1) 
    divisors = []

    for i in xrange(2,BOUND):
        tmp = []
        for prime in primes:
            if prime > (i / 2):
                break
            if not i % prime:
                tmp.append(prime)
        divisors.append(tmp)
    print divisors

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Start: ', time.time() - start
