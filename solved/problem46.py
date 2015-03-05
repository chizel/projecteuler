#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

class OddComposite:
    def __init__(self, ubound):
        self.ubound = ubound
        self.double_squares = [2 * x**2 for x in range(1, self.ubound)]
        self.primes = libpe.generate_primes(self.ubound)

    def is_golbach(self, number):
        if number in self.primes:
            return True

        for double_square in self.double_squares:
            if double_square > number:
                break

            for prime in self.primes:
                sum_num = prime + double_square
                if sum_num > number:
                    break
                if number == sum_num:
                    return True
        return False

def main():
    ubound = 6000
    check = OddComposite(ubound)
    for number in range(9, ubound, 2):
        if not check.is_golbach(number):
            print number
            break

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

