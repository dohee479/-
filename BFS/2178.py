# 미로 탐색
import sys
sys.stdin = open('input.txt', 'r')

def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    stack = [(x, y)]
    adj[x][y] = 1
    while stack:
        x, y = stack.pop(0)
        if x == N-1 and y == M-1:
            print(adj[x][y])
            break
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and adj[nx][ny] == 0:
                stack.append((nx, ny))
                adj[nx][ny] = adj[x][y] + 1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
adj = [[0] * M for _ in range(N)]
bfs(0, 0)
