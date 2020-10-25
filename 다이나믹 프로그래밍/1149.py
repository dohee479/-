# RGB 거리
import sys
sys.stdin = open('input.txt', 'r')


def rgb():
    for i in range(1, N):
        home[i][0] = home[i][0] + min(home[i - 1][1], home[i - 1][2])
        home[i][1] = home[i][1] + min(home[i - 1][0], home[i - 1][2])
        home[i][2] = home[i][2] + min(home[i - 1][0], home[i - 1][1])
    return min(home[N-1])


N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
print(rgb())
print(home)

