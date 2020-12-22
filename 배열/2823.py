# 유턴 싫어
import sys
sys.stdin = open('input.txt', 'r')


def drive(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]
        if 0 <= nx < R and 0 <= ny < C and road[nx][ny] == '.':
            cnt += 1
    return cnt


R, C = map(int, input().split())
road = [list(input()) for _ in range(R)]
result = []
for i in range(R):
    for j in range(C):
        if road[i][j] == '.':
            if drive(i, j) <= 1:
                print(1)
            else:
                print(0)
            result.append(drive(i, j))
if result.count(1) or result.count(0):
    print(1)
else:
    print(0)


def drive():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(R):
        for y in range(C):
            cnt = 0
            if road[x][y] == '.':
                for direct in range(4):
                    nx = x + dx[direct]
                    ny = y + dy[direct]
                    if 0 <= nx < R and 0 <= ny < C and road[nx][ny] == '.':
                        cnt += 1
                if cnt <= 1:
                    return 1
    return 0


R, C = map(int, input().split())
road = [list(input()) for _ in range(R)]
print(drive())

