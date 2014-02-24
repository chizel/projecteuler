#! /usr/bin/env python
# -*- coding: utf-8 -*-

def number_of_digits(number):
    '''return count of digits in number'''
    #number is 0 and has 1 digit
    if not number:
        return 1

    res = 0

    while number:
        res += 1
        number /= 10

    return res

def is_pandigital(number, bound=9, include_zero=0, all_digits=1):
    '''return True if number is pandigital
    if number may have 0, set include_zero to 1
    if number may have not all digits, set all_digits=0
    '''
    #split digits
    digits = list(str(number))

    if not include_zero and '0' in digits:
        return False

    if all_digits and len(digits) < (9 + include_zero):
        return False

    if len(digits) > len(set(digits)):
        return False
    else:
        return True

def generate_primes(upper_bound, lower_bound = 0, result_is_tuple=1):
    '''generate list of primes from 2 to upper_bound
        if result must be list, set result_is_tuple to 0
        lower_bound < 0 is equal lower_bound = 1'''

    if upper_bound < 2:
        print 'Error! upper_bound can\'t be less 2!'
        print 'upper_bound: ', upper_bound
        exit()

    if lower_bound:
        if lower_bound > upper_bound:
            print 'Error! lower_bound can\'t be more upper_bound!'
            print 'lower_bound: ', lower_bound, ', upper_bound: ', upper_bound
            exit()

    primes = range(0, upper_bound + 1)

    for num in primes:
        #0 and 1 aren't primes
        if num < 2:
            continue

        for i in range(2 * num, len(primes), num):
            primes[i] = 0

    #remove elements equal 0, except first element
    primes = list(set(primes))

    primes.sort()

    #remove 0 and 1
    i = 2

    #remove elements less than lower_bound
    if lower_bound:
        while lower_bound > primes[i]:
            i += 1

    primes = primes[i:]

    if result_is_tuple:
        primes = tuple(primes)
    return primes

def generate_squares(upper_bound, start=0, result_tuple=1):
    '''generate list of squares from start(default 0) to upper_bound
    if result must be list, set result_tuple to 0'''

    squares = range(start, upper_bound + 1)
    squares = [x**2 for x in squares]
    return squares

def split_number(number, result_tuple=1):
    '''split number's digits
    return tuple/list
    if result must be list, set result_tuple to 0'''

    result = []

    while number:
        result.append(number % 10)
        number /= 10

    result = reversed(result)

    if result_tuple:
        result = tuple(result)

    return result
