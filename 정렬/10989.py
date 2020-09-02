# 수 정렬하기 3
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N = int(input())
number = [0] * 10001
for _ in range(N):
    n = int(input())
    number[n] = number[n] + 1
for index in range(len(number)):
    if number[index]:
        for _ in range(number[index]):
            print(index)


N = int(input())

