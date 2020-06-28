# N과 M(3)

import sys
sys.stdin = open('input.txt', 'r')

def seq(idx, n, m):
    if idx == m:
        for i in range(m):
            print(num[i], end=' ')
        print()
        return

    for i in range(1, n+1):
        num[idx] = i
        seq(idx+1, n, m)


N, M = map(int, input().split())
visited = [0] * (N+1)
num = [0] * M
seq(0, N, M)