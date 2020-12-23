# 수 정렬하기
import sys
sys.stdin = open('input.txt', 'r')


def countingSort(arr, digit):
    n = len(arr)
    result = [0] * n
    count = [0] * 10

    for i in range(len(arr)):
        index = int(arr[i]/digit)
        count[(index % 10)] += 1

    for i in range(9):
        count[i + 1] += count[i]

    for i in range(n-1, -1, -1):
        index = int(arr[i]/digit)
        result[count[(index % 10)] - 1] = arr[i]
        count[(index % 10)] -= 1

    for i in range(n):
        arr[i] = result[i]


def radixSort(arr):
    maxNum = max(arr)
    digit = 1
    while int(maxNum/digit) > 0:
        countingSort(arr, digit)
        digit *= 10


N = int(input())
plus = []
minus = []
for i in range(N):
    num = int(input())
    if num >= 0:
        plus.append(num)
    else:
        minus.append(abs(num))
if plus:
    radixSort(plus)
if minus:
    radixSort(minus)
for m_num in reversed(minus):
    print(-m_num)
for p_num in plus:
    print(p_num)
