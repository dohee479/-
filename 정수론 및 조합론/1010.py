# 다리 놓기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    factorial = [0] * (M + 1)
    factorial[0] = 1
    factorial[1] = 1
    for i in range(2, M + 1):
        factorial[i] = factorial[i - 1] * i
    print(factorial[M] // (factorial[N] * factorial[M - N]))