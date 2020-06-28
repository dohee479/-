# 게임을 만든 동준이
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
level = []
for _ in range(N):
    num = int(input())
    level.append(num)
cnt = 0
i = N-2
max_num = level[N-1]
while i >= 0:
    if level[i] >= max_num:
        level[i] = level[i] - 1
        cnt += 1
    else:
        max_num = level[i]
        i -= 1
print(cnt)

# while i < N-1:
#     if level[i] >= level[i+1]:
#         level[i] = level[i]-1
#         cnt += 1
#         if level[i-1] == level[i]:
#             level[i-1] = level[i-1] - 1
#             cnt += 1
#     else:
#         i += 1
# print(level)
# print(cnt)