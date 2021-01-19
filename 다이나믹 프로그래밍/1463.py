# 1로 만들기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


# bfs
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


# dp
# 점화식 dp[n] = dp[n // 3] + 1, dp[n] = dp[n // 2] + 1, dp[n] = dp[n - 1] + 1
N = int(input())
dp = [0 for _ in range(N + 1)]
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    # 2로 나누었을 때, -1 한 경우보다 작을 경우
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
    # 3로 나누었을 때, -1 or 2로 나눈 경우보다 작을 경우
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[N])


# dp
def dp(n):
    if n in memo:
        return memo[n]
    # 나머지를 더해준 이유 짐작: 7의 경우 2, 3으로 나누어 지지 않으므로 -1를 무조건 해줘야한다.
    # 이 경우를 나머지로 더해주는 것으로 짐작된다.
    m = 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3)
    memo[n] = m
    return m


memo = {1: 0, 2: 1}
N = int(input())
print(dp(N))