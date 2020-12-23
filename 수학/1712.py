# 손익분기점
import sys
sys.stdin = open('input.txt', 'r')


A, B, C = map(int, input().split())
if C > B:
    print(A // (C - B) + 1)
else:
    print(-1)