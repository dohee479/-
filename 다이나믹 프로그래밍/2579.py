# 계단 오르기
import sys
sys.stdin = open('input.txt', 'r')


def dp(n):
    result = [0] * n
    result[0] = stairs[0]
    if n == 1:
        return result[-1]
    result[1] = stairs[0] + stairs[1]
    if n == 2:
        return result[-1]
    result[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    if result == 3:
        return result[-1]
    for i in range(3, n):
        result[i] = max(stairs[i] + stairs[i - 1] + result[i - 3], stairs[i] + result[i - 2])
    return result[-1]


N = int(input())
stairs = [int(input()) for _ in range(N)]
print(dp(N))


a, b, c = 0, 0, 0
n = int(input())
for _ in range(n):
    pb = int(input())
    d_0, d_1, d_2 = max(b, c), a+pb, b+pb
    a, b, c = d_0, d_1, d_2

print(max(d_2, d_1))