# 적록색약
import sys
sys.stdin = open('input.txt', 'r')


def dfs(x, y, color):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    stack = [(x, y)]
    visited[x][y] = 1
    while len(stack) > 0:
        x, y = stack.pop()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and Color[nx][ny] == color:
                stack.append((nx, ny))
                visited[nx][ny] = 1


# def dfs2(x, y, color):
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     stack = [(x, y)]
#     visited[x][y] = 0
#     while len(stack) > 0:
#         x, y = stack.pop(0)
#         for direct in range(4):
#             nx = x + dx[direct]
#             ny = y + dy[direct]
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 1 and Color[nx][ny] == color:
#                 stack.append((nx, ny))
#                 visited[nx][ny] = 0
#                 continue
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 1 and (color == 'R' and Color[nx][ny] == 'G') or (color == 'G' and Color[nx][ny] == 'R'):
#                 stack.append((nx, ny))
#                 visited[nx][ny] = 0



N = int(input())
Color = [list(map(str, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if (Color[i][j] == 'R' or Color[i][j] == 'B' or Color[i][j] == 'G') and visited[i][j] == 0:
            cnt += 1
            color = Color[i][j]
            dfs(i, j, color)

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if Color[i][j] == 'G':
            Color[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if Color[i][j] == 'R' and visited[i][j] == 0:
            cnt2 += 1
            dfs(i, j, Color[i][j])
        elif Color[i][j] == 'B' and visited[i][j] == 0:
            cnt2 += 1
            dfs(i, j, Color[i][j])
print(cnt, cnt2)
# for i in range(N):
#     for j in range(N):
#         if (Color[i][j] == 'R' or Color[i][j] == 'B' or Color[i][j] == 'G') and visited[i][j] == 1:
#             cnt2 += 1
#             color = Color[i][j]
#             dfs2(i, j, color)
# print(cnt, cnt2)




# def dfs(x, y, color):
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     stack = [(x, y)]
#     while len(stack) > 0:
#         visited[x][y] = 1
#         for direct in range(4):
#             nx = x + dx[direct]
#             ny = y + dy[direct]
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and Color[nx][ny] == color:
#                 stack.append((x, y))
#                 x = nx
#                 y = ny
#                 break
#         else:
#             x, y = stack.pop()
#
#
# def dfs2(x, y, color):
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     stack = [(x, y)]
#     while len(stack) > 0:
#         visited[x][y] = 0
#         for direct in range(4):
#             nx = x + dx[direct]
#             ny = y + dy[direct]
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 1 and Color[nx][ny] == color:
#                 stack.append((x, y))
#                 x = nx
#                 y = ny
#                 break
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 1 and (color == 'R' and Color[nx][ny] == 'G') or (color == 'G' and Color[nx][ny] == 'R'):
#                 stack.append((x, y))
#                 x = nx
#                 y = ny
#                 break
#         else:
#             x, y = stack.pop()







