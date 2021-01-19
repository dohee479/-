# 1로 만들기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


# bfs와 메모이제이션 이용
def dp(n):
    memo = set()
    queue = deque([(n, 0)])
    while queue:
        x, cnt = queue.popleft()
        if x == 1:
            return cnt
        if x not in memo:
            if not x % 3:
                queue.append((x // 3, cnt + 1))
            if not x % 2:
                queue.append((x // 2, cnt + 1))
            queue.append((x - 1, cnt + 1))


N = int(input())
print(dp(N))


# 