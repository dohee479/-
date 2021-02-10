# 이항 계수 2
import sys
sys.stdin = open('input.txt', 'r')


# 시간초과
def combine(n, k):
    if k == 0:
        return 1
    if k == n:
        return 1
    if memo[n][k] != -1:
        return memo[n][k]
    return combine(n - 1, k - 1) + combine(n - 1, k)


N, K = [int(x) for x in input().split(' ')]
memo = [[-1 for k in range(K + 1)] for n in range(N + 1)]
print(combine(N, K))