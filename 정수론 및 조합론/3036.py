# 링
import sys
sys.stdin = open('input.txt', 'r')


# 최대공약수를 구하는 방법인 유클리드호제법
def euclid(n1, n2):
    if n2 > n1:
        n1, n2 = n2, n1
    # 큰수를 작은 수로 나누어 나머지가 0이 될 때 작은수가 최대공약수
    while n2:
        n1, n2 = n2, n1 % n2
    return n1


N = int(input())
ring = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(1, N):
    gcd = euclid(ring[0], ring[i])
    # 최대공약수로 나눈 몫
    q1 = ring[0] // gcd
    q2 = ring[i] // gcd
    print('{}/{}'.format(q1, q2))
