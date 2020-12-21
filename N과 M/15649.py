# N과 M(1)

import sys
sys.stdin = open('input.txt', 'r')


def seq(idx, n, m):
    if idx == m:
        for i in range(m):
            print(num[i], end=' ')
        print()
        return

    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        num[idx] = i
        visited[i] = 1
        seq(idx+1, n, m)
        visited[i] = 0


N, M = map(int, input().split())
visited = [0] * (N+1)
num = [0] * M
seq(0, N, M)


# def nm(idx, n, m):
#     if idx == m:
#         for i in range(m):
#             print(sol[i], end = ' ')
#         print()
#         return
#
#     for i in range(1, n + 1):
#         if check[i]:
#             continue
#         check[i] = True
#         sol[idx] = i
#         nm(idx + 1, n, m)
#         check[i] = False
#
# n, m = map(int, input().split())
# check = [False] * (n + 1)
# sol = [0] * m
# nm(0, n, m)
