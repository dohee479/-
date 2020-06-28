# 알파벳
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
#
# def BFS(x, y):
#     global answer
#     q = set([(x, y, board[x][y])])
#
#     while q:
#         x, y, ans = q.pop()
#
#         # 좌우상하 갈 수 있는지 살펴본다
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
#             if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
#                 q.add((nx,ny,ans + board[nx][ny]))
#                 answer = max(answer, len(ans)+1)
#
#
# R, C = map(int, sys.stdin.readline().split())
# board = [list(sys.stdin.readline().strip()) for _ in range(R)]
#
# answer = 1
# BFS(0, 0)
# print(answer)


# # 좌, 하, 우, 상
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
#
# def DFS(x, y, ans):
#     global answer
#
#     answer = max(ans, answer)
#
#     # 좌우상화 다 확인한다
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
#         if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in passed):
#             passed.append(board[nx][ny])
#             DFS(nx, ny, ans+1)
#             passed.remove(board[nx][ny])
#
#
#
# R, C = map(int, sys.stdin.readline().split())
# board = [list(sys.stdin.readline().strip()) for _ in range(R)]
#
# answer = 1
# DFS(0, 0, answer)
# print(answer)



def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = deque()
    stack.append((x, y, alphabet[x][y]))
    max_num = 0
    while stack:
        x, y, path = stack.pop()
        check = False
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < R and 0 <= ny < C and (alphabet[nx][ny] not in path):
                check = True
                if visited[nx][ny] != path + alphabet[nx][ny]:
                    visited[nx][ny] = path + alphabet[nx][ny]
                    stack.append((nx, ny, path + alphabet[nx][ny]))
        if not check:
            max_num = max(max_num, len(path))
    return max_num


R, C = map(int, input().split())
alphabet = [list(input()) for _ in range(R)]
visited = [[''] * C for _ in range(R)]
print(bfs(0, 0))


# def dfs(x, y, z, cnt):
#     max_num = 0
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     stack = deque()
#     stack.append((x, y, alphabet[x][y], cnt))
#     while stack:
#         x, y, path, cnt = stack.pop()
#         for direct in range(4):
#             nx = x + dx[direct]
#             ny = y + dy[direct]
#             if 0 <= nx < R and 0 <= ny < C and alphabet[nx][ny] not in path:
#                 stack.append((nx, ny, path+alphabet[nx][ny], cnt+1))
#
#         if cnt > max_num:
#             max_num = cnt
#     return max_num
#
#
# R, C = map(int, input().split())
# alphabet = [list(input()) for _ in range(R)]
# visited = [[''] * C for _ in range(R)]
# print(dfs(0, 0, alphabet[0][0], 1))
