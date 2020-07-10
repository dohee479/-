# 안전영역
import sys
sys.stdin = open('input.txt', 'r')


def dfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        if rain[x][y] <= height:
            rain[x][y] = 0
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < N and rain[nx][ny] > height and visited[nx][ny] == 0:
                stack.append((nx, ny))
                visited[nx][ny] = 1
        else:
            x, y = stack.pop()


N = int(input())
rain = [list(map(int, input().split())) for _ in range(N)]
max_num = max(map(max, rain))
min_num = min(map(min, rain))
max_size = 0
sibal = 1
for height in range(min_num, max_num+1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if rain[i][j] > height and visited[i][j] == 0:
                cnt += 1
                dfs(i, j)
    if cnt > max_size:
        max_size = cnt
print(max(sibal, max_size))








