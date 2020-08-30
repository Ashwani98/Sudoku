import numpy as np


def is_safe(grid, r, c, v):
    for i in range(9):
        if grid[r][i] == v or grid[i][c] == v:
            return False

    for i in range(3):
        for j in range(3):
            if grid[r // 3 * 3 + i][c // 3 * 3 + j] == v:
                return False
    return True


def is_valid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                v = grid[i][j]
                grid[i][j] = 0
                if is_safe(grid, i, j, v):
                    grid[i][j] = v
                else:
                    return False
    return True


def is_complete(grid):
    return np.product(np.array(grid))


def empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j


def solve(grid):
    if is_complete(grid):
        return grid

    r, c = empty_cell(grid)

    for i in range(1, 10):
        if is_safe(grid, r, c, i):
            grid[r][c] = i

            if solve(grid):
                return grid

            grid[r][c] = 0

    return False


def print_board(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' ')
            if j % 3 == 2 and j < 7:
                print('|', end=' ')
        if i % 3 == 2 and i < 7:
            print()
            print('---------------------')
        else:
            print()


'''
weekly unsolvable board from sudokuwiki:

board = [[6,0,0,0,0,8,9,4,0],
        [9,0,0,0,0,6,1,0,0],
        [0,7,0,0,4,0,0,0,0],
        [2,0,0,6,1,0,0,0,0],
        [0,0,0,0,0,0,2,0,0],
        [0,8,9,0,0,2,0,0,0],
        [0,0,0,0,6,0,0,0,5],
        [0,0,0,0,0,0,0,3,0],
        [8,0,0,0,0,1,6,0,0]]
'''

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 2, 3, 4, 5, 0, 0],
         [0, 0, 7, 0, 0, 0, 6, 0, 0],
         [1, 0, 6, 0, 0, 0, 7, 0, 0],
         [0, 0, 5, 0, 0, 0, 8, 0, 0],
         [0, 0, 4, 3, 2, 1, 9, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

try:
    if is_valid(board):
        if not solve(board):
            print("Board can't be solved")
    else:
        print('Invalid Board')
except:
    print_board(board)
