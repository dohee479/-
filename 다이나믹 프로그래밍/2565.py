# 전깃줄
import sys
sys.stdin = open('input.txt', 'r')

# 가장 적은 수의 전깃줄을 자르려면 반대로 가장 많은 갯수의 전깃줄을 구하면 된다.
N = int(input())
# A번째 전깃줄로 먼저 정렬
wire = sorted([list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)], key=lambda x: x[0])
lis = [0] * N
# B를 기준으로 LIS 적용
for i in range(N):
    lis[i] = 1
    for j in range(i):
        if wire[i][1] > wire[j][1]:
            lis[i] = max(lis[i], lis[j] + 1)
print(N - max(lis))