# 설탕 배달
import sys
sys.stdin = open('input.txt', 'r')


def sugar(n):
    for i in range((n // 3) + 1):
        for j in range((n // 5) + 1):
            if 3 * i + 5 * j == N:
                return i + j
    return -1


N = int(input())
print(sugar(N))


