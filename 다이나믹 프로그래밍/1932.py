# 정수 삼각형
import sys
sys.stdin = open('input.txt', 'r')

#
# def dp():
#     for i in range(n-1):
#         for j, value in enumerate(triangle[i]):
#             if not i:
#                 triangle[i + 1][j] = value + triangle[i + 1][j]
#                 triangle[i + 1][j + 1] = value + triangle[i + 1][j + 1]
#             else:
#                 if not j:
#                     triangle[i + 1][j] = value + triangle[i + 1][j]
#                     triangle[i + 1][j + 1] = max(value + triangle[i + 1][j + 1], triangle[i][j + 1] + triangle[i + 1][j + 1])
#                 else:
#                     if j + 1 < len(triangle[i]):
#                         triangle[i + 1][j + 1] = max(value + triangle[i + 1][j + 1], triangle[i][j + 1] + triangle[i + 1][j + 1])
#                     else:
#                         triangle[i + 1][j + 1] = value + triangle[i + 1][j + 1]
#     return max(triangle[n - 1])

def sol(n, data):
    for i in range(n - 1, 0, -1):
        for j in range(len(data[i]) - 1):
            if data[i][j] > data[i][j + 1]:
                data[i - 1][j] += data[i][j]
            else:
                data[i - 1][j] += data[i][j + 1]
    return data[0][0]


n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
print(sol(n, triangle))
# # print(dp())


def solution():
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))

    accum = []
    for i in range(n):
        accum = [max(a + c, b + c) for a, b, c in zip([0] + accum, accum + [0], triangle[i])]
    print(max(accum))


solution()



