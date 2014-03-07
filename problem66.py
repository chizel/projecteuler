#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from math import sqrt

class problem66():
    def __init__(self):
        pass

    def generate_squares(self, border):
        self.squares = [x**2 for x in xrange(1, border + 1)]

    def find_equation(self, d):
        if d in self.squares:
            return [d, 0]

        for y in xrange(0, len(self.squares)):
            mult = d * self.squares[y]

            if mult > self.squares[-1]:
                return [d, 0]
            elif (mult + 1) in self.squares:
                return [d, mult + 1]
        return [d, 0]

    def find_solution(self):
        tmp = [0,0]

        for d in xrange(2, 1001):
            result = self.find_equation(d)

            if result[1] > tmp[1]:
                tmp = result[:]
        tmp[1] = sqrt(tmp[1])
        return tmp

def main():
    p = problem66()
    p.generate_squares(50000)
    #print p.find_solution()
    print p.find_equation(58)
    return

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

