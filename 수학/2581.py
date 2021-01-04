# 소수
import sys
sys.stdin = open('input.txt', 'r')


def prime(n):
    if n == 0 or n == 1:
        return []
    # 제곱근의 이유: 어떤 수의 약수는 무조건 제곱근의 범위에 존재한다.
    for j in range(2, int(n ** 0.5) + 1):
        if not (n % j):
            return []
    return [n]


M = int(input())
N = int(input())
answer = []
for i in range(M, N + 1):
    answer += prime(i)
if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)
