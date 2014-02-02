#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

def find_path(numbers):

#len(tmp) == number of rows
    count_of_rows = len(numbers) 
    count_of_columns = len(numbers[0])

    for col in range(count_of_columns - 2, -1, -1):
        tmp = []

        for row in numbers:
            tmp.append(row[col] + row[col + 1])

        numbers[0][col] = tmp[0]
        numbers[count_of_rows - 1][col] = tmp[count_of_rows - 1]

        for i in range(1, count_of_rows - 1):
            numbers[i][col] += min(tmp[i - 1], tmp[i + 1], numbers[i][col + 1])

    path = numbers[0][0]

    for row in numbers:
        if path > row[0]:
            path = row[0]
            print row[0]
    return path

def main():
    numbers = []

    with open('matrix.txt', 'r') as f:
        for line in f:
            tmp_list = line.split(',')
            numbers.append([int(x) for x in tmp_list])

    print find_path(numbers)

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start

