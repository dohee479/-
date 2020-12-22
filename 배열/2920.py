# 음계
import sys
sys.stdin = open('input.txt', 'r')

num = list(map(int, input().split()))
cnt = 0
count = 0
for i in range(len(num) - 1):
    if num[i] < num[i + 1]:
        cnt += 1
    else:
        count += 1
if cnt == len(num) - 1:
    print('ascending')
elif count == len(num) - 1:
    print('descending')
else:
    print('mixed')









