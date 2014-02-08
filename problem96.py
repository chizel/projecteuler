#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Sudoku():
    '''Solve sudoku'''

    def __init__(self, lines):
        self.__lines = lines
        self.reset_sudoku()
    

    def reset_sudoku(self):
        self.__generate_sudoku()
        self.__generate_guess_nums()

    def __generate_sudoku(self):
        '''generate sudoku, input is 1-9 for filled cells,
        0 for empty cells. Each line of sudoku must contain
        only digits. Lines delimeter is space.
        Input example (first sudoku's line): 098001030'''
        self.sudoku = []

        for i in range(0, len(self.__lines)):
            self.sudoku.append([])

            for digit in self.__lines[i]:
                self.sudoku[i].append(int(digit))

    def __generate_guess_nums(self):
        '''guess_nums contains all possible variants of digits
        that cab be filled in current cell.
        If cell filled, guess_nums of this cell is empty.'''
        self.guess_nums = []

        for i in range(0,9):
            self.guess_nums.append([])

            for j in range(0, 9):
#cell contain number
                if self.sudoku[i][j]:
                    self.guess_nums[i].append([])
                else:
                    self.guess_nums[i].append([x for x in range(1,10)])

    def __what_square(self, row=0, column=0, square_number=-1):
        '''return square's indicex by:
            row and column
            square number (0..8)'''

        square = []

        if square_number >= 0:
            if square_number < 3:
                square.append([0,1,2])
            elif square_number < 6:
                square.append([3,4,5])
            else:
                square.append([6,7,8])

            if not square_number % 3:
                square.append([0,1,2])
            elif (square_number % 3) == 1:
                square.append([3,4,5])
            else:
                square.append([6,7,8])
            return square

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
        '''if number filled to sudoku, delete it
        from guess_nums same row, column and square'''

        square = self.__what_square(row, column)

#delete number from square
        for i in square[0]:
            for j in square[1]:
                if not self.guess_nums[i][j]:
                    continue
                if not number in self.guess_nums[i][j]:
                    continue
                self.guess_nums[i][j].remove(number)

#delete number from current row
        for i in range(0, 9):
            if not self.guess_nums[row][i]:
                continue
            if not number in self.guess_nums[row][i]:
                continue
            self.guess_nums[row][i].remove(number)

#delete number from current column
        for i in range(0, 9):
            if not self.guess_nums[i][column]:
                continue
            if not number in self.guess_nums[i][column]:
                continue
            self.guess_nums[i][column].remove(number)

        while self.__check():
            pass

    def __check(self):
        '''if guess_nums[i][j] contain only one number - 
        fill it to sudoku and delete it from guess_nums
        row i, column j, square, that contain [i][j]'''

        changed = False

        for i in range(0,9):
            for j in range(0,9):
                if len(self.guess_nums[i][j]) == 1:
                    changed = True
                    self.sudoku[i][j] = self.guess_nums[i][j][0]
                    self.__delete_number(self.sudoku[i][j], i, j)
        return changed
         
    def check_row(self, row):
        '''if we meet digit only once in this row - fill it
        to sudoku'''

#contain how many times we meet digit
        tmp = [0] * 9
#contain index of column of latest digit
        col_ind = [0] * 9
        changed = False

        for i in range(0, 9):
            for number in self.guess_nums[row][i]:
                tmp[number - 1] += 1
                col_ind[number - 1] = i

        for i in range(0, 9):
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
        square  = self.__what_square(square_number=square_num)
        tmp = [0] * 9
        row_ind = [0] * 9
        col_ind = [0] * 9
        changed = False

        for row in square[0]:
            for column in square[1]:
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
                    f_num, s_num = self.guess_nums[row][j]

                    for k in range(0, 9):
                        if k == i or k == j:
                            continue
                        if f_num in self.guess_nums[row][k]:
                            changed = True
                            self.guess_nums[row][k].remove(f_num)
                        if s_num in self.guess_nums[row][k]:
                            changed = True
                            self.guess_nums[row][k].remove(s_num)
        return changed

    def check_column_pair(self, column):
        changed = False

        for i in range(0, 9):
            if not len(self.guess_nums[i][column]) == 2:
                continue

            for j in range(i + 1, 9):
                if self.guess_nums[i][column] == self.guess_nums[j][column]:
                    f_num, s_num = self.guess_nums[j][column]

                    for k in range(0, 9):
                        if k == i or k == j:
                            continue
                        if f_num in self.guess_nums[k][column]:
                            changed = True
                            self.guess_nums[k][column].remove(f_num)
                        if s_num in self.guess_nums[k][column]:
                            changed = True
                            self.guess_nums[k][column].remove(s_num)
        return changed

    def solve_sudoku(self):
        for i in range(0,9):
            for j in range(0,9):
                if not self.sudoku[i][j]:
                    continue
                self.__delete_number(self.sudoku[i][j], i, j)

        again = True

        while again:
            again = False

            while self.__check():
                again = True

            changed = True
            while changed:
                changed  = False

                for i in range(0, 9):
                    if self.check_square(i):
                        changed = True
                        again = True

            changed = True
            while changed:
                changed = False

                for i in range(0, 9):
                    if self.check_column(i):
                        changed = True
                        again = True

            changed = True
            while changed:
                changed = False
                for i in range(0, 9):
                    if self.check_row(i):
                        again = True 
                        changed = True

            changed = True
            while changed:
                changed = False

                for i in range(0, 9):
                    if self.check_row_pair(i):
                        again = True
                        changed = True

            changed = True
            while changed:
                changed = False

                for i in range(0, 9):
                    if self.check_column_pair(i):
                        again = True
                        changed = True

        self.print_len_guess()

    def is_solved(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.guess_nums[i][j]:
                    return False

        for row in self.sudoku:
            for i in range(0, 9):
                if row[i] in row[i + 1:]:
                    return False
        
        tmp = []

        for i in range(0, 9):
            for j in range(0, 9):
                tmp.append(self.sudoku[i][j])

        for i in range(0, 9):
            if tmp[i] in tmp[i + 1:]:
                return False

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
    #source = []
    #with open('sudoku.txt', 'r') as f:
        #for line in f:
            #if line[0] == 'G':
                #source.append('')
            #else:
                #if line[-1] == '\n':
                    #line = line[:-1]
    #            source[-1] += ' ' + line
    source = ['100920000 524010000 000000070 050008102 000000000 402700090 060000000 000030945 000071006']

    for line in source:
        p = Sudoku(line.split())
        p.print_sudoku()
        p.solve_sudoku()
        p.print_sudoku()
        #inp = raw_input('Next')
        p.print_guess_nums()

if __name__ == "__main__":
    main()
