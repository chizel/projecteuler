#! /usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *

def is_cycling(num):
    num_str = str(num)
    num_str = num_str[2:]
    new_str = ''
    new_str += num_str[0]
    end = len(num_str)/2
    for i in range(1, end):
        new_str += num_str[i]
        if num_str[i + 1] == new_str[0] and len(num_str) > 5:
            start = i + 1
            end = i + len(new_str) + 1
            ans = is_equal(new_str, num_str[start:end])
            if ans == False:
                continue 
            start = i + len(new_str) + 1
            end = 2 * len(new_str) + i + 1
            if end < len(num_str):
                ans = is_equal(new_str, num_str[start:end])
            if ans == False:
                continue 
            return len(new_str) 
    return 0

def is_equal(str1, str2):
    if str1 == str2:
        return True
    return False

getcontext().prec = 2000
useless_numbers = [2, 5]
max_len = 0

for i in range(2, 1000):
    if i % 2 == 0 or i % 5 == 0:
        continue
    res = Decimal(1)/Decimal(i)
    cycle_len = is_cycling(res)
    if cycle_len > max_len:
        max_len = cycle_len
        max_i = i
print max_i
