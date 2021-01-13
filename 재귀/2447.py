# 별 찍기 - 10
import sys
sys.stdin = open('input.txt', 'r')


def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]


def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' ' * n] * n)
    c = a + b + a
    return a + b + a


print('\n'.join(star10(int(input()))))


# 별 찍는 재귀 함수
def draw_star(n):
    if n == 3:
        Map[0][:3] = Map[2][:3] = [1] * 3
        Map[1][:3] = [1, 0, 1]
        return

    a = n // 3
    draw_star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]  # 핵심 아이디어


N = int(input())
Map = [[0 for i in range(N)] for i in range(N)]
draw_star(N)
for i in Map:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()



