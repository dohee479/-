# 줄 세우기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
height = deque(map(int, input().split()))
for m in range(M-1):
    tall = deque(map(int, input().split()))
    for i in range(len(height)):
        if tall[1] == height[i]:
            height.insert(i, tall[0])
            break
    else:
        height.extend(tall)
print(' '.join(map(str, height)))



