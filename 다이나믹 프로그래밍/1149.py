# RGB 거리
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def rgb(n):
    queue = deque([(0, 0, home[0][0]), (0, 1, home[0][1]), (0, 2, home[0][2])])
    while queue:
        x, y, color = queue.popleft()
        if x + 1 < N and y <= N:
            for i, value in enumerate(home[x + 1]):
                if y != i and color + home[x + 1][i] <= memory[x + 1][i]:
                    memory[x + 1][i] = color + home[x + 1][i]
                    queue.append((x + 1, i, color + home[x + 1][i]))
    return min(memory[N - 1])


N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')
memory = [[INF] * N for _ in range(N)]
print(rgb(0))
