# 프린터 큐
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, 1+T):
    N, M = map(int, input().split())
    printer = list(map(int, input().split()))
    max_num = max(printer)
    num = []
    for j in range(N):
        num.append(j)
    cnt = 0
    while True:
        if printer[0] < max_num:
            printer.append(printer.pop(0))
            num.append(num.pop(0))
        elif printer[0] == max_num:
            cnt += 1
            printer.pop(0)
            deQ = num.pop(0)
            if len(printer) == 0:
                print(cnt)
                break
            else:
                max_num = max(printer)
            if deQ == M:
                print(cnt)
                break




