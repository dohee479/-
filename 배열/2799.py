# 블라인드
import sys
sys.stdin = open('input.txt', 'r')

M, N = map(int, input().split())
Apartment = []
for i in range(5*M+1):
    word = input()
    line = []
    for w in word:
        line.append(w)
    Apartment.append(line)
arr = [0] * 5
for i in range(1, 5*M+1, 5):
    for j in range(1, 5*N+1, 5):
        cnt = 0
        for x in range(i, i+4):
            for y in range(j, j+4):
                if Apartment[x][y] == '*':
                    cnt += 1
        if cnt == 0:
            arr[0] += 1
        elif cnt == 4:
            arr[1] += 1
        elif cnt == 8:
            arr[2] += 1
        elif cnt == 12:
            arr[3] += 1
        else:
            arr[4] += 1
for i in range(len(arr)):
    print(arr[i], end=' ')












