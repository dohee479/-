# 오큰수
import sys
sys.stdin = open('input.txt', 'r')


def right_big():
    stack = []
    answer = [-1] * N
    for i, val in enumerate(A):
        if i == N - 1:
            answer[i] = -1
        else:
            # 스택을 거꾸로 반복문을 돌리면 시간초과
            # while을 사용하여 뒤에 들어가 있는 값만 비교하면 통과
            while stack and stack[-1][1] < A[i + 1]:
                answer[stack[-1][0]] = A[i + 1]
                stack.pop()
            if A[i] < A[i + 1]:
                answer[i] = A[i + 1]
            else:
                stack.append((i, val))
    return ' '.join(map(str, answer))


N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
print(right_big())


# 이중 반복으로 하면 시간초과: 입력값이 크므로
