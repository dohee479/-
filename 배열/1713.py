# 후보 추천하기
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
result = []
vote = [0] * N
time = [0] * N
M = int(input())
select = list(map(int, input().split()))
for i in range(M):
    if len(result) != N:
        if select[i] not in result:
            result.append(select[i])
            for j in range(len(result)):
                time[j] += 1
        else:
            vote[result.index(select[i])] += 1
            for j in range(len(result)):
                time[j] += 1
    else:
        if select[i] in result:
            vote[result.index(select[i])] += 1
            for j in range(N):
                time[j] += 1
        else:
            max_num = 0
            for j in range(N):
                if vote[j] == min(vote):
                    if max_num < time[j]:
                        max_num = time[j]
                        point = j
            result[point] = select[i]
            vote[point] = 0
            time[point] = 0
            for k in range(N):
                time[k] += 1

result.sort()
for i in result:
    print(i, end=' ')

# N = int(input())
# V = int(input())
# S = list(map(int, input().split()))
# voted = [0 for _ in range(101)]
# ans = []
#
# for s in S:
#     mini = 1001
#     if voted[s]:
#         voted[s] += 1
#     else:
#         ans.append(s)
#         voted[s] = 1
#
#     if len(ans) > N:
#         for idx in range(0,len(ans) - 1):
#             if voted[ans[idx]] < mini:
#                 mini = voted[ans[idx]]
#                 a = ans[idx]
#         ans.remove(a)
#         voted[a] = 0
#
# for answer in sorted(ans):
#     print(answer, end=" ")

