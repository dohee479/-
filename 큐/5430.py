# AC
import sys
import re
from collections import deque
sys.stdin = open('input.txt', 'r')


# 슬라이싱 + pop(0) 시간초과, reverse + popleft 시간초과
def AC(command):
    flip = False
    for cmd in command:
        # R 명령 : 배열을 진짜 뒤집으면 안된다. 원소의 순서를 바꾸면 원소 수만큼 시간이 걸린다.
        # 뒤집지 않고 구현 효과를 내야한다. [::-1] 사용 하면 안된다.
        if cmd == 'R':
            flip = not flip
        elif cmd == 'D':
            if x:
                # list.pop() 역시 원소의 수에 비례하여 소요, deque 처리
                # pop, popleft를 해주는 대신 앞, 뒤 자를 인덱스를 계산해주어 잘라도 된다.
                # 정위치일 때는 앞에서 빼주는 위치를 +1 해주고
                # 역위치일 때는 뒤에서 빼주는 위치를 -1 해주면 된다. 즉 + 1 씩 해주고 총 길이에서 빼준다.
                if flip:
                    x.pop()
                else:
                    x.popleft()
            else:
                return 'error'
    if not flip:
        return "[" + ','.join(x) + "]"
    else:
        return "[" + ','.join(reversed(x)) + "]"


T = int(input())
r = re.compile("[0-9]+")
for t in range(T):
    p = sys.stdin.readline().rstrip()
    n = sys.stdin.readline().rstrip()
    x = deque(r.findall(sys.stdin.readline().rstrip()))
    print(AC(p))







