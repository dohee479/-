# 패션왕 신해빈
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    clothes = dict()
    n = int(input())
    for _ in range(n):
        name, kinds = map(str, sys.stdin.readline().rstrip().split())
        if clothes.get(kinds):
            clothes[kinds] += 1
        else:
            clothes[kinds] = 2
    sum_dict = 1
    for i in clothes:
        sum_dict *= clothes[i]
    print(sum_dict - 1)
