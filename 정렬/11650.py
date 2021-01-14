# 좌표 정렬하기
import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
coordinate = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))
for i in coordinate:
    print(i[0], i[1])