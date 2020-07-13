# 경로 찾기
import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):
    visited = [0] * N
    stack = [v]
    while stack:
        current = stack.pop()
        if visited[current] == 0:
            visited[current] = 1
            stack += line[current]
            if v != current:
                result[v][current] = 1
            if graph[current][v] == 1:
                result[v][v] = 1


N = int(input())
line = [[] for _ in range(N)]
graph = []
result = [[0] * N for _ in range(N)]
for i in range(N):
    info = list(map(int, input().split()))
    for j in range(N):
        if info[j] == 1:
            line[i].append(j)
    graph.append(info)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i)
for i in range(N):
    for j in range(N):
        print(result[i][j], end=' ')
    print()



