# 수 정렬하기 2
import sys
sys.stdin = open('input.txt', 'r')

# 첫번째 radix sort
def counting_sort(arr, digit):
    n = len(arr)

    result = [0] * n
    count = [0] * 10

    for i in range(n):
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


def radix_sort(arr):
    maxNum = max(arr)
    digit = 1
    while int(maxNum/digit) > 0:
        counting_sort(arr, digit)
        digit *= 10


N = int(input())
arr = [int(input()) + 1000000 for _ in range(N)]
radix_sort(arr)
for num in arr:
    print(num - 1000000)




