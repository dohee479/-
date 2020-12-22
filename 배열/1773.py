# 폭죽쇼
import sys
sys.stdin = open('input.txt', 'r')

N, C = map(int, input().split())
Fire = set()
cnt = 0
for n in range(N):
    num = int(input())
    if num == 1:
        cnt = C
        continue
    for i in range(num, C+1, num):
        Fire.add(i)
        cnt = len(Fire)
print(cnt)