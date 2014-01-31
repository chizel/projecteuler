#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

def main():
    primes = libpe.generate_primes(999999, lower_bound = 100000)
    #print primes
    return

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

