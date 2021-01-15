# 좌표 정렬하기 2
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
coordinate = sorted([list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
for i in coordinate:
    print(i[0], i[1])

