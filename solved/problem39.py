#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

def num_of_sol(number, squares):
    '''returns number of right triangles'''

    res = 0

    for i in range(1, number/3):
        for j in range(i, number/2):
            k = number - i - j

            if k < j:
                break

            if k > 500:
                continue

            if (squares[i] + squares[j]) == squares[k]:
                res += 1

    return res


def main():
    squares = [x**2 for x in range(0, 501)]
    max_res = 0
    max_num = 0

    for i in range(6, 1001):
        res = num_of_sol(i, squares)

        if max_res < res:
            max_res = res
            max_num = i

    print max_num

if __name__ == "__main__":
    start  = time.time()
    main()
    print "Time: ", time.time() - start, " seconds."
