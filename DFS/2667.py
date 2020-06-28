# 단지 번호 붙이기
import sys
sys.stdin = open('../input.txt', 'r')


def danzi(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = [(x, y)]
    count = 0
    while len(stack) > 0:
        arr[x][y] = 0
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                stack.append((x, y))
                x = nx
                y = ny
                break
        else:
            x, y = stack.pop()
            count += 1
    return count


N = int(input())
arr = []

for _ in range(N):
    num = input()
    line = []
    for i in range(N):
        line.append(int(num[i]))
    arr.append(line)
cnt = 0
result = []
for c in range(N):
    for r in range(N):
        if arr[c][r] == 1:
            cnt += 1
            result.append(danzi(c, r))
            result.sort()
print(cnt)
for i in result:
    print(i)












