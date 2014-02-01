#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

class Pandigital:
    '''generate pandigital number, check number is it pandigital'''
    def __init__(self,):
        pass
 
    def is_pandigital(self, number, bound=9, include_zero=0, all_digits=1):
        '''return True if number is pandigital
        if number may have 0, set include_zero to 1
        if number may have not all digits, set all_digits=0
        '''
        digits = list(str(number))

        if not include_zero and '0' in digits:
            return False

        if all_digits and len(digits) < (9 + include_zero):
            return False

        if len(digits) > len(set(digits)):
            return False
        else:
            return True

    #def generate_pandigital(self, start=1, end=9, start_min=1):
    def generate_pandigital(self, start=1, end=3, start_min=1):
        '''generate pandigital number, next number will be
        bigger, if start_min=1
        generate_pandigital([start, [end, [start_min]]]'''

        if start < 0:
            print 'Error! start must be more or equal 0!'
            return
        if end > 10:
            print 'Error! end can\'t be more then 10!'
            return
        if start > end:
            print 'Error! start can\'t be more then end!'
            return

        digits = range(start, end +1)

        for i in range(0, 5):
            for j in range(0, 5):
                pass
        for i in range(len(digits) - 2, -1, -1):
            digits[i:] = sorted(digits[i:])
            tmp = digits[i]
            digits[i] = digits[i + 1]
            digits[i + 1] = tmp
            print digits

    def __iter__(self, direction=0):
        '''return next pandigital number'''
        if direction:
            pass
        else:
            pass
        return


def main():
    p = Pandigital()
    p.generate_pandigital()


if __name__ == "__main__":
    start  = time.time()
    main()
    print "Time: ", time.time() - start, " seconds."
