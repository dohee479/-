# 동전 0
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
coin = []
result = K
cnt = 0
for _ in range(N):
    n = int(input())
    coin.append(n)
for i in range(N-1, -1, -1):
    if result != 0:
        cnt += (result // coin[i])
        result = result % coin[i]
    else:
        break
print(cnt)


