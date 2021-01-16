# 약수
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
div = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
print(div[0] * div[-1])