# 알파벳
import sys
from collections import deque
input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')


def dfs(x, y):
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
print(dfs(0, 0))


def dfs(x, y, z, cnt):
    max_num = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = deque()
    stack.append((x, y, alphabet[x][y], cnt))
    while stack:
        x, y, path, cnt = stack.pop()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < R and 0 <= ny < C and alphabet[nx][ny] not in path:
                stack.append((nx, ny, path+alphabet[nx][ny], cnt+1))

        if cnt > max_num:
            max_num = cnt
    return max_num


R, C = map(int, input().split())
alphabet = [list(input()) for _ in range(R)]
visited = [[''] * C for _ in range(R)]
print(dfs(0, 0, alphabet[0][0], 1))
