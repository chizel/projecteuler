#! /usr/bin/env python
# -*- coding: utf-8 -*-

def mult():
    res = 1
    num = 0
    while num < 7830457:
        res *= 2
        res = int(res)
        num += 1
        print num
    print res
def main():
    mult()
    return

if __name__ == "__main__":
    main()

