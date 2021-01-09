# 골드바흐의 추측
import sys
sys.stdin = open('input.txt', 'r')

prime = [False, False] + [True] * 9999
for i in range(2, 101):
    if prime[i]:
        prime[i * 2::i] = [False] * (10000 // i - 1)


T = int(input())
for _ in range(T):
    n = int(input())
    diff = float('inf')
    answer = []
    # n의 합은 n // 2 기준으로 갈린다.
    # 2 부터 탐색하여 n의 절반값까지만 보고 판단
    for i in range(2, (n // 2) + 1):
        if prime[i] and prime[n - i]:
            if n - 2 * i < diff:
                diff = n - 2 * i
                answer = [i, n - i]
    print(answer[0], answer[1])

    # 절반부터 n까지 탐색하는 방법
    # 조건을 만족하는 첫 값이 두 수 사이의 값이 가장 작다.
    # 4배 가량 빠르다
    for i in range(n // 2, n):
        if prime[i] and prime[n - i]:
            print(n - i, i)
            break


