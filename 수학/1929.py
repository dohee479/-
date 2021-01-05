# 소수 구하기
import sys
sys.stdin = open('input.txt', 'r')

M, N = map(int, input().split())
prime = [False, False] + [True] * (N - 1)
for i in range(2, int((N + 1) ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, N + 1, i):
            prime[j] = False
for i, value in enumerate(prime):
    if value and i >= M:
        print(i)