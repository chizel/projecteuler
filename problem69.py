#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from math import sqrt
import libpe

BOUND = 1000000

def is_have_same_numbers(a, b):
    for number in a:
        if number in b:
            return True
    return False

def main():
    primes = libpe.generate_primes(1000)#, include_1=1) 
    divisors = [[],[]]

    for i in xrange(2,BOUND):
        tmp = []
        
        for prime in primes:
            if not i % prime:
                i /= prime
                tmp.append(prime)

                while not i % prime:
                    i /= prime
        divisors.append(tmp)

    #maxz = [0,0]
    #for i in range(len(divisors)):
        #if maxz[0] < len(divisors[i]):
            #maxz[0] = len(divisors[i])
            #maxz[1] = i
    #print maxz
    count_rprimes = [1] * len(divisors)
    maxm = [0.0, 0]
    

    for i in range(51, BOUND, 51):#BOUND - 3000, BOUND-2000,51):
        print i
        for j in range(3, i, 2):
            if not is_have_same_numbers(divisors[j], divisors[i]):
                count_rprimes[i] += 1
        if float(i) / count_rprimes[i] > maxm[0]:
            maxm[0] = float(i) / count_rprimes[i]
            maxm[1] = i
    print maxm

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start
