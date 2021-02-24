# AC
import sys
import re
from collections import deque
sys.stdin = open('input.txt', 'r')


# 슬라이싱 + pop(0) 시간초과, reverse + popleft 시간초과
def AC(command, x):
    for cmd in command:
        if cmd == 'R':
            x = deque(sorted(x, reverse=True))
        elif cmd == 'D':
            if x:
                x.popleft()
            else:
                return 'error'
    return x


T = int(input())
r = re.compile("[0-9]+")
for t in range(T):
    p = sys.stdin.readline().rstrip()
    n = sys.stdin.readline().rstrip()
    x = deque(r.findall(sys.stdin.readline().rstrip()))
    print(AC(p, x))




