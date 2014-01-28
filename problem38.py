#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

def mult(number):
    mult = 1
    res_num = ''

    while 1:
        res_num += str(number * mult)
        mult += 1

        if len(res_num) >= 9:
            break

    if len(res_num) == 9 and libpe.is_pandigital(int(res_num)):
        return int(res_num)

    return 0
 
def main():
    max_pand = 0
    
    for i in range(1, 9999):
        tmp = mult(i)
        
        if tmp > max_pand:
            max_pand = tmp
    print max_pand

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

