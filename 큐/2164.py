# 카드2
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

N = int(input())
queue = deque(i for i in range(1, N + 1))
while len(queue) != 1:
    for _ in range(2):
        num = queue.popleft()
    queue.append(num)
print(queue[0])
