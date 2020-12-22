# 숫자의 합
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
result = 0
for num in input():
    result += int(num)
print(result)