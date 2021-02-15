# 조합 0의 개수
import sys
sys.stdin = open('input.txt', 'r')


def count_k(x, k):
    cnt = 0
    # x! 안에 k가 몇 번 들어있는지 구한다.
    # 5의 배수 + 25의 배수 + 125의 배수 ~~~
    # 5의 배수이자 25의 배수가 아닌 것 + 2*(25의 배수이자 125 배수 아닌 것)
    # k*(5**k 의 배수이자 5**(k+1) 배수가 아닌 것)
    while x:
        x //= k
        cnt += x
    return cnt


n, m = map(int, input().split())
print(min(count_k(n, 5) - count_k(m, 5) - count_k(n - m, 5), count_k(n, 2) - count_k(m, 2) - count_k(n - m, 2)))


