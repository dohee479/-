# 연구소
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def combi(cnt):
    if cnt == 3:
        if bfs() > result[0]:
            result[0] = bfs()
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] != 0 or visited[i][j] == 1:
                continue
            lab[i][j] = 1
            for k in range(j+1):
                visited[i][k] = 1
            combi(cnt+1)
            lab[i][j] = 0
            for k in range(M):
                visited[i][k] = 0


def bfs():
    stack = deque()
    adj = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                stack.append((i, j))
                adj[i][j] = 1
            if lab[i][j] == 1:
                adj[i][j] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while stack:
        x, y = stack.popleft()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0 and adj[nx][ny] == 0:
                adj[nx][ny] = 1
                stack.append((nx, ny))
    count = 0
    for i in range(N):
        for j in range(M):
            if adj[i][j] == 0:
                count += 1
    return count


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = [0]
combi(0)
print(result[0])

