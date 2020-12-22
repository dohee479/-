# 피보나치 함수
import sys
sys.stdin = open('input.txt', 'r')


# 리스트 이용
def fibo(n):
    if n == 0:
        return '1 0'
    elif n == 1:
        return '0 1'
    numbers = [0] * (n + 1)
    numbers[1] = 1
    for i in range(2, n+1):
        numbers[i] = numbers[i - 1] + numbers[i - 2]
    return '{} {}'.format(numbers[n - 1], numbers[n])


# 리스트 없이
def fibo(n):
    if n == 0:
        return '1 0'
    elif n == 1:
        return '0 1'

    f1, f2 = 0, 1
    for i in range(2, n+1):
        f1, f2 = f2, f1 + f2
    return '{} {}'.format(f1, f2)


T = int(input())
for t in range(T):
    N = int(input())
    print(fibo(N))
