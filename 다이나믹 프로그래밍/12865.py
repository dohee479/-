# 평범한 배낭
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().rstrip().split())
memo = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    # j는 무게합
    for j in range(1, K + 1):
        # j가 w보다 작다면, w는 담을 수 없다. 전의 값으 복사
        if j < w:
            memo[i][j] = memo[i - 1][j]
        # j가 w를 감당할 수 있으면, max값을 찾는다.
        # j의 이전값과 j - w(만약 w가 3이고 j값이 7이면 4일때 값)에 v를 더한값 중의 최대값
        else:
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - w] + v)
print(memo[N][K])