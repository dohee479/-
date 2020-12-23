# 달팽이는 올라가고 싶다
import sys, math
sys.stdin = open('input.txt', 'r')


def snail(a, b, v):
    return math.ceil((v - a) / (a - b)) + 1


A, B, V = map(int, input().split())
print(snail(A, B, V))


def snail(a, b, v):
    return round(((v - a) / (a - b)) + 0.49) + 1


A, B, V = map(int, input().split())
print(snail(A, B, V))
