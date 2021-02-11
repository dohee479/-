# 이항 계수 2
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().rstrip().split())
factorial = [0] * (N + 1)
factorial[0] = 1
factorial[1] = 1
for i in range(2, N + 1):
    factorial[i] = factorial[i - 1] * i
print((factorial[N] // (factorial[K] * factorial[N - K])) % 10007)


# 시간초과
# 점화식 이용
# def combine(n, k):
#     if k == 0:
#         return 1
#     if k == n:
#         return 1
#     if memo[n][k] != -1:
#         return memo[n][k]
#     return combine(n - 1, k - 1) + combine(n - 1, k)
#
#
# N, K = [int(x) for x in input().split(' ')]
# memo = [[-1 for k in range(K + 1)] for n in range(N + 1)]
# print(combine(N, K))


