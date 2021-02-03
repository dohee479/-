# 최소공배수
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


T = int(input())
for t in range(T):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    gcd = euclid(num1, num2)
    # 두 수를 곱한 후 최대공약수로 나누면 최소공배수
    print(num1 * num2 // gcd)
