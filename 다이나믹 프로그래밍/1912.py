# 연속합
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
memo = [0] * n
memo[0] = seq[0]
for i in range(n):
    for j in range(i + 1, n):
        memo[j] = max(memo[j - 1] + seq[j], memo[j])
print(max(memo))