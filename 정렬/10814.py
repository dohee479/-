# 나이순 정렬
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
member = sorted([list(map(str, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: int(x[0]))
for i in member:
    print('{} {}'.format(i[0], i[1]))