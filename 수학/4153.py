# 직각삼각형
import sys
sys.stdin = open('input.txt', 'r')


while True:
    x, y, z = sorted(map(int, input().split()))
    if x == 0 and y == 0 and z == 0:
        break
    print('right' if x ** 2 + y ** 2 == z ** 2 else 'wrong')

