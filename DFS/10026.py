# 적록색약
import sys
sys.stdin = open('input.txt', 'r')


def dfs(x, y, color):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and Color[nx][ny] == color:
                stack.append((nx, ny))
                visited[nx][ny] = 1


N = int(input())
Color = [list(map(str, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if (Color[i][j] == 'R' or Color[i][j] == 'G' or Color[i][j] == 'B') and visited[i][j] == 0:
            cnt += 1
            color = Color[i][j]
            dfs(i, j, color)

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if Color[i][j] == 'G':
            Color[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if Color[i][j] == 'R' and visited[i][j] == 0:
            cnt2 += 1
            dfs(i, j, Color[i][j])
        elif Color[i][j] == 'B' and visited[i][j] == 0:
            cnt2 += 1
            dfs(i, j, Color[i][j])
print(cnt, cnt2)








