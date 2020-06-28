# NBA 농구
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
Team = []
Hour = []
Min = []
arr = []
for _ in range(N):
    T, H = map(str, input().split())
    Team.append(int(T))
    arr.append(H.split(':'))
    for i in range(len(arr)):
        Hour.append(int(arr[i][0]))
        Min.append(int(arr[i][1]))
    arr = []
cnt1 = 0
cnt2 = 0
H1 = 0
H2 = 0
M1 = 0
M2 = 0
for i in range(len(Team)):
    if i == 0 and Team[i] == 1:
        cnt1 += 1
        if Team[i+1] == 1:
            M1 = 




    elif i == 0 and Team[i] == 2:
        cnt2 += 1
        if Team[i+1] ==2:




