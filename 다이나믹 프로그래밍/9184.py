# 신나는 함수 실행
import sys
sys.stdin = open('input.txt', 'r')


# 피보나치를 유사하다고 생각하면서 풀려했지만 도움을 빌렸다.
# 피보나치와 유사하다.
# 3차원 배열을 생성하여 그 안에 계산된 값들을 저장, 불러오는 로직이다.
def w(a, b, c):
    if dp[a + 50][b + 50][c + 50]:
        return dp[a + 50][b + 50][c + 50]

    if a <= 0 or b <= 0 or c <= 0:
        dp[a + 50][b + 50][c + 50] = 1
        return 1

    if a > 20 or b > 20 or c > 20:
        dp[a + 50][b + 50][c + 50] = w(20, 20, 20)
        return w(20, 20, 20)

    if a < b and b < c:
        dp[a + 50][b + 50][c + 50] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)

    dp[a + 50][b + 50][c + 50] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)


dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))


# 굳이 50을 더할 필요가 없다.
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]


dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
