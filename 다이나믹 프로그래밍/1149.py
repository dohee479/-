# RGB 거리
import sys
sys.stdin = open('input.txt', 'r')







N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
memory = [[0] * N for _ in range(N)]