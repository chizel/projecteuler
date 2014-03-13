#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libpe

class Cubes():
    def __init__(self, start):
        self.start = start

    def generate_cubes(self):
        i = self.start
        res = []

        start_cube = self.start ** 3

        while 1:
            tmp = i ** 3
            i += 1

            if libpe.number_of_digits(tmp) == libpe.number_of_digits(start_cube):
                res.append(tmp)
            else:
                break

        self.start = i
        return res

    def check_nubmers(self):
        while 1:
            cubes = self.generate_cubes()
            tmp = []
            check_arr = []

            if not cubes:
                continue

            for cube in cubes:
                cube_digits = libpe.split_number(cube, result_tuple=0, normal_order=1)
                tmp.append([cube_digits, sorted(cube_digits)])

            tmp.sort(key=lambda x: x[1])
            i = 0

            while i < (len(tmp) - 1):
                j = i + 1

                while tmp[i][1] == tmp[j][1]:
                    j += 1

                if (j - i) == 5:
                    for number in tmp[i:j]:
                        print number
                    return
                i = j

def main():
    p = Cubes(1)
    print p.check_nubmers()

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

