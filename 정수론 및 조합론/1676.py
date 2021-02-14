# 팩토리얼 0의 개수
import sys
sys.stdin = open('input.txt', 'r')


def factorial(n):
    fac = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i
    return str(fac[-1])


N = int(input())
number = factorial(N)
answer = 0
for i in range(len(number) - 1, -1, -1):
    if number[i] != '0':
        print(answer)
        break
    answer += 1


# 참조
# 팩토리얼에서 0이 늘어나는 순간은 10(2 * 5)이 곱해지는 순간이다.
# 따라서, 5의 개수를 찾으면 된다.
# 10! 일 경우 5에서 한번, 10에서 한번 총 2번이다.
n = int(input())
arr = [0 for i in range(n+1)]
for i in range(1,n+1):
    arr[i] = arr[i-1]
    idx = i
    if i%5 == 0:
        t = 0
        while i % 5 == 0:
            i //=5
            t+=1
        arr[idx] += t
print(arr[n])
