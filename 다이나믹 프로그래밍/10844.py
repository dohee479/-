# 쉬운 계단 수
import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline().rstrip())
dp = [1 if i else 0 for i in range(10)]
n = 1
while n < N:
    # dp 는 반복문을 돌릴 때 마다 값이 변하기 때문에 복사하여 놓는다.
    a = dp[:]
    for i in range(10):
        if i == 0:
            dp[i] = dp[i + 1]
        elif 1 <= i < 9:
            dp[i] = a[i - 1] + a[i + 1]
        else:
            dp[i] = a[i - 1]
    n += 1
print(sum(dp) % 1_000_000_000)

# 0 1 2 3 4 5 6 7 8 9 -> 이 숫자들로 끝나는 수
# 0 1 1 1 1 1 1 1 1 1 -> n = 1 일 때 개수
# 1 1 2 2 2 2 2 2 2 1 -> n = 2 일 때 개수
# i 번째는 [i- 1] + [i + 1]의 개수이다.
# 예를 들어, 숫자가 3으로 끝나고 길이가 2일 경우 3가지
# 212 234 432
