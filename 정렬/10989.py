# 수 정렬하기 3
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


# def counting_sort(length, max_num):
#     counting_array = [0] * (max_num+1)
#     result_array = [0] * length
#
#     for num in number:
#         counting_array[num] += 1
#
#     for index in range(len(counting_array)-1):
#         counting_array[index+1] += counting_array[index]
#
#     for num in number:
#         result_array[counting_array[num]-1] = num
#         counting_array[num] -= 1
#     return result_array
#
#
# N = int(input())
# number = [int(input()) for _ in range(N)]
# result = counting_sort(len(number), max(number))
# for num in result:
#     print(num)

N = int(input())
number = [0] * 10001
for _ in range(N):
    n = int(input())
    number[n] = number[n] + 1
for index in range(len(number)):
    if number[index]:
        for _ in range(number[index]):
            print(index)

