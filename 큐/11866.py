# 요세푸스 문제 0
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().rstrip().split())
yose = [i for i in range(1, N + 1)]
adj = [0] * N
result = []
front = 0
cnt = 1
while len(result) != N:
    # 인덱스의 길이를 넘어갈 시 0으로 가게 하기 위해서
    if front >= N:
        front %= N
    if yose[front]:
        if not cnt % K:
            result.append(yose[front])
            yose[front] = 0
    # 0 이면 카운트 되지 않으므로 -1을 해준다.
    else:
        cnt -= 1
    front += 1
    cnt += 1
print(str(result).replace('[', '<').replace(']', '>'))

# 내가 시도하려고 했던 방식
N, K = map(int, input().split())
l = list(range(1, N+1))
p = list()
i = 0
while l:
    i = (i + K - 1) % len(l)
    p.append(str(l.pop(i)))

print('<'+', '.join(p)+'>')