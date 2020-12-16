# 택시 기하학
import sys, math
sys.stdin = open('input.txt', 'r')

R = int(input())
print("{0:.6f}".format(math.pi * (R ** 2)))
print("{0:.6f}".format(2 * (R ** 2)))