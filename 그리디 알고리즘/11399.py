# ATM
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
t = list(map(int, input().split()))
t.sort()    # 정렬
result = 0
for i in range(n):
    result += int(t[i]) * (n-i)

print(result)

n = int(input())
p = list(map(int, input().split()))
p.sort()    # 정렬
result = 0
for i in range(len(p), -1, -1):
    for j in range(i):
        result += p[j]
print(result)