# ATM
import sys
sys.stdin = open('input.txt', 'r')

# def permute(arr):
#     result = [arr[:]]
#     c = [0] * len(arr)
#     i = 0
#     while i < len(arr):
#         if c[i] < i:
#             if i % 2 == 0:
#                 arr[0], arr[i] = arr[i], arr[0]
#             else:
#                 arr[c[i]], arr[i] = arr[i], arr[c[i]]
#             result.append(arr[:])
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#     return result


def dfs(x):
    if len(result) == N:
        b = sum_num(result)
        total.append(b)

    for i in range(N):
        if visited[i] == 1:
            continue
        result.append(num[i])
        visited[i] = 1
        dfs(x)
        visited[i] = 0
        result.pop()

def sum_num(x):
    sum_num = 0
    for i in range(len(x), -1, -1):
        for j in range(i):
            sum_num += x[j]
    return sum_num


N = int(input())
result = []
num = list(map(int, input().split()))
visited = [0] * N
score = 99999999999
total = []
dfs(num)
print(min(total))


# n = int(input())
# t = list(map(int, input().split()))
# t.sort()    # 정렬
# result = 0
# for i in range(n):
#     result += int(t[i]) * (n-i)
#
# print(result)

n = int(input())
p = list(map(int, input().split()))
p.sort()    # 정렬
result = 0
for i in range(len(p), -1, -1):
    for j in range(i):
        result += p[j]
print(result)