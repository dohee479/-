# 숨바꼭질
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def bfs(n):
    queue = deque([(n, 0)])
    visited = [False] * 100001
    while queue:
        current, cnt = queue.popleft()
        if current == K:
            return cnt
        if 0 <= current - 1 and not visited[current-1]:
            queue.append((current - 1, cnt + 1))
            visited[current-1] = True
        if current + 1 <= K+1 and not visited[current+1]:
            queue.append((current + 1, cnt + 1))
            visited[current+1] = True
        if current * 2 <= K+1 and not visited[current*2]:
            queue.append((current * 2, cnt + 1))
            visited[current*2] = True


N, K = map(int, input().split())
print(bfs(N))


