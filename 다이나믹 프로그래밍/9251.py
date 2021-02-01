# LCS
import sys
sys.stdin = open('input.txt', 'r')

s1 = list(sys.stdin.readline().rstrip())
s2 = list(sys.stdin.readline().rstrip())
# 메모할 배열
memo = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        # 비교하는 문자가 같을 경우 왼쪽 대각선의 값 + 1
        # 예를 들어, n번째와 m번째가 같은 경우 길이가 가장 길다.
        # 그러므로, n - 1번째와 m - 1번째의 최장값에 + 1 을 해주면 된다.
        if s1[i - 1] == s2[j - 1]:
            memo[i][j] = memo[i - 1][j - 1] + 1
        # 다른 경우, 바로 윗 행의 값과 바로 왼쪽 열 비교
        # 둘 중에 하나의 문자열이 수열에 들어갈 수도 있고 들어가지 않을 수도 있다.
        else:
            memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
print(memo[-1][-1])
