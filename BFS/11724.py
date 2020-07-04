# 연결 요소의 개수
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
adj = [0] * (N+1)
for m in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
cnt = 0
for i in range(1, N+1):
    if adj[i] == 0:
        queue = [i]
        adj[i] = 1
        cnt += 1
        while queue:
            current = queue.pop(0)
            for j in range(1, N+1):
                if graph[current][j] == 1 and adj[j] == 0:
                    queue.append(j)
                    adj[j] = 1
print(cnt)






