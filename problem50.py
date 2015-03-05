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

top = generate_tuple_of_primes(1000000)

def v():
    res = 0
    max_len = 21
    tmp_num = 0
    tmp_len = 0
    ind = 0

    for item in top:
        print item

        res = item
        tmp_len = 1
        i = top.index(item) + 1

        while res < top[-1]:
            if tmp_len > 21 and res in top:
                if max_len < tmp_len:
                    max_len = tmp_len
                    tmp_num = res 
            res += top[i]
            tmp_len += 1
            i += 1

    print 'answer: ', tmp_num, '; lenght: ', max_len

def main():
    max_len = 0
    v()
    return

if __name__ == "__main__":
    main()
