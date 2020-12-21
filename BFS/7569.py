# 토마토
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def bfs():
    dz = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]
    while queue:
        z, x, y = queue.popleft()
        for direct in range(6):
            nz = z + dz[direct]
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomato[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                tomato[nz][nx][ny] = tomato[z][x][y] + 1

    min_day = 0
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if tomato[z][x][y] == 0:
                    return -1
                min_day = max(min_day, tomato[z][x][y])
    return min_day-1


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomato[z][x][y] == 1:
                queue.append((z, x, y))
print(bfs())

