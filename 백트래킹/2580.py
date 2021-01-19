# 스도쿠
import sys
sys.stdin = open('input.txt', 'r')


# 가로 체크
def horizontal(x, val):
    if val in sudoku[x]:
        return False
    return True


# 세로 체크
def vertical(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True


# 3x3 체크
def square(x, y, val):
    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nx+i][ny+j]:
                return False
    return True


def backtrack(index):
    if index == len(zeros):
        for row in sudoku:
            for n in row:
                print(n, end=" ")
            print()
        sys.exit(0)
    else:
        for i in range(1, 10):
            nx = zeros[index][0]
            ny = zeros[index][1]

            # 세로, 가로, 3x3에 내가 대체하려고하는 숫자가 존재하는지 확인
            if horizontal(nx, i) and vertical(ny, i) and square(nx, ny, i):
                sudoku[nx][ny] = i
                backtrack(index+1)
                sudoku[nx][ny] = 0


sudoku = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
backtrack(0)

