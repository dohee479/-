# 스타트와 링크
import sys
sys.stdin = open('input.txt', 'r')
def backtrack(idx):
    for i in range(N):
        if visited[i]:
            continue
        team_1[idx] = i
        visited[i] = 1
        backtrack(idx + 1)
        visited[i] = 0


    return

N = int(input())
team_1 = [0] * (N//2)
visited = [0] * N
ablity = [list(map(int, input().split())) for _ in range(N)]
