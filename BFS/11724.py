# 연결 요소의 개수
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for m in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        stack = [i]
        visited[i] = 1
        cnt += 1
        while len(stack) > 0:
            deQ = stack.pop(0)
            for j in range(1, N+1):
                if graph[deQ][j] == 1 and visited[j] == 0:
                    stack.append(j)
                    visited[j] = 1
print(cnt)



