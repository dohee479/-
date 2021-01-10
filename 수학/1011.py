# Fly me to the Alpha Centauri
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    if distance <= 3:
        print(distance)
    else:
        sqrt = int(distance ** 0.5)
        # 거리의 차의 값이 차의 제곱근의 제곱일 때
        if distance == sqrt ** 2:
            print(2 * sqrt - 1)
        # 제곱과 제곱 + 제곱근 사이일 때
        elif sqrt ** 2 < distance <= sqrt ** 2 + sqrt:
            print(2 * sqrt)
        # 제곱 + 제곱근보다 클 때
        else:
            print(2 * sqrt + 1)