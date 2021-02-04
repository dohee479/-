# 연속합
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
memo = [0] * n
memo[0] = seq[0]
# i번째서의 최대값은 i - 1까지의 최대값에 i를 더해준 값이다.
for i in range(1, n):
    memo[i] = max(memo[i - 1] + seq[i], seq[i])
print(max(memo))