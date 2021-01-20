# 쉬운 계단 수
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
cnt = 0
if N == 1:
    print(9)
else:
    for i in range(10, 100):
        a = str(i)
        count = 0
        for j in range(N - 1):
            if abs(int(a[j]) - int(a[j + 1])) == 1:
                count += 1
        if count == N - 1:
            cnt += 1
    print(cnt % 1000000000)