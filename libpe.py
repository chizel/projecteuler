#! /usr/bin/env python
# -*- coding: utf-8 -*-

def number_of_digits(number):
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
    digits = list(str(number))

    if not include_zero and '0' in digits:
        return False

    if all_digits and len(digits) < (9 + include_zero):
        return False

    if len(digits) > len(set(digits)):
        return False
    else:
        return True

def generate_primes(upper_bound, result_is_tuple=1):
    '''generate list of primes from 2 to upper_bound
    if result must be list, set result_is_tuple to 0'''
    primes = range(0, upper_bound + 1)
    for num in primes:
        if num < 2:
            continue
        for i in range(2 * num, len(primes), num):
            primes[i] = 0
    primes = list(set(primes))
    primes.remove(0)
    primes.remove(1)
    primes.sort()
    if result_is_tuple:
        primes = tuple(primes)
    return primes


def main():
    print is_pandigital(123456789)
    return

if __name__ == "__main__":
    main()

