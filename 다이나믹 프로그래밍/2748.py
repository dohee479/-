# 피보나치 수
import sys
sys.stdin = open('input.txt', 'r')



def fibo(n):
    numbers = [0] * (n+1)
    numbers[1] = 1
    for i in range(2, n+1):
        numbers[i] = numbers[i - 1] + numbers[i - 2]
    return numbers[n]


n = int(input())
print(fibo(n))
