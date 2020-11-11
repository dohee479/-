# 달팽이는 올라가고 싶다
import sys
sys.stdin = open('input.txt', 'r')


def snail(a, b, v):
    day = 0
    height = 0
    while True:
        height += a
        day += 1
        if height >= v:
            return day
        height -= b


A, B, V = map(int, input().split())
print(snail(A, B, V))
