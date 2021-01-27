# 가장 긴 바이토닉 부분 수열
import sys
sys.stdin = open('input.txt', 'r')

A = int(input())
bitonic = list(map(int, sys.stdin.readline().rstrip().split()))
answer = [0] * A
# 가장 긴 증가하는 부분 수열 푸는 방법
for i in range(A):
    answer[i] = 1
    for j in range(i):
        if bitonic[i] > bitonic[j]:
            answer[i] = max(answer[i], answer[j] + 1)
# 위의 방법 응용
# index 까지의 증가 수열의 개수를 최대값을 리스트에 저장해 놓았다.
# 그 이후 부터 기준이 되는 값보다 작아지면 값을 비교해서 저장
for i in range(A):
    for j in range(i + 1, A):
        if bitonic[i] > bitonic[j]:
            answer[j] = max(answer[i] + 1, answer[j])
print(max(answer))