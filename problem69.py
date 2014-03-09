#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from math import sqrt
import libpe

BOUND = 1000000
#BOUND = 10

def main():
    primes = libpe.generate_primes(1000)#, include_1=1) 
    divisors = []

    for i in xrange(2,BOUND):
        tmp = []

        for prime in primes:
            if prime > int(sqrt(i)):
                break
            while not i % prime:
                i /= prime
                tmp.append(prime)
        divisors.append(tmp)
    #for i in range(len(divisors)):
        #print i + 2, divisors[i]

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Start: ', time.time() - start
