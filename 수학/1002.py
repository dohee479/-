# 터렛
import sys
sys.stdin = open('input.txt', 'r')


def turret(a1, b1, c1, a2, b2, c2):
    # 원 중심 사이의 거리
    d = ((a2 - a1) ** 2 + (b2 - b1) ** 2) ** 0.5
    # 두 반지름의 합
    R1 = c1 + c2
    # 두 반지름의 차
    R2 = abs(c1 - c2)

    # 만나지 않는다
    # 동심원
    if not d and c1 == c2:
        return -1
    # 외부
    elif R1 < d:
        return 0
    # 내부
    elif R2 > d:
        return 0
    # 한점에서 만난다.
    # 외접
    elif R1 == d:
        return 1
    # 내접
    elif R2 == d:
        return 1
    # 두점에서 만난다.
    else:
        return 2


T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(turret(x1, y1, r1, x2, y2, r2))