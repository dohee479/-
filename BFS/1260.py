# DFS와 BFS
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 인접행렬
def dfs(v):
    result = [v]
    stack = [v]
    visited[v] = 1
    while stack:
        current = stack[-1]
        for i in range(1, N+1):
            if graph[current][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                result.append(i)
                break
        else:
            stack.pop()

    print(' '.join(map(str, result)))


def bfs(v):
    result = [v]
    queue = [v]
    adj[v] = 1
    while queue:
        current = queue.pop(0)
        for i in range(1, N+1):
            if graph[current][i] == 1 and adj[i] == 0:
                queue.append(i)
                adj[i] = 1
                result.append(i)
    print(' '.join(map(str, result)))


N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
adj = [0] * (N+1)
for m in range(M):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1
dfs(V)
bfs(V)

# 인접리스트
def dfs(v):
    stack = [v]
    result = []
    while stack:
        current = stack.pop()
        if visited[current] == 0:
            stack += graph[current]
            visited[current] = 1
            result.append(current)
    print(' '.join(map(str, result)))

def bfs(v):
    queue = [v]
    result = [v]
    adj[v] = 1
    while queue:
        current = queue.pop(0)
        for i in reversed(graph[current]):
            if adj[i] == 0:
                queue.append(i)
                adj[i] = 1
                result.append(i)
    print(' '.join(map(str, result)))


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
adj = [0] * (N+1)
for m in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
for i in range(len(graph)):
    graph[i].sort(reverse=True)
dfs(V)
bfs(V)


def bfs(v):
    queue = [v]
    result = []
    while queue:
        current = queue.pop(0)
        if adj[current] == 0:
            queue += graph[current]
            adj[current] = 1
            result.append(current)
    print(' '.join(map(str, result)))


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
adj = [0] * (N+1)
for m in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
for i in range(len(graph)):
    graph[i].sort()
bfs(V)