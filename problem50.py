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

top = generate_tuple_of_primes(1000)

def f(num):
    i = 0
    j = 0
    lenght = 0
    res = 0

    while 1:
        while res < num:
            res += top[i]
            i += 1
        print res

        if res == num:
            return lenght

        while top[i] < (num/2):
            if res == num:
                return lenght

            if res > num:
                res -= top[j]
                j += 1
                lenght -= 1
            else:
                res += top[i]
                i += 1
                lenght += 1
    return lenght
print f(953)
#tmp = 0
#for i in top:
    #if tmp < 953:
        #tmp += top[i]

#print tmp

def main():
    return

if __name__ == "__main__":
    main()

