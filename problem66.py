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
        for x in xrange(0, len(self.squares)):
            for y in xrange(x - 1, -1, -1):
                print 'y:',y, 'x:', x
                #print self.squares[x], self.squares[y]
                result = self.squares[x] - d * self.squares[y]
                if result < 1:
                    continue
                elif result > 1:
                    break
                else:
                    return [sqrt(self.squares[x]), d]
        return [0,0]

    def find_solution(self):
        tmp = [0,0]

        for d in xrange(2, 10):#01):
            print d
            result = self.find_equation(d)
            if result[0] > tmp[0]:
                tmp = result[:]
        return tmp


def main():
    p = problem66()
    p.generate_squares(100000)
    print p.find_solution()
    #p.find_equation(5)
    return

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

