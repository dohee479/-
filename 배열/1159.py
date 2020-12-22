# 농구경기
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
arr = []
for n in range(N):
    word = input()
    arr.append(word[0])
    arr1 = []
    for i in range(len(arr)):
        if arr[i] not in arr1:
            arr1.append(arr[i])
            arr1.sort()

cnt = 0
for i in range(len(arr1)):
    if arr.count(arr1[i]) >= 5:
        print(arr1[i], end='')
    else:
        cnt += 1

if cnt == len(arr1):
    print("PREDAJA")


