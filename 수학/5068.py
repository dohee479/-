# 배수와 약수
import sys
sys.stdin = open('input.txt', 'r')


while True:
    num1, num2 = map(int, input().split())
    if not num1 and not num2:
        break
    else:
        if num1 >= num2 and num1 % num2 == 0:
            print('multiple')
        elif num1 < num2 and num2 % num1 == 0:
            print('factor')
        else:
            print('neither')
