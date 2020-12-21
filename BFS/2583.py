# 영역 구하기
import sys
sys.stdin = open('input.txt', 'r')


def bfs(x, y):
    result = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = [(x, y)]
    adj[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        space[x][y] = 2
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < M and space[nx][ny] == 0 and adj[nx][ny] == 0:
                queue.append((nx, ny))
                adj[nx][ny] = 1
                result += 1
    return result


M, N, K = map(int, input().split())
space = [[0] * M for _ in range(N)]
adj = [[0] * M for _ in range(N)]
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            space[i][j] = 1
answer = []
cnt = 0
for i in range(N):
    for j in range(M):
        if space[i][j] == 0:
            cnt += 1
            answer.append(bfs(i, j))
answer.sort()
print(cnt)
print(' '.join(map(str, answer)))


