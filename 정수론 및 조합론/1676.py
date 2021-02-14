# 팩토리얼 0의 개수
import sys
sys.stdin = open('input.txt', 'r')


def factorial(n):
    fac = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i
    return str(fac[-1])


N = int(input())
number = factorial(N)
answer = 0
for i in range(len(number) - 1, -1, -1):
    if number[i] != '0':
        print(answer)
        break
    answer += 1
