# 로또
import sys
sys.stdin = open('input.txt', 'r')


def lotto(idx, n, m):
    if idx == m:
        for i in range(m):
            print(num[i], end=' ')
        print()
        return

    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        num[idx] = S[i]
        for j in range(1, i+1):
            visited[j] = 1
        lotto(idx+1, n, m)
        for j in range(1, n+1):
            visited[j] = 0


res = True
while res:
    S = list(map(int, input().split()))
    N = S[0]
    visited = [0] * (len(S)+1)
    num = [0] * 6
    if N == 0:
        res = False
        break
    lotto(0, len(S) - 1, 6)
    print()
