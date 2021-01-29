# 주유소
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
distance = list(map(int, sys.stdin.readline().rstrip().split()))
prices = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
price = float('inf')
for i in range(len(distance)):
    # 현재 기름값이 이전까지의 기름값보다 작을 때
    # 기름값의 최소값은 현재 기름값이 되고 거리를 곱해준다.
    if prices[i] < price:
        price = prices[i]
        answer += distance[i] * price
    # 현재 기름값이 이전 기름값보다 크면
    # 이전 저장되어있는 기름값의 최소와 현재 거리를 곱해준다.
    else:
        answer += distance[i] * price
print(answer)