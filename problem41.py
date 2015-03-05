#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

def generate_list_of_primes(ubound):
    list_of_primes = []

    step = 100000
    tmp_ubound = step

    # !!! add this piece of code to the loop !!! 
    if ubound > step:
        tmp_nums = range(0, tmp_ubound)
    else:
        tmp_nums = range(0, ubound + 1)

    len_of_tmp_nums = len(tmp_nums)

    for i in range(2, len_of_tmp_nums):
        if tmp_nums[i]:
            for j in range(i + tmp_nums[i], len_of_tmp_nums, tmp_nums[i]):
                tmp_nums[j] = 0
    tmp_nums = list(sorted(set(tmp_nums)))
    tmp_nums.remove(0)
    tmp_nums.remove(1)
    list_of_primes = tmp_nums

    #for i in range(0, len(list_of_primes)):
        #pass

    #for num in list_of_primes:
        #if num < 2:
            #continue
        #for i in range(2 * num, len(list_of_primes), num):
            #list_of_primes[i] = 0
    #list_of_primes = list(set(list_of_primes))
    #for num in list_of_primes:
        #if num < 100000000:
            #list_of_primes.remove(num)
    #return list_of_primes


#def generate_list_of_primes(ubound):
    #list_of_primes = range(0, ubound + 1)

    #for num in list_of_primes:
        #if num < 2:
            #continue
        #for i in range(2 * num, len(list_of_primes), num):
            #list_of_primes[i] = 0
    #list_of_primes = list(set(list_of_primes))
    #for num in list_of_primes:
        #if num < 100000000:
            #list_of_primes.remove(num)
    #return list_of_primes

#lop = generate_list_of_primes(1000000000)

def is_prime(search):
    return search in lop 

def gen_pandigital():
    for i in range(9, 0, -1):
        print i

def main():
    #gen_pandigital()
    #generate_list_of_primes(987654321)
    generate_list_of_primes(4321)

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start
