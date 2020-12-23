# 스택
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'push':
        lst.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(lst) != 0:
            print(lst.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(lst))
    elif cmd[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(lst) != 0:
            print(lst[-1])
        else:
            print(-1)



