# 벌집
import sys
sys.stdin = open('input.txt', 'r')



def bee(n):
    cnt = 1
    num = 1
    if n == 1:
        return 1
    while num < n:
        num += cnt * 6
        cnt += 1
    return cnt


N = int(input())
print(bee(N))