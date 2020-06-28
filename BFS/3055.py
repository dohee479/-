# 탈출
import sys
sys.stdin = open('input.txt', 'r')

def water():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = []
    stack2 = []
    for x in range(R):
        for y in range(C):
            if cave[x][y] == '*':
                stack.append((x, y))
            if cave[x][y] == 'S':
                stack2 = [(x, y)]
    while stack or stack2:
        for _ in range(len(stack)):
            x, y = stack.pop(0)
            for direct in range(4):
                nx = x + dx[direct]
                ny = y + dy[direct]
                if 0 <= nx < R and 0 <= ny < C and cave[nx][ny] == '.':
                    stack.append((nx, ny))
                    cave[nx][ny] = '*'
        for _ in range(len(stack2)):
            x2, y2 = stack2.pop(0)
            for direct in range(4):
                nx2 = x2 + dx[direct]
                ny2 = y2 + dy[direct]
                if 0 <= nx2 < R and 0 <= ny2 < C and (cave[nx2][ny2] == '.' or cave[nx2][ny2] == 'D') and adj[nx2][ny2] == 0:
                    stack2.append((nx2, ny2))
                    adj[nx2][ny2] = adj[x2][y2] + 1
    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'D' and adj[i][j]:
                print(adj[i][j])
                break
            if cave[i][j] == 'D' and adj[i][j] == 0:
                print('KAKTUS')
                break


R, C = map(int, input().split())
cave = [list(map(str, input())) for _ in range(R)]
adj = [[0] * C for _ in range(R)]
water()
# for i in range(R):
#     print(cave[i])
# print('-----------------------')
# for i in range(R):
#     print(adj[i])



