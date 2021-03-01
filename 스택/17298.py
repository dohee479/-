# 오큰수
import sys
sys.stdin = open('input.txt', 'r')


def right_big():
    stack = []
    answer = [0] * N
    for i, val in enumerate(A):
        if i == N - 1:
            answer[i] = -1
        else:
            for j in range(len(stack) - 1, -1, -1):
                if stack[j][1] < A[i + 1]:
                    answer[stack[j][0]] = A[i + 1]
                    stack.pop()
            if A[i] < A[i + 1]:
                answer[i] = A[i + 1]
            else:
                stack.append((i, val))
    for i, val in stack:
        answer[i] = -1
    return ' '.join(map(str, answer))


N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
print(right_big())


# 이중 반복으로 하면 시간초과: 입력값이 크므로
