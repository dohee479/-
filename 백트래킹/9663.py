# N-Queen
import sys
sys.stdin = open('input.txt', 'r')


# def Queen(r):
#     global count
#     if r == N:
#         count += 1
#         return
#     for i in range(N):
#         if check[r][i] != 0:
#             continue
#         marking(r, i)
#         Queen(r+1)
#         un_marking(r, i)
#
#
# def marking(r, c):
#     for i in range(N):
#         check[r][i] += 1
#     for i in range(N):
#         check[i][c] += 1
#     left = c-1
#     right = c+1
#     for i in range(r+1, N):
#         if left >= 0:
#             check[i][left] += 1
#         if right < N:
#             check[i][right] += 1
#         left -= 1
#         right += 1
#
#
# def un_marking(r, c):
#     for i in range(N):
#         check[r][i] -= 1
#     for i in range(N):
#         check[i][c] -= 1
#     left = c-1
#     right = c+1
#     for i in range(r+1, N):
#         if left >= 0:
#             check[i][left] -= 1
#         if right < N:
#             check[i][right] -= 1
#         left -= 1
#         right += 1
#
#
# N = int(input())
# check = [[0] * N for _ in range(N)]
# count = 0
# Queen(0)
# print(count)

def queen(row):
    global cnt
    if row == N:
        cnt += 1
        return

    for i in range(N):
        if not visited[i] and not diag_1[row-i] and not diag_2[row+i]:
            visited[i] = 1
            diag_1[row-i] = 1
            diag_2[row+i] = 1
            queen(row+1)
            visited[i] = 0
            diag_1[row-i] = 0
            diag_2[row+i] = 0


N = int(input())
visited = [0] * N
diag_1 = [0] * (N*2)
diag_2 = [0] * (N*2)
cnt = 0
queen(0)
print(cnt)