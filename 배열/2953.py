# 나는 요리사다
import sys
sys.stdin = open('input.txt', 'r')

N = 5
max_num = []
for n in range(1, N+1):
    num = list(map(int, input().split()))
    result = 0
    for i in range(len(num)):
        result += num[i]
    max_num.append(result)
print(max_num)
max_number = 0
idx = 1
for i in range(len(max_num)):
    if max_num[i] > max_number:
        max_number = max_num[i]
        idx = i
print(idx + 1, max_number)




