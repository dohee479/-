# 01타일
import sys
sys.stdin = open('input.txt', 'r')


# def tile(n, result):
#     global cnt
#     binary = ['00', '1']
#     if len(result) == n:
#         cnt += 1
#         return
#
#     for i in binary:
#         if len(result + i) <= n:
#             tile(n, result + i)
#     return cnt % 15746


def tile(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    count1, count2 = 1, 2
    for _ in range(2, n+1):
        count1, count2 = count2, count1 + count2
    return count2 % 15


N = int(input())
cnt = 0
print(tile(N))

