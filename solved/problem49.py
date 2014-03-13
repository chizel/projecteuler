#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

def find_seq(number, primes):
    res = []

    for prime in primes:
        tmp = prime - number

        if tmp > primes[-1]:
            break

        if (tmp + prime) in primes:
            res.append([number, prime,  tmp + prime])

    return res

def is_permutation(list_numbers):
    tmp_list = []

    for number in list_numbers:
        tmp = list(str(number))
        tmp.sort()
        tmp_list.append(tmp)

    for i in range(1, len(tmp_list)):
        if not tmp_list[i - 1] == tmp_list[i]:
            return False

    return True

def main():
    primes = libpe.generate_primes(9999)
    primes = [n for n in primes if n > 1000]

    for i in range(0, len(primes)):
        res = find_seq(primes[i], primes[i + 1:])

        for item in res:
            if is_permutation(item):
                print 'Answer: ', item

                if not item[0] == 1487:
                    return

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start
