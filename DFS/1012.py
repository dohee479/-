# 유기농 배추
import sys
sys.stdin = open('../input.txt', 'r')
T = int(input())
for t in range(1, 1+T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        arr[c][r] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    stack = []
    direct = 0
    count = 0
    cnt = 0
    for c in range(N):
        for r in range(M):
            res = True
            if arr[c][r] == 1:
                direct = 0
                while res:
                    if arr[c][r] == 1:
                        stack.append(c)
                        stack.append(r)

                        dc = c + dx[direct]
                        dr = r + dy[direct]
                        if dc >= N or dr >= M or dc < 0 or dr < 0 or arr[dc][dr] == 0:
                            direct = (direct+1) % 4
                            dc = c + dx[direct]
                            dr = r + dy[direct]
                            count += 1
                        c = dc
                        r = dr
                    if count >= 1 and arr[c][r] == 0:
                        count = 0
                        for k in range(len(stack)//2):
                            pr = stack.pop()
                            pc = stack.pop()
                            arr[pc][pr] = 0
                            if not stack:
                                cnt += 1
                                res = False

    print(cnt)






