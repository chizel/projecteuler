#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

def find_path(numbers):
    path = 0

#len(tmp) == number of rows
    tmp = []
    for row in numbers:
        print row

    return path

def main():
    numbers = [[131 ,673 ,234 ,103 ,18],
               [201 ,96, 342 ,965 ,150],
               [630 ,803 ,746 ,422 ,111],
               [537 ,699 ,497 ,121 ,956],
               [805 ,732 ,524 ,37,331]]
    print find_path(numbers)
    return

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

