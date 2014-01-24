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

    def generate_pandigital(self, start=1, end=9):
        pass

    def __iter__(self, direction=0):
        '''return next pandigital number'''
        if direction:
#return from less to greater number
            pass
        else:
            pass
        return


def main():
    pand = Pandigital()

if __name__ == "__main__":
    start  = time.time()
    main()
    print "Time: ", time.time() - start, " seconds."
