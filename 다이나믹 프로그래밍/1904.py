# 01타일
import sys
sys.stdin = open('input.txt', 'r')


def tile(n, result):
    global cnt
    binary = ['00', '1']
    if len(result) == n:
        cnt += 1
        return

    for i in binary:
        if len(result + i) <= n:
            tile(n, result + i)
    return cnt % 15746


N = int(input())
cnt = 0
print(tile(N, ''))

