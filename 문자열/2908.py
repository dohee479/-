#상수
import sys
sys.stdin = open('input.txt', 'r')

A, B = input()[::-1].split()
if A > B:
    print(A)
else:
    print(B)