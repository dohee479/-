# ACM 호텔
import sys
sys.stdin = open('input.txt', 'r')



def hotel(h, w, n):
    layer = (n-1) % h + 1
    q, r = divmod(n, h)
    if r:
        room = q + 1
    else:
        room = q
    if room < 10:
        return '{}0{}'.format(layer, room)
    return '{}{}'.format(layer, room)


T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    print(hotel(H, W, N))