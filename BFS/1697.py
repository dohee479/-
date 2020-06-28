# 숨바꼭질
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(n):
    stack = deque([(n, 0)])
    visited = [False] * 200001
    result = 0
    while stack:
        current, cnt = stack.popleft()
        if current == K:
            result = cnt
            break
        if 0 <= current - 1 <= 200000 and not visited[current-1]:
            stack.append((current - 1, cnt + 1))
            visited[current-1] = True
        if 0 <= current + 1 <= 200000 and not visited[current+1]:
            stack.append((current + 1, cnt + 1))
            visited[current+1] = True
        if 0 <= current * 2 <= 200000 and not visited[current*2]:
            stack.append((current * 2, cnt + 1))
            visited[current*2] = True
    return result


N, K = map(int, input().split())
print(bfs(N))


