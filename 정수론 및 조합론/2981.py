# 검문
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
number = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])
gcd = number[1] - number[0]
for i in range(2, N):
    gcd = euclid(gcd, number[i] - number[i - 1])
answer = set([gcd])
for i in range(2, int(gcd ** 0.5) + 1):
    if not gcd % i:
        answer.add(i)
        answer.add(gcd // i)
print(' '.join(map(str, sorted(answer))))

# number[0] = k[0] * M + R
# number[1] = k[1] * M + R
# number[2] = k[2] * M + R
# number[1] - number[0] = M * (k[1] - k[0])
# k[1] - k[0]은 number[1] - number[0]의 약수
# 숫자들의 차들간의 최대공약수를 구해 약수를 구하면 된다.