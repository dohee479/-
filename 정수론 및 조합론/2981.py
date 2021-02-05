# 검문
import sys
sys.stdin = open('input.txt', 'r')


# 시간초과
# 최대공약수를 구하는 방법인 유클리드호제법
def euclid(n1, n2):
    if n2 > n1:
        n1, n2 = n2, n1
    # 큰수를 작은 수로 나누어 나머지가 0이 될 때 작은수가 최대공약수
    while n2:
        n1, n2 = n2, n1 % n2
    return n1


N = int(input())
number = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
gcd = number[0]
for i in range(1, N):
    gcd = euclid(gcd, number[i])
# 주어진 수들의 최대공약수의 배수, 단 첫번째 수는 포함하지 않는다.
for i in range(gcd, number[-1] + 1, gcd):
    remainder = number[0] % i
    cnt = 1
    for j in range(1, N):
        if remainder == number[j] % i:
            cnt += 1
    if cnt == N:
        print(i, end=' ')