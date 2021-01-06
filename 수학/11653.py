# 소인수분해
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
i = 2
# 이 경우, 9991의 경우 99를 구하고 103을 구할때까지 진행한다.
while N > 1:
    if N % i:
        i += 1
    else:
        N //= i
        print(i)


N = int(input())
i = 2
r = int(N ** 0.5)
# 제곱근 값은 99이다. 99까지만 돌고 N = 103이다. 위와 다르게 103일 때까지 반복하지 않는다.
# 수가 커질수록 더욱 그러할 것으로 예측된다. 속도차이는 22배 정도 차이가 난다.
while i <= r:
    if N % i:
        i += 1
    else:
        N //= i
        print(i)
if N > 1:
    print(N)


