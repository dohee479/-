# 이항 계수 1
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().rstrip().split())
factorial = [0] * (N + 1)
factorial[0] = 1
factorial[1] = 1
for i in range(2, N + 1):
    factorial[i] = factorial[i - 1] * i
print(factorial[N] // (factorial[K] * factorial[N - K]))