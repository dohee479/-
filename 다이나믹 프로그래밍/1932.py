# 정수 삼각형
import sys
sys.stdin = open('input.txt', 'r')


def dp():
    for i in range(1, n):
        index = triangle[i - 1].index(max(triangle[i - 1]))
        max_num = max(triangle[i][index], triangle[i][index + 1])
        j = triangle[i].index(max_num)
        triangle[i][j] = triangle[i - 1][index] + max_num
    return max(triangle[n - 1])


n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
print(dp())