# AC
import sys
import re
from collections import deque
sys.stdin = open('input.txt', 'r')


def AC(command, x):
    for cmd in command:
        if cmd == 'R':
            x = x[len(x) - 1::-1]
        elif cmd == 'D':
            if x:
                x.pop(0)
            else:
                return 'error'
    return x


T = int(input())
r = re.compile("[0-9]+")
for t in range(T):
    p = sys.stdin.readline().rstrip()
    n = sys.stdin.readline().rstrip()
    x = r.findall(sys.stdin.readline().rstrip())
    print(x)
    # print(AC(p, x))




