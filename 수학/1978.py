# 소수 찾기
import sys
sys.stdin = open('input.txt', 'r')


def prime(n):
    if n == 1:
        return 0
    # 제곱근의 이유: 어떤 수의 약수는 무조건 제곱근의 범위에 존재한다.
    for i in range(2, int(n ** 0.5) + 1):
        if not (n % i):
            return 0
    return 1


N = int(input())
number = list(map(int, input().split()))
cnt = 0
for num in number:
    cnt += prime(num)
print(cnt)
