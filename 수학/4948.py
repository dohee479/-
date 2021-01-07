# 베르트랑 공준
import sys
sys.stdin = open('input.txt', 'r')


def prime(N):
    end = 2 * N
    number = [True] * end
    for i in range(2, int(end ** 0.5) + 1):
        if number[i]:
            for j in range(i * 2, end, i):
                number[j] = False

    cnt = 0
    for i in range(N + 1, end):
        if number[i]:
            cnt += 1
    return cnt if n > 1 else 1


while True:
    n = int(input())
    if not n:
        break
    print(prime(n))


# 리스트 슬라이스 이용한 에라토스테네스의 체
t = 246912
x = [0, 0]+[1]*(t-1)
for i in range(int(t**.5) + 1):
    if x[i]:
        # 리스트 슬라이스를 사용하여 0을 대입하는 방법, -1을 해준 이유는 소수는 안들어 가기 때문이다.
        x[2*i::i] = [0]*(t//i - 1)  # 에라토스테네스의 체 활용

