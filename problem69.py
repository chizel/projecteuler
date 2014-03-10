#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from math import sqrt
import libpe

BOUND = 1000000
BOUND = 10

def main():
    primes = libpe.generate_primes(1000)#, include_1=1) 
    divisors = [[],[]]

    for i in xrange(2,BOUND):
        tmp = []
        
        if i in primes:
            divisors.append([i])
            continue

        primes_bound = int(sqrt(i))

        for prime in primes:
            if prime > primes_bound:
                break
            while not i % prime:
                i /= prime
                tmp.append(prime)
        divisors.append(tmp)

    for num in divisors:
        print num

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Start: ', time.time() - start
