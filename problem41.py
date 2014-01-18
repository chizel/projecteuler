#! /usr/bin/env python
# -*- coding: utf-8 -*-

def generate_list_of_primes(ubound):
    list_of_primes = range(0, ubound + 1)
    for num in list_of_primes:
        if num < 2:
            continue
        for i in range(2 * num, len(list_of_primes), num):
            list_of_primes[i] = 0
    list_of_primes = list(set(list_of_primes))
    for num in list_of_primes:
        if num < 100000000:
            list_of_primes.remove(num)
    return list_of_primes

#lop = generate_list_of_primes(1000000000)

def is_prime(search):
    return search in lop 

def gen_pandigital():
    for i in range(9, 0, -1):
        print i

def main():
    gen_pandigital()

if __name__ == "__main__":
    main()
