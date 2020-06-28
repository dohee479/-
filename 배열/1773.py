# 폭죽쇼
import sys

sys.stdin = open('input.txt', 'r')
# N, C = map(int, input().split())
# Fire = []
# for n in range(N):
#     num = int(input())
#     result = 0
#     while result < C:
#         result += num
#         if result <= C and result not in Fire:
#             Fire.append(result)
# print(len(Fire))

N, C = map(int, input().split())
Fire = set()
cnt = 0
for n in range(N):
    num = int(input())
    if num == 1:
        cnt = C
        continue
    for i in range(num, C+1, num):
        Fire.add(i)
        cnt = len(Fire)
print(cnt)


# Firework = []
# for number in Fire:
#     if number not in Firework:
#         Firework.append(number)
# print(len(Firework))


# N, C = map(int, input().split())
# check = [False]*(C+1)
# ans = 0
# for _ in range(N):
#     n = int(input())
#     for i in range(n, C+1, n):
#         if not check[i]:
#             check[i] = True
#             ans += 1
# print(ans)