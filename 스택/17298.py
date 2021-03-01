# 오큰수
import sys
sys.stdin = open('input.txt', 'r')


def right_big(k):
    for j in range(k + 1, N):
        if A[k] < A[j]:
            return A[j]
    return -1


N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(N):
    print(right_big(i), end=" ")


# 이중 반복으로 하면 시간초과: 입력값이 크므로
