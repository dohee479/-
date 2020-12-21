# 유기농 배추
import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = deque()
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 1:
                farm[nx][ny] = 0
                stack.append((nx, ny))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 1:
                farm[nx][ny] = 0
                queue.append((nx, ny))


T = int(input())
for t in range(1, 1+T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    for _ in range(K):
        n1, n2 = map(int, input().split())
        farm[n2][n1] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                farm[i][j] = 0
                cnt += 1
                dfs(i, j)
    print(cnt)











