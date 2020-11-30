# 네번째 점
import sys
sys.stdin = open('input.txt', 'r')

# X = [0] * 1001
# Y = [0] * 1001
# for _ in range(3):
#     x, y = map(int, input().split())
#     X[x] += 1
#     Y[y] += 1
# for i, value in enumerate(X):
#     if value == 1:
#         print(i, end=' ')
# for i, value in enumerate(Y):
#     if value == 1:
#         print(i)
#
# x=y=0
# exec("a,b=map(int,input().split());x^=a;y^=b;"*3)
# print(x,y)

i, j = 0, 0
for _ in range(3):
    x, y = map(int, input().split())
    i ^= x
    j ^= y
print(i, j)
