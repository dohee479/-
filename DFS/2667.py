# 단지 번호 붙이기
import sys
sys.stdin = open('input.txt', 'r')


def danzi(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = [(x, y)]
    count = 0
    while stack:
        x, y = stack.pop()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < N and subdivision[nx][ny] == 1:
                stack.append((nx, ny))
                subdivision[nx][ny] = 0
        count += 1
    return count


N = int(input())
subdivision = [list(map(int, input())) for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if subdivision[i][j] == 1:
            subdivision[i][j] = 0
            result.append(danzi(i, j))
            result.sort()
print(len(result))
for i in result:
    print(i)












