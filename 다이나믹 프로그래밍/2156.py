# 포도주 시식
import sys
sys.stdin = open('input.txt', 'r')


def dp(n):
    result = [0] * n
    result[0] = wine[0]
    if n == 1:
        return result[0]
    result[1] = wine[0] + wine[1]
    if n == 2:
        return result[1]
    result[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])
    if n == 3:
        return result[-1]
    for i in range(3, n):
        result[i] = max(result[i - 3] + wine[i - 1] + wine[i], result[i - 2] + wine[i], result[i - 1])
    return result[-1]


n = int(input())
wine = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
print(dp(n))