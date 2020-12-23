# 로봇 청소기
import sys
sys.stdin = open('input.txt', 'r')


def clean(x, y, dr):
    count = 0
    cnt = 1
    while True:
        dx = direct[dr][0]
        dy = direct[dr][1]
        dx2 = direct[dr][2]
        dy2 = direct[dr][3]
        room[x][y] = 2  # 청소를 한다.
        if count == 4:
            nx = x + dx2
            ny = y + dy2
            x = nx
            y = ny
            count = 0
            if room[nx][ny] == 1:
                print(cnt)
                break
            continue
        else:
            nx = x + dx
            ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if room[nx][ny] == 0:  # 탐색한 곳이 청소를 안한 곳이면
                dr = (dr+3) % 4  # 다음 방향으로 바꿔준다.
                x = nx
                y = ny
                cnt += 1
                count = 0
            else:
                dr = (dr+3) % 4
                count += 1


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
direct = {0: [0, -1, 1, 0], 1: [-1, 0, 0, -1], 2: [0, 1, -1, 0], 3: [1, 0, 0, 1]} # 북 동 남 서 (왼쪽으로 돌아야하는 방향)
clean(r, c, d)


# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if room[i][j] == 2:
#             cnt += 1
# print(cnt)


def clean(x, y, dr):
    count = 0
    cnt = 1
    while True:
        dx = direct[dr][0]
        dy = direct[dr][1]
        dx2 = direct[dr][2]
        dy2 = direct[dr][3]
        room[x][y] = 2  # 청소를 한다.
        if count == 4:
            nx = x + dx2
            ny = y + dy2
            x = nx
            y = ny
            count = 0
            if room[nx][ny] == 1:
                print(cnt)
                break
            continue
        else:
            nx = x + dx
            ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if room[nx][ny] == 0:  # 탐색한 곳이 청소를 안한 곳이면
                dr = (dr+3) % 4  # 다음 방향으로 바꿔준다.
                x = nx
                y = ny
                cnt += 1
                count = 0
            else:
                dr = (dr+3) % 4
                count += 1