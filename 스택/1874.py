# 스택 수열
import sys
sys.stdin = open('input.txt', 'r')


# 참조
n = int(sys.stdin.readline())
p = map(lambda x: int(x.rstrip()), sys.stdin.readlines())


def solution():
    stack, result, cnt = [], [], 1
    for i in p:
        while cnt <= i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack.pop() != i:
            return 'NO'
        else:
            result.append('-')
    return '\n'.join(result)


print(solution())

# 처음 방식
n = int(input())
seq = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
stack = []
answer = []
possible = True
i = 1
j = 0
while j < n:
    if not stack:
        stack.append(i)
        answer.append("+")
        i += 1
    if i <= n:
        if stack[-1] == seq[j]:
            stack.pop()
            answer.append("-")
            j += 1
            continue

        if stack[-1] != seq[j]:
            if i > stack[-1]:
                stack.append(i)
                answer.append("+")
            else:
                print("NO")
                possible = False
                break
        i += 1
    else:
        if stack[-1] == seq[j]:
            stack.pop()
            answer.append("-")
            j += 1
            continue

        if stack[-1] != seq[j]:
            if stack[-1] > seq[j]:
                print("NO")
                possible = False
                break
if possible:
    print("\n".join(answer))











