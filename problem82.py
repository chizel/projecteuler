#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

class FindMinPath():
    def __init__(self, numbers):
        self.numbers = numbers
        self.count_row = len(numbers) 
        self.count_col = len(numbers[0])
        self.reset_moves()

    def reset_moves(self):
        self.where_move = [0] * self.count_row
        self.tmp_sum = [0] * self.count_row
        self.result = [0] * self.count_row

    def find_path(self):
        for col in range(self.count_col - 2, -1, -1):
            self.reset_moves()

            for row in range(0, self.count_row):
                self.tmp_sum[row] = self.numbers[row][col] + self.numbers[row][col + 1]

            pos = self.tmp_sum.index(min(self.tmp_sum))

#minimum path in this column
            self.result[pos] = self.tmp_sum[pos]
            self.where_move[pos] = pos

            for i in range(pos - 1, -1, -1):
                self.check_up(i, col)

            for i in range(pos + 1, self.count_row):
                self.check_down(i, col)

            for i in range(0, self.count_row):
                self.numbers[i][col] = self.result[i]

        path = self.numbers[0][0]

        for row in self.numbers:
            if path > row[0]:
                path = row[0]
        return path

    def check_up(self, row, col):
        if row < 0:
            return
#set sum of current cell and cell[row][col - 1] the minimum path
        current_cell = self.numbers[row][col]
        min_path = self.tmp_sum[row]
        self.where_move[row] = row
        
#if element [row + 1] has path less then current min_path - set it as min_path
        if min_path > current_cell + self.result[row + 1] and self.where_move[row + 1] > row:
            min_path = current_cell + self.result[row + 1]
            self.where_move[row] = row + 1

#check upper elements for best path
        for i in range(row - 1, -1, -1):
            if self.where_move[i] > i:
                break

            tmp = 0

            for j in range(row, i, -1):
                tmp += self.numbers[j][col]
 
            tmp += self.tmp_sum[i]

            if min_path > tmp:
                min_path = tmp
                self.where_move[row] = i
            else:
                break
        

        self.result[row] = min_path

    def check_down(self, row, col):
        if row >= self.count_row:
            return

#set sum of current cell and cell[row][col - 1] the minimum path
        current_cell = self.numbers[row][col]
        min_path = self.tmp_sum[row]
        self.where_move[row] = row
 
#if upper element has path less then current min_path - set it as min_path
        if min_path > current_cell + self.result[row - 1] and self.where_move[row - 1] < row:
            min_path = current_cell + self.result[row - 1]
            self.where_move[row] = row - 1

        for i in range(row + 1, self.count_row):
            if self.where_move[i] < i:
                break


            tmp = 0
            for j in range(row, i):
                tmp += numbers[row][col]

            tmp += self.tmp_sum[i]

            if min_path > tmp:
                min_path = tmp
                self.where_move[row] = i
            else:
                break
        self.result[row] = min_path

def main():
    numbers = []

    with open('matrix.txt', 'r') as f:
        for line in f:
            tmp_list = line.split(',')
            numbers.append([int(x) for x in tmp_list])

    path = FindMinPath(numbers)
    print path.find_path()

if __name__ == "__main__":
    start = time.time()
    main()
    print 'Time: ', time.time() - start
