# 스도쿠
import sys
sys.stdin = open('input.txt', 'r')


# 실패 
def backtrack(idx):
    if idx == 9:
        return
    for j in range(9):
        if not sudoku[idx][j]:
            for k in range(1, 10):
                if not sudoku[idx][j] and k not in sudoku[idx]:
                    sudoku[idx][j] = k
                    if not vertical(idx, j, k) or not square(idx, j, k):
                        sudoku[idx][j] = 0
            backtrack(idx + 1)


def vertical(row, col, k):
    for i in range(9):
        if i != row and sudoku[i][col] == k:
            return False
    else:
        return True


def square(row, col, num):
    if 0 <= row < 3:
        if 0 <= col < 3:
            for j in range(3):
                for k in range(3):
                    if j != row and k != col and sudoku[j][k] == num:
                        return False

        elif 3 <= col < 6:
            for j in range(3):
                for k in range(3, 6):
                    if j != row and k != col and sudoku[j][k] == num:
                        return False

        elif 6 <= col < 9:
            for j in range(3):
                for k in range(6, 9):
                    if j != row and k != col and sudoku[j][k] == num:
                        return False

    elif 3 <= row < 6:
        if 0 <= col < 3:
            for j in range(3, 6):
                for k in range(3):
                    if j != row and k != col and sudoku[j][k] == num:
                        return False

        elif 3 <= col < 6:
            for j in range(3, 6):
                for k in range(3, 6):
                    if j != row and k != col and sudoku[j][k] == num:
                        return False

        elif 6 <= col < 9:
            for j in range(3, 6):
                for k in range(6, 9):
                    if j != row and k != col and sudoku[j][k] == num:
                        return False

    elif 6 <= row < 9:
        if 0 <= col < 3:
            for j in range(6, 9):
                for k in range(3):
                    if j != row and k != col and sudoku[j][k] == num:
                        return False

        elif 3 <= col < 6:
            for j in range(6, 9):
                for k in range(3, 6):
                    if j != row and k != col and sudoku[j][k] == num:
                        return False

        elif 6 <= col < 9:
            for j in range(6, 9):
                for k in range(6, 9):
                    if j != row and k != col and sudoku[j][k] == num:
                        return False
    return True


sudoku = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
backtrack(0)
print('\n'.join([' '.join([str(j) for j in i]) for i in sudoku]))