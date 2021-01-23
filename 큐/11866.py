# 요세푸스 문제 0
import sys
sys.stdin = open('input.txt', 'r')

# 실패
N, K = map(int, sys.stdin.readline().rstrip().split())
yose = [i for i in range(1, N + 1)]
adj = [0] * N
result = []
front = 0
cnt = 1
while len(result) != N:
    if front >= N:
        front %= N
    if yose[front]:
        if not cnt % 3:
            result.append(yose[front])
            yose[front] = 0
    else:
        cnt -= 1
    front += 1
    cnt += 1
print(str(result).replace('[', '<').replace(']', '>'))

