# 토마토
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def bfs():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque()
    for x in range(N):
        for y in range(M):
            if tomato[x][y] == 1:
                queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                queue.append((nx, ny))
                tomato[nx][ny] = tomato[x][y] + 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j] != 0:
                cnt += 1
        
    if cnt == N * M:
        return tomato[x][y] - 1
    else:
        return -1
    # for t in tomato:
    #     if 0 in t:
    #         print(-1)
    #         break
    # else:
    #     print(tomato[x][y] - 1)


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
print(bfs())

# M, N = map(int, input().split())
# stack = deque()
# tomato = []
# for i in range(N):
#     a = list(map(int, input().split()))
#     for j in range(M):
#         if a[j] == 1:
#             stack.append((i, j))
#     tomato.append(a)
# bfs()