# 소트인사이드
import sys
sys.stdin = open('input.txt', 'r')

N = list(map(int, input()))
result = sorted(N, reverse=True)
print(''.join(map(str, result)))
