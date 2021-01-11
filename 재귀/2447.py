# 별 찍기 - 10
import sys
sys.stdin = open('input.txt', 'r')

# 시간초과
def star(x, y, num):
    if (x // num) % 3 == 1 and (y // num) % 3 == 1:
        print(' ', end='')
    else:
        if num // 3 == 0:
            print('*', end='')
        else:
            star(x, y, num // 3)


N = int(input())
for i in range(N):
    for j in range(N):
        star(i, j, N)
    print()




