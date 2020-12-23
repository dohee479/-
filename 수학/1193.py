# 분수찾기
import sys
sys.stdin = open('input.txt', 'r')


def fraction(n):
    num = 0
    cnt = 1
    while num < n:
        num += cnt
        cnt += 1
    if (cnt - 1) % 2:
        return '{}/{}'.format(1+num-n, cnt-1-(num-n))
    else:
        return '{}/{}'.format(cnt-1-(num-n), 1+num-n)


X = int(input())
print(fraction(X))
