# 나무 조각
import sys
sys.stdin = open('input.txt', 'r')

num = list(map(int, input().split()))
for i in range(len(num)-1, 0, -1):
    for j in range(0, i):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
            for k in num:
                print(k, end=' ')
            print()