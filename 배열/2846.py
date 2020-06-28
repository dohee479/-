# 오르막길
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
Asc = list(map(int, input().split()))
min_size = Asc[0]
result = 0
Asc_size = 0
for i in range(1, N):
    if Asc[i-1] == Asc[i]:
        min_size = Asc[i]
        Asc_size = Asc[i] - min_size
    else:
        if Asc[i] < min_size:
            min_size = Asc[i]
        else:
            Asc_size = Asc[i] - min_size
            if Asc[i-1] > Asc[i]:
                min_size = Asc[i]
    if Asc_size > result:
        result = Asc_size
print(result)

