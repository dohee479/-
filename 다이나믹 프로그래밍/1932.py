# 정수 삼각형
import sys
sys.stdin = open('input.txt', 'r')


def dp():
    for i in range(n-1):
        for j, value in enumerate(triangle[i]):
            if not i:
                triangle[i + 1][j] = value + triangle[i + 1][j]
                triangle[i + 1][j + 1] = value + triangle[i + 1][j + 1]
            else:
                if not j:
                    triangle[i + 1][j] = value + triangle[i + 1][j]
                    triangle[i + 1][j + 1] = max(value + triangle[i + 1][j + 1], triangle[i][j + 1] + triangle[i + 1][j + 1])
                else:
                    if j + 1 < len(triangle[i]):
                        triangle[i + 1][j + 1] = max(value + triangle[i + 1][j + 1], triangle[i][j + 1] + triangle[i + 1][j + 1])
                    else:
                        triangle[i + 1][j + 1] = value + triangle[i + 1][j + 1]
    return max(triangle[n - 1])


n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
print(dp())