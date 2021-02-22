# 회전하는 큐
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().rstrip().split())
queue = deque([i for i in range(1, N + 1)])
order = list(map(int, sys.stdin.readline().rstrip().split()))
i = 0
answer = 0
while i < M:
    if queue[0] == order[i]:
        queue.popleft()
        i += 1
    else:
        location = queue.index(order[i])
        # 주어진 위치가 왼쪽, 오른쪽 거리차이를 구한다.
        # 오른쪽 거리가 더 긴 경우, 왼쪽으로 민다.
        if len(queue) - location > location:
            queue.append(queue.popleft())
            answer += 1
        # 왼쪽 거리가 더 긴 경우, 오른쪽으로 민다.
        else:
            queue.appendleft(queue.pop())
            answer += 1
print(answer)

# 참조
# 위의 로직 간략화
n, m = map(int, input().split())
dq = [i for i in range(1, n+1)]

ans = 0

for find in map(int, input().split()):
    ix = dq.index(find)
    ans += min(len(dq[ix:]), len(dq[:ix]))
    dq = dq[ix+1:] + dq[:ix]

print(ans)
