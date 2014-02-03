#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

class FindMinPath():
    def __init__(self, numbers):
        self.numbers = numbers

    def check_down(self, row, column):
        current_cell = self.numbers[row][column]

        if (current_cell + self.numbers[row - 1][column]) < (current_cell + self.numbers[row][column + 1]):
            self.numbers[row_pos][col] += self.numbers[row_pos - 1][col]
        return

    def check_up(self, row_pos, col_pos):
        pass

    def find_path(numbers):

        count_of_rows = len(numbers) 
        count_of_columns = len(numbers[0])

        for col in range(count_of_columns - 2, -1, -1):
            direction = [] * len(count_of_rows)

            for row_pos in range(0, count_of_rows - 1):
                cell = numbers[row_pos][col]

                else:
                    up = i

            #for i in range(1, count_of_rows - 1):
                #numbers[i][col] += min(tmp[i - 1], tmp[i + 1], numbers[i][col + 1])

        path = numbers[0][0]

        for row in numbers:
            if path > row[0]:
                path = row[0]
                print row[0]
        return path

def main():
    numbers = []

    with open('matrixT.txt', 'r') as f:
        for line in f:
            tmp_list = line.split(',')
            numbers.append([int(x) for x in tmp_list])

    print find_path(numbers)

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

