# 분해합
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
primary_num = N
result = 0
constructor = 0
while True:
    for num in str(N):
        N -= int(num)
    constructor = N
    for num in str(constructor):
        constructor += int(num)
    if constructor == primary_num:
        result = N
    else:
        break
print(result)


n = input()
num = int(n)
start = max(num - 9 * len(n), 0)
for i in range(start, num):
    if num == sum(map(int, str(i))) + i:
        print(i)
        break
else:
    print(0)


N = int(input())
start = max(N - 9 * len(str(N)), 0)
for number in range(start, N+1):
    result = number
    for num in str(number):
        number += int(num)
    if number == N:
        print(result)
        break
else:
    print(0)




