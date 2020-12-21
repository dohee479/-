# 회의실배정
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
meeting = sorted([list(map(int, sys.stdin.readline().split())) for i in range(N)], key=lambda x: (x[1], x[0]))
# meeting = sorted(meeting, key=lambda time: time[0])
# meeting = sorted(meeting, key=lambda time: time[1])

cnt = 0
end = 0
for m in meeting:
    if m[0] >= end:
        end = m[1]
        cnt += 1
print(cnt)


