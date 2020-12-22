# 블랙잭
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
num = list(map(int, input().split()))
result = 0
max_num = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            result = num[i] + num[j] + num[k]
            if max_num < result <= M:
                max_num = result
print(max_num)



