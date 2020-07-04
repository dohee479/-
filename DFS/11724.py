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
for k in range(1, N+1):
    if visited[k] == 0:
        stack = [k]
        visited[k] = 1
        cnt += 1
    while len(stack) > 0:
        current = stack[-1]
        for i in range(1, N+1):
            if graph[current][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
print(cnt)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
adj = [0] * (N+1)
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 0
for i in range(1, N+1):
    if adj[i] == 0:
        stack = [i]
        cnt += 1
        while stack:
            current = stack.pop()
            if adj[current] == 0:
                adj[current] = 1
                stack += graph[current]
print(cnt)






