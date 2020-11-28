# 네번째 점
import sys
sys.stdin = open('input.txt', 'r')

X = dict()
Y = dict()
for _ in range(3):
    x, y = input().split()
    X.update(x)
    Y.update(y)
print(X, Y)
