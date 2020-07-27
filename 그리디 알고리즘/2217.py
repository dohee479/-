# 로프
import sys
input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())
max_weight = 0
rope = sorted([int(input()) for _ in range(N)])
i = 0
while i < N:
    if rope[i] * (N-i) > max_weight:
        max_weight = rope[i] * (N - i)
    i += 1
print(max_weight)

# n = int(input())
# rope = [0] * 10001
# for _ in range(n):
#     rope[int(input())] += 1
# m, s = 0, 0
# for x in range(15, -1, -1):
#     s += rope[x]
#     m = max(m, x * s)
# print(m)