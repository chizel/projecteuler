#! /usr/bin/env python
# -*- coding: utf-8 -*-

import libpe

class Cubes():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.stop = 10

    def generate_cubes(self):
        i = self.start
        res = []
        tmp = i

        while 1:
            i += 1
            tmp = i ** 3

            if tmp < self.stop:
                res.append(tmp)
            else:
                break

        print res
        self.start = i
        self.stop *= 10
        return res

    def check_nubmers(self):
        while 1:
            cubes = self.generate_cubes()
            tmp = []
            check_arr = []

            if not cubes:
                continue

            for cube in cubes:
                cube_digits = libpe.split_number(cube, result_tuple=0, normal_order=0)
                if cube_digits[0] == 5 and cube_digits[1] == 2:
                    print cube_digits
                tmp.append(cube_digits)
                check_arr.append(cube_digits)
                tmp[-1] = sorted(tmp[-1])

            tmp = sorted(tmp)
            i = 0

            while i < (len(tmp) - 1):
                j = i + 1

                while tmp[i] == tmp[j]:
                    j += 1

                if (j - i) >= 3:
                    check_arr = sorted(check_arr)
                    for cube in check_arr:
                        if sorted(cube) == tmp[i]:
                            print cube, tmp[i]
                    if tmp[i][-1] == 6:
                        return tmp[i]
                i = j

def main():
    p = Cubes(300,10000000000)
    print p.check_nubmers()

if __name__ == "__main__":
    main()

