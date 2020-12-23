# 제로
import sys
sys.stdin = open('input.txt', 'r')


K = int(input())
stack = []
for _ in range(K):
    N = int(input())
    if N:
        stack.append(N)
    else:
        stack.pop()
print(sum(stack))