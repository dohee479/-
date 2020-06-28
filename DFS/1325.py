# 효율적인 해킹
import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):
    visited = [0] * (N + 1)
    stack = [v]
    cnt = 0
    while stack:
        current = stack.pop()
        if visited[current] == 0:
            visited[current] = 1
            stack += com[current]
            cnt += 1
    return cnt


N, M = map(int, input().split())
com = [[] for _ in range(N+1)]
for m in range(M):
    n1, n2 = map(int, input().split())
    com[n2].append(n1)
max_num = 0
result = []
for i in range(1, N+1):
    if com[i]:
        count = dfs(i)
        if count > max_num:
            result = [i]
            max_num = count
        elif count == max_num:
            result.append(i)
for j in result:
    print(j, end=' ')

