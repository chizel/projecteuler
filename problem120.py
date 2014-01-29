#! /usr/bin/env python
# -*- coding: utf-8 -*-

LBOUND = 3
UBOUND = 10 + 2
DEGREE = 10 + 1
# a < 50 n=100
#a < 100 n=200
#a< 200 n= 300 
#a<300 n= 500
#a<400 n= 600
#a<500 n= 800
#a<600 n= 900
#a<700 n= 1100
#a<800 n= 1200
#a<900 n= 1400
#a<1000 n= 1700
def gen_powers(power):
    powers = [0] * UBOUND
    for i in range(LBOUND, UBOUND):
        powers[i] = i**power
    return powers

def find_diff(numbers):
    diff = [0] * len(numbers)
    for i in range(3, len(numbers) - 1):
        diff[i] = (numbers[i - 1] + numbers[i + 1]) % i**2
    return diff

def find_sum_max(diff):
    tmp_pow = 0
    max_diff = [0] * len(diff[1])
    for i in range(3, len(diff[1])):
        for j in range(1, DEGREE):
            #print 'degree: ', j, ', result: ', diff[j][i]
            if diff[j][i] > max_diff[i]:
                max_diff[i] = diff[j][i]
                tmp_pow = j
            #    if j == DEGREE - 1:
            #        print 'eeee ', i
        #print i, tmp_pow, max_diff[i]
    return max_diff

def main():
    diff = [0] * DEGREE 

    for i in range(1, DEGREE):
        powers = gen_powers(i)
        diff[i] = find_diff(powers)
        print i

    res = find_sum_max(diff)
  #  for i in range(3, len(res)):
        #print "max ", i, " is ", res[i]
    print sum(res)

if __name__ == "__main__":
    main()

