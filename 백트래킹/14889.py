# 스타트와 링크
import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


# def backtrack(idx):
#     global min_result
#
#     if min_result == 0:
#         return
#
#     if idx == (N // 2):
#         team_2 = []
#         for i in range(N):
#             if i not in team_1:
#                 team_2.append(i)
#         team = list(combinations(team_1, 2))
#         other_team = list(combinations(team_2, 2))
#
#         result_1 = result_2 = 0
#         for i, j in team:
#             result_1 += ablity[i][j] + ablity[j][i]
#
#         for i, j in other_team:
#             result_2 += ablity[i][j] + ablity[j][i]
#
#         if abs(result_1 - result_2) < min_result:
#             min_result = abs(result_1 - result_2)
#         return
#
#     for i in range(N):
#         if visited[i]:
#             continue
#         team_1[idx] = i
#         for j in range(i + 1):
#             visited[j] = 1
#         backtrack(idx + 1)
#         for j in range(N):
#             visited[j] = 0
#
#
# N = int(input())
# team_1 = [0] * (N // 2)
# visited = [0] * N
# min_result = float('INF')
# ablity = [list(map(int, input().split())) for _ in range(N)]
# backtrack(0)
# print(min_result)


def cal(arr):
    result = 0
    for i in arr:
        for j in arr:
            result += ability[i][j]
    return result


def backtrack(idx, index):
    global min_result

    if min_result == 0:
        return

    if idx == (N//2):
        print(team_1)
        team_2 = []
        for i in range(N):
            if i not in team_1:
                team_2.append(i)
        min_result = min(min_result, abs(cal(team_1) - cal(team_2)))
        return

    for i in range(index, N):
        team_1[idx] = i
        backtrack(idx + 1, i + 1)



N = int(input())
team_1 = [0] * (N//2)
visited = [0] * N
min_result = float('INF')
ability = [list(map(int, input().split())) for _ in range(N)]
backtrack(0, 0)
print(min_result)





