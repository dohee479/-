# 미로 탐색
import sys
sys.stdin = open('input.txt', 'r')


def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [(x, y)]
    adj[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        if x == N-1 and y == M-1:
            return adj[x][y]
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and adj[nx][ny] == 0:
                queue.append((nx, ny))
                adj[nx][ny] = adj[x][y] + 1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
adj = [[0] * M for _ in range(N)]
print(bfs(0, 0))
