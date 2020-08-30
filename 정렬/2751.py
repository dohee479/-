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


# 두번째 quick sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     small_num, equal, large_num = [], [], []
#     for num in arr:
#         if num < pivot:
#             small_num.append(num)
#         elif num > pivot:
#             large_num.append(num)
#         else:
#             equal.append(num)
#     return quick_sort(small_num) + equal + quick_sort(large_num)
#
#
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# result = quick_sort(arr)
# for num in result:
#     print(num)


# 세번째 quick sort
# def quick_sort(arr):
#     def sort(low, high):
#         if high <= low:
#             return
#
#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)
#
#     def partition(low, high):
#         pivot = arr[(low + high) // 2]
#         while low <= high:
#             while arr[low] < pivot:
#                 low += 1
#             while arr[high] > pivot:
#                 high -= 1
#             if low <= high:
#                 arr[low], arr[high] = arr[high], arr[low]
#                 low, high = low + 1, high - 1
#         return low
#
#     return sort(0, len(arr) - 1)


# N = int(input())
# arr = [int(input()) for _ in range(N)]
# quick_sort(arr, 0, len(arr) - 1)
# for num in arr:
#     print(num)










