#! /usr/bin/env python
# -*- coding: utf-8 -*-

import libpe

def generate_degrees(bound):
    for i in range(0, 11):
        tmp
    tmp = 10

    while tmp < bound:
        tmp *= 10
def main():
    numbers = []

#    with open('base_exp.txt', 'r') as f:
        #for line in f:
            #tmp_li = line.split(',')
            #tmp_li[0] = int(tmp_li[0])
            #tmp_li[1] = int(tmp_li[1])
            #numbers.append(tmp_li)

    #632382 518061 > 519432 525806
    numbers = [[632382,518061], [519432,525806]]
    res = []

    for base, exp in numbers:
        res.append((libpe.number_of_digits(base) - 1) * exp)


    for i in range(0, len(numbers)):
        num = numbers[i][0] 

        while num > 10:
            num /= 10
            print num

        #tmp_num = num ** numbers[i][1]
        #res[i] += libpe.number_of_digits(tmp_num)

    print res


    return

if __name__ == "__main__":
    main()

