# 택시 기하학
import sys, math
sys.stdin = open('input.txt', 'r')

R = int(input())
# 유클리드 기하학에서의 원의 넓이
print("{0:.6f}".format(math.pi * (R ** 2)))
# 택시 기하학에서의 원의 넓이, 택시가 가는 경로를 취하는 것: 거리, 원: 마름모 꼴의 정사각형 
print("{0:.6f}".format(2 * (R ** 2)))