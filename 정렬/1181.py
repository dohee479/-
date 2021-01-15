# 단어 정렬
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
string = set(sys.stdin.readline().rstrip() for _ in range(N))
for i in sorted(string, key=lambda x: (len(x), x)):
    print(i)
