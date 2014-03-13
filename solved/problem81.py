#! /usr/bin/env python
# -*- coding: utf-8 -*-

def read_matrix():
    matrix = []

    with open('matrix.txt', 'rb') as f:
        data = f.readlines()

        for line in data:
            matrix.append(line.split(','))

    for line in range(0, len(matrix)):
        for i in range(0, len(matrix[0])):
            matrix[line][i] = int(matrix[line][i])

    return matrix

def find_path(matrix):
    last_row = len(matrix) - 1
    last_column = len(matrix[0]) - 1

    for i in range(len(matrix[0]) - 1, -1, -1):
        matrix[last_row][i - 1] += matrix[last_row][i]

    for i in range(len(matrix) - 1, -1, -1):
        matrix[i - 1][last_column] = matrix[i][last_column] 

    for row in range(len(matrix) - 2, -1, -1):
        for col in range(len(matrix[0]) - 2, -1, -1):
                matrix[row][col] += min(matrix[row + 1][col], matrix[row][col + 1])
    print matrix[0][0]

def main():
    matrix = read_matrix()
    find_path(matrix)

if __name__ == "__main__":
    main()

