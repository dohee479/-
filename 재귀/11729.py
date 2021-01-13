# 하노이 탑 이동 순서
import sys
sys.stdin = open('input.txt', 'r')


# 과정
def hanoi(n, start, destination, layover):
    if n == 1:
        print('{} {}'.format(start, destination))
    else:
        # 제일 큰 원반을 옮기려면 나머지 원반이 2번 막대에 가야한다.
        hanoi(n - 1, start, layover, destination)
        # 제일 큰 원반 목적지로 옮김
        print('{} {}'.format(start, destination))
        # 2번에 있는 원반들을 3번으로 다시 옮겨야 한다.
        hanoi(n - 1, layover, destination, start)


N = int(input())
# 점화식(횟수)
print(2 ** N - 1)
hanoi(N, '1', '3', '2')





