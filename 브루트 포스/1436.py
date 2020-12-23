# 영화감독 숌
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
first = 666
while N:
    if '666' in str(first):
        N -= 1
    first += 1
print(first - 1)