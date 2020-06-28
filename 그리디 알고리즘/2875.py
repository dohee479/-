# 대회 or 인턴
import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())
N_minus = K
M_minus = 0
result = 0
while N_minus >= 0:
    N -= N_minus
    M -= M_minus
    if N // 2 >= M:
        if M > result:
            result = M
    else:
        if N // 2 > result:
            result = N//2
    N += N_minus
    M += M_minus
    N_minus -= 1
    M_minus += 1
print(result)

# a, b, c = map(int, input().split(' '))
# while c > 0:
#     if a // 2 >= b:
#         a -= 1
#     else:
#         b -= 1
#     c -= 1
# print(min(a//2, b))