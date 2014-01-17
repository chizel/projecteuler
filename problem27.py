#! /usr/bin/env python
# -*- coding: utf-8 -*-

def generate_tuple_of_primes(ubound):
    lop = range(0, ubound + 1)
    for num in lop:
        if num < 2:
            continue
        for i in range(2 * num, len(lop), num):
            lop[i] = 0
    lop = list(set(lop))
    lop.remove(0)
    lop.remove(1)
    lop.sort()
    top = tuple(lop)
    return top 

top = generate_tuple_of_primes(100000)

def is_prime(search):
    return search in top 

def len_of_prime_row(a, b):
    n = 0
    len_prime = 0
    while is_prime(n**2 + a * n + b): 
        n += 1
        len_prime += 1
    return len_prime

def main():
    len_prime = 0
    tmp_a = 0
    tmp_b = 0

    for a in range(-1000, 1001):
        print a

        for b in top:
            if b > 1000:
                break
            if a < 0 and (b + a) < 0:
                continue
            if not is_prime(a + b + 1):
                continue

            tmp = len_of_prime_row(a, b)
            if tmp > len_prime:
                len_prime = tmp
                tmp_a = a
                tmp_b = b
    print len_prime
    print tmp_a * tmp_b

if __name__ == "__main__":
    main()
