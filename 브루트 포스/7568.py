# 덩치
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
bulk = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    cnt = 1
    for j in range(N):
        if bulk[i][0] < bulk[j][0] and bulk[i][1] < bulk[j][1]:
            cnt += 1
    print(cnt, end=' ')




