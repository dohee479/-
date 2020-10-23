# RGB 거리
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def rgb(n):
    queue = deque([(home[0][0]), (home[0][1]), (home[0][2])])
    for i, value in enumerate(home[n]):


    return


N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
memory = [[0] * N for _ in range(N)]
print(rgb(0))
