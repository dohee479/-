# 피보나치 수 5
import sys
sys.stdin = open('input.txt', 'r')


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


N = int(input())
print(fibo(N))