# 파도반 수열
import sys
sys.stdin = open('input.txt', 'r')



def padovan(n):
    numbers = [1] * n
    for i in range(3, n):
        numbers[i] = numbers[i - 2] + numbers[i - 3]
    return numbers[n - 1]


T = int(input())
for _ in range(T):
    N = int(input())
    print(padovan(N))