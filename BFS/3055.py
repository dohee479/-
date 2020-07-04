# 탈출
import sys
sys.stdin = open('input.txt', 'r')

def water():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = []
    queue2 = []
    for x in range(R):
        for y in range(C):
            if cave[x][y] == '*':
                queue.append((x, y))
            if cave[x][y] == 'S':
                queue2 = [(x, y)]
    while queue or queue2:
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            for direct in range(4):
                nx = x + dx[direct]
                ny = y + dy[direct]
                if 0 <= nx < R and 0 <= ny < C and cave[nx][ny] == '.':
                    queue.append((nx, ny))
                    cave[nx][ny] = '*'
        for _ in range(len(queue2)):
            x2, y2 = queue2.pop(0)
            for direct in range(4):
                nx2 = x2 + dx[direct]
                ny2 = y2 + dy[direct]
                if 0 <= nx2 < R and 0 <= ny2 < C and (cave[nx2][ny2] == '.' or cave[nx2][ny2] == 'D') and adj[nx2][ny2] == 0:
                    queue2.append((nx2, ny2))
                    adj[nx2][ny2] = adj[x2][y2] + 1
    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'D' and adj[i][j]:
                return adj[i][j]

            if cave[i][j] == 'D' and adj[i][j] == 0:
                return 'KAKTUS'


R, C = map(int, input().split())
cave = [list(map(str, input())) for _ in range(R)]
adj = [[0] * C for _ in range(R)]
print(water())




