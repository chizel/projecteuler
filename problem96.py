#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Sudoku():
    '''Solve sudoku'''

    def __init__(self, lines):
        self.__generate_sudoku(lines)
        self.__generate_guess_nums()

    def __generate_sudoku(self, lines):
        self.sudoku = []

        for i in range(0, len(lines)):
            self.sudoku.append([])

            for digit in lines[i]:
                self.sudoku[i].append(int(digit))

    def __generate_guess_nums(self):
        self.guess_nums = []

        for i in range(0,9):
            self.guess_nums.append([])

            for j in range(0, 9):
                if self.sudoku[i][j]:
                    self.guess_nums[i].append([])
                else:
                    self.guess_nums[i].append([x for x in range(1,10)])

    def __what_square(self, row, column):
        square = []

        if row <= 2:
            square.append([0,1,2])
        elif row <= 5:
            square.append([3,4,5])
        else:
            square.append([6,7,8])

        if column <= 2:
            square.append([0,1,2])
        elif column <= 5:
            square.append([3,4,5])
        else:
            square.append([6,7,8])

        return square

    def __delete_number(self, number, row, column):
        square = self.__what_square(row, column)

        for i in square[0]:
            for j in square[1]:
                if not self.guess_nums[i][j]:
                    continue
                if not number in self.guess_nums[i][j]:
                    continue
                self.guess_nums[i][j].remove(number)

        for i in range(0, 9):
            if not self.guess_nums[row][i]:
                continue
            if not number in self.guess_nums[row][i]:
                continue
            self.guess_nums[row][i].remove(number)

        for i in range(0, 9):
            if not self.guess_nums[i][column]:
                continue
            if not number in self.guess_nums[i][column]:
                continue
            self.guess_nums[i][column].remove(number)

        while self.__check():
            pass

    def __check(self):
        changed = False

        for i in range(0,9):
            for j in range(0,9):
                if len(self.guess_nums[i][j]) == 1:
                    changed = True
                    self.sudoku[i][j] = self.guess_nums[i][j][0]
                    self.__delete_number(self.sudoku[i][j], i, j)
        return changed
         
    def check_row(self, row):
        tmp = [0] * 9
        col_ind = [0] * 9
        changed = False

        for i in range(0, 9):
            for number in self.guess_nums[row][i]:
                tmp[number - 1] += 1
                col_ind[number - 1] = i

        for i in range(0, 9):
            #if tmp[i] == 1 and len(self.guess_nums[row][i]) > 1:
            if tmp[i] == 1:
                number = i + 1 
                ind = col_ind[number - 1]
                self.sudoku[row][ind] = number
                self.guess_nums[row][ind] = []
                self.__delete_number(number, row, ind)
                changed = True
        return changed

    def check_column(self, column):
        tmp = [0] * 9
        row_ind = [0] * 9
        changed = False

        for i in range(0, 9):
            for number in self.guess_nums[i][column]:
                tmp[number - 1] += 1
                row_ind[number - 1] = i

        for i in range(0, 9):
            #if tmp[i] == 1 and len(self.guess_nums[i][column]) > 1:
            if tmp[i] == 1:
                number = i + 1 
                ind = row_ind[number - 1]
                self.sudoku[ind][column] = number
                self.guess_nums[ind][column] = []
                self.__delete_number(number, ind, column)
                changed = True
        return changed

    def check_square(self, square_num):
        if square_num < 3:
            i = [0,1,2]
        elif square_num < 6:
            i = [3,4,5]
        else:
            i = [6,7,8]

        if not square_num % 3:
            j = [0,1,2]
        elif (square_num % 3) == 1:
            j = [3,4,5]
        else:
            j = [6,7,8]

        tmp = [0] * 9
        row_ind = [0] * 9
        col_ind = [0] * 9
        changed = False

        for row in i:
            for column in j:
                for number in self.guess_nums[row][column]:
                    tmp[number - 1] += 1
                    row_ind[number - 1] = row
                    col_ind[number - 1] = column
        for i in range(0, 9):
            #if tmp[i] == 1 and len(self.guess_nums[row][column]) > 1:
            if tmp[i] == 1:
                number = i + 1 
                ind_r = row_ind[number - 1]
                ind_c = col_ind[number - 1]
                self.guess_nums[ind_r][ind_c] = []
                self.sudoku[ind_r][ind_c] = number
                self.__delete_number(number, ind_r, ind_c)
                changed = True
        return changed
    
    def check_row_pair(self, row):
        changed = False
        for i in range(0, 9):
            if not len(self.guess_nums[row][i]) == 2:
                continue

            for j in range(i + 1, 9):
                if self.guess_nums[row][i] == self.guess_nums[row][j]:
                    changed = True
                    f_num, s_num = self.guess_nums[row][j]

                    for k in range(0, 9):
                        if k == i or k == j:
                            continue
                        if f_num in self.guess_nums[row][k]:
                            self.guess_nums[row][k].remove(f_num)
                        if s_num in self.guess_nums[row][k]:
                            self.guess_nums[row][k].remove(s_num)
        return changed

    def check_column_pair(self, column):
        changed = False

        for i in range(0, 9):
            if not len(self.guess_nums[i][column]) == 2:
                continue

            for j in range(i + 1, 9):
                if self.guess_nums[i][column] == self.guess_nums[j][column]:
                    changed = True
                    f_num, s_num = self.guess_nums[j][column]

                    for k in range(0, 9):
                        if k == i or k == j:
                            continue
                        if f_num in self.guess_nums[k][column]:
                            self.guess_nums[k][column].remove(f_num)
                        if s_num in self.guess_nums[k][column]:
                            self.guess_nums[k][column].remove(s_num)
        return changed

    def solve_sudoku(self):
        for i in range(0,9):
            for j in range(0,9):
                if not self.sudoku[i][j]:
                    continue
                self.__delete_number(self.sudoku[i][j], i, j)

        for j in range(0,2):
            while self.__check():
                pass

            changed = True
            while changed:
                for i in range(0, 9):
                    changed = self.check_square(i)

            changed = True
            while changed:
                for i in range(0, 9):
                    changed = self.check_column(i)

            changed = True
            while changed:
                for i in range(0, 9):
                    changed = self.check_row(i)

            changed = True
            while changed:
                for i in range(0, 9):
                    changed = self.check_row_pair(i)

            changed = True
            while changed:
                for i in range(0, 9):
                    changed = self.check_column_pair(i)

        self.print_len_guess()

    def print_len_guess(self):
        res = 0

        for line in self.guess_nums:
            for i in line:
                if len(i) > 0:
                    res += 1
        print res

    def print_sudoku(self):
        res = '.___________.\n'

        for i in range(0,9):

            if i == 3 or i == 6:
                res += '.---+---+---.\n'
            res += '|'

            for j in range(0,9):
                res += str(self.sudoku[i][j])
                if j == 2 or j == 5:
                    res += '|'
            res += '|\n'
        res += '.-----------.\n'
        print res

    def print_guess_nums(self):
        for line in self.guess_nums:
            print line

def main():
    #source = '003020600 900305001 001806400 008102900 700000008 006708200 002609500 800203009 005010300'
    source = '300200000 000107000 706030500 070009080 900020004 010800050 009040301 000702000 000008006'
    lines = source.split()
    
    p = Sudoku(lines)
    #p.print_sudoku()
    p.solve_sudoku()
    p.print_sudoku()
    p.print_guess_nums()

if __name__ == "__main__":
    main()
