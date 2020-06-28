# 회의실배정
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
meeting = sorted([list(map(int, sys.stdin.readline().split())) for i in range(N)], key=lambda x: (x[1], x[0]))
print(meeting)

end = 0
cnt = 0
for m in meeting:
    if m[0] >= end:
        end = m[1]
        cnt += 1
print(cnt)

# N = int(input())
# meeting = [list(map(int, input().split())) for _ in range(N)]
# meeting.sort()
# for i in range(N-1, -1, -1):
#     for j in range(i):
#         if meeting[j][1] > meeting[j+1][1]:
#             meeting[j], meeting[j + 1] = meeting[j+1], meeting[j]
#
# print(meeting)
