# 가장 긴 증가하는 부분 수열
import sys
sys.stdin = open('input.txt', 'r')

# DP
A = int(input())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
answer = [0] * A
for i in range(len(seq)):
    answer[i] = 1
    # i 번째의 수보다 j번 째의 수가 더 클 경우
    # answer[i]의 수열 길이랑 비교하여 큰 길이를 넣어준다.
    for j in range(i):
        if seq[i] > seq[j]:
            answer[i] = max(answer[i], answer[j] + 1)
print(max(answer))

